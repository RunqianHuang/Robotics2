#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from foundations_hw2.msg import Ackermann

def callback(data):
    global vx
    global vy
    global w
    vx=data.linear.x
    vy=data.linear.y
    w=data.angular.z

def p5a():
    rospy.init_node('p5a')
    global vx
    global vy
    global w
    vx=vy=w=0
    rospy.Subscriber('foundations_hw2/cmd_vel',Twist,callback)
    pub1=rospy.Publisher('vrep/youbot/base/cmd_vel',Twist,queue_size=10)
    pub2=rospy.Publisher('vrep/ackermann/cmd_vel',Ackermann,queue_size=10)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        message=Twist()
        message.linear.x=vx
        message.linear.y=vy
        message.linear.z=0
        message.angular.x=0
        message.angular.y=0
        message.angular.z=w
        result=Ackermann()
        v=math.pow(vx*vx+vy*vy,0.5)
        result.vel=v
        tag2=0
        if w<0:
            tag2=1
        else:
            tag2=-1
        if w==0:
            result.steering_angle=0
        else:
            result.steering_angle=tag2*math.atan2(2.5772,abs(v/w))
        pub1.publish(message)
        pub2.publish(result)
        rate.sleep()   
    rospy.spin()
    
if __name__ == '__main__':
    p5a()