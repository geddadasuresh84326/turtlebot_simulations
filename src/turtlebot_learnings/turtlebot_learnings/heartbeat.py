#!usr/bin/env python
import rclpy
import time
from rclpy.node import Node

def main(args = None):
    # initialize ros2 communication
    rclpy.init(args=args)

    # create a node
    node = Node("heartbeat_node")

    i = 0 
    max_i = 100 
    while(i <= 100):
        i +=1 
        ros_time_stamp = node.get_clock().now()
        node.get_logger().info(f" I am alive : {ros_time_stamp}")
        time.sleep(1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()