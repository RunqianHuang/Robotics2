#!/usr/bin/env python
import rospy
import math
from numpy import *
from std_msgs.msg import *
from hw2.srv import *
from std_srvs.srv import Empty
from geometry_msgs.msg import Point
from foundations_hw2.msg import JointAngles

def test_p3b():
    rospy.init_node('testp3b')
    test = rospy.ServiceProxy('p3b', Empty)
    
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        rospy.wait_for_service('p3b')
        test
        rate.sleep()   
    rospy.spin()
    
if __name__ == '__main__':
    test_p3b()