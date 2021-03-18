#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
#This is an example for creating a talker/listener nodes and communicate via publisher/subscriber method
def talker():

	rospy.init_node('talker',anonymous=True) #if anonymous is true it will assign a random number to end of node so each new topic is unique
	pub= rospy.Publisher('chatter',String,queue_size=10)
	#incoming_message=rospy.get_param("username","ObiWan")										
	hello_str="Hello there %s" %rospy.get_param("username","ObiWan")
	rate=rospy.Rate(10) #10Hz
	while not rospy.is_shutdown():# as long as rospy is not shutdown
		#hello_str= "Hi malika %s" % rospy.get_time() # the string to send
		
		rospy.loginfo(hello_str) #send string to roslog file using 
		pub.publish(hello_str)
		rate.sleep() # 

if __name__ == '__main__': ## ask about this
	try:
		talker()

	except rospy.ROSInterruptException:
		pass