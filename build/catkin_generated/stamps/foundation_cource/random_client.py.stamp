#!/usr/bin/env python3
import rospy
from foundation_cource.srv import GetRandomNumber, GetRandomNumberResponse
#This is an example for creating a client/server nodes and communicate via Service method
#Here client request a task and wait for server to respond. The server defenition is in srv folder in a .srv file
def get_random_number_client(start,stop):
    rospy.wait_for_service("get_random_number")

    try:
        get_random_number=rospy.ServiceProxy("get_random_number",GetRandomNumber)
        response=get_random_number(start,stop)
        return response.result
    except rospy.ServiceException as e:
        rospy.logerror("Service call failed %s"%e)


if __name__=='__main__':
    rospy.init_node("random_client",anonymous=True)
    while not rospy.is_shutdown():
        start=int(input("start: "))
        stop=int(input("stop: "))
        rospy.loginfo("Requesting a random int")
        rospy.loginfo("Randomm int : %s"%get_random_number_client(start,stop))

    