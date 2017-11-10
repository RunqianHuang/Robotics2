#!/usr/bin/env python
import rospy
import math
from numpy import *
from std_msgs.msg import *
from hw2.srv import *
from geometry_msgs.msg import Point, Pose
from foundations_hw2.msg import JointAngles
  
def callbackangle(data):
    #rospy.loginfo('angle called')
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
    
def callbackposition(data):
    #rospy.loginfo('position called')
    global x
    global y
    global z
    x=data.position.x
    y=data.position.y
    z=data.position.z
    
def callbackp3a(data):
    global p1
    global p2
    global p3
    global p4
    global p5
    global x
    global y
    global z
    global x0
    global y0
    global z0
    p1=p2=p3=p4=p5=x=y=z=0
    x0=data.goal.x
    y0=data.goal.y
    z0=data.goal.z
    rospy.Subscriber('/vrep/youbot/arm/pose', JointAngles, callbackangle)
    rospy.Subscriber('/vrep/youbot/arm/gripper/pose', Pose, callbackposition)
    j = rospy.ServiceProxy('p2b', p2b)
    e = rospy.ServiceProxy('p1b', p1b)
    rospy.wait_for_service('p2b')
    rospy.wait_for_service('p1b')
    rospy.loginfo((x,y,z))
    q=mat([[p1],[p2],[p3],[p4],[p5]])
    output = []
    while True:
        if (abs(x-x0)<0.001)and(abs(y-y0)<0.001)and(abs(z-z0)<0.001):
            break
        tempq=[]
        for i in range(0,5):
            tempq.append(q[i][0])
        data = j(tempq).data
        m = data.data
        row = data.layout.dim[0].size
        column = data.layout.dim[1].size
        jacobian = zeros([row,column])
        for i in range(0,row):
            for k in range(0,column):
                jacobian[i][k]=m[i*5+k]
        jacobian = mat(jacobian)
        jacobian_in = jacobian.I
        delta_e=([[0.1*(x0-x)],[0.1*(y0-y)],[0.1*(z0-z)]])
        delta_q=jacobian_in*delta_e
        q=q+delta_q
        temp = []
        for i in range(0,5):
            temp.append(q[i][0])
        newe = e(temp).goal
        output=temp
        x=newe.x
        y=newe.y
        z=newe.z
        #rospy.loginfo((x,y,z))
        #rospy.loginfo(((x-x0)*(x-x0)+(y-y0)*(y-y0)+(z-z0)*(z-z0)))
    #rospy.loginfo('p3a finished')
    #rospy.loginfo(output)
    return p3aResponse(output)
    

def p3a_server():
    rospy.init_node('p3a_server')
    s=rospy.Service('/p3a', p3a, callbackp3a)
    
    rospy.spin()
    
if __name__ == '__main__':
    p3a_server()