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