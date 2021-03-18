#include "ros/ros.h"
#include "foundation_cource/CalcNumber.h"

bool cal_handle(foundation_cource::CalcNumber::Request &req,foundation_cource::CalcNumber::Response &res)
{
    float result_value=0;
    bool result_succes=true;

    if (req.opp =="a")
    {
        result_value=req.num1+req.num2;
        result_succes=true;

    }
        


    else if (req.opp =="s")
    {
        result_value=req.num1-req.num2;
        result_succes=true;
    }
        

    else if (req.opp =="m")
    {
        result_value=req.num1*req.num2;
        result_succes=true;
    }
        

    else if (req.opp =="d")
    {
         if (req.num2!=0)
         {
             result_value=req.num1/req.num2;
             result_succes=true;
         }
            
        else
        {
            result_value=0;
            result_succes=false;
        }
            


    }
       
    
    else
    {
        result_value=0;
        result_succes=false;
    }
        
    res.success=result_succes;
    res.value=result_value;
    //ROS_INFO("request: x=%ld, y=%ld  operation: %s", (long int)req.num1, (long int)req.num2,req.opp);
    //ROS_INFO("sending back response: [%ld]", (long int)res.value);
    
    return true;


}
int main(int argc,char** argv)
{
    ros::init(argc,argv,"calculator_server");
    ros::NodeHandle n;

    ros::ServiceServer service = n.advertiseService("calc_service",cal_handle);
    ROS_INFO("Calculator server Ready");
    ros::spin();
    return 0;


}