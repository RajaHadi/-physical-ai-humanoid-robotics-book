# Quickstart: Module 1 - ROS 2 Foundations

## Prerequisites
- Ubuntu 22.04 (Native or WSL2)
- ROS 2 Humble installed (`sudo apt install ros-humble-desktop`)
- Node.js 18+ (for documentation build)

## 1. Build the Code
```bash
# Create workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# Link/Copy the package
ln -s /path/to/book/src/ros2_foundations .

# Install dependencies
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y

# Build
colcon build --symlink-install
source install/setup.bash
```

## 2. Run Examples
```bash
# Terminal 1
ros2 run ros2_foundations talker

# Terminal 2
ros2 run ros2_foundations listener
```

## 3. Visualize Robot
```bash
ros2 launch ros2_foundations visualize.launch.py model:=urdf/humanoid.urdf
```

## 4. Build Documentation
```bash
cd website
npm install
npm run start
```
