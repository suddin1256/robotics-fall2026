# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Shadib Uddin
- Email: shadib.uddin93@login.cuny.edu

## final.architecture_evidence

The node makes decisions only from each incoming Lidar /scan inputs in real time, calculating velocity directly without saving previous states or maps/ planning routes. For a hybrid system, I would need to add a database that holds on to the lidar data from each position the robot has been in and then use that somehow with the real-time lidar data to make better decisions and requests.

## final.course_reflection

This activity made me realize how essential software is when engineering and designing physical systems. The sheer number of variables that both electrical engineers and software engineers must account for is substantial, from sensor noise to physical delays. Working through this showed me how much I genuinely enjoy robotics and computing, and it solidified my interest in exploring the engineering challenges that bridge software and hardware. 

## final.hardware_next

I would measure real wheel slip on different floor materials and test sensor latency under varying ambient lighting and surface reflectivities, because we can use that data to change the behavior of the robot like slow down velostiy and or treat the inf and nan inputs differently then just a stop, maybe instead of a stop we can set up a rotation exserise that the robot will do a 360 to use other sensors or change the angle of the sensor to detect more information.

## final.middleware_debugging

Using the commands ros2 node info and ros2 topic info --verbose allows me to look at the publisher and subscriber counts and topic naming across /student_cmd_vel and /cmd_vel. If a publisher count is 0 or message types mismatch, the graph pinpoints the broken link in the network.

## final.system_synthesis

Robotics software is difficult because computational processes must interact reliably with an uncertain, continuous physical environment. Unlike traditional software that operates on discrete, straightforward digital inputs, a robotic system deals with sensor noise, physical inertia, wheel slippage, and non-deterministic timing delays across its nodes. During the open-loop motion trials, a command specifying 0.15 m/s for 3.0 s, which would mean a 0.45 m theoretical path, translated to only 0.224 m of actual odometry path distance due to motor ramp-up, wheel slippage, and timing overhead, illustrating the persistent gap between commanded intent and physical execution.

Mission 3 made us implement a reactive program. This program directly maps directy lidar inputs to simple control outputs without maintaining internal state, global path history, or world representations. The trade-off is high execution speed and immediate collision avoidance at the expense of goal-oriented intelligence; a purely reactive robot cannot automatically navigate around dead ends, plan multi-step paths, or recognize when it is trapped.

The ROS 2 middleware connected four distinct computational components across three core communication relationships:

1. ros_gz_bridge published raw laser scans over /scan to the obstacle_guard subscriber.

2. obstacle_guard processed those ranges through Python decision helpers and published proposed velocities onto /student_cmd_vel to the course_cmd_vel_guard subscriber.

3. course_cmd_vel_guard verified safety parameters and published approved velocity commands to /cmd_vel, which ros_gz_bridge received to actuate the wheels in Gazebo.

Timing anomalies and invalid data directly threaten physical safety. Real LiDAR returns frequently contain inf or nan when beams are absorbed, reflected away, or out of range. If software treats missing data as clear open space, the robot drives blindly into undetected obstacles. To enforce a fail-safe posture, the front_distance() function treats any lack of valid readings as None, causing decide_velocity() to command a complete stop (0.0m/s).

The final layer restricting unsafe motion is the course_cmd_vel_guard. Functioning as an independent safety mediator between the student made decision node and the hardware bridge, it limits linear speeds exceeding 0.18 m/s, enforces a 0.5 s timeout to halt the motors if the controlling node drops communication, and blocks unverified trajectory commands.


## final.timing_evidence

Observing that missing or infinite LiDAR returns (inf/nan) must command an immediate stop rather than being treated as clear space. Assuming missing sensor returns mean "no obstacle" leads directly to blind collisions during sensor failures.

## mission_1.command_path_explanation

A requested command would travel on the /student_cmd_vel topic. The guard node, /course_cmd_vel_guard, checks whether the proposed motion violates any safety rules or constraints, and if it doesn't, approves the request by publishing it to the /cmd_vel topic for /ros_gz_bridge node to pick up and drive the simulation wheels.

## mission_1.graph_explanation

A ROS 2 graph shows basically a network of programs that are called nodes, their communication lines as topics that carry messages and data streams between them. For example, the /ros_gz_bridge node translates the simulation data and publishes the LIDAR readings to the /scan topic.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found ranges, which represents an array of distance measurements from the robot, and it includes some values reading .inf where the readings maybe outside the sensor's range limits.

## mission_1.tools_explanation

Gazebo is the simulation. It simulates the physical world the robots in; it calculates the kinematics, collisions, and sensor data. RViz, on the other hand, is responsible for visualizing live ROS data streams and sensor feeds so developers like us can inspect what is happening with the robot OS without extra physics computing.

## mission_2.measurement_explanation

For the first curved trial, the estimated traveled path is 0.289 m because it tracks the actual curved arc path that the wheels took over time. However, the start-to-end distance measures the straight-line displacement between the starting point and the finishing point, which would yield different values since the robot hasn't traveled in a straight line.

## mission_2.modified_settings

{'linear_x': 0.13, 'angular_z': 0.8, 'duration': 4.0}

## mission_2.motion_comparison

My predictions were roughly correct; however, I have failed to understand the real-world aspects of the environment that the robot is in. For the straight-line trial, I predicted the robot would move 0.45 meters forward. While the commanded path length was calculated to be 0.45 m, as I've said, the estimated traveled path recorded from odometry was only 0.224 m. This means that there was wheel slippage occurring on the robot when it tried to accelerate, which prevented the robot from moving to my predicted distance.

## mission_2.prediction_locks

{'curve': '2026-09-05T16:13:54.403524+00:00', 'curve_modified': '2026-09-05T16:17:22.763315+00:00', 'rotation': '2026-09-05T16:11:52.888418+00:00', 'straight': '2026-09-05T16:07:56.865400+00:00'}

## mission_2.predictions

{'curve': 'I predict a curve because the robot is gonna move both forward and turn right for 4 seconds, which will make a right-hand curve', 'curve_modified': 'The curve is gonna go the opposite direction, going left instead of right, and it will be a much tighter curve because the turning speed is faster', 'rotation': 'I predict its position will remain the same while its direction will turn left.', 'straight': 'I predict the robot will move about .45 meters forward only.'}

## mission_2.safety_explanation

The command guard checks every incoming velocity message against safety limits. So if for example, if the velocity is too high and the robot will lose traction, the guard can verify that before that happens and limit the speed. The Final zero command makes sure that the robot will receive a stop request so it doesn't run away. Finally, the Stale_command timeout, similar to the final zero, of the robot doesn't receive a new request within 0.5 seconds, it will send the stop command to the robot to stop movement since that is a sign that the program has crashed.

## mission_3.data_to_command

1. front_distance() iterates through the LiDAR ranges list using the enumerate() funtion to calculate each beam's angle.
2. It then filters for valid, finite, and positive readings within the frontal cone (abs(angle) <= half_width_radians) and returns the minimum distance found or None if it's empty.
3. decide_velocity() then receives that minimum distance: if it is None or less than the stop_distance, it returns 0.0 or stop; otherwise, it returns the requested forward speed bounded between 0.0 and 0.18 m/s.

## mission_3.missing_data_safety

It follows the fail-safe protocol. If there are missing or non-finite measurements, such as when the lidar sensor disconnects or the light beam is absorbed or reflected away, treating missing data as an empty path could cause the robot to drive blindly into an undetectable hazard.

## mission_3.system_layers

The obstacle_guard node subscribes to  /scan messages and passes the data to the Python decision functions to compute a desired velocity. The node then publishes that proposed motion request to the /student_cmd_vel topic. Finally, the course command guard inspects /student_cmd_vel against safety boundaries and timeouts before approving and publishing the command to /cmd_vel topic for the robot to execute.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
