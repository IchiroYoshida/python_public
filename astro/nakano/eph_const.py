"""
# 3-6 EPH CONST <p.74>
# 4000 **** 
eph_const.py

  INPUT | PE = Peri.
	| ND = Node.
	| IC = Inc.
 OUTPUT | F(1,2,3)=F(x,y,z)
	| Q(1,2,3)=Q(x,y,z)

eph_const[F(x,y,z),Q(x,y,z)]=EphConst(pe,nd,ic)

"""
from math import *
from astro import *

def EphConst(pe,nd,ic):
	eph_const=[[0.0 for i in range(3)]for j in range(2)]

	r1=sin(pe)
	r2=sin(nd)
	r3=sin(ic)

	r4=cos(pe)
	r5=cos(nd)
	r6=cos(ic)

        px = r5*r4-r1*r6*r2
        qx =-r1*r5-r4*r6*r2

	r7= r6*r5*K4
	r8= r2*K4
	r9= r3*K5

        py = r1*r7+r4*r8-r1*r9
        qy = r4*r7-r1*r8-r4*r9

	r7= r3*K4
	r8= r6*r5*K5
	r9= r2*K5

        pz = r1*r7+r1*r8+r4*r9
        qz = r4*r7+r4*r8-r1*r9

	eph_const[0][0]= px  #F(1)
	eph_const[1][0]= qx  #Q(1)
	eph_const[0][1]= py  #F(2)
	eph_const[1][1]= qy  #Q(2)
	eph_const[0][2]= pz  #F(3)
	eph_const[1][2]= qz  #Q(3)
       
	return eph_const

