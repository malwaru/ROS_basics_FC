#!/usr/bin/env python3

import rospy
import actionlib
from foundation_cource.msg import turtle_mv_baseAction, turtle_mv_baseGoal


def printfeedback(msg):
    print("Turtle is currently at: ",msg)
def sendMvCommand():
    client=actionlib.SimpleActionClient("move_turtle_action",turtle_mv_baseAction)
    client.wait_for_server()
    goal_input=[0,0] # intialise input goal with zeros
    goal_input[0]=int(input("Enter X coordinate: "))
    goal_input[1]=int(input("Enter Y coordinate: "))
    goal=turtle_mv_baseGoal()
    goal.order.append(goal_input[0])
    goal.order.append(goal_input[1])
    rospy.loginfo("Started to send goal order from client to server")
    client.send_goal(goal,feedback_cb=printfeedback)
    client.wait_for_result()

    return client.get_result()
  




if __name__ == "__main__":
    try:
        rospy.init_node("move_base_client")
        result=sendMvCommand()
        rospy.loginfo("Final position is %s",str(result.final_pos))

    except rospy.ROSInitException as e:
        rospy.logerr("Didnt work in client main %s",e)

    