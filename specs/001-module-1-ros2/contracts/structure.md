# Deliverable Structure: Module 1

The module deliverables adhere to the following file hierarchy and contracts.

## 1. Documentation Modules (`modules/ros2/`)

Each markdown file must include standard Docusaurus frontmatter:
```yaml
---
id: [chapter-slug]
title: [Chapter Title]
sidebar_label: [Short Title]
description: [SEO Description]
---
```

**Required Chapters:**
1. `01-introduction.md`: ROS 2 concepts, installation.
2. `02-nodes-topics.md`: Publishers, Subscribers, CLI tools.
3. `03-services-actions.md`: Service/Client, Action Server/Client.
4. `04-urdf-modeling.md`: Building the humanoid URDF.
5. `05-rviz-visualization.md`: Launch files, TF2, RViz.
6. `06-control-loops.md`: Timers, logic, publishing commands.
7. `07-ai-bridge.md`: Integrating Python AI scripts.
8. `08-mini-project.md`: Full "Nervous System" assembly.

## 2. ROS 2 Package (`src/ros2_foundations/`)

**Package Contract:**
- Build system: `ament_python`
- Dependencies: `rclpy`, `std_msgs`, `sensor_msgs`, `geometry_msgs`, `trajectory_msgs`, `urdf`, `xacro`

**Executable Contract (setup.py entry_points):**
- `talker = ros2_foundations.talker:main`
- `listener = ros2_foundations.listener:main`
- `simple_urdf_display = ros2_foundations.urdf_display:main` (launch)
- `controller = ros2_foundations.control_loop:main`
- `ai_bridge = ros2_foundations.ai_bridge:main`

**Topic Contract:**
- `/cmd_vel` (geometry_msgs/Twist): Velocity commands
- `/joint_states` (sensor_msgs/JointState): Robot posture
- `/ai/command` (std_msgs/String): JSON commands from AI
