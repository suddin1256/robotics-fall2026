# Mission 2

## Frame Context

The rear camera is mounted directly on the robot's chassis, so it position and orientation relative to base_link never change; however, the hallway camera is fixed to the environment, so when base_link moves through the world frame, it will cause the relative position to change.

## Improved Changes

It mainly validates that header.frame_id == hall_camera is the source frame, and it raises a ValueError if it's incorrect. It also transforms the point into the base_link frame as the target frame. For the timestamp handling, instead of using the latest available time it preserves point.header.stamp during the TF lookup. It imports tf2_geometry_msgs to use TF. Then, on failure, if the transform is unavailable or an exception occurs, it returns None and doesn't send velocity commands or publish to motion topics.

## Initial Analysis

I think it's missing dependencies because it uses a function that has no imported library, "tf2_geometry_msgs.do_transform_point". 

## Initial Output

To convert a 3D point detected in the hallway camera frame (hall_camera) into the robot's base frame (base_link), you can use the ROS 2 tf2_ros library to lookup the active rigid-body transform and transform a PointStamped message.

Below is a standard ROS 2 Python node that listens to the TF tree and transforms points from hall_camera to base_link:

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Source

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import tf2_ros
import tf2_geometry_msgs

class PointTransformNode(Node):
    def __init__(self):
        super().__init__('point_transform_node')
        
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
        
        self.timer = self.create_timer(1.0, self.transform_point)

    def transform_point(self):
        point_in_camera = PointStamped()
        point_in_camera.header.frame_id = 'hall_camera'
        point_in_camera.header.stamp = self.get_clock().now().to_msg()
        point_in_camera.point.x = 1.0
        point_in_camera.point.y = 0.5
        point_in_camera.point.z = 0.2

        try:
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                'hall_camera',
                rclpy.time.Time()
            )
            
            point_in_base = tf2_geometry_msgs.do_transform_point(point_in_camera, transform)
            self.get_logger().info(
                f"Transformed point in base_link: x={point_in_base.point.x:.2f}, "
                f"y={point_in_base.point.y:.2f}, z={point_in_base.point.z:.2f}"
            )
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            self.get_logger().warn(f"Could not transform point: {e}")

## Live Issue

Live camera verification is stuck on pending, most likely because python3 scripts/evaluate_camera_transform.py --live timed out or it couldn't look up the active TF transform between hall_camera and base_link. 

## Live Pending

True

## Snapshot

{'captured_at': '2026-09-19T14:46:55.765313+00:00', 'frame_chain': ['hall_camera', 'odom', 'base_link', 'base_scan', 'rear_camera_link'], 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'point_prompts': {'hall_camera_point': 'Transform point (0.5, 0.0, 0.0) from hall_camera to base_link.'}, 'schema_version': 2, 'source': 'live', 'transformed_points': {'hall_camera_point_in_base': {'x': -9.60264599730497e-09, 'y': -1.5}, 'rear_camera_point_in_base': {'x': -1.18, 'y': -1.0206624774663903e-11}, 'scan_point_in_base': {'x': 0.968, 'y': 0.0}}, 'transforms': {'base_scan_to_base_link': {'translation': {'x': -0.032, 'y': 0.0, 'z': 0.172}, 'yaw': 0.0}, 'hall_camera_to_base_link': {'translation': {'x': -9.599863586976825e-09, 'y': -2.0, 'z': 1.19}, 'yaw': 1.5707963268004614}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': -3.1415926535795866}}}

## Synthesis

The initial ai blatantly made its own code with its own library imports, depencencies, and  funtion with out knowing the function naming convention being used in this lab. It created its own ROS node class, used current time instead of point timestamps, and it had error handling. The improved prompt fixed this by using input checks, using original timestamps, and returning "None "if a transforms fail. This is important because using an incorrect transform near people could mean the robot miscalculates a pedestrian location and causing a collision. When transform data is missing, the robot should be able to safely stop motion and return “None”.
