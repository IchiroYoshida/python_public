#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define IN_DIR "../EMPS_mpi"
#define OUT_DIR "../EMPS_mpi"
#define NUM_PROCESS 4

FILE* fp;
char filename[256];
int NumberOfParticle;
int FileNumber = 130;
double *Position;
double *Velocity;
double *Pressure;
double *pressave;
int *ParticleType;
int *PE;

void read_data(int iFile) {
	int i_rank,num_p,k;
	NumberOfParticle=0;
	for(i_rank=0;i_rank<NUM_PROCESS;i_rank++){
		sprintf(filename, "%s/output%05d_%d.prof",IN_DIR,iFile,i_rank);
		fp = fopen(filename, "r");
		fscanf(fp,"%d",&num_p);
		NumberOfParticle+=num_p;
		fclose(fp);
	}
	printf("NumberOfParticle: %d\n",NumberOfParticle);

	Position = (double*)malloc(sizeof(double)*NumberOfParticle*3);
	Velocity = (double*)malloc(sizeof(double)*NumberOfParticle*3);
	Pressure = (double*)malloc(sizeof(double)*NumberOfParticle);
	pressave = (double*)malloc(sizeof(double)*NumberOfParticle);
	ParticleType = (int*)malloc(sizeof(int)*NumberOfParticle);
	PE = (int*)malloc(sizeof(int)*NumberOfParticle);

	k=0;
	for(i_rank=0;i_rank<NUM_PROCESS;i_rank++){
		sprintf(filename, "%s/output%05d_%d.prof",IN_DIR,iFile,i_rank);
		fp = fopen(filename, "r");
		fscanf(fp,"%d",&num_p);
		for(int i=0;i<num_p;i++) {
			int a[2];
			double b[8];
			fscanf(fp," %d %d %lf %lf %lf %lf %lf %lf %lf %lf",&a[0],&a[1],&b[0],&b[1],&b[2],&b[3],&b[4],&b[5],&b[6],&b[7]);
			ParticleType[k]=a[1];
			Position[k*3]=b[0];	Position[k*3+1]=b[1];	Position[k*3+2]=b[2];
			Velocity[k*3]=b[3];	Velocity[k*3+1]=b[4];	Velocity[k*3+2]=b[5];
			Pressure[k]=b[6];
			pressave[k]=b[7];
			PE[k]=i_rank;
			k++;
		}
		fclose(fp);
	}
}

void mk_vtu(int iFile) {
	sprintf(filename, "%s/particle_%05d.vtu",OUT_DIR,iFile);
    printf("Creating %s ... ", filename);

	FILE *fp;
	fp=fopen(filename,"w");
	fprintf(fp,"<?xml version='1.0' encoding='UTF-8'?>\n");
	fprintf(fp,"<VTKFile xmlns='VTK' byte_order='LittleEndian' version='0.1' type='UnstructuredGrid'>\n");
	fprintf(fp,"<UnstructuredGrid>\n");
 	fprintf(fp,"<Piece NumberOfCells='%d' NumberOfPoints='%d'>\n",NumberOfParticle,NumberOfParticle);

 	fprintf(fp,"<Points>\n");
 	fprintf(fp,"<DataArray NumberOfComponents='3' type='Float32' Name='Position' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++)fprintf(fp,"%lf %lf %lf\n",Position[i*3],Position[i*3+1],Position[i*3+2]);
 	fprintf(fp,"</DataArray>\n");
  	fprintf(fp,"</Points>\n");

  	fprintf(fp,"<PointData>\n");
 	fprintf(fp,"<DataArray NumberOfComponents='1' type='Int32' Name='ParticleType' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++){fprintf(fp,"%d\n",ParticleType[i]);}
 	fprintf(fp,"</DataArray>\n");
 	fprintf(fp,"<DataArray NumberOfComponents='1' type='Float32' Name='Velocity' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++){
		double val=sqrt(Velocity[i*3]*Velocity[i*3]+Velocity[i*3+1]*Velocity[i*3+1]+Velocity[i*3+2]*Velocity[i*3+2]);
		fprintf(fp,"%f\n",(float)val);
	}
 	fprintf(fp,"</DataArray>\n");
 	fprintf(fp,"<DataArray NumberOfComponents='1' type='Float32' Name='pressave' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++){	fprintf(fp,"%f\n",(float)pressave[i]);}
 	fprintf(fp,"</DataArray>\n");
 	fprintf(fp,"<DataArray NumberOfComponents='1' type='Int32' Name='PE' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++){	fprintf(fp,"%d\n",PE[i]);}
 	fprintf(fp,"</DataArray>\n");
  	fprintf(fp,"</PointData>\n");

 	fprintf(fp,"<Cells>\n");
 	fprintf(fp,"<DataArray type='Int32' Name='connectivity' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++)fprintf(fp,"%d\n",i);
 	fprintf(fp,"</DataArray>\n");
 	fprintf(fp,"<DataArray type='Int32' Name='offsets' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++)fprintf(fp,"%d\n",i+1);
 	fprintf(fp,"</DataArray>\n");
 	fprintf(fp,"<DataArray type='UInt8' Name='types' format='ascii'>\n");
	for(int i=0;i<NumberOfParticle;i++)fprintf(fp,"1\n");
 	fprintf(fp,"</DataArray>\n");
 	fprintf(fp,"</Cells>\n");

 	fprintf(fp,"</Piece>\n");
 	fprintf(fp,"</UnstructuredGrid>\n");
 	fprintf(fp,"</VTKFile>\n");

	fclose(fp);
	printf("done.\n");
}

int main( int argc, char** argv) {

	for(int iFile=0;iFile<FileNumber;iFile++){

		read_data(iFile);
		mk_vtu(iFile);

		free(Position);
		free(Velocity);
		free(Pressure);
		free(pressave);
		free(ParticleType);
	}
	printf(" END. \n");

	return 0;
}

