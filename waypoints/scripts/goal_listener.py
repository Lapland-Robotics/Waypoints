#!/usr/bin/env python

import os
import rospy
import math
import tf.transformations
from geometry_msgs.msg import PoseStamped

FILE = os.path.expanduser("~") + '/catkin_ws/src/waypoints/waypoints/waypoints.csv'

def goal_callback(data):
    print "Goal Received"

    #open(FILE, 'w').close()
    f = file(FILE,"a")
    f.write(str(data.pose.position.x)+","+str(data.pose.position.y)+","+str(data.pose.orientation.z)+","+str(data.pose.orientation.w)+"\n")
    f.close()
    print "Goal added to waypoints file."

rospy.init_node('goal_listener')
rospy.Subscriber("/move_base_simple/goal", PoseStamped, goal_callback, queue_size=1)


r = rospy.Rate(1.0)
while not rospy.is_shutdown():
    r.sleep()
