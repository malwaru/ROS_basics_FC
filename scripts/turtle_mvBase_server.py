#!/usr/bin/env python3
import rospy
import actionlib
from foundation_cource.msg import turtle_mv_baseAction,turtle_mv_baseFeedback,turtle_mv_baseResult,turtle_mv_baseGoal
import math
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



class receiveMvCommand():
    def __init__(self):

        ## subscribing to pose and publishing to cmd_vel
        self._sub_pose=rospy.Subscriber('/turtle1/pose',Pose,self.receiveposition)
        self._pub_cmd_vel=rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
        ##Setting up action message variables
        self._action_name="move_turtle_action"
        self._feedback=turtle_mv_baseFeedback()
        self._result=turtle_mv_baseResult()
        self._goal=turtle_mv_baseGoal()
        self._action=actionlib.SimpleActionServer(self._action_name,turtle_mv_baseAction,execute_cb=self.callback,auto_start=False)
        self._rate=rospy.Rate(10)

        #Initialise velocites and other variables
        self._vel_msg=Twist()
        self._kp_vel_linear=0.1
        self._kp_vel_angular=0.05

    
        #set up pose and error values
        self._position=np.array([0,0])#current position 
        self._orientation=0#current orientation
        self._goal_linear=np.array([0,0])
        self._goal_angular=0
        self._error_to_goal=np.array([0,0]) #linear and angular error
        
        ## the tolerance values for how close the turtle should go
        self._tolerance_angular=0.5
        self._tolerance_linear=2
        

        #start of action
        self._action.start()


    def sendfeedback(self):
        self._feedback.current_pos=self._position
        self._action.publish_feedback(self._feedback)

    def receiveposition(self,msg):
        self._position=np.array([msg.x,msg.y],dtype='f')
        self._orientation=msg.theta
        

    def calculate_error(self):
        linear_diff=self._goal_linear-self._position
        linear_error=np.linalg.norm(linear_diff)  
        angular_error=float(self._goal_angular-self._orientation)
        errooe=math.atan2(self._goal_linear[1],self._goal_linear[0])-self._orientation
        #angular_error=math.atan2(linear_diff[1],linear_diff[0])
        rospy.loginfo("Error linear %s",str(linear_error))
        rospy.loginfo("Error angular %s",str(angular_error))
        rospy.loginfo("Error in two angs %s",str(errooe))
       

        return linear_error,angular_error

    def send_vel_commands(self):
        
        self._pub_cmd_vel.publish(self._vel_msg)
        


    def callback(self,goal):
        success=False
        rospy.loginfo("Trying to reach %s",goal.order)
        self._goal_linear=np.array([goal.order[0],goal.order[1]],dtype='f')
        self._goal_angular=math.atan2(goal.order[1],goal.order[0])
        rospy.loginfo("Goal linear %s",self._goal_linear)
        rospy.loginfo("Goal angular %s",self._goal_linear)
        self.calculate_error()

        

        while not success:

            if self._action.is_preempt_requested():
                rospy.loginfo("Cancelled by client")
                self._action.set_preempted()
                success=False
                break

            error_lin,erro_ang=self.calculate_error()

            if abs(erro_ang)>self._tolerance_angular:
                self._vel_msg.linear.x=0
                self._vel_msg.angular.z=self._kp_vel_angular*erro_ang
                self.send_vel_commands()

            elif abs(erro_ang)<self._tolerance_angular and abs(error_lin)>self._tolerance_linear:
                self._vel_msg.linear.x=self._kp_vel_linear*error_lin
                self._vel_msg.angular.z=0
                self.send_vel_commands()

            elif (abs(erro_ang)<self._tolerance_angular) and (abs(error_lin)<self._tolerance_linear):
                success=True
                self._result=self._position
                self._action.set_succeeded(self._result)
                break
                               
            self.sendfeedback()
        
       
            self._rate.sleep()

        



    
if __name__ == "__main__":
    rospy.init_node("move_base_server")
    server=receiveMvCommand()
    rospy.spin()