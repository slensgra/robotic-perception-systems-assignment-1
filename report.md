# Robotic Perception Systems Assignment 1

In this git repository is the data collected for assignment 1 along with the source code for collecting the data. Each node is briefly described here along with the launch files

## Node for part 1 (driving forward)

This node operates by publishing a `Twist` message from the `geometry_msgs` package to the `/cmd_vel` topic. It publishes a forward message in which the message's `linear.x` component is set to the desired speed in meters per second. A while loop in the node repeatedly publishes this forward message until the desired amount of time elapses and then publishes a "stop" message -- one in which the `linear.x` component is set to `0`. The desired drive speed and the desired drive time are set as ros node parameters.

## Node for part 3 (plotting odom data)

This node operates by starting up a subscriber to the `/pose` topic which publishes `geometry_msgs.PoseStamped` messages which encode the robot's position in the `/odom` frame. This data comes from a combination of wheel encoders and IMUs in the robot. The node starts the subscriber and reads the desired data collection time in seconds as a ros node parameter. After the desired amount of time has elapsed, the position history is read and written to a csv file. As a post processing step, the script `plot_csv_position_data.sh` can be used to get a scatter plot of the position data. The provided csv file is the result of driving the robot forward for 20 seconds at 0.1 meters per second. The data collection node takes longer to spin up than the driving node, so there is an offset in the data and the driving. A screenshot of the plot is provided. An example output can be found in the file `X-y-odom-plot.png`.

## Part 2 experiment

For Part 2, the launch file `record_sensors_while_driving.launch` may be used. The bag files from this experiment are in the `bag_files` directory. A csv file with manual measurements taken from a video of the vehicle driving are provided in the same directory.

## Evaluation

For part 2, the robot was video taped while driving forward for the specified distance over a measuring tape. The robot drove forward about the specified one meter. 
