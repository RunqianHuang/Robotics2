#!/usr/bin/env python
import rospy
import math
import time
from numpy import *
from geometry_msgs.msg import Point
from std_msgs.msg import *
from foundations_hw2.msg import JointAngles
from hw2.srv import *

def test_p3a():
    rospy.init_node('testp3a')
    print('testp3a start')
    test = rospy.ServiceProxy('p3a', p3a)
    rospy.wait_for_service('p3a')
    point = Point(0,0,0.6075)
    result = test(point).angles
    print(result)
 
    rospy.spin()
    
if __name__ == '__main__':
    test_p3a()