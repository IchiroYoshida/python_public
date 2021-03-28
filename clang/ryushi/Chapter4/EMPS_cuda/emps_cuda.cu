#include <stdio.h>
#include <cuda_runtime.h>
#include <helper_functions.h>
#include <helper_cuda.h>

#ifdef __CDT_PARSER__
#define __global__
#define __device__
#define __host__
#define __shared__
#endif

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
double n0,lmd,A1,A2,A3,rlim,rlim2,COL;
double Dns[NUM_TYP],invDns[NUM_TYP];

void ChkPcl(int i){
	if(Typ[i] != GST){
	if(	Pos[i*3  ]>MAX_X || Pos[i*3  ]<MIN_X ||
		Pos[i*3+1]>MAX_Y || Pos[i*3+1]<MIN_Y ||
		Pos[i*3+2]>MAX_Z || Pos[i*3+2]<MIN_Z)
	{
		Typ[i] = GST;
		Prs[i]=Vel[i*3]=Vel[i*3+1]=Vel[i*3+2]=0.0;
	}}
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
	DB = r*(1.0+CRT_NUM);	DB2 = DB*DB;		DBinv = 1.0/DB;
	nBx = (int)((MAX_X - MIN_X)*DBinv) + 3;
	nBy = (int)((MAX_Y - MIN_Y)*DBinv) + 3;
	nBz = (int)((MAX_Z - MIN_Z)*DBinv) + 3;
	nBxy = nBx*nBy;
	nBxyz = nBx*nBy*nBz;
	printf("nBx:%d  nBy:%d  nBz:%d  nBxy:%d  nBxyz:%d\n",nBx,nBy,nBz,nBxy,nBxyz);
}

void SetPara(void){
	n0 = lmd =0.0;
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


int BLOCKS,TOTAL_THREADS;
#define THREADS 128

#define ERR_CHK(func){ checkCudaErrors(func); }
#define ERR_KNL(func){ func; getLastCudaError(#func); }

__global__ void d_initialize_double_array(int n, double *d_array, double a){
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<n){d_array[i] = a;}
}

__global__ void d_initialize_int_array(int n, int *i_array, int a){
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<n){i_array[i] = a;}
}

__global__ void d_add_double_array(int n, double *d_array1, double *d_array0){
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<n){d_array1[i] += d_array0[i];}
}

double *d_Acc,*d_Pos,*d_Vel,*d_Prs,*d_pav;
int *d_Typ;
int *d_bfst,*d_blst,*d_nxt;
double *d_Dns,*d_invDns;

__device__ void d_ChkPcl(int i, int d_nP,	int *d_Typ, double* d_Pos, double* d_Vel, double* d_Acc, double* d_Prs)
{
	if(d_Typ[i] != GST){
	if(	d_Pos[i*3  ]>MAX_X || d_Pos[i*3  ]<MIN_X ||
		d_Pos[i*3+1]>MAX_Y || d_Pos[i*3+1]<MIN_Y ||
		d_Pos[i*3+2]>MAX_Z || d_Pos[i*3+2]<MIN_Z)
	{
		d_Typ[i] = GST;
		d_Prs[i]=d_Vel[i*3]=d_Vel[i*3+1]=d_Vel[i*3+2]=0.0;
	}}
}

__global__ void d_MkBkt(int d_nP, int d_nBx, int d_nBxy, int d_nBxyz, double d_DBinv,
		int* d_bfst, int* d_blst, int* d_nxt,
		int *d_Typ, double* d_Pos)
{
	int i = blockIdx.x*blockDim.x + threadIdx.x;
//	int i = blockIdx.x + threadIdx.x*gridDim.x;
	if(i<d_nP){
		if(d_Typ[i] != GST){
			int ix = (int)((d_Pos[i*3  ] - MIN_X)*d_DBinv) +1;
			int iy = (int)((d_Pos[i*3+1] - MIN_Y)*d_DBinv) +1;
			int iz = (int)((d_Pos[i*3+2] - MIN_Z)*d_DBinv) +1;

			int ib = iz*d_nBxy + iy*d_nBx + ix;
			int j = atomicExch(&d_blst[ib],i);
			if(j == -1){	d_bfst[ib] = i;	}
			else{				d_nxt[j] = i;}
		}
	}
}

__global__ void d_VscTrm(int d_nP, int d_nBx, int d_nBxy, int d_nBxyz, double d_DBinv,
		int* d_bfst, int* d_blst, int* d_nxt,
		int *d_Typ, double* d_Pos, double* d_Vel, double* d_Acc, double d_r, double d_A1)
{
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<d_nP){
	if(d_Typ[i] == FLD){
		double Acc_x = 0.0;			double Acc_y = 0.0;			double Acc_z = 0.0;
		double pos_ix = d_Pos[i*3  ];	double pos_iy = d_Pos[i*3+1];	double pos_iz = d_Pos[i*3+2];
		double vec_ix = d_Vel[i*3  ];	double vec_iy = d_Vel[i*3+1];	double vec_iz = d_Vel[i*3+2];
		int ix = (int)((pos_ix - MIN_X)*d_DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*d_DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*d_DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*d_nBxy + jy*d_nBx + jx;
			int j = d_bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = d_Pos[j*3  ] - pos_ix;
				double v1 = d_Pos[j*3+1] - pos_iy;
				double v2 = d_Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<d_r*d_r){
				if(j!=i && d_Typ[j]!=GST){
					double dst = sqrt(dst2);
					double w =  WEI(dst, d_r);
					Acc_x +=(d_Vel[j*3  ]-vec_ix)*w;
					Acc_y +=(d_Vel[j*3+1]-vec_iy)*w;
					Acc_z +=(d_Vel[j*3+2]-vec_iz)*w;
				}}
				j = d_nxt[j];
				if(j==-1) break;
			}
		}}}
		d_Acc[i*3  ]=Acc_x*d_A1 + G_X;
		d_Acc[i*3+1]=Acc_y*d_A1 + G_Y;
		d_Acc[i*3+2]=Acc_z*d_A1 + G_Z;
	}}
}

__global__ void d_UpPcl1(	int d_nP, int *d_Typ, double* d_Pos, double* d_Vel, double* d_Acc, double* d_Prs)
{
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<d_nP){
		if(d_Typ[i] == FLD){
			d_Vel[i*3  ] +=d_Acc[i*3  ]*DT;	d_Vel[i*3+1] +=d_Acc[i*3+1]*DT;	d_Vel[i*3+2] +=d_Acc[i*3+2]*DT;
			d_Pos[i*3  ] +=d_Vel[i*3  ]*DT;		d_Pos[i*3+1] +=d_Vel[i*3+1]*DT;		d_Pos[i*3+2] +=d_Vel[i*3+2]*DT;
			d_Acc[i*3]=d_Acc[i*3+1]=d_Acc[i*3+2]=0.0;
			d_ChkPcl(i, d_nP, d_Typ, d_Pos, d_Vel, d_Acc, d_Prs);
		}
	}
}

__global__ void d_ChkCol(int d_nP, int d_nBx, int d_nBxy, int d_nBxyz, double d_DBinv,
		int* d_bfst, int* d_blst, int* d_nxt,
		int *d_Typ, double* d_Pos, double* d_Vel, double* d_Acc, double *d_Dns , double d_rlim2, double d_COL)
{
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<d_nP){
	if(d_Typ[i] == FLD){
		double mi = d_Dns[d_Typ[i]];
		double pos_ix = d_Pos[i*3  ];	double pos_iy = d_Pos[i*3+1];	double pos_iz = d_Pos[i*3+2];
		double vec_ix = d_Vel[i*3  ];	double vec_iy = d_Vel[i*3+1];	double vec_iz = d_Vel[i*3+2];
		double vec_ix2 = d_Vel[i*3  ];	double vec_iy2 = d_Vel[i*3+1];	double vec_iz2 = d_Vel[i*3+2];
		int ix = (int)((pos_ix - MIN_X)*d_DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*d_DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*d_DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*d_nBxy + jy*d_nBx + jx;
			int j = d_bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = d_Pos[j*3  ] - pos_ix;
				double v1 = d_Pos[j*3+1] - pos_iy;
				double v2 = d_Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<d_rlim2){
				if(j!=i && d_Typ[j]!=GST){
					double fDT = (vec_ix-d_Vel[j*3  ])*v0+(vec_iy-d_Vel[j*3+1])*v1+(vec_iz-d_Vel[j*3+2])*v2;
					if(fDT > 0.0){
						double mj = d_Dns[d_Typ[j]];
						fDT *= d_COL*mj/(mi+mj)/dst2;
						vec_ix2 -= v0*fDT;		vec_iy2 -= v1*fDT;		vec_iz2 -= v2*fDT;
					}
				}}
				j = d_nxt[j];
				if(j==-1) break;
			}
		}}}
		d_Acc[i*3  ]=vec_ix2;	d_Acc[i*3+1]=vec_iy2;	d_Acc[i*3+2]=vec_iz2;
	}}
}
__global__ void d_MkPrs(int d_nP, int d_nBx, int d_nBxy, int d_nBxyz, double d_DBinv,
		int* d_bfst, int* d_blst, int* d_nxt,
		int *d_Typ, double* d_Pos, double* d_Prs, double *d_Dns ,double d_r, double d_n0, double d_A2)
{
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<d_nP){
	if(d_Typ[i] != GST){
		double pos_ix = d_Pos[i*3  ];	double pos_iy = d_Pos[i*3+1];	double pos_iz = d_Pos[i*3+2];
		double ni = 0.0;
		int ix = (int)((pos_ix - MIN_X)*d_DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*d_DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*d_DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*d_nBxy + jy*d_nBx + jx;
			int j = d_bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = d_Pos[j*3  ] - pos_ix;
				double v1 = d_Pos[j*3+1] - pos_iy;
				double v2 = d_Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<d_r*d_r){
				if(j!=i && d_Typ[j]!=GST){
					double dst = sqrt(dst2);
					double w =  WEI(dst, d_r);
					ni += w;
				}}
				j = d_nxt[j];
				if(j==-1) break;
			}
		}}}
		double mi = d_Dns[d_Typ[i]];
		double pressure = (ni > d_n0)*(ni - d_n0) * d_A2 * mi;
		d_Prs[i] = pressure;
	}}
}

__global__ void d_PrsGrdTrm(int d_nP, int d_nBx, int d_nBxy, int d_nBxyz, double d_DBinv,
		int* d_bfst, int* d_blst, int* d_nxt,
		int *d_Typ, double* d_Pos, double* d_Acc, double* d_Prs, double *d_invDns, double d_r, double d_A3)
{
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<d_nP){
	if(d_Typ[i] == FLD){
		double Acc_x = 0.0;			double Acc_y = 0.0;			double Acc_z = 0.0;
		double pos_ix = d_Pos[i*3  ];	double pos_iy = d_Pos[i*3+1];	double pos_iz = d_Pos[i*3+2];
		double pre_min = d_Prs[i];
		int ix = (int)((pos_ix - MIN_X)*d_DBinv) +1;
		int iy = (int)((pos_iy - MIN_Y)*d_DBinv) +1;
		int iz = (int)((pos_iz - MIN_Z)*d_DBinv) +1;
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*d_nBxy + jy*d_nBx + jx;
			int j = d_bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = d_Pos[j*3  ] - pos_ix;
				double v1 = d_Pos[j*3+1] - pos_iy;
				double v2 = d_Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<d_r*d_r){
				if(j!=i && d_Typ[j]!=GST){
					if(pre_min > d_Prs[j])pre_min = d_Prs[j];
				}}
				j = d_nxt[j];
				if(j==-1) break;
			}
		}}}
		for(int jz=iz-1;jz<=iz+1;jz++){
		for(int jy=iy-1;jy<=iy+1;jy++){
		for(int jx=ix-1;jx<=ix+1;jx++){
			int jb = jz*d_nBxy + jy*d_nBx + jx;
			int j = d_bfst[jb];
			if(j == -1) continue;
			for(;;){
				double v0 = d_Pos[j*3  ] - pos_ix;
				double v1 = d_Pos[j*3+1] - pos_iy;
				double v2 = d_Pos[j*3+2] - pos_iz;
				double dst2 = v0*v0+v1*v1+v2*v2;
				if(dst2<d_r*d_r){
				if(j!=i && d_Typ[j]!=GST){
					double dst = sqrt(dst2);
					double w =  WEI(dst, d_r);
					w *= (d_Prs[j] - pre_min)/dst2;
					Acc_x += v0*w;	Acc_y += v1*w;	Acc_z += v2*w;
				}}
				j = d_nxt[j];
				if(j==-1) break;
			}
		}}}
		d_Acc[i*3  ]=Acc_x*d_invDns[FLD]*d_A3;
		d_Acc[i*3+1]=Acc_y*d_invDns[FLD]*d_A3;
		d_Acc[i*3+2]=Acc_z*d_invDns[FLD]*d_A3;
	}}
}

__global__ void d_UpPcl2(int d_nP,	int *d_Typ, double* d_Pos, double* d_Vel, double* d_Acc, double* d_Prs)
{
	int i = blockIdx.x*blockDim.x + threadIdx.x;
	if(i<d_nP){
		if(d_Typ[i] == FLD){
			d_Vel[i*3  ] +=d_Acc[i*3  ]*DT;		d_Vel[i*3+1] +=d_Acc[i*3+1]*DT;		d_Vel[i*3+2] +=d_Acc[i*3+2]*DT;
			d_Pos[i*3  ] +=d_Acc[i*3  ]*DT*DT;	d_Pos[i*3+1] +=d_Acc[i*3+1]*DT*DT;	d_Pos[i*3+2] +=d_Acc[i*3+2]*DT*DT;
			d_Acc[i*3]=d_Acc[i*3+1]=d_Acc[i*3+2]=0.0;
			d_ChkPcl(i, d_nP, d_Typ, d_Pos, d_Vel, d_Acc, d_Prs);
		}
	}
}

void ClcEMPS_cuda(void){

	dim3 threads(THREADS, 1, 1);
	TOTAL_THREADS = nBxyz;	BLOCKS = TOTAL_THREADS/THREADS+1;
	dim3 blocks_nBxyz(BLOCKS, 1, 1);
	TOTAL_THREADS = nP;	BLOCKS = TOTAL_THREADS/THREADS+1;
	dim3 blocks_nP(BLOCKS, 1, 1);
	TOTAL_THREADS = nP*3;	BLOCKS = TOTAL_THREADS/THREADS+1;
	dim3 blocks_nP3(BLOCKS, 1, 1);

	while(1){
		if(iLP%OPT_FQC == 0 ){
			ERR_CHK(cudaMemcpy(Typ, d_Typ, sizeof(int)*nP, cudaMemcpyDeviceToHost));
			ERR_CHK(cudaMemcpy(Pos, d_Pos, sizeof(double)*nP*3, cudaMemcpyDeviceToHost));
			ERR_CHK(cudaMemcpy(Vel, d_Vel, sizeof(double)*nP*3, cudaMemcpyDeviceToHost));
			ERR_CHK(cudaMemcpy(Prs, d_Prs, sizeof(double)*nP, cudaMemcpyDeviceToHost));
			ERR_CHK(cudaMemcpy(pav, d_pav, sizeof(double)*nP, cudaMemcpyDeviceToHost));
			ERR_KNL((d_initialize_double_array<<<blocks_nP, threads>>>(nP, d_pav, 0.0)));
			WrtDat();

			int p_num=0;
			for(int i=0;i<nP;i++){if(Typ[i] != GST)p_num++;}
			printf("%5d th TIM: %lf / p_num: %d\n", iLP,TIM,p_num);

			if(TIM >= FIN_TIM ){
				break;
			}
		}

		ERR_KNL((d_initialize_int_array<<<blocks_nBxyz, threads>>>(nBxyz, d_bfst, -1)));
		ERR_KNL((d_initialize_int_array<<<blocks_nBxyz, threads>>>(nBxyz, d_blst, -1)));
		ERR_KNL((d_initialize_int_array<<<blocks_nP, threads>>>(nP, d_nxt, -1)));
		ERR_KNL((d_MkBkt<<<blocks_nP, threads>>>(nP, nBx, nBxy, nBxyz, DBinv,
				d_bfst, d_blst, d_nxt, d_Typ, d_Pos)));

		ERR_KNL((d_VscTrm<<<blocks_nP, threads>>>(nP, nBx, nBxy, nBxyz, DBinv,
				d_bfst, d_blst, d_nxt, d_Typ, d_Pos, d_Vel, d_Acc, r, A1)));
		ERR_KNL((d_UpPcl1<<<blocks_nP, threads>>>(nP, d_Typ, d_Pos, d_Vel, d_Acc, d_Prs)));

		ERR_KNL((d_ChkCol<<<blocks_nP, threads>>>(nP, nBx, nBxy, nBxyz, DBinv,
				d_bfst, d_blst, d_nxt, d_Typ, d_Pos, d_Vel, d_Acc, d_Dns, rlim2, COL)));
		ERR_CHK(cudaMemcpy(d_Vel, d_Acc, sizeof(double)*nP*3, cudaMemcpyDeviceToDevice));


		ERR_KNL((d_MkPrs<<<blocks_nP, threads>>>(nP, nBx, nBxy, nBxyz, DBinv,
				d_bfst, d_blst, d_nxt, d_Typ, d_Pos, d_Prs, d_Dns, r, n0, A2)));

		ERR_KNL((d_PrsGrdTrm<<<blocks_nP, threads>>>(nP, nBx, nBxy, nBxyz, DBinv,
				d_bfst, d_blst, d_nxt, d_Typ, d_Pos, d_Acc, d_Prs, d_invDns, r, A3)));
		ERR_KNL((d_UpPcl2<<<blocks_nP, threads>>>(nP, d_Typ, d_Pos, d_Vel, d_Acc, d_Prs)));

		ERR_KNL((d_MkPrs<<<blocks_nP, threads>>>(nP, nBx, nBxy, nBxyz, DBinv,
				d_bfst, d_blst, d_nxt, d_Typ, d_Pos, d_Prs, d_Dns, r, n0, A2)));
		ERR_KNL((d_add_double_array<<<blocks_nP, threads>>>(nP,d_pav,d_Prs)));

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
int main( int argc, char** argv)
{
	ERR_CHK(cudaSetDevice(0));

	printf("start emps_cuda.\n");
	RdDat();

	ERR_CHK(cudaMalloc( (void**) &d_Typ, sizeof(int)*nP ));
	ERR_CHK(cudaMalloc( (void**) &d_Acc, sizeof(double)*nP*3 ));
	ERR_CHK(cudaMalloc( (void**) &d_Pos, sizeof(double)*nP*3 ));
	ERR_CHK(cudaMalloc( (void**) &d_Vel, sizeof(double)*nP*3 ));
	ERR_CHK(cudaMalloc( (void**) &d_Prs, sizeof(double)*nP ));
	ERR_CHK(cudaMalloc( (void**) &d_pav, sizeof(double)*nP ));

	ERR_CHK(cudaMemcpy(d_Typ, 	Typ,	sizeof(int)*nP, 		cudaMemcpyHostToDevice));
	ERR_CHK(cudaMemcpy(d_Acc, 	Acc, 	sizeof(double)*nP*3, cudaMemcpyHostToDevice));
	ERR_CHK(cudaMemcpy(d_Pos, 	Pos,	sizeof(double)*nP*3, cudaMemcpyHostToDevice));
	ERR_CHK(cudaMemcpy(d_Vel, 	Vel,	sizeof(double)*nP*3,	cudaMemcpyHostToDevice));
	ERR_CHK(cudaMemcpy(d_Prs, 	Prs,	sizeof(double)*nP, 	cudaMemcpyHostToDevice));
	ERR_CHK(cudaMemcpy(d_pav, 	pav,	sizeof(double)*nP, 	cudaMemcpyHostToDevice));

	AlcBkt();

	ERR_CHK(cudaMalloc( (void**) &d_bfst, sizeof(int)*nBxyz ));
	ERR_CHK(cudaMalloc( (void**) &d_blst, sizeof(int)*nBxyz ));
	ERR_CHK(cudaMalloc( (void**) &d_nxt, sizeof(int)*nP ));

	SetPara();

	ERR_CHK(cudaMalloc( (void**) &d_Dns,		sizeof(double)*2 ));
	ERR_CHK(cudaMalloc( (void**) &d_invDns, 	sizeof(double)*2 ));
	ERR_CHK(cudaMemcpy(d_Dns, 	Dns,		sizeof(double)*2, cudaMemcpyHostToDevice));
	ERR_CHK(cudaMemcpy(d_invDns,invDns,	sizeof(double)*2, cudaMemcpyHostToDevice));

	double timer_sta = get_dtime();

	ClcEMPS_cuda();

	double timer_end = get_dtime();
	printf("Total        : %13.6lf sec\n",timer_end -timer_sta);

	ERR_CHK(cudaFree(d_Typ));	ERR_CHK(cudaFree(d_Acc));	ERR_CHK(cudaFree(d_Pos));
	ERR_CHK(cudaFree(d_Vel));	ERR_CHK(cudaFree(d_Prs));	ERR_CHK(cudaFree(d_pav));
	ERR_CHK(cudaFree(d_bfst));	ERR_CHK(cudaFree(d_blst));	ERR_CHK(cudaFree(d_nxt));
	free(Acc);	free(Pos);	free(Vel);	free(Prs);	free(pav);	free(Typ);
	printf("end emps_cuda.\n");

	ERR_CHK(cudaDeviceReset());
	return 0;
}
