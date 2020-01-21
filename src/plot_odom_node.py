#! /usr/bin/python2.7
import rospy
import datetime
import datetime
import geometry_msgs.msg

from matplotlib import pyplot

ODOMETRY_TOPIC = "/pose"
OUTPUT_FILE = "/home/husarion/sam_assignment_1_pose_data.csv"

collection_start_time = None
total_collection_time = None
pose_history = []
collection_completed = False

def odom_callback(odometry_message):
    global collection_start_time, total_collection_time, pose_history, collection_completed

    if collection_start_time is None:
        collection_start_time = datetime.datetime.now()

    elapsed_collection_time = (datetime.datetime.now() - collection_start_time).total_seconds()

    if elapsed_collection_time > total_collection_time:
        collection_completed = True
        return

    pose_history.append(odometry_message.pose)


def plot_data():
    global pose_history, total_collection_time

    position_x_components = [
        pose.position.x for pose in pose_history
    ]
    position_y_components = [
        pose.position.y for pose in pose_history
    ]

    rospy.loginfo("Saving position data to csv file: {}".format(OUTPUT_FILE))

    csv_string = "position_x,position_y\n"

    for (x, y) in zip(position_x_components, position_y_components):
        csv_string = csv_string + "{},{}\n".format(str(x), str(y))

    output_stream = open(OUTPUT_FILE, "w")
    output_stream.write(csv_string)
    output_stream.close()


def main():
    global total_collection_time

    rospy.init_node("plot_odom_node")

    total_collection_time = rospy.get_param("~total_collection_time_seconds")

    odom_subscriber = rospy.Subscriber(ODOMETRY_TOPIC, geometry_msgs.msg.PoseStamped, odom_callback)

    rospy.loginfo("Collecting odom data for {} seconds".format(total_collection_time))

    collection_time_poll_rate = rospy.Rate(20)
    while not collection_completed and not rospy.is_shutdown():
        collection_time_poll_rate.sleep()

    rospy.loginfo("Completed data collection. Plotting.")
    plot_data()


if __name__ == "__main__":
    main()
