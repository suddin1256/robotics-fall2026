# Mission 2

## Predictions

{'straight': 'I predict the robot will move about .45 meters forward only.', 'rotation': 'I predict its position will remain the same while its direction will turn left.', 'curve': 'I predict a curve because the robot is gonna move both forward and turn right for 4 seconds, which will make a right-hand curve', 'curve_modified': 'The curve is gonna go the opposite direction, going left instead of right, and it will be a much tighter curve because the turning speed is faster'}

## Prediction Locks

{'straight': '2026-09-05T16:07:56.865400+00:00', 'rotation': '2026-09-05T16:11:52.888418+00:00', 'curve': '2026-09-05T16:13:54.403524+00:00', 'curve_modified': '2026-09-05T16:17:22.763315+00:00'}

## Motion Comparison

My predictions were roughly correct; however, I have failed to understand the real-world aspects of the environment that the robot is in. For the straight-line trial, I predicted the robot would move 0.45 meters forward. While the commanded path length was calculated to be 0.45 m, as I've said, the estimated traveled path recorded from odometry was only 0.224 m. This means that there was wheel slippage occurring on the robot when it tried to accelerate, which prevented the robot from moving to my predicted distance.

## Measurement Explanation

For the first curved trial, the estimated traveled path is 0.289 m because it tracks the actual curved arc path that the wheels took over time. However, the start-to-end distance measures the straight-line displacement between the starting point and the finishing point, which would yield different values since the robot hasn't traveled in a straight line.

## Safety Explanation

The command guard checks every incoming velocity message against safety limits. So if for example, if the velocity is too high and the robot will lose traction, the guard can verify that before that happens and limit the speed. The Final zero command makes sure that the robot will receive a stop request so it doesn't run away. Finally, the Stale_command timeout, similar to the final zero, of the robot doesn't receive a new request within 0.5 seconds, it will send the stop command to the robot to stop movement since that is a sign that the program has crashed.

## Modified Settings

{'linear_x': 0.13, 'angular_z': 0.8, 'duration': 4.0}
