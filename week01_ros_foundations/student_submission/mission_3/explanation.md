# Mission 3

## Data To Command

1. front_distance() iterates through the LiDAR ranges list using the enumerate() funtion to calculate each beam's angle.
2. It then filters for valid, finite, and positive readings within the frontal cone (abs(angle) <= half_width_radians) and returns the minimum distance found or None if it's empty.
3. decide_velocity() then receives that minimum distance: if it is None or less than the stop_distance, it returns 0.0 or stop; otherwise, it returns the requested forward speed bounded between 0.0 and 0.18 m/s.

## Missing Data Safety

It follows the fail-safe protocol. If there are missing or non-finite measurements, such as when the lidar sensor disconnects or the light beam is absorbed or reflected away, treating missing data as an empty path could cause the robot to drive blindly into an undetectable hazard.

## System Layers

The obstacle_guard node subscribes to  /scan messages and passes the data to the Python decision functions to compute a desired velocity. The node then publishes that proposed motion request to the /student_cmd_vel topic. Finally, the course command guard inspects /student_cmd_vel against safety boundaries and timeouts before approving and publishing the command to /cmd_vel topic for the robot to execute.
