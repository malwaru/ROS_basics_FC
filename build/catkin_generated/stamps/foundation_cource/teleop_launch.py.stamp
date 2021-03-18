#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import String,Float64

from geometry_msgs.msg import Twist

##this is a practice code to see how to use launch files work




def teleop_launch():
    rospy.init_node('malika_move_launch',anonymous=True)
    
    pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)#this will be changed so that when i create multiple turtles from launch
                                                                # this will publish to two different cmd_vel topics rather than one 
                                                                #check it in get params function 
    vel=Twist()
    lin_vel=2
    ang_vel=2
    rate=rospy.Rate(10)
    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0 
    while not rospy.is_shutdown():
        
        vel.linear.x=lin_vel
        vel.angular.z=ang_vel
        
        rospy.loginfo(vel)     
               
        pub.publish(vel)
        
        rate.sleep()




        
    


if __name__=='__main__':
    try :
        teleop_launch()
    except rospy.ROSInterruptException:
        pass
    
   