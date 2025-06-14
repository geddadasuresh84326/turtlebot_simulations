#!usr/bin/env python

import rclpy
from rclpy.node import Node

class HeartBeatNode(Node):
    def __init__(self,node_name,time_period = 0.2):
        # call super() in the constructor to initialize the Node object
        # the parameter we pass is the node name
        self._node_name = node_name
        super().__init__(self._node_name)

        # create a timer sending two parameters:
        # - the duration between two callbacks (0.2 seconds)
        # - the timer function (timer_callback)
        self.create_timer(time_period,self.timer_callback)

    def timer_callback(self):
        ros_time_stamp = self.get_clock().now()
        self.get_logger().info(f"{self._node_name} is alive... {ros_time_stamp}")
    

def main(args = None):
    # initialize the ROS2 communication
    rclpy.init(args=args)

    node = HeartBeatNode(node_name="heartbeat_checker")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()