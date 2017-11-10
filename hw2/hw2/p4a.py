#!/usr/bin/env python
import rospy
import math
import time
import numpy as np
from geometry_msgs.msg import Point
from std_msgs.msg import *
from hw2.srv import *
from foundations_hw2.msg import EulerAngles
from foundations_hw2.srv import *

def p4a():
    rospy.init_node('p4a')
    rospy.wait_for_service('foundations_hw2/interpolate_problem')
    test = rospy.ServiceProxy('foundations_hw2/interpolate_problem', Interpolate)
    ini=test().initial
    fin=test().final
    sec=test().seconds*10
    step1=(fin.phi-ini.phi)/sec
    step2=(fin.theta-ini.theta)/sec
    step3=(fin.psi-ini.psi)/sec
    num=0
    i_phi=[]
    i_theta=[]
    i_psi=[]
    while True:
        i_phi.append(ini.phi+num*step1)
        i_theta.append(ini.theta+num*step2)
        i_psi.append(ini.psi+num*step3)
        num=num+1
        if num>sec:
            break
    pub=rospy.Publisher('vrep/shape_pose', EulerAngles, queue_size=10)
    
    rate = rospy.Rate(10)
    i=0
    while not rospy.is_shutdown():
        if i>=sec:
            break
        ea=EulerAngles(i_phi[i],i_theta[i],i_psi[i])
        pub.publish(ea)
        rospy.loginfo(ea)
        i=i+1
        rate.sleep()   
    rospy.spin()
    
if __name__ == '__main__':
    p4a()