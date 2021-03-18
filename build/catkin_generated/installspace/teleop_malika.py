#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import String,Float64

from geometry_msgs.msg import Twist
##this is a practice code to see how to publish to topics

def teleop_malika():
    rospy.init_node('malika_move',anonymous=True)
    pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)#publish to the topic cmd_vel
                                                                # the '/' infront of turtle makes it a constant variable 
                                                                # and not a global one. you can see the difference in ros launch tute   
    vel_msg=Twist()
    speed=2
    distance=1
    stop_time=2
    instruction='e'
    rate=rospy.Rate(10)
    while(instruction!='q' and not (rospy.is_shutdown())):
        instruction=input("Enter commands: ")
        
        #if statments create the commands
        if instruction=='w': 
            vel_msg.linear.x=speed
            vel_msg.linear.y=0
            vel_msg.linear.z=0
            vel_msg.angular.x=4
            vel_msg.angular.y=0
            vel_msg.angular.z=0

        elif instruction=='a':
            vel_msg.linear.x=speed
            vel_msg.linear.y=0
            vel_msg.linear.z=0
            vel_msg.angular.x=0
            vel_msg.angular.y=0
            vel_msg.angular.z=2
        elif instruction=='d':
            vel_msg.linear.x=speed
            vel_msg.linear.y=0
            vel_msg.linear.z=0
            vel_msg.angular.x=0
            vel_msg.angular.y=0
            vel_msg.angular.z=-2
        elif instruction=='s':
            vel_msg.linear.x=-speed
            vel_msg.linear.y=0
            vel_msg.linear.z=0
            vel_msg.angular.x=0
            vel_msg.angular.y=0
            vel_msg.angular.z=0

        
        rospy.loginfo(vel_msg)     
               
        pub.publish(vel_msg)
        #time.sleep(2)            
                
                

        # vel_msg.linear.x=0
        # vel_msg.linear.y=0
        # vel_msg.linear.z=0
        # vel_msg.angular.x=0
        # vel_msg.angular.y=0
        # vel_msg.angular.z=0
        # pub.publish(vel_msg)
        rate.sleep()




        
    


if __name__=='__main__':
    try :
        teleop_malika()
    except rospy.ROSInterruptException:
        pass
    
   