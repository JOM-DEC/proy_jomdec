import os
import random
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    res = []

   
    launch_robot_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("proy_jomdec_my_world"), 'launch/turtlebot3_my_world.launch.py'))
    )      
    res.append(launch_robot_world)

    launch_robot_nav = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("proy_jomdec_nav2_system"), 'launch/my_nav2_waypoints_follower.launch.py'))
    )      
    res.append(launch_robot_nav)
    
    '''
    .
    .
    .
    .
    '''
    # El resto de lanzadores se añaden teniendo en cuenta el orden de lanzamiento.

    return LaunchDescription(res)        