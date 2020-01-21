echo "Launching roscore"
roscore &

echo "Waiting for roscore to initialize"
sleep 5

echo "Launching husarion serial bridge"
cd /home/husarion/catkin_ws && source devel/setup.bash && rosrun rosbot_webui serial_bridge.sh
