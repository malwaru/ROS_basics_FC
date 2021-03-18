#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

#This is an example for creating a talker/listener nodes and communicate via publisher/subscriber method

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data) # specifically requesitn data part from data variable



def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('chatter',String,callback)# run callback function everytime a message is received
    rospy.spin()

if __name__=='__main__':
    listener()