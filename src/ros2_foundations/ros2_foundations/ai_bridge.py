import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Imu # To simulate receiving sensor data

import json

class AIBridgeNode(Node):

    def __init__(self):
        super().__init__('ai_bridge_node')

        # Subscriber for commands from an external AI (via another ROS node)
        self.ai_command_subscription = self.create_subscription(
            String,
            '/ai/command',
            self.ai_command_callback,
            10
        )
        self.ai_command_subscription # prevent unused variable warning

        # Publisher to send processed ROS data to an external AI (via another ROS node)
        self.ai_data_publisher = self.create_publisher(String, '/ai/data_to_agent', 10)

        # Subscriber for simulated sensor data within ROS
        self.imu_subscription = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_data_callback,
            10
        )
        self.imu_subscription # prevent unused variable warning

        self.get_logger().info('AI Bridge Node started.')

    def ai_command_callback(self, msg):
        """
        Callback for commands received from the external AI.
        Translates string command (e.g., JSON) to internal ROS actions.
        """
        try:
            command_dict = json.loads(msg.data)
            self.get_logger().info(f"Received AI command: {command_dict}")
            # Example: Process command_dict and then publish a ROS action/service request
            # For this example, we just log it.
        except json.JSONDecodeError:
            self.get_logger().error(f"Failed to decode AI command JSON: {msg.data}")

    def imu_data_callback(self, msg):
        """
        Callback for ROS sensor data.
        Translates ROS sensor data to a format suitable for the external AI.
        """
        # Create a simple JSON representation of the IMU data
        data_for_ai = {
            "linear_acceleration_x": msg.linear_acceleration.x,
            "angular_velocity_z": msg.angular_velocity.z,
            "timestamp": msg.header.stamp.sec + msg.header.stamp.nanosec / 1e9
        }
        json_data = json.dumps(data_for_ai)
        
        ai_data_msg = String()
        ai_data_msg.data = json_data
        self.ai_data_publisher.publish(ai_data_msg)
        # self.get_logger().info(f"Published data to AI: {json_data}")


def main(args=None):
    rclpy.init(args=args)
    node = AIBridgeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('AI Bridge node stopped cleanly.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
