"""
#
# LIST 6-3 NEARLY PARABOLIC <p.203>
# 8600 -
# 
# INPUT mjd
#       ec  : Eccentricity
	q   : q

  OUTPUT  ss = r * cos(V)
  	  cc = r * sin(V)
	  V

np[ss,cc,V] 
"""
def NearlyParabolic(mjd,ec,q):

	r1 = 1.0+9.0*ec
				#<6.2.1>
	aa = sqrt(.1*r1)
	bb = 5.0*(1.0-ec)/r1	#<6.2.2>
	cc = sqrt(5.0*(1.0+ec)/r1)  #<6.2.3>

	b  = 1.0
	a0 = 0.0

        while 1:

	    u = b*aa*K1*(mjd-T)/(sqrt(2)*q**1.5)       #<6.2.4> p.190	
    	    r2 = 1.0
            
            while 1:

                v = (u+2.0*r2**3/3.0)/(1+r2*r2)     #<6.2.7> p.191

	        if abs(v-r2)>1.0e-6 :
		    	r2 = v
                else :
                        break
	
	    a = bb*v*v                        #  <6.2.8> p.191
	   a2 = a*a
	   a3 = a*a*a

	    b = 1-.017142857*a2-0.003809524*a3   #  <6.2.9> p.191
                    
            if abs(a-a0)>1.0e-6 :
                  a0 = a
            else :
                  break

        c = 1.0 + .4*a+.21714286*a2+.12495238*a3      #  <6.2.10> p.191
        d = 1.0 -  a  +.2*a2+5.71429e-3*a3            #  <6.2.11> p.191

        qd = q*d                                      #<6.2.13> p.191

        v  = cc*c*v
        cc = qd*(1.0-v*v)
        ss = 2.0*qd*v
        v  = 2.0*atan(v)

        np=[cc,ss,v]

        return np



