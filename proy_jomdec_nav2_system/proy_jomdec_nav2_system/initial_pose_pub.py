# initial_pose_pub.py
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped

class Publisher(Node):

    def __init__(self):
        super().__init__('initial_pose_pub_node')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 1)
        timer_period = 0.5  # seconds
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.callback)

    def callback(self):
        msg = PoseWithCovarianceStamped()
        msg.header.frame_id = 'map'

        x = 0.2
        y = 0.0
        o = 1.0

        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.orientation.w = o

        position = self.position(x, y, o)

        self.get_logger().info('Publishing  Initial Position  \n X= 0.2 \n Y=0.0 \n W = 1.0 ')
        self.publisher_.publish(msg)

    def position(self, x, y, o):
        position = [x, y, o]
        return position

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    try:
        rclpy.spin_once(publisher)
    except KeyboardInterrupt:
        publisher.destroy_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()