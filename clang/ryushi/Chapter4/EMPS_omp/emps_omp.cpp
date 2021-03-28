#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define IN_FILE "../mk_particle/dambreak.prof"
#define PCL_DST 0.02
#define MIN_X  (0.0 - PCL_DST*3)
#define MIN_Y  (0.0 - PCL_DST*3)
#define MIN_Z  (0.0 - PCL_DST*3)
#define MAX_X  (1.0 + PCL_DST*3)
#define MAX_Y  (0.2 + PCL_DST*3)
#define MAX_Z  (0.6 + PCL_DST*30)

#define GST -1
#define FLD 0
#define WLL  1
#define NUM_TYP  2
#define DNS_FLD 1000
#define DNS_WLL 1000
#define DT 0.0005
#define FIN_TIM 1.0
#define SND 22.0
#define OPT_FQC 100
#define KNM_VSC 0.000001
#define DIM 3
#define CRT_NUM 0.1
#define COL_RAT 0.2
#define DST_LMT_RAT 0.9
#define G_X 0.0
#define G_Y 0.0
#define G_Z -9.8
#define WEI(dst, re) 		((re/dst) - 1.0)

FILE* fp;
char filename[256];
int iLP,iF;
double TIM;
int nP;
double *Acc,*Pos,*Vel,*Prs,*pav;
int *Typ;
double r,r2;
double DB,DB2,DBinv;
int nBx,nBy,nBz,nBxy,nBxyz;
int *bfst,*blst,*nxt;
double n0,lmd,A1,A2,A3,rlim,rlim2,COL;
double Dns[NUM_TYP],invDns[NUM_TYP];

void ChkPcl(int i){
	if(	Pos[i*3  ]>MAX_X || Pos[i*3  ]<MIN_X ||
		Pos[i*3+1]>MAX_Y || Pos[i*3+1]<MIN_Y ||
		Pos[i*3+2]>MAX_Z || Pos[i*3+2]<MIN_Z)
	{
		Typ[i] = GST;
		Prs[i]=Vel[i*3]=Vel[i*3+1]=Vel[i*3+2]=0.0;
	}
}

void RdDat(void) {
	fp = fopen(IN_FILE, "r");
	fscanf(fp,"%d",&nP);
	printf("nP: %d\n",nP);
	Acc = (double*)malloc(sizeof(double)*nP*3);
	Pos = (double*)malloc(sizeof(double)*nP*3);
	Vel = (double*)malloc(sizeof(double)*nP*3);
	Prs = (double*)malloc(sizeof(double)*nP);
	pav = (double*)malloc(sizeof(double)*nP);
	Typ = (int*)malloc(sizeof(int)*nP);
	for(int i=0;i<nP;i++) {
		int a[2];
		double b[8];
		fscanf(fp," %d %d %lf %lf %lf %lf %lf %lf %lf %lf",&a[0],&a[1],&b[0],&b[1],&b[2],&b[3],&b[4],&b[5],&b[6],&b[7]);
		Typ[i]=a[1];
		Pos[i*3]=b[0];	Pos[i*3+1]=b[1];	Pos[i*3+2]=b[2];
		Vel[i*3]=b[3];	Vel[i*3+1]=b[4];	Vel[i*3+2]=b[5];
		Prs[i]=b[6];		pav[i]=b[7];
	}
	fclose(fp);
	for(int i=0;i<nP;i++) {ChkPcl(i);}
	for(int i=0;i<nP*3;i++) {Acc[i]=0.0;}
}

void WrtDat(void) {
	char outout_filename[256];
	sprintf(outout_filename, "output%05d.prof",iF);
	fp = fopen(outout_filename, "w");
	fprintf(fp,"%d\n",nP);
	for(int i=0;i<nP;i++) {
		int a[2];
		double b[8];
		a[0]=i;	a[1]=Typ[i];
		b[0]=Pos[i*3];	b[1]=Pos[i*3+1];	b[2]=Pos[i*3+2];
		b[3]=Vel[i*3];	b[4]=Vel[i*3+1];	b[5]=Vel[i*3+2];
		b[6]=Prs[i];		b[7]=pav[i]/OPT_FQC;
		fprintf(fp," %d %d %lf %lf %lf %lf %lf %lf %lf %lf\n",a[0],a[1],b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]);
		pav[i]=0.0;
	}
	fclose(fp);
	iF++;
}

void AlcBkt(void) {
	r = PCL_DST*2.1;		r2 = r*r;
	DB = r*(1.0+CRT_NUM);	DB2 = DB*DB;	DBinv = 1.0/DB;
	nBx = (int)((MAX_X - MIN_X)*DBinv) + 3;
	nBy = (int)((MAX_Y - MIN_Y)*DBinv) + 3;
	nBz = (int)((MAX_Z - MIN_Z)*DBinv) + 3;
	nBxy = nBx*nBy;
	nBxyz = nBx*nBy*nBz;
	printf("nBx:%d  nBy:%d  nBz:%d  nBxy:%d  nBxyz:%d\n",nBx,nBy,nBz,nBxy,nBxyz);
	bfst = (int*)malloc(sizeof(int) * nBxyz);
	blst = (int*)malloc(sizeof(int) * nBxyz);
	nxt  = (int*)malloc(sizeof(int) * nP);
}

void SetPara(void){
	n0 = lmd = 0.0;
	for(int ix= -4;ix<5;ix++){
	for(int iy= -4;iy<5;iy++){
	for(int iz= -4;iz<5;iz++){
		double x = PCL_DST* (double)ix;
		double y = PCL_DST* (double)iy;
		double z = PCL_DST* (double)iz;
		double dst2 = x*x+y*y+z*z;
		if(dst2 <= r2){
			if(dst2==0.0)continue;
			double dst = sqrt(dst2);
			n0 += WEI(dst, r);
			lmd += dst2 * WEI(dst, r);
		}
	}}}
	lmd = lmd/n0;
	A1 = 2.0*KNM_VSC*DIM/n0/lmd;
	A2 = SND*SND/n0;
	A3 = -DIM/n0;
	Dns[FLD]=DNS_FLD;			Dns[WLL]=DNS_WLL;
	invDns[FLD]=1.0/DNS_FLD;	invDns[WLL]=1.0/DNS_WLL;
	rlim = PCL_DST * DST_LMT_RAT;	rlim2 = rlim*rlim;
	COL = 1.0 + COL_RAT;
	iLP=iF=0;
	TIM=0.0;
}

void MkBkt(void) {
	for(int i=0;i< nBxyz ;i++){	bfst[i] = -1;	}
	for(int i=0;i< nBxyz ;i++){	blst[i] = -1;	}
	for(int i=0;i< nP ;i++){	nxt[i] = -1;	}
	for(int i=0;i<nP;i++){
		if(Typ[i] == GST)continue;
		int ix = (int)((Pos[i*3  ] - MIN_X)*DBinv) +1;
		int iy = (int)((Pos[i*3+1] - MIN_Y)*DBinv) +1;
		int iz = (int)((Pos[i*3+2] - MIN_Z)*DBinv) +1;
		int ib = iz*nBxy + iy*nBx + ix;
		int j = blst[ib];
		blst[ib] = i;
		if(j == -1){	bfst[ib] = i;	}
		else{			nxt[j] = i;}
	}
}

void VscTrm_omp(){
#pragma omp parallel for schedule(dynamic,64)
	for(int i=0;i<nP;i++){
	if(Typ[i] == FLD){
		double Acc_x = 0.0;			double Acc_y = 0.0;			double Acc_z = 0.0;
		double pos_ix = Pos[i*3  ];	double pos_iy = Pos[i*3+1];	double pos_iz = Pos[i*3+2];
		double vec_ix = Vel[i*3  ];	double vec_iy = Vel[i*3+1];	double vec_iz = Vel[i*3+2];
		int ix = (int)((pos_ix - MIN_X)*DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*nBxy + jy*nBx + jx;
			int j = bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = Pos[j*3  ] - pos_ix;
				double v1 = Pos[j*3+1] - pos_iy;
				double v2 = Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<r2){
				if(j!=i && Typ[j]!=GST){
					double dst = sqrt(dst2);
					double w =  WEI(dst, r);
					Acc_x +=(Vel[j*3  ]-vec_ix)*w;
					Acc_y +=(Vel[j*3+1]-vec_iy)*w;
					Acc_z +=(Vel[j*3+2]-vec_iz)*w;
				}}
				j = nxt[j];
				if(j==-1) break;
			}
		}}}
		Acc[i*3  ]=Acc_x*A1 + G_X;
		Acc[i*3+1]=Acc_y*A1 + G_Y;
		Acc[i*3+2]=Acc_z*A1 + G_Z;
	}}
}

void UpPcl1_omp(){
#pragma omp parallel for
	for(int i=0;i<nP;i++){
		if(Typ[i] == FLD){
			Vel[i*3  ] +=Acc[i*3  ]*DT;	Vel[i*3+1] +=Acc[i*3+1]*DT;	Vel[i*3+2] +=Acc[i*3+2]*DT;
			Pos[i*3  ] +=Vel[i*3  ]*DT;		Pos[i*3+1] +=Vel[i*3+1]*DT;		Pos[i*3+2] +=Vel[i*3+2]*DT;
			Acc[i*3]=Acc[i*3+1]=Acc[i*3+2]=0.0;
			ChkPcl(i);
		}
	}
}

void ChkCol_omp(){
#pragma omp parallel for schedule(dynamic,64)
	for(int i=0;i<nP;i++){
	if(Typ[i] == FLD){
		double mi = Dns[Typ[i]];
		double pos_ix = Pos[i*3  ];	double pos_iy = Pos[i*3+1];	double pos_iz = Pos[i*3+2];
		double vec_ix = Vel[i*3  ];	double vec_iy = Vel[i*3+1];	double vec_iz = Vel[i*3+2];
		double vec_ix2 = Vel[i*3  ];double vec_iy2 = Vel[i*3+1];double vec_iz2 = Vel[i*3+2];
		int ix = (int)((pos_ix - MIN_X)*DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*nBxy + jy*nBx + jx;
			int j = bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = Pos[j*3  ] - pos_ix;
				double v1 = Pos[j*3+1] - pos_iy;
				double v2 = Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<rlim2){
				if(j!=i && Typ[j]!=GST){
					double fDT = (vec_ix-Vel[j*3  ])*v0+(vec_iy-Vel[j*3+1])*v1+(vec_iz-Vel[j*3+2])*v2;
					if(fDT > 0.0){
						double mj = Dns[Typ[j]];
						fDT *= COL*mj/(mi+mj)/dst2;
						vec_ix2 -= v0*fDT;		vec_iy2 -= v1*fDT;		vec_iz2 -= v2*fDT;
					}
				}}
				j = nxt[j];
				if(j==-1) break;
			}
		}}}
		Acc[i*3  ]=vec_ix2;	Acc[i*3+1]=vec_iy2;	Acc[i*3+2]=vec_iz2;
	}}
#pragma omp parallel for
	for(int i=0;i<nP;i++){
		Vel[i*3  ]=Acc[i*3  ];	Vel[i*3+1]=Acc[i*3+1];	Vel[i*3+2]=Acc[i*3+2];
	}
}

void MkPrs_omp(){
#pragma omp parallel for schedule(dynamic,64)
	for(int i=0;i<nP;i++){
	if(Typ[i] != GST){
		double pos_ix = Pos[i*3  ];	double pos_iy = Pos[i*3+1];	double pos_iz = Pos[i*3+2];
		double ni = 0.0;
		int ix = (int)((pos_ix - MIN_X)*DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*nBxy + jy*nBx + jx;
			int j = bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = Pos[j*3  ] - pos_ix;
				double v1 = Pos[j*3+1] - pos_iy;
				double v2 = Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<r2){
				if(j!=i && Typ[j]!=GST){
					double dst = sqrt(dst2);
					double w =  WEI(dst, r);
					ni += w;
				}}
				j = nxt[j];
				if(j==-1) break;
			}
		}}}
		double mi = Dns[Typ[i]];
		double pressure = (ni > n0)*(ni - n0) * A2 * mi;
		Prs[i] = pressure;
	}}
}

void PrsGrdTrm_omp(){
#pragma omp parallel for schedule(dynamic,64)
	for(int i=0;i<nP;i++){
	if(Typ[i] == FLD){
		double Acc_x = 0.0;			double Acc_y = 0.0;			double Acc_z = 0.0;
		double pos_ix = Pos[i*3  ];	double pos_iy = Pos[i*3+1];	double pos_iz = Pos[i*3+2];
		double pre_min = Prs[i];
		int ix = (int)((pos_ix - MIN_X)*DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*nBxy + jy*nBx + jx;
			int j = bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = Pos[j*3  ] - pos_ix;
				double v1 = Pos[j*3+1] - pos_iy;
				double v2 = Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<r2){
				if(j!=i && Typ[j]!=GST){
					if(pre_min > Prs[j])pre_min = Prs[j];
				}}
				j = nxt[j];
				if(j==-1) break;
			}
		}}}
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*nBxy + jy*nBx + jx;
			int j = bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = Pos[j*3  ] - pos_ix;
				double v1 = Pos[j*3+1] - pos_iy;
				double v2 = Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<r2){
				if(j!=i && Typ[j]!=GST){
					double dst = sqrt(dst2);
					double w =  WEI(dst, r);
					w *= (Prs[j] - pre_min)/dst2;
					Acc_x += v0*w;	Acc_y += v1*w;	Acc_z += v2*w;
				}}
				j = nxt[j];
				if(j==-1) break;
			}
		}}}
		Acc[i*3  ]=Acc_x*invDns[FLD]*A3;
		Acc[i*3+1]=Acc_y*invDns[FLD]*A3;
		Acc[i*3+2]=Acc_z*invDns[FLD]*A3;
	}}
}

void UpPcl2_omp(void){
#pragma omp parallel for
	for(int i=0;i<nP;i++){
		if(Typ[i] == FLD){
			Vel[i*3  ] +=Acc[i*3  ]*DT;		Vel[i*3+1] +=Acc[i*3+1]*DT;		Vel[i*3+2] +=Acc[i*3+2]*DT;
			Pos[i*3  ] +=Acc[i*3  ]*DT*DT;	Pos[i*3+1] +=Acc[i*3+1]*DT*DT;	Pos[i*3+2] +=Acc[i*3+2]*DT*DT;
			Acc[i*3]=Acc[i*3+1]=Acc[i*3+2]=0.0;
			ChkPcl(i);
		}
	}
}

void ClcEMPS(void){
	while(1){
		if(iLP%100==0){
			int p_num=0;
			for(int i=0;i<nP;i++){if(Typ[i] != GST)p_num++;}
			printf("%5d th TIM: %lf / p_num: %d\n", iLP,TIM,p_num);
		}
		if(iLP%OPT_FQC == 0 ){
			WrtDat();
			if(TIM >= FIN_TIM ){	break;}
		}
		MkBkt();
		VscTrm_omp();
		UpPcl1_omp();
		ChkCol_omp();
		MkPrs_omp();
		PrsGrdTrm_omp();
		UpPcl2_omp();
		MkPrs_omp();
		for(int i=0;i<nP;i++){pav[i] += Prs[i];}
		iLP++;
		TIM += DT;
	}
}
#include <sys/time.h>
double get_dtime(void){
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return ((double)(tv.tv_sec) + (double)(tv.tv_usec) * 0.000001);
}
int main( int argc, char** argv) {
	printf("start emps_omp.\n");
	RdDat();
	AlcBkt();
	SetPara();

	double timer_sta = get_dtime();

	ClcEMPS();

	double timer_end = get_dtime();
	printf("Total        : %13.6lf sec\n",timer_end -timer_sta);


	free(Acc);	free(Pos);	free(Vel);
	free(Prs);	free(pav);	free(Typ);
	free(bfst);	free(blst);	free(nxt);
	printf("end emps_omp.\n");
	return 0;
}
