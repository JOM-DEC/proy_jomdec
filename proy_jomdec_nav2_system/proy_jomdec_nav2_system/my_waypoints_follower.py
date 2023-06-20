import rclpy
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints

class WaypointFollower:
    def __init__(self):
        rclpy.init()
        self.node = rclpy.create_node('my_waypoint_follower')
        self.client = ActionClient(self.node, FollowWaypoints, 'follow_waypoints')
        self.client.wait_for_server()
        self.node.get_logger().info("Connected to follow_waypoints server.")

    def send_waypoints(self, waypoints):
        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints

        self.node.get_logger().info("Sending waypoints...")
        future = self.client.send_goal_async(goal_msg)

        rclpy.spin_until_future_complete(self.node, future)
        if future.result() is not None:
            result = future.result().result
            if result:
                self.node.get_logger().info("Waypoints reached successfully.")
            else:
                self.node.get_logger().warn("Failed to reach waypoints.")
        else:
            self.node.get_logger().error("Failed to send waypoints.")

        self.node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    try:
        follower = WaypointFollower()
        waypoints = [
            [1.0, 2.0, 0.0, 1.0],   # Example waypoint 1
            [3.0, 4.0, 0.707, 0.707] # Example waypoint 2
        ]
        follower.send_waypoints(waypoints)
    except KeyboardInterrupt:
        pass

