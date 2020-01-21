#! /bin/bash
echo "Launching husarion drivers"
cd /home/husarion/catkin_ws && source devel/setup.bash && roslaunch husarion_ros rosbot_drivers.launch
