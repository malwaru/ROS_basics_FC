#include "ros/ros.h"
#include "std_msgs/String.h"



void chatterCallback(const std_msgs::String::ConstPtr& msg)
{

  ROS_INFO("I heard: [%s]", msg->data.c_str());


}

int main(int argc, char ** argv)
{

  ros::init(argc,argv,"listener");

  ros::NodeHandle n;

  ros::Subscriber sub=n.subscribe("chatter",1000,chatterCallback);

  /**
    78    * ros::spin() will enter a loop, pumping callbacks.  With this version, all
    79    * callbacks will be called from within this thread (the main one).  ros::spin()
    80    * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
    81    */

  ros::spin();


  return 0;



}