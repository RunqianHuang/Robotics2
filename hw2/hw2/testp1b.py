#!/usr/bin/env python
import rospy
import math
import time
import numpy as np
from geometry_msgs.msg import Point
from std_msgs.msg import *
from hw2.srv import *
from foundations_hw2.msg import JointAngles

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

def test_p1b():
    rospy.init_node('testp1b')
    #rospy.loginfo('running')
    global p1
    global p2
    global p3
    global p4
    global p5
    p1=p2=p3=p4=p5=0
    goal=None
    rospy.Subscriber('foundations_hw2/arm_config', JointAngles, callbackconfig)
    test = rospy.ServiceProxy('p1b', p1b)
    pub1=rospy.Publisher('/vrep/youbot/target/position', Point, queue_size=10)
    pub2=rospy.Publisher('/vrep/youbot/arm/joint1/angle', Float64, queue_size=10)
    pub3=rospy.Publisher('/vrep/youbot/arm/joint2/angle', Float64, queue_size=10)
    pub4=rospy.Publisher('/vrep/youbot/arm/joint3/angle', Float64, queue_size=10)
    pub5=rospy.Publisher('/vrep/youbot/arm/joint4/angle', Float64, queue_size=10)
    pub6=rospy.Publisher('/vrep/youbot/arm/joint5/angle', Float64, queue_size=10)
    
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        rospy.wait_for_service('p1b')
        #print('before')
        #p1=p2=p3=p4=p5=0
        goal = test([p1,p2,p3,p4,p5]).goal
        #print('after')
        #print(p1)
        #print(p2)
        #print(p3)
        #print(p4)
        #print(p5)
        #print(goal)
        pub1.publish(goal)
        pub2.publish(p1)
        pub3.publish(p2)
        pub4.publish(p3)
        pub5.publish(p4)
        pub6.publish(p5)
        rate.sleep()   
    rospy.spin()
    
if __name__ == '__main__':
    test_p1b()