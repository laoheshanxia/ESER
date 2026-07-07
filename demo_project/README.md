# ROS2 + OpenCV 课堂演示项目

## 快速开始

```bash
# 1. 放到 ROS2 工作空间
cp -r color_detector ~/ros2_ws/src/
cd ~/ros2_ws

# 2. 编译
colcon build

# 3. source
source install/setup.bash

# 4. 跑起来
# 终端 1：模拟摄像头（发送图片流）
python3 path/to/mock_camera.py

# 终端 2：颜色检测节点
ros2 run color_detector color_detector_node

# 终端 3：查看输出坐标
ros2 topic echo /target_position
```

## 文件结构

```
color_detector/
├── package.xml              # 包配置
├── setup.py                 # Python 安装配置
├── setup.cfg                # ROS2 安装配置
├── resource/
│   └── color_detector       # 包标记文件
├── launch/
│   └── demo.launch.py       # 一键启动 launch 文件
├── color_detector/
│   ├── __init__.py
│   ├── environment_publisher.py     # 演示 2：发布者
│   ├── environment_subscriber.py    # 演示 2：订阅者
│   └── color_detector_node.py       # 综合项目：颜色检测节点
├── test_images/
│   └── generate_test_images.py      # 生成测试图片
└── mock_camera.py                   # 模拟摄像头（发布图片流）
```

## 文件说明

| 文件 | 对应课件 | 说明 |
|------|---------|------|
| `environment_publisher.py` | Slides 48-52 | 每秒发布温度/CO2 数据 |
| `environment_subscriber.py` | Slides 54-57 | 订阅并打印环境数据 |
| `color_detector_node.py` | Slides 113-121 | 完整检测节点：订阅图像 → 颜色检测 → 发布坐标 |
| `mock_camera.py` | Slides 87-123 | 用预生成图片模拟摄像头输入，无需 USB 摄像头 |
| `generate_test_images.py` | 课前准备 | 生成蓝/红/绿色测试图片 |
| `demo.launch.py` | Slide 61 | 一键启动 mock 摄像头 + 检测节点 |

## 注意事项

- 本仓库不需要 USB 摄像头，mock_camera.py 自动循环播放测试图片
- 如要追踪其他颜色，修改 color_detector_node.py 中的 HSV 阈值
- 测试图片生成：`python3 test_images/generate_test_images.py`
