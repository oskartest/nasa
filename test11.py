#!/usr/bin/env python3
from tkinter.constants import NO
import rospy
from std_msgs.msg import float32

def callback(data):
    yaho = data.data
    rospy.loginfo(yaho)
    
def listener():
    rospy.init_node('sub_steers', anonymous=True)
    rospy.Subscriber("steers", float32, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
