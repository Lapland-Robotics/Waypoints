#!/usr/bin/env python
# Script open waypoints.csv file in text editor "gedit" from folder /waypoints.

import os
FILE = os.path.expanduser("~") + '/catkin_ws/src/waypoints/waypoints/waypoints.csv'
os.system("gedit "+FILE)
