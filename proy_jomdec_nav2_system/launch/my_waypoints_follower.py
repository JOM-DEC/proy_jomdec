import rospy
import actionlib
from my_robot_msgs.msg import FollowWaypointsAction, FollowWaypointsGoal


class WaypointFollower:
    def __init__(self):
        rospy.init_node('waypoint_follower')
        self.client = actionlib.SimpleActionClient('follow_waypoints', FollowWaypointsAction)
        self.client.wait_for_server()

    def send_waypoints(self, waypoints):
        goal = FollowWaypointsGoal()
        goal.waypoints = waypoints
        self.client.send_goal(goal)
        self.client.wait_for_result()


if __name__ == '__main__':
    try:
        follower = WaypointFollower()

        # Define una lista de puntos a recorrer
        waypoints = [
            [1.0, 2.0, 0.0],  # Punto 1 (x, y, z)
            [3.0, 4.0, 0.0],  # Punto 2 (x, y, z)
            [5.0, 6.0, 0.0]   # Punto 3 (x, y, z)
        ]

        follower.send_waypoints(waypoints)
    except rospy.ROSInterruptException:
        pass
