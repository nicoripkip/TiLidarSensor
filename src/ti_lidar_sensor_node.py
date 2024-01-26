#!/usr/bin/env python3


import rospy


def main():
    rospy.init_node("ti_lidar_sensor")
    rospy.loginfo("Yo mama")


    rospy.spin()


if "__main__" == __name__:
    main()
