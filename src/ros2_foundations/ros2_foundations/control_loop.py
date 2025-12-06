import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration
import math

class ControlLoopNode(Node):

    def __init__(self):
        super().__init__('control_loop_node')
        self.imu_subscription = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            10)
        self.imu_subscription  # prevent unused variable warning

        self.imu_publisher = self.create_publisher(Imu, '/imu/data', 10) # Dummy IMU publisher
        self.imu_timer = self.create_timer(0.05, self.publish_dummy_imu) # 20 Hz dummy IMU

        self.joint_trajectory_publisher = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.control_timer = self.create_timer(0.1, self.publish_joint_command) # 10 Hz control loop

        self.get_logger().info('Control Loop Node started.')

        self.current_acceleration = 0.0
        self.joint_position = 0.0
        self.imu_sequence = 0
        self.time_offset = self.get_clock().now().nanoseconds / 1e9

    def publish_dummy_imu(self):
        msg = Imu()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'imu_link' # Assuming an IMU frame

        # Simulate a simple sine wave acceleration
        time_elapsed = self.get_clock().now().nanoseconds / 1e9 - self.time_offset
        msg.linear_acceleration.x = math.sin(time_elapsed) * 5.0 # Max 5 m/s^2
        msg.linear_acceleration.y = 0.0
        msg.linear_acceleration.z = 9.81 # Gravity

        # Dummy angular velocity and orientation
        msg.angular_velocity.x = 0.0
        msg.angular_velocity.y = 0.0
        msg.angular_velocity.z = 0.0
        msg.orientation.x = 0.0
        msg.orientation.y = 0.0
        msg.orientation.z = 0.0
        msg.orientation.w = 1.0

        self.imu_publisher.publish(msg)
        self.imu_sequence += 1
        # self.get_logger().info(f'Published dummy IMU - Accel X: {msg.linear_acceleration.x:.2f}')


    def imu_callback(self, msg):
        self.current_acceleration = msg.linear_acceleration.x
        # self.get_logger().info(f'Received IMU data - Accel X: {self.current_acceleration:.2f}')

    def publish_joint_command(self):
        # Simple control logic: if acceleration is high, move joint
        if self.current_acceleration > 1.0:
            self.joint_position += 0.01 # Increment position slowly
            if self.joint_position > 1.0: # Limit max position
                self.joint_position = 1.0
        elif self.current_acceleration < -1.0:
            self.joint_position -= 0.01 # Decrement position slowly
            if self.joint_position < -1.0: # Limit min position
                self.joint_position = -1.0
        else:
            # Gradually return to center
            if self.joint_position > 0.01:
                self.joint_position -= 0.005
            elif self.joint_position < -0.01:
                self.joint_position += 0.005
            else:
                self.joint_position = 0.0

        joint_command = JointTrajectory()
        joint_command.header.stamp = self.get_clock().now().to_msg()
        joint_command.joint_names = ['shoulder_joint'] # Assuming our URDF has this joint

        point = JointTrajectoryPoint()
        point.positions = [self.joint_position]
        point.time_from_start = Duration(sec=1, nanosec=0) # Reach position in 1 second
        joint_command.points.append(point)

        self.joint_trajectory_publisher.publish(joint_command)
        # self.get_logger().info(f'Published joint command: {self.joint_position:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = ControlLoopNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Control loop node stopped cleanly.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()