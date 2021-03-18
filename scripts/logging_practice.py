#!/usr/bin/env python3

import rospy


def logger():

    rospy.init_node('logger',anonymous=True)
    rate=rospy.Rate(10)
    ints=1

    while not rospy.is_shutdown() and (ints<=20):
        if ints%2==0:
            rospy.loginfo("%i is divisible by2",ints)

        elif ints%3==0:
            rospy.logerr("%i is divisible by3",ints)
        
        elif ints%5==0:
            rospy.logwarn("%i is divisible by 5",ints)

        elif ints%7==0:
            rospy.logfatal("%i is divisible by 7",ints)
        
        else:
            rospy.logdebug("Nothing")
        
        ints+=1
        rate.sleep()

if __name__ == "__main__":
    logger()
    