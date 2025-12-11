#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def circle():
    rospy.init_node('turtle_circle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    move = Twist()
    move.linear.x = 2.0
    move.angular.z = 1.8
    while not rospy.is_shutdown():
        pub.publish(move)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
