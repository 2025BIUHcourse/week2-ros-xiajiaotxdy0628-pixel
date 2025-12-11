#include <ros/ros.h>
int main(int argc, char **argv){
  ros::init(argc, argv, "hello_node");
  ROS_INFO("Hello from ROS1 Noetic - week2!");
  return 0;
}
