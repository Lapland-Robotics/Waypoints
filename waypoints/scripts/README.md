## Scrips for waypoint generation:

### generator_pub_waypoints.py:
**Script for publish waypoints. Waypoints in file waypoints.csv in folder Waypoints/waypoints.**


### goal_listener.py:
**Script listening "/move_base_simple/goal" (user give new 2d Goal) and add coordinates of goal to waypoints.csv file (in folder /waypoints.**


### open_gedit.py:
**Script open waypoints.csv file in text editor "gedit" from folder /waypoints.**


## Scripts for robot (use these in your robot):

**Note! Check FILE paths in the script files and change right path for your robot/installation**

### pub_waypoints.py:
**Script for publish waypoints. Waypoints in file waypoints.csv in folder  < YOUR PACKAGE >/waypoints.**


### waypoint_navigation.py:
**Script for launch/start navigation via waypoint. Waypoints need to be publish first with pub_waypoints.py.**
