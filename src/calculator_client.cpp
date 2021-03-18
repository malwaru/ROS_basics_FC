#include "ros/ros.h"
#include "foundation_cource/CalcNumber.h"
#include <iostream>
#include <string>


using namespace std;
int main(int argc, char **argv)
{

    ros::init(argc,argv,"calculator_client");
    if(argc != 3)
    {
        ROS_INFO("Usage: calculator for numbers");
        return 1;
    }

    ros::NodeHandle n;
    ros::ServiceClient client= n.serviceClient<foundation_cource::CalcNumber>("calc_service");
    foundation_cource::CalcNumber srv;
    
    cout<<"Enter num1"<<endl;
    float n11;
    cin>>n11;
    cout<<"Enter num2"<<endl;
    float n22;
    cin>>n22;
    cout<<"Enter operation"<<endl;
    string op11;
    cin>>op11;

    // srv.request.num1 = atoll(argv[1]);// atoll is convert string to long long
    // srv.request.num2 = atoll(argv[2]);
    // srv.request.opp=argc;

    srv.request.num1 = n11;
    srv.request.num2 = n22;
    srv.request.opp=string(op11);


    if(client.call(srv))
    {
        ROS_INFO("Sum: %ld", (long int)srv.response.value);

    }

    else
    {
        ROS_ERROR("Failed to call service add_two_ints");
        return 1;

    }
    
    return 0;

}