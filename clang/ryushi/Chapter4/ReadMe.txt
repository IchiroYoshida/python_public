本ファイルでは，Linux環境での実行方法が記されている．

（１）収納されているファイル
mk_particle/mk_particle.cpp
EMPS/emps.cpp
EMPS_omp/emps_omp.cpp 
EMPS_cuda/emps_cuda.cu  
EMPS_mpi/emps_mpi.cpp  
prof2vtk/prof2vtk.cpp
prof2vtk_mpi/prof2vtk_mpi.cpp

（２）粒子生成コードの実行方法
$ cd mk_particle/
$ ls
mk_particle.cpp
$ g++ mk_particle.cpp 
$ ls
a.out  mk_particle.cpp
$ ./a.out 
start mk_particle
nx:56 ny:16 nz:36 nxyz:32256
NumberOfParticle:     19136
end mk_particle
$ ls
a.out  dambreak.prof  mk_particle.cpp
$ cd ..

（３）single版MPSコードの実行方法
$ cd EMPS/
$ ls
emps.cpp
$ g++ -O3 emps.cpp -lm
$ ls
a.out  emps.cpp
$ ./a.out 
start emps.
nP: 19136
nBx:27  nBy:9  nBz:30  nBxy:243  nBxyz:7290
    0 th TIM: 0.000000 / p_num: 19136
  100 th TIM: 0.050000 / p_num: 19136
  200 th TIM: 0.100000 / p_num: 19136
  300 th TIM: 0.150000 / p_num: 19136
  400 th TIM: 0.200000 / p_num: 19136
  500 th TIM: 0.250000 / p_num: 19136
  600 th TIM: 0.300000 / p_num: 19136
  700 th TIM: 0.350000 / p_num: 19136
  800 th TIM: 0.400000 / p_num: 19136
  900 th TIM: 0.450000 / p_num: 19136
 1000 th TIM: 0.500000 / p_num: 19136
 1100 th TIM: 0.550000 / p_num: 19136
 1200 th TIM: 0.600000 / p_num: 19136
 1300 th TIM: 0.650000 / p_num: 19136
 1400 th TIM: 0.700000 / p_num: 19134
 1500 th TIM: 0.750000 / p_num: 19132
 1600 th TIM: 0.800000 / p_num: 19126
 1700 th TIM: 0.850000 / p_num: 19126
 1800 th TIM: 0.900000 / p_num: 19124
 1900 th TIM: 0.950000 / p_num: 19124
 2000 th TIM: 1.000000 / p_num: 19122
 2100 th TIM: 1.050000 / p_num: 19121
Total        :    141.288622 sec
end emps.
$ cd ..

（４）OpenMP版MPSコードの実行方法
$ cd EMPS_omp/
$ ls
emps_omp.cpp
$ g++ -O3 -fopenmp emps_omp.cpp -lm
$ ls
a.out  emps_omp.cpp
$ ./a.out 
start emps_omp.
nP: 19136
nBx:27  nBy:9  nBz:30  nBxy:243  nBxyz:7290
    0 th TIM: 0.000000 / p_num: 19136
  100 th TIM: 0.050000 / p_num: 19136
  200 th TIM: 0.100000 / p_num: 19136
  300 th TIM: 0.150000 / p_num: 19136
  400 th TIM: 0.200000 / p_num: 19136
  500 th TIM: 0.250000 / p_num: 19136
  600 th TIM: 0.300000 / p_num: 19136
  700 th TIM: 0.350000 / p_num: 19136
  800 th TIM: 0.400000 / p_num: 19136
  900 th TIM: 0.450000 / p_num: 19136
 1000 th TIM: 0.500000 / p_num: 19136
 1100 th TIM: 0.550000 / p_num: 19136
 1200 th TIM: 0.600000 / p_num: 19136
 1300 th TIM: 0.650000 / p_num: 19136
 1400 th TIM: 0.700000 / p_num: 19134
 1500 th TIM: 0.750000 / p_num: 19132
 1600 th TIM: 0.800000 / p_num: 19126
 1700 th TIM: 0.850000 / p_num: 19126
 1800 th TIM: 0.900000 / p_num: 19124
 1900 th TIM: 0.950000 / p_num: 19124
 2000 th TIM: 1.000000 / p_num: 19122
 2100 th TIM: 1.050000 / p_num: 19121
Total        :     38.480784 sec
end emps_omp.
$ cd ..

（５）CUDA版MPSコードの実行方法
$ cd EMPS_cuda/
$ ls
emps_cuda.cu  
$ nvcc -gencode arch=compute_35,code=sm_35 emps_cuda.cu -lm -lcuda -lcudart -I/usr/local/cuda-5.5/include -I/usr/local/cuda-5.5/samples/common/inc
$ ls
a.out  emps_cuda.cpp
$ ./a.out 
start emps_cuda.
nP: 19136
nBx:27  nBy:9  nBz:30  nBxy:243  nBxyz:7290
    0 th TIM: 0.000000 / p_num: 19136
  100 th TIM: 0.050000 / p_num: 19136
  200 th TIM: 0.100000 / p_num: 19136
  300 th TIM: 0.150000 / p_num: 19136
  400 th TIM: 0.200000 / p_num: 19136
  500 th TIM: 0.250000 / p_num: 19136
  600 th TIM: 0.300000 / p_num: 19136
  700 th TIM: 0.350000 / p_num: 19136
  800 th TIM: 0.400000 / p_num: 19136
  900 th TIM: 0.450000 / p_num: 19136
 1000 th TIM: 0.500000 / p_num: 19136
 1100 th TIM: 0.550000 / p_num: 19136
 1200 th TIM: 0.600000 / p_num: 19136
 1300 th TIM: 0.650000 / p_num: 19136
 1400 th TIM: 0.700000 / p_num: 19134
 1500 th TIM: 0.750000 / p_num: 19132
 1600 th TIM: 0.800000 / p_num: 19126
 1700 th TIM: 0.850000 / p_num: 19126
 1800 th TIM: 0.900000 / p_num: 19124
 1900 th TIM: 0.950000 / p_num: 19124
 2000 th TIM: 1.000000 / p_num: 19122
 2100 th TIM: 1.050000 / p_num: 19121
Total        :     22.849892 sec
end emps_cuda.
$ cd ..

（６）MPI版MPSコードの実行方法
$ cd EMPS_mpi/
$ ls
emps_mpi.cpp
$ mpicxx -O3 emps_mpi.cpp -lm
$ ls
a.out  emps_mpi.cpp
$ mpirun -np 4 ./a.out 
start emps_mpi.
nP: 19136
    0 th TIM: 0.000000 / p_num: 19136
  100 th TIM: 0.050000 / p_num: 19136
  200 th TIM: 0.100000 / p_num: 19136
  300 th TIM: 0.150000 / p_num: 19136
  400 th TIM: 0.200000 / p_num: 19136
  500 th TIM: 0.250000 / p_num: 19136
  600 th TIM: 0.300000 / p_num: 19136
  700 th TIM: 0.350000 / p_num: 19136
  800 th TIM: 0.400000 / p_num: 19136
  900 th TIM: 0.450000 / p_num: 19136
 1000 th TIM: 0.500000 / p_num: 19136
 1100 th TIM: 0.550000 / p_num: 19136
 1200 th TIM: 0.600000 / p_num: 19136
 1300 th TIM: 0.650000 / p_num: 19136
 1400 th TIM: 0.700000 / p_num: 19134
 1500 th TIM: 0.750000 / p_num: 19132
 1600 th TIM: 0.800000 / p_num: 19130
 1700 th TIM: 0.850000 / p_num: 19129
 1800 th TIM: 0.900000 / p_num: 19129
 1900 th TIM: 0.950000 / p_num: 19128
 2000 th TIM: 1.000000 / p_num: 19128
 2100 th TIM: 1.050000 / p_num: 19127
end emps_mpi.
$ cd ..

（７）single版，OpenMP版，CUDA版MPSコード解析結果の可視化方法
$ cd prof2vtk
$ ls
prof2vtk.cpp  
$ emacs prof2vtk.cpp

可視化したいディレクトリを選択する．
#define IN_DIR "../EMPS"
#define OUT_DIR "../EMPS"
//#define IN_DIR "../EMPS_omp"
//#define OUT_DIR "../EMPS_omp"
//#define IN_DIR "../EMPS_cuda"
//#define OUT_DIR "../EMPS_cuda"

$ g++ prof2vtk.cpp
$ ls
a.out  prof2vtk.cpp  
$ ./a.out 
NumberOfParticle: 19136
Creating ../EMPS/particle_00000.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00001.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00002.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00003.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00004.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00005.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00006.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00007.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00008.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00009.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00010.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00011.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00012.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00013.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00014.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00015.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00016.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00017.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00018.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00019.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00020.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS/particle_00021.vtu ... done.

$ ls ../EMPS
a.out             output00008.prof  output00018.prof    particle_00006.vtu  particle_00016.vtu
emps.cpp          output00009.prof  output00019.prof    particle_00007.vtu  particle_00017.vtu
output00000.prof  output00010.prof  output00020.prof    particle_00008.vtu  particle_00018.vtu
output00001.prof  output00011.prof  output00021.prof    particle_00009.vtu  particle_00019.vtu
output00002.prof  output00012.prof  particle_00000.vtu  particle_00010.vtu  particle_00020.vtu
output00003.prof  output00013.prof  particle_00001.vtu  particle_00011.vtu  particle_00021.vtu
output00004.prof  output00014.prof  particle_00002.vtu  particle_00012.vtu
output00005.prof  output00015.prof  particle_00003.vtu  particle_00013.vtu
output00006.prof  output00016.prof  particle_00004.vtu  particle_00014.vtu
output00007.prof  output00017.prof  particle_00005.vtu  particle_00015.vtu
$ paraview
Openから「particle_..vtu」を選択する．

$ cd ..

（８）MPI版MPSコード解析結果の可視化方法
$ cd prof2vtk_mpi/
$ ls
prof2vtk_mpi.cpp
$ g++ prof2vtk_mpi.cpp 
$ ls
a.out  prof2vtk_mpi.cpp
$ ./a.out 
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00000.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00001.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00002.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00003.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00004.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00005.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00006.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00007.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00008.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00009.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00010.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00011.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00012.vtu ... done.
NumberOfParticle: 19136
Creating ../EMPS_mpi/particle_00013.vtu ... done.
NumberOfParticle: 19134
Creating ../EMPS_mpi/particle_00014.vtu ... done.
NumberOfParticle: 19132
Creating ../EMPS_mpi/particle_00015.vtu ... done.
NumberOfParticle: 19130
Creating ../EMPS_mpi/particle_00016.vtu ... done.
NumberOfParticle: 19129
Creating ../EMPS_mpi/particle_00017.vtu ... done.
NumberOfParticle: 19129
Creating ../EMPS_mpi/particle_00018.vtu ... done.
NumberOfParticle: 19128
Creating ../EMPS_mpi/particle_00019.vtu ... done.
NumberOfParticle: 19128
Creating ../EMPS_mpi/particle_00020.vtu ... done.
NumberOfParticle: 19127
Creating ../EMPS_mpi/particle_00021.vtu ... done.
$ ls ../EMPS_mpi/
a.out               output00005_1.prof  output00011_0.prof  output00016_3.prof  particle_00002.vtu
emps_mpi.cpp        output00005_2.prof  output00011_1.prof  output00017_0.prof  particle_00003.vtu
output00000_0.prof  output00005_3.prof  output00011_2.prof  output00017_1.prof  particle_00004.vtu
output00000_1.prof  output00006_0.prof  output00011_3.prof  output00017_2.prof  particle_00005.vtu
output00000_2.prof  output00006_1.prof  output00012_0.prof  output00017_3.prof  particle_00006.vtu
output00000_3.prof  output00006_2.prof  output00012_1.prof  output00018_0.prof  particle_00007.vtu
output00001_0.prof  output00006_3.prof  output00012_2.prof  output00018_1.prof  particle_00008.vtu
output00001_1.prof  output00007_0.prof  output00012_3.prof  output00018_2.prof  particle_00009.vtu
output00001_2.prof  output00007_1.prof  output00013_0.prof  output00018_3.prof  particle_00010.vtu
output00001_3.prof  output00007_2.prof  output00013_1.prof  output00019_0.prof  particle_00011.vtu
output00002_0.prof  output00007_3.prof  output00013_2.prof  output00019_1.prof  particle_00012.vtu
output00002_1.prof  output00008_0.prof  output00013_3.prof  output00019_2.prof  particle_00013.vtu
output00002_2.prof  output00008_1.prof  output00014_0.prof  output00019_3.prof  particle_00014.vtu
output00002_3.prof  output00008_2.prof  output00014_1.prof  output00020_0.prof  particle_00015.vtu
output00003_0.prof  output00008_3.prof  output00014_2.prof  output00020_1.prof  particle_00016.vtu
output00003_1.prof  output00009_0.prof  output00014_3.prof  output00020_2.prof  particle_00017.vtu
output00003_2.prof  output00009_1.prof  output00015_0.prof  output00020_3.prof  particle_00018.vtu
output00003_3.prof  output00009_2.prof  output00015_1.prof  output00021_0.prof  particle_00019.vtu
output00004_0.prof  output00009_3.prof  output00015_2.prof  output00021_1.prof  particle_00020.vtu
output00004_1.prof  output00010_0.prof  output00015_3.prof  output00021_2.prof  particle_00021.vtu
output00004_2.prof  output00010_1.prof  output00016_0.prof  output00021_3.prof
output00004_3.prof  output00010_2.prof  output00016_1.prof  particle_00000.vtu
output00005_0.prof  output00010_3.prof  output00016_2.prof  particle_00001.vtu

$ paraview
Openから「particle_..vtu」を選択する．

$ cd ..

