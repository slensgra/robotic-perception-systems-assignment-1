#! /usr/bin/python2.7
import rospy
import datetime
import geometry_msgs.msg

CMD_VEL_TOPIC = "/cmd_vel"

def main():
    rospy.init_node("drive_forward_node")
    drive_speed = rospy.get_param("~drive_speed")
    drive_time = rospy.get_param("~drive_time")

    twist_publisher = rospy.Publisher(CMD_VEL_TOPIC, geometry_msgs.msg.Twist)

    rospy.loginfo(
        "Initializing drive forward node with velocity {drive_speed} m/s and drive time {drive_time} seconds".format(
            drive_speed=drive_speed,
            drive_time=drive_time
        )
    )

    drive_forward_message = geometry_msgs.msg.Twist()
    drive_forward_message.linear.x = drive_speed

    stop_message = geometry_msgs.msg.Twist()
    stop_message.linear.x = 0

    drive_start_time = datetime.datetime.now()
    publish_rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        current_drive_time_seconds = (datetime.datetime.now() - drive_start_time).total_seconds()

        if current_drive_time_seconds > drive_time:
            twist_publisher.publish(stop_message)
            rospy.loginfo("Finished driving. Stopping.")
            break

        twist_publisher.publish(drive_forward_message)
        publish_rate.sleep()

    if not rospy.is_shutdown():
        rospy.loginfo("Terminating drive forward node")


if __name__ == "__main__":
    main()
