#!/usr/bin/env python3 

import rospy
from foundation_cource.srv import CalcNumber,CalcNumberResponse
#This is the task for creating a client/server nodes and communicate via Service method
#Here server handles the requests from client and output them to client.
#The server defenition is in srv folder in a .srv file

def handle_request(req):
    if req.opp =="a":
        result_value=req.num1+req.num2
        result_succes=True


    elif req.opp =="s":
        result_value=req.num1-req.num2
        result_succes=True

    elif req.opp =="m":
        result_value=req.num1*req.num2
        result_succes=True

    elif req.opp =="d":
        if req.num2!=0:
            result_value=req.num1/req.num2
            result_succes=True
        else:
            result_value=0
            result_succes=False
    
    else:
        result_value=0
        result_succes=False
    return CalcNumberResponse(result_succes,result_value)

    
def server():
    rospy.init_node("calc_number_server")
    srv=rospy.Service("calculate_number",CalcNumber,handle_request)
    rospy.loginfo("Server ready for calculation request")
    rospy.spin()
if __name__=="__main__":
    server()
