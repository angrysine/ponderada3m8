from launch import LaunchDescription,LaunchContext,LaunchService
from launch_ros.actions import Node,LifecycleNode
from launch_ros.event_handlers import OnStateTransition

from launch.actions import IncludeLaunchDescription,RegisterEventHandler,ExecuteProcess,LogInfo,EmitEvent
import os
from launch.events.process import ProcessStarted
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import ( OnProcessExit,OnProcessStart)



def generate_launch_description():
    
    gazebo = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'),
        '/turtlebot3_world.launch.py'])
        
    )

    saved_map = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_navigation2'), 'launch'), '/navigation2.launch.py']), launch_arguments={'use_sim_time': 'True', 'map':'my_map.yaml'}.items())
     
    nav2 = Node(
            package='pacote',
            executable='node',
            output='screen',
          prefix = 'xterm -e',
        )

    return LaunchDescription([
       nav2,
        saved_map,
        gazebo,
        
       
    ],
    
    
    
    )
#ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=False map:=path/to/map.yaml
if __name__ == '__main__':
    ls = LaunchService()
    ls.include_launch_description(generate_launch_description())
    ls.run()