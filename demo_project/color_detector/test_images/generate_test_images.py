import cv2
import numpy as np


def create_test_image(width=640, height=480):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    img[:] = (200, 200, 200)

    cv2.rectangle(img, (100, 100), (250, 300), (255, 0, 0), -1)
    cv2.circle(img, (175, 200), 75, (255, 0, 0), -1)

    cv2.rectangle(img, (350, 120), (500, 320), (0, 255, 0), -1)
    cv2.circle(img, (425, 220), 80, (0, 255, 0), -1)

    cv2.rectangle(img, (200, 340), (440, 420), (0, 0, 255), -1)
    cv2.circle(img, (320, 380), 40, (0, 0, 255), -1)

    cv2.imwrite('test_blue_objects.png', img)
    print('Created: test_blue_objects.png')


def create_moving_sequence(num_frames=30):
    width, height = 640, 480
    frames = []

    for i in range(num_frames):
        img = np.zeros((height, width, 3), dtype=np.uint8)
        img[:] = (220, 220, 220)

        x_offset = int(i * 15)
        cv2.circle(img, (100 + x_offset, 240), 50, (255, 0, 0), -1)
        cv2.imwrite(f'frame_{i:02d}.png', img)
        frames.append(f'frame_{i:02d}.png')

    print(f'Created {num_frames} frames for mock camera input')
    return frames


if __name__ == '__main__':
    create_test_image()
    create_moving_sequence()
    print('All test images generated. Run mock_camera.py to play the sequence.')
