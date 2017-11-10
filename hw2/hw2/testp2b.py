#!/usr/bin/env python
import rospy
import math
import time
from numpy import *
from geometry_msgs.msg import Point
from std_msgs.msg import *
from foundations_hw2.msg import JointAngles
from hw2.srv import *

def callbackconfig(data):
    global p1
    global p2
    global p3
    global p4
    global p5
    p1=data.angles[0]
    p2=data.angles[1]
    p3=data.angles[2]
    p4=data.angles[3]
    p5=data.angles[4]

def test_p2b():
    rospy.init_node('testp2b')
    global p1
    global p2
    global p3
    global p4
    global p5
    p1=p2=p3=p4=p5=0
    goal=None
    #rospy.Subscriber('foundations_hw2/arm_config', JointAngles, callbackconfig)
    test = rospy.ServiceProxy('p2b', p2b)
    
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        rospy.wait_for_service('p2b')
        #p1=p2=p3=p4=p5=0
        data = test([p1,p2,p3,p4,p5]).data
        m = data.data
        row = data.layout.dim[0].size
        column = data.layout.dim[1].size
        j = zeros([row,column])
        for i in range(0,row):
            for k in range(0,column):
                j[i][k]=m[i*5+k]
        j = mat(j)
        v = mat([[0],[1],[0],[0],[0]])
        w = j*v
        #print(p1)
        #print(p2)
        #print(p3)
        #print(p4)
        #print(p5)
        print(w)
        rate.sleep()   
    rospy.spin()
    
if __name__ == '__main__':
    test_p2b()