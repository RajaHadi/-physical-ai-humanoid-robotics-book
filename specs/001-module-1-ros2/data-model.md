# Data Model: Module 1 - ROS 2 Foundations

## ROS 2 Entities

### Node
Represents a single process in the ROS graph.
- **Name**: Unique identifier (e.g., `motion_controller`)
- **Package**: `ros2_foundations`
- **Executable**: Entry point in `setup.py`

### Topic
A channel for data exchange.
- **Name**: `/joint_commands`, `/imu/data`
- **Type**: `trajectory_msgs/JointTrajectory`, `sensor_msgs/Imu`
- **QoS**: Reliability (Reliable/BestEffort), Durability (Volatile/TransientLocal)

### Service
Synchronous request/response communication.
- **Name**: `/reset_simulation`
- **Type**: `std_srvs/Trigger`

## URDF Entities (Robot Model)

### Link
A rigid body part.
- **Attributes**: `name`
- **Visual**: `<geometry>` (box, cylinder, sphere), `<material>` (color)
- **Collision**: `<geometry>` (simplified for physics)
- **Inertial**: `mass`, `inertia` matrix

### Joint
A connection between links.
- **Attributes**: `name`, `type` (revolute, fixed, continuous)
- **Elements**:
  - `parent`: link name
  - `child`: link name
  - `origin`: xyz, rpy (relative pose)
  - `axis`: xyz (axis of rotation)
  - `limit`: lower, upper, effort, velocity

## AI Bridge Data

### Command Protocol
Simplified dictionary format for the AI agent.
```json
{
  "action": "move_arm",
  "target": [0.5, 0.2, 0.1],
  "duration": 2.0
}
```

### Sensor Snapshot
Simplified dictionary format received by AI agent.
```json
{
  "status": "idle",
  "joints": {"shoulder": 0.0, "elbow": 1.5},
  "battery": 98.5
}
```
