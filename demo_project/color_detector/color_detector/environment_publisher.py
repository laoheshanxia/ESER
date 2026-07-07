import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class EnvironmentPublisher(Node):

    def __init__(self):
        super().__init__('environment_publisher')
        self.publisher = self.create_publisher(String, 'environment_data', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.temperature = 25.3
        self.co2 = 412.0

    def timer_callback(self):
        msg = String()
        msg.data = f'Temperature: {self.temperature:.1f}°C, CO2: {self.co2:.0f}ppm'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.temperature += 0.1
        self.co2 += 1.0


def main(args=None):
    rclpy.init(args=args)
    node = EnvironmentPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
