#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import actionlib
import math
from foundation_cource.msg import MoveTurtleAction,MoveTurtleFeedback,MoveTurtleResult


class MoveTurtleAction():
    
    def __init(self):
        #defining action file classes to variables
        self._feedback=MoveTurtleFeedback
        self._result=MoveTurtleResult
        self._action_name="Turtle_move_ac_client"
        #subcribing to pose and publish to cmd_vel and start action server
        self._as=actionlib.SimpleActionServer(self._action_name,MoveTurtleAction,excecute_cb=self.execute_cb,auto_start=False)
        self._sub_pos=rospy.Subscriber('/turtle1/pose',Pose,self._pose_callback)
        self._pub_cmd_vel=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
        self._rate=10
        ## defining and initilasing vel message
        self._vel_message=Twist()
        self._vel_msg.linear.x=0
        self._vel_msg.linear.y=0
        self._vel_msg.linear.z=0
        self._vel_msg.angular.x=0
        self._vel_msg.angular.y=0
        self._vel_msg.angular.z=0
        self._kp_vel_linear=1
        self._kp_vel_angular=1
        ## the tolerance values for how close the turtle should go
        self._tolerance_angular=0.5
        self._tolerance_linear=0.1
        #set up position call back values
        self.position=[0,0]
        self.orientation=0
        self._goal=[0,0]
        
        self._as.start()


    ##Function to take pose values    
    def _pose_callback(self,msg):
        self.position=[msg.x,msg.y]
        self.orientation=msg.theta



    def calculate_error(self):
        x_goal=self._goal.order[0]
        y_goal=self._goal.order[1]
        theta_goal=math.atan2(y_goal,x_goal)
        error_x=self._goal.order[0]-self.position[0]
        error_y=y_goal-self.position[1]
        error_linear=(error_x**2)+(error_y**2)
        error_theta=theta_goal-self.orientation

        return error_linear,error_theta


    #this is exceuted everytime a new goal is received
    def excecute_cb(self,goal):
        #Set up some helping variables
        r=rospy.Rate(self._rate)
        success=True # set task success true initially then if it completes sucessfull in while, i dont have to change the value
        self._goal=[goal.order[0],goal.order[1]]

        


        #initialise the feedback with zeros can use current_pos[0]=0 instead of append 
        self._feedback.current_pos=[]
        self._feedback.current_pos.append(0)
        self._feedback.current_pos.append(0)
        
        #starting feedback and logging the initial values
        rospy.loginfo('%s: Executing, move %i with initial values %i, %i' % (self._action_name, goal.order, self._feedback.current_pos[0], self._feedback.current_pos[1]))
        
        #while error_linear>(self._tolerance_linear):
        while not rospy.is_shutdown():

            #calculate erroe values at beginging           
           
            error_linear,error_theta=calculate_error()
            

            #check if client asked to cancel
            if self._as.is_preempt_requested():
                rospy.loginfo("%s Cancelled by client request",self._action_name)
                self._as.set_preempted()
                success==False
                break

            #command loop  #get pose and calculage cmd vel here
            
            if (error_theta>self._tolerance_angular) or (error_linear>self._tolerance_linear):
                self._vel_message.angular.z=self._kp_vel_angular*error_theta


            elif(error_theta<=self._tolerance_angular) and (error_linear>self._tolerance_linear):
                self._vel_message.linear.x=self._kp_vel_linear*error_linear
           
            


            if (error_theta<self._tolerance_angular) and (error_linear<self._tolerance_linear):
                success=True
                break
            #send feedback and 
            self._feedback.current_pos[0]=self.position[0]
            self._feedback.current_pos[1]=self.position[1]
            self._as.publish_feedback(self._feedback)
            self._pub_cmd_vel.publish(self._vel_message)
            r.sleep()#check the value


        #if task is successful set and send result
        if success:
            self._result.final_pos=self._feedback.current_pos
            rospy.loginfo("%s action server succeeded",self._action_name)
            self._as.set_succeeded(self._result)




if __name__ == "__main__":
    rospy.init_node("move_turtle_server")
    server=MoveTurtleAction()
    rospy.spin()