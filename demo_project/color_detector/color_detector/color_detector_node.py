import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped
from cv_bridge import CvBridge
import cv2
import numpy as np


class ColorDetectorNode(Node):

    def __init__(self):
        super().__init__('color_detector_node')
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.image_callback,
            10
        )
        self.publisher = self.create_publisher(
            PointStamped,
            '/target_position',
            10
        )
        self.bridge = CvBridge()
        self.get_logger().info('Color detector node started')

        self.lower_blue = np.array([100, 80, 80])
        self.upper_blue = np.array([130, 255, 255])

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_blue, self.upper_blue)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            if cv2.contourArea(c) > 500:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                M = cv2.moments(c)
                if M['m00'] > 0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    cv2.circle(cv_image, (cx, cy), 5, (0, 0, 255), -1)

                    pos_msg = PointStamped()
                    pos_msg.header.stamp = self.get_clock().now().to_msg()
                    pos_msg.point.x = float(cx)
                    pos_msg.point.y = float(cy)
                    pos_msg.point.z = 0.0
                    self.publisher.publish(pos_msg)

        cv2.imshow('result', cv_image)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    node = ColorDetectorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
