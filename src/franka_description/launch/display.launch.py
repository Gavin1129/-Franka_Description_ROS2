from launch import LaunchDescription
from launch_ros.actions import Node
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch_ros.actions import PushRosNamespace
# from launch.actions import GroupAction
# from launch.event_handlers import OnProcessStart, OnProcessExit
# from launch.actions import ExecuteProcess, RegisterEventHandler, LogInfo
from ament_index_python.packages import get_package_share_directory

from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command

def generate_launch_description():

    franka_value = ParameterValue(Command(["xacro ",get_package_share_directory("franka_description")+"/robots/panda_arm_hand.urdf.xacro"]))
    robot_state_pub_franka = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description":franka_value}]

    )
    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher"
    )
    # joint_gui = Node(
    #     package="joint_state_publisher_gui",
    #     executable="joint_state_publisher_gui",
    #     parameters=[{"use_gui":True}]
    # )
    rviz2 = Node(package="rviz2",executable="rviz2") 
    return LaunchDescription([robot_state_pub_franka,rviz2,joint_state_publisher])