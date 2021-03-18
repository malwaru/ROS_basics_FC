#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

using namespace std;

int main(int argc, char **argv)
{

  ros::init(argc,argv,"talker"); // taking the argumets let you remap the name on command line
  ros::NodeHandle n;// This is little like a instnace of a class , it created on begining and destroyed at the end of program
  ros::Publisher chatter_pub=n.advertise<std_msgs::String>("chatter",1000);
  //simillar to this in python
  //pub= rospy.Publisher('chatter',String,queue_size=10)
  ros::Rate loop_rate(10);

  int count=0;

    while(ros::ok()) // This is simmilar to not is.shutdown()
    {
      std_msgs::String msg;
      stringstream ss;
      ss<<"Hello Malika in cpp"<<count;
      msg.data=ss.str();
      ROS_INFO("%s", msg.data.c_str());
      
      chatter_pub.publish(msg);
      ros::spinOnce();

      loop_rate.sleep();
      ++count;

      
    }



  return 0;
}