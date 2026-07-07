import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class EnvironmentSubscriber(Node):

    def __init__(self):
        super().__init__('environment_subscriber')
        self.subscription = self.create_subscription(
            String,
            'environment_data',
            self.callback,
            10
        )
        self.get_logger().info('Environment subscriber started')

    def callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = EnvironmentSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
