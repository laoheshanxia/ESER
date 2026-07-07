# ESER
节能减排创新实践
# ESER Innovation Practice — ROS2 & OpenCV Smart Perception

> 节能减排创新实践课程 · ROS2与OpenCV智能感知技术

---

## 📌 这是什么

本仓库是**节能减排创新实践课程**中《ROS2与OpenCV智能感知技术》一课的配套代码与课件。

**一句话**：教机器人"看见"颜色并作出反应——用 ROS2 让机器人互相通信，用 OpenCV 让机器人看懂画面。

---

## 🎯 你能学到什么

- ROS2 基础：节点、话题、发布者/订阅者
- OpenCV 基础：图像处理、颜色检测、轮廓追踪
- ROS2 + OpenCV 集成：让视觉数据在机器人系统中流转
- 完整项目：一个能"看见指定颜色、追踪目标、输出坐标"的 ROS2 节点

> 不需要计算机专业背景。有基础 Python 知识即可，零基础也备有速查。

---

## 📦 仓库结构

```
├── docs/
│   └── 学生课前准备手册.md     ← 学生看这个
└── demo_project/
    └── color_detector/         ← ROS2 演示包（完整可运行）
        ├── package.xml
        ├── setup.py
        └── color_detector/
            ├── environment_publisher.py    # 发布者节点
            ├── environment_subscriber.py   # 订阅者节点
            └── color_detector_node.py      # 颜色检测综合项目
```

---

## 🚀 快速开始

### 方案 A：本地安装（推荐）

按 [`docs/学生课前准备手册.md`](docs/学生课前准备手册.md) 的 WSL2 步骤安装环境，然后：

```bash
# 克隆本仓库
git clone https://github.com/laoheshanxia/ESER.git
cd ESER

# 将演示包放到 ROS2 工作空间
mkdir -p ~/ros2_ws/src
cp -r demo_project/color_detector ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash

# 终端 1：运行发布者
ros2 run color_detector environment_publisher

# 终端 2：运行订阅者
ros2 run color_detector environment_subscriber
```

### 方案 B：GitHub Codespaces（零安装）

点击仓库右上角的 **Code** → **Create codespace on main**，等待 2 分钟，终端直接可用：

```bash
# ROS2 + OpenCV 已预装，直接运行
ros2 run color_detector environment_publisher
```

> ⚠️ Codespaces 无法连接 USB 摄像头，课堂演示用模拟图片输入替代。

---

## 📋 课前准备

快速 3 步：

1. **看** [`docs/学生课前准备手册.md`](docs/学生课前准备手册.md)（5 分钟）
2. **选** 本地安装（WSL2）或 Codespaces（浏览器）
3. **验** 终端跑 `ros2 --help`，看到帮助信息即就绪

遇到问题 → 在课程群提问，或直接来教室用 Codespaces。

---

## 📝 课程信息

| 项目 | 内容 |
|------|------|
| 课程 | 节能减排创新实践 |
| 课时 | 150 分钟（纯讲授 + 演示） |
| 面向 | 大二能源环境专业 |
| 预备知识 | 基础 Python（无基础有速查） |
| 技术栈 | ROS2 Humble + OpenCV 4.x + Python 3.10 |
