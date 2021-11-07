# Waypoints

### Functions:
1. Waypoint generator for ROS with RViz interface
2. Waypoint publisher for publish the waypoints in ROS (robot)
3. Waypoint navigation for publishing 2D navigation goals from waypoints in ROS (robot)

### TODO:
- add comments to script files

Yes, video is speeded up....

https://user-images.githubusercontent.com/90048225/133481640-d8d7f007-2685-453f-a889-6ad5905eb71f.mp4

## Waypoint Generator
### ROS Installation (Copy from ros.org)
[http://wiki.ros.org/melodic/Installation/Ubuntu](http://wiki.ros.org/melodic/Installation/Ubuntu)

Configure your Ubuntu repositories repositories to allow "restricted," "universe," and "multiverse.":
[https://help.ubuntu.com/community/Repositories/Ubuntu](https://help.ubuntu.com/community/Repositories/Ubuntu)

Setup your computer to accept software from packages.ros.org.
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
Set up your keys
```
$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```
Make sure your Debian package index is up-to-date:
sudo apt update
```
$ sudo apt update        # Fetches the list of available updates
$ sudo apt upgrade       # Installs some updates; does not remove packages
$ sudo apt full-upgrade  # Installs updates; may also remove some packages, if needed
$ sudo apt autoremove    # Removes any old packages that are no longer needed
```

ROS Desktop Install: ROS, rqt, rviz, and robot-generic libraries
```
$ sudo apt install ros-melodic-desktop
```
Source bash...
```
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
```

### Install dependencies for building ROS packages, run:
```
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```
Initialize rosdep:
```
$ sudo rosdep init
$ rosdep update
```

### Make ROS workspace
Open new Terminal window.
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
Source bash...
```
$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

## Create waypoints ros package:

```
$ cd catkin_ws/src
$ catkin_create_pkg waypoints
```
Move waypoints folder contents to yours waypoints folder in ROS workspace source folder (assuming here ws is ~/catkin_ws/src/waypoints).
```
$ cd ~/catkin_ws
$ catkin_make
```

# Waypoint generation
### Launch Waypoint generator
```
$ roslaunch waypoints waypoints_generator.launch
```
Or you can (because you can) make *.desktop icon and launch it that way ;) .

Two windows will be open:
1. Rviz -window: where you can add/generate waypoints
2. Text-editor: where you can delete/edit your waypoint (yes i know this is crappy way :( )

### How to use
In the Rviz select tool "2D navigation Goal" (purple arrow) and select yours waypoint locations and direcions on map. Waypoint Generator will draw those waypoints to the map.
Easiest way to delete waypoint is delete it directly from the waypoints.csv file with the text editor.

### Where generated waypoints.csv file is?
```
$ cd ~catkin_ws/waypoints/waypoints
```
There will be waypoints.csv.
You can copy this file to your robots file location and you can use "waypoint publisher" (pub_waypoints.py) and "waypoint navigation" (waypoint_navigation.py) (follow this README) ==> ==>

# Waypoint publisher and navigation
### Waypoint publisher
**Install script**
1. Copy pub_waypoints.py from waypoints/scripts folder to your robot's scripts folder (Remember check that script file is executable (chmod +x pub_waypoints.py))
2. Copy generated waypoints (Use Waypoint generator) waypoints.csv to your robot's waypoints folder
4. Add to your robot's launch file:
```
 <!--  *************** Waypoints ***************  -->
 <node pkg="YOUR ROBOT PACKAGES" name="waypoint_publisher" type="pub_waypoints.py" output="screen"></node>
```
4. Execute "catkin_make" in robot's workspace (catkin_ws)

**Launch your robot**

**If you want to see waypoints in RViz:**
   - In the RViz click "Add" (under "Displays" tree)
   - Select "By topic" tab
   - Select on the list "MarkerArray" waypoints
   - Click OK
   - Check that the "MarkerArray" is activated on "Display" tree
   - You can save RViz setting now (menu: "File" - "Save")

### Waypoint navigation
**Note! Waypoint publisher need to be installed**

**Install script**
1. Copy waypoint_navigation.py from waypoints/scripts folder to your robot's scripts folder (Remember check that script file is executable (chmod +x waypoint_navigation.py))
2. Copy generated waypoints (generated with "Waypoint generator") waypoints.csv to your robot's waypoints folder
3. Execute "catkin_make" in robot's workspace (catkin_ws)

**Launch your robot**

**Launch waypoint navigation**
```
$ rosrun <YOUR ROBOT PACKAGE> waypoint_navigation.py
```

**Remote run with bash script**



## Tip for remote use

https://github.com/Lapland-Robotics/miniATV/tree/main/atv_remote#this-is-for-remote-control-and-monitoring-miniatv-robot

## Troubleshooter:
If some:
```
ERROR: cannot launch node of type [map_server/map_server]: map_server
```
than:
```
sudo apt-get install ros-melodic-map-server
```
NOTE! MISSING "map_server", BUT INSTALLATION PACKAGE IS "map-server"
