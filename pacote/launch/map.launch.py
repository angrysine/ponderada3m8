from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription,RegisterEventHandler,ExecuteProcess,LogInfo
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import ( OnShutdown,OnProcessExit)
from launch.substitutions import LocalSubstitution

def generate_launch_description():

    turtlesim_world_1 = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'),
        '/turtlebot3_world.launch.py'])
        
    )

    mapper = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_cartographer'), 'launch'),
        '/cartographer.launch.py']),
        launch_arguments={'use_sim_time': 'True'}.items(),
    )



    teleop = Node(
            package='turtlebot3_teleop',
            executable='teleop_keyboard',
            output='screen',
            prefix = 'xterm -e',
          
        )
    teleop_close_event = RegisterEventHandler(
    OnProcessExit(
        target_action=teleop,
        on_exit=[
            LogInfo(msg=(' closed the turtlesim window')),
            ExecuteProcess(
                #os2 run nav2_map_server map_saver_cli -f ~./my_map
               cmd=["ros2", "run", "nav2_map_server", "map_saver_cli", "-f", "./my_map"],
               output='screen'
            )

        ]
    )
)    
    
    return LaunchDescription([
        teleop,
        turtlesim_world_1,
        mapper,
        teleop_close_event
    ],
    
    
    
    )
#ros2 run turtlebot3_teleop teleop_keyboard