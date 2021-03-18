#!/usr/bin/env python3
import rospy
import random
from foundation_cource.srv import GetRandomNumber,GetRandomNumberResponse
#from __future__ import print_function use the print function with this. or use loginfo method

#This is an example for creating a client/server nodes and communicate via Service method
#Here server handles the requests from client and output them to client.
#The server defenition is in srv folder in a .srv file
def handler_request(req):
    random_int=random.randint(req.start,req.stop)
    rospy.loginfo("Return random number: %s"%random_int)
    return GetRandomNumberResponse(random_int)

def server():
    rospy.init_node("random_number_server")
    srv=rospy.Service("get_random_number",GetRandomNumber,handler_request)
    rospy.loginfo("Server ready for request")
    rospy.spin()


if __name__=="__main__":
    server()