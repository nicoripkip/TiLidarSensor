#!/usr/bin/env python3


import rospy
import ti_lidar_sensor as tls


def main():
    rospy.init_node("ti_lidar_sensor")
    rospy.loginfo("Yo mama")
    
    lidar_sensor = LidarSensor(0x)

    rospy.spin()


if "__main__" == __name__:
    main()
