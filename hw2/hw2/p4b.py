#!/usr/bin/env python
import rospy
import math
import time
from numpy import *
from geometry_msgs.msg import Point
from std_msgs.msg import *
from hw2.srv import *
from foundations_hw2.msg import EulerAngles
from foundations_hw2.srv import *

def p4b():
    rospy.init_node('p4b')
    rospy.wait_for_service('foundations_hw2/interpolate_problem')
    test = rospy.ServiceProxy('foundations_hw2/interpolate_problem', Interpolate)
    ini=test().initial
    fin=test().final
    sec=test().seconds*10
    q_ini=mat([[math.cos(ini.phi/2)*math.cos(ini.theta/2)*math.cos(ini.psi/2)+math.sin(ini.phi/2)*math.sin(ini.theta/2)*math.sin(ini.psi/2)],[math.sin(ini.phi/2)*math.cos(ini.theta/2)*math.cos(ini.psi/2)-math.cos(ini.phi/2)*math.sin(ini.theta/2)*math.sin(ini.psi/2)],[math.cos(ini.phi/2)*math.sin(ini.theta/2)*math.cos(ini.psi/2)+math.sin(ini.phi/2)*math.cos(ini.theta/2)*math.sin(ini.psi/2)],[math.cos(ini.phi/2)*math.cos(ini.theta/2)*math.sin(ini.psi/2)-math.sin(ini.phi/2)*math.sin(ini.theta/2)*math.cos(ini.psi/2)]])
    q_fin=mat([[math.cos(fin.phi/2)*math.cos(fin.theta/2)*math.cos(fin.psi/2)+math.sin(fin.phi/2)*math.sin(fin.theta/2)*math.sin(fin.psi/2)],[math.sin(fin.phi/2)*math.cos(fin.theta/2)*math.cos(fin.psi/2)-math.cos(fin.phi/2)*math.sin(fin.theta/2)*math.sin(fin.psi/2)],[math.cos(fin.phi/2)*math.sin(fin.theta/2)*math.cos(fin.psi/2)+math.sin(fin.phi/2)*math.cos(fin.theta/2)*math.sin(fin.psi/2)],[math.cos(fin.phi/2)*math.cos(fin.theta/2)*math.sin(fin.psi/2)-math.sin(fin.phi/2)*math.sin(fin.theta/2)*math.cos(fin.psi/2)]])
    #abini=q_ini[1][0]*q_ini[1][0]+q_ini[2][0]*q_ini[2][0]+q_ini[3][0]*q_ini[3][0]
    #inif=mat([[],[],[],[]])
    i_phi=[]
    i_theta=[]
    i_psi=[]
    i=1
    while i<sec:
        t=sec/i
        result=mat([[],[],[],[]])
        ad=mat([[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])
        c=q_ini.T*q_fin
        if c<0:
            q_fin=ad*q_fin
            c=-c
        if abs(c)>0.9995:
            k0=mat([[1-1/t,0,0,0],[0,1-1/t,0,0],[0,0,1-1/t,0],[0,0,0,1-1/t]])
            k1=mat([[1/t,0,0,0],[0,1/t,0,0],[0,0,1/t,0],[0,0,0,1/t]])
            result=k0*q_ini+k1*q_fin
        else:
            s=math.pow(1-c*c,0.5)
            o=math.atan2(s,c)
            os=1/s
            k0=mat([[sin((1-1/t)*o)*os,0,0,0],[0,sin((1-1/t)*o)*os,0,0],[0,0,sin((1-1/t)*o)*os,0],[0,0,0,sin((1-1/t)*o)*os]])
            k1=mat([[sin(o/t)*os,0,0,0],[0,sin(o/t)*os,0,0],[0,0,sin(o/t)*os,0],[0,0,0,sin(o/t)*os]])
            result=k0*q_ini+k1*q_fin
        w=result[0][0]
        x=result[1][0]
        y=result[2][0]
        z=result[3][0]
        sqw=w*w
        sqx=x*x
        sqy=y*y
        sqz=z*z
        unit=sqx+sqy+sqz+sqw
        test=x*y+z*w
        heading=attitude=bank=0
        if test>0.499*unit:
            heading=2*math.atan2(x,w)
            attitude=math.pi/2
            bank=0
        elif test<-0.499*unit:
            heading=-2*math.atan2(x,w)
            attitude=-math.pi/2
            bank=0
        else:
            heading=math.atan2(2*y*w-2*x*z,1-2*sqy-2*sqz)
            attitude=math.asin(2*test/unit)
            bank=math.atan2(2*x*w-2*y*z,1-2*sqx-2*sqz)
            i_phi.append(bank)
            i_theta.append(attitude)
            i_psi.append(heading)
        i=i+1
    pub=rospy.Publisher('vrep/shape_pose', EulerAngles, queue_size=10)
    
    rate = rospy.Rate(10)
    i=0
    while not rospy.is_shutdown():
        if i>=sec-1:
            break
        ea=EulerAngles(i_phi[i],i_theta[i],i_psi[i])
        pub.publish(ea)
        rospy.loginfo(ea)
        i=i+1
        rate.sleep()   
    rospy.spin()
    
if __name__ == '__main__':
    p4b()