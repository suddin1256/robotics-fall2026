# Mission 1

## Command Path Explanation

A requested command would travel on the /student_cmd_vel topic. The guard node, /course_cmd_vel_guard, checks whether the proposed motion violates any safety rules or constraints, and if it doesn't, approves the request by publishing it to the /cmd_vel topic for /ros_gz_bridge node to pick up and drive the simulation wheels.

## Graph Explanation

A ROS 2 graph shows basically a network of programs that are called nodes, their communication lines as topics that carry messages and data streams between them. For example, the /ros_gz_bridge node translates the simulation data and publishes the LIDAR readings to the /scan topic.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found ranges, which represents an array of distance measurements from the robot, and it includes some values reading .inf where the readings maybe outside the sensor's range limits.

## Tools Explanation

Gazebo is the simulation. It simulates the physical world the robots in; it calculates the kinematics, collisions, and sensor data. RViz, on the other hand, is responsible for visualizing live ROS data streams and sensor feeds so developers like us can inspect what is happening with the robot OS without extra physics computing.
