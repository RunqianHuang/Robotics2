#!/usr/bin/env python
import rospy
import math
import time
from numpy import *
from std_msgs.msg import *
from hw2.srv import *
from std_srvs.srv import Empty
from geometry_msgs.msg import Point, Pose
from foundations_hw2.msg import JointAngles

def callbackp3b(data):
    rospy.loginfo('callback')
      
def callbackposition(data):
    rospy.loginfo('position called')
    global x
    global y
    global z
    x=data.position.x
    y=data.position.y
    z=data.position.z
        
def p3b_server():
    global x
    global y
    global z
    x=y=z=0
    rospy.init_node('p3b_server')
    s=rospy.Service('/p3b', Empty, callbackp3b)
    #rospy.loginfo('p3b start!')
    test = rospy.ServiceProxy('p3a', p3a)
    pub1=rospy.Publisher('/vrep/youbot/arm/joint1/angle', Float64, queue_size=10)
    pub2=rospy.Publisher('/vrep/youbot/arm/joint2/angle', Float64, queue_size=10)
    pub3=rospy.Publisher('/vrep/youbot/arm/joint3/angle', Float64, queue_size=10)
    pub4=rospy.Publisher('/vrep/youbot/arm/joint4/angle', Float64, queue_size=10)
    pub5=rospy.Publisher('/vrep/youbot/arm/joint5/angle', Float64, queue_size=10)
    
    word = [[0,0,0],[0,0,0.1],[0,0,0.2],[0,0,0.1],[0.1,0,0.1],[0.1,0,0.2],[0.1,0,0],[0.2,0,0],[0.2,0,0.2]]
    
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        #rospy.loginfo('p3a finished')
        #for i in range(0,9):
        rospy.wait_for_service('p3a')
        point = Point(0,0,0.1)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
        point = Point(0,0,0.2)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
        point = Point(0,0,0.1)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
        point = Point(0.1,0,0.1)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
        point = Point(0.1,0,0.2)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
        point = Point(0.1,0,0)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
        point = Point(0.2,0,0)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
        point = Point(0.2,0,0.2)
        result = test(point).angles
        pub1.publish(result[0])
        pub2.publish(result[1])
        pub3.publish(result[2])
        pub4.publish(result[3])
        pub5.publish(result[4])
        
            #time.sleep(5)
        rate.sleep() 
    
    rospy.spin()
    
if __name__ == '__main__':
    p3b_server()