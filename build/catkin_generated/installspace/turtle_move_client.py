#!/usr/bin/env python3

import rospy
import roslib
import actionlib

from foundation_cource.msg import MoveTurtleAction,MoveTurtleGoal

def turtle_move_client():
    #start the client node and set it to moveturtle action
    client=actionlib.SimpleActionClient("Turtle_move_ac_client",MoveTurtleAction)
    #wait until the server is active to start sending goals
    client.wait_for_server()
    #create a goal to send 
    goal=MoveTurtleGoal()
    #request x and y goals from user and cast it to float
    goal[0]=float(input("Enter goal X: "))
    goal[1]=float(input("Enter goal Y: "))
    #send goal to action server
    client.send_goal(goal)
    #wait fot client to finish performing action
    client.wait_for_result()
    #return the final pos to main method to be printed
    return client.get_result()






if __name__ == "__main__":
    try:
        rospy.init_node('move_turtle_client')
        result=turtle_move_client()
        rospy.loginfo("Final position is x:%f , y:%f ",result.final_pos[0],result.final_pos[1])
    except rospy.ROSInterruptException:
        rospy.loginfo("Program interupted before completion")