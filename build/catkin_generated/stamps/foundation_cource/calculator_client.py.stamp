#!/usr/bin/env python3
import rospy
from foundation_cource.srv import CalcNumber,CalcNumberResponse
#This is the task for creating a client/server nodes and communicate via Service method
#Here client request a task and wait for server to respond. The server defenition is in srv folder in a .srv file
def calculate_number_client(num1,num2,opp):
    rospy.wait_for_service("calculate_number")

    try:
        calculate_number=rospy.ServiceProxy("calculate_number",CalcNumber)
        response=calculate_number(num1,num2,opp)
        return response.success,response.value
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed %s"%e)



if __name__=="__main__":
    rospy.init_node("calculator_client",anonymous=True)
    while not rospy.is_shutdown():
        num1=float(input("Enter First Number: "))
        num2=float(input("Enter Second Number: "))
        opp=str(input("Enter operation: "))
        rospy.loginfo("Requesting calcualtion from server")
        rospy.loginfo("The calculated result is: %s"%str(calculate_number_client(num1,num2,opp)))
