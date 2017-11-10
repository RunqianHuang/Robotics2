#!/usr/bin/env python
import rospy
import math
import time
from numpy import *
from geometry_msgs.msg import Point
from hw2.srv import *
from std_msgs.msg import *
from foundations_hw2.msg import JointAngles
    
def callbackp1b(data):
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
    a0=mat([[0,0,1,0],[0,1,0,0.033],[-1,0,0,0.1],[0,0,0,1]])
    a01=mat([[-1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]])
    a1=mat([[1,0,0,0],[0,math.cos(p1),-math.sin(p1),0],[0,math.sin(p1),math.cos(p1),0],[0,0,0,1]])
    a11=mat([[math.cos(p2),-math.sin(p2),0,0],[math.sin(p2),math.cos(p2),0,0],[0,0,1,0],[0,0,0,1]])
    a2=mat([[math.cos(p3),-math.sin(p3),0,0.155],[math.sin(p3),math.cos(p3),0,0],[0,0,1,0],[0,0,0,1]])
    a30=mat([[0,1,0,0.135],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
    a3=mat([[math.cos(p4),-math.sin(p4),0,0],[math.sin(p4),math.cos(p4),0,0],[0,0,1,0],[0,0,0,1]])
    a4=mat([[0],[0.2175],[0],[1]])
    a=a0*a01*a1*a11*a2*a30*a3*a4
    pointx=a[0][0]
    pointy=a[1][0]
    pointz=a[2][0]
    point=Point(pointx,pointy,pointz)
    #rospy.loginfo(point)
    return p1bResponse(point)
    

def p1b_server():
    rospy.init_node('p1b_server')
    #rospy.loginfo('running')
    #rate = rospy.Rate(2)
    #while not rospy.is_shutdown():
    s=rospy.Service('/p1b', p1b, callbackp1b)
    #rate.sleep()
    
    rospy.spin()
    
if __name__ == '__main__':
    p1b_server()