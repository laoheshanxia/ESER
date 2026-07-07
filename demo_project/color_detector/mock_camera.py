"""
Mock camera: Publishes pre-generated images as ROS2 Image messages.
No USB camera required. Works with Codespaces.
"""
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os


class MockCamera(Node):

    def __init__(self):
        super().__init__('mock_camera')
        self.publisher = self.create_publisher(Image, '/image_raw', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.bridge = CvBridge()
        self.frame_index = 0
        self.frames = self._load_frames()
        self.get_logger().info(f'Mock camera started: {len(self.frames)} frames loaded')

    def _load_frames(self):
        test_dir = os.path.join(os.path.dirname(__file__), 'test_images')
        frames = []
        for i in range(30):
            path = os.path.join(test_dir, f'frame_{i:02d}.png')
            if os.path.exists(path):
                frame = cv2.imread(path)
                if frame is not None:
                    frames.append(frame)

        if not frames:
            img = np.zeros((480, 640, 3), dtype=np.uint8)
            img[:] = (200, 200, 200)
            x = 100
            cv2.circle(img, (x, 240), 50, (255, 0, 0), -1)
            frames.append(img)

        return frames

    def timer_callback(self):
        frame = self.frames[self.frame_index % len(self.frames)]
        self.frame_index += 1

        x_offset = int((self.frame_index * 5) % 500)
        frame_copy = frame.copy()
        cv2.circle(frame_copy, (100 + x_offset, 240), 50, (255, 0, 0), -1)

        msg = self.bridge.cv2_to_imgmsg(frame_copy, 'bgr8')
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera_frame'
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MockCamera()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
