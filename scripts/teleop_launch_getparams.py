#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import String,Float64

from geometry_msgs.msg import Twist

##this is a practice code to see how to use launch files work while using get params function 




def teleop_launch():
    rospy.init_node('malika_move_launch_getparams',anonymous=True)
    
    pub=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)#this will be changed so that when i create multiple turtles from launch
                                                                # this will publish to two different cmd_vel topics rather than one 
                                                                # the '/ ' beofore turtle was removed

    vel=Twist()
    lin_vel=rospy.get_param("lin_vel",2.0)# the default is set to 2 so that even if we use this without launch just use rosrun we will have 
                                          # initiated a value
    ang_vel=rospy.get_param("ang_vel",2.0)
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
    
   