#!/usr/bin/env python
import rospy
import math
from numpy import *
from std_msgs.msg import *
from hw2.srv import *
    
def callbackp2b(data):
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
    a=[0.2175*(math.cos(p1)*math.cos(p2)*math.cos(p3)*math.sin(p4)-math.cos(p1)*math.sin(p2)*math.sin(p3)*math.sin(p4)+math.cos(p1)*math.cos(p3)*math.cos(p4)*math.sin(p2)+math.cos(p1)*math.cos(p2)*math.cos(p4)*math.sin(p3))+0.135*(math.cos(p1)*math.cos(p3)*math.sin(p2)+math.cos(p1)*math.cos(p2)*math.sin(p3))+0.155*math.cos(p1)*math.sin(p2),0.2175*(math.sin(p1)*math.cos(p2)*math.cos(p3)*math.cos(p4)-math.sin(p1)*math.sin(p3)*math.sin(p4)*math.cos(p2)-math.sin(p1)*math.sin(p2)*math.sin(p4)*math.cos(p3)-math.sin(p1)*math.sin(p2)*math.sin(p3)*math.cos(p4))+0.135*(math.sin(p1)*math.cos(p2)*math.cos(p3)-math.sin(p1)*math.sin(p2)*math.sin(p3))+0.155*math.sin(p1)*math.cos(p2),0.2175*(math.sin(p1)*math.cos(p3)*math.cos(p2)*math.cos(p4)-math.sin(p1)*math.sin(p4)*math.cos(p2)*math.sin(p3)-math.sin(p1)*math.sin(p2)*math.sin(p3)*math.cos(p4))+0.135*(math.sin(p1)*math.cos(p3)*math.cos(p2)-math.sin(p1)*math.sin(p2)*math.sin(p3)),0.2175*(math.cos(p2)*math.cos(p3)*math.cos(p4)*math.sin(p1)-math.sin(p1)*math.sin(p2)*math.sin(p3)*math.cos(p4)-math.sin(p1)*math.sin(p2)*math.sin(p4)*math.cos(p3)-math.sin(p1)*math.sin(p3)*math.sin(p4)*math.cos(p2)),0.0,0.2175*(math.sin(p1)*math.sin(p4)*math.cos(p2)*math.cos(p3)+math.sin(p1)*math.sin(p2)*math.cos(p3)*math.cos(p4)+math.sin(p1)*math.sin(p3)*math.cos(p2)*math.cos(p4)-math.sin(p1)*math.sin(p2)*math.sin(p3)*math.sin(p4))+0.135*(math.sin(p1)*math.sin(p2)*math.cos(p3)+math.sin(p1)*math.sin(p3)*math.cos(p2))+0.155*math.sin(p1)*math.sin(p2),0.2175*(math.cos(p1)*math.cos(p2)*math.sin(p3)*math.sin(p4)+math.cos(p1)*math.cos(p3)*math.sin(p2)*math.sin(p4)-math.cos(p1)*math.cos(p2)*math.cos(p3)*math.cos(p4)+math.cos(p1)*math.cos(p4)*math.sin(p2)*math.sin(p3))-0.135*(math.cos(p1)*math.cos(p2)*math.cos(p3)-math.cos(p1)*math.sin(p2)*math.sin(p3))-0.155*math.cos(p1)*math.cos(p2),0.2175*(math.cos(p1)*math.cos(p3)*math.sin(p2)*math.sin(p4)+math.cos(p1)*math.cos(p2)*math.sin(p3)*math.sin(p4)+math.cos(p1)*math.cos(p4)*math.sin(p2)*math.sin(p3)-math.cos(p1)*math.cos(p2)*math.cos(p3)*math.cos(p4))-0.135*(math.cos(p1)*math.cos(p2)*math.cos(p3)-math.cos(p1)*math.sin(p2)*math.sin(p3)),0.2175*(math.cos(p1)*math.cos(p4)*math.sin(p2)*math.sin(p3)-math.cos(p1)*math.cos(p2)*math.cos(p3)*math.cos(p4)+math.cos(p1)*math.cos(p3)*math.sin(p2)*math.sin(p4)+math.cos(p1)*math.cos(p2)*math.sin(p3)*math.sin(p4)),0.0,0.0,0.2175*(math.sin(p2)*math.sin(p3)*math.sin(p4)-math.sin(p2)*math.cos(p3)*math.cos(p4)-math.cos(p2)*math.cos(p3)*math.sin(p4)-math.cos(p2)*math.sin(p3)*math.cos(p4))-0.135*(math.sin(p2)*math.cos(p3)+math.cos(p2)*math.sin(p3))-0.155*math.sin(p2),0.2175*(math.sin(p2)*math.sin(p3)*math.sin(p4)-math.cos(p2)*math.cos(p4)*math.sin(p3)-math.cos(p2)*math.cos(p3)*math.sin(p4)-math.cos(p3)*math.cos(p4)*math.sin(p2))-0.135*(math.cos(p2)*math.sin(p3)+math.sin(p2)*math.cos(p3)),0.2175*(math.sin(p2)*math.sin(p3)*math.sin(p4)-math.cos(p2)*math.cos(p3)*math.sin(p4)-math.cos(p2)*math.cos(p4)*math.sin(p3)-math.cos(p3)*math.cos(p4)*math.sin(p2)),0.0]
    layout = MultiArrayLayout()
    layout.dim = [MultiArrayDimension('height', 3, 2 * 1),
                MultiArrayDimension('width', 5, 2)]
    output=Float64MultiArray()
    output.layout=layout
    output.data=a
    return p2bResponse(output)
    

def p2b_server():
    rospy.init_node('p2b_server')
    s=rospy.Service('/p2b', p2b, callbackp2b)
    
    rospy.spin()
    
if __name__ == '__main__':
    p2b_server()