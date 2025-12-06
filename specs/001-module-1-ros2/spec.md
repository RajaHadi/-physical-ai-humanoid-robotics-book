# Feature Specification: Module 1 - ROS 2 Foundations

**Feature Branch**: `001-module-1-ros2`
**Created**: 2025-12-06
**Status**: Draft
**Input**: Module 1 — The Robotic Nervous System (ROS 2)

## User Scenarios & Testing

### User Story 1 - Environment & Basic Nodes (Priority: P1)

As a student, I want to set up my ROS 2 development environment and create my first communicating nodes so that I can verify my system is ready for robot control.

**Why this priority**: foundational step; without a working ROS 2 install and understanding of nodes/topics, no other work is possible.

**Independent Test**: Student can run a `talker` and `listener` python node on their Ubuntu machine and see messages exchanged.

**Acceptance Scenarios**:

1. **Given** a fresh Ubuntu 22.04 system, **When** the student follows the setup guide, **Then** they can run `ros2 doctor` and see a healthy report.
2. **Given** a configured workspace, **When** the student runs `colcon build`, **Then** the build succeeds without errors.
3. **Given** two terminal windows, **When** the student runs a publisher node and a subscriber node, **Then** data appears in the subscriber output and `ros2 topic list` shows the active topic.

### User Story 2 - URDF Robot Modeling (Priority: P2)

As a student, I want to define the physical structure of a humanoid robot using URDF so that I can visualize and simulate its kinematics in RViz2.

**Why this priority**: Defining the robot's body is prerequisite for moving it.

**Independent Test**: Student can launch RViz2 and see a correctly articulated 3D model of the humanoid torso, limb, and head.

**Acceptance Scenarios**:

1. **Given** the URDF file, **When** launched in RViz2, **Then** the robot model appears with correct link dimensions and colors.
2. **Given** the `joint_state_publisher_gui`, **When** the student moves a slider, **Then** the corresponding robot joint rotates in the visualizer.
3. **Given** the URDF, **When** checked with `check_urdf`, **Then** it passes with no syntax errors.

### User Story 3 - Control Loops & Sensors (Priority: P3)

As a student, I want to implement a control loop that reads sensors and publishes joint commands so that I can make the robot move responsively.

**Why this priority**: This connects the "nervous system" (ROS) to the "muscles" (actuators) and "senses".

**Independent Test**: Student runs a control node that reacts to dummy sensor data by publishing joint trajectory commands.

**Acceptance Scenarios**:

1. **Given** a running simulation/mock, **When** the control node receives a sensor value above a threshold, **Then** it publishes a specific joint command.
2. **Given** a `ros2 topic echo`, **When** the control loop is running, **Then** `JointTrajectory` messages are published at a fixed frequency.
3. **Given** a mock IMU publisher, **When** data is published, **Then** the control node logs/prints the received acceleration data.

### User Story 4 - AI Agent Bridge (Priority: P4)

As a student, I want to bridge a simple Python AI agent to ROS 2 so that I can control the robot using higher-level logic.

**Why this priority**: Sets the stage for the book's core theme (Physical AI).

**Independent Test**: A standalone Python script (simulating an AI agent) sends a high-level command (e.g., "wave") which the ROS bridge translates into joint movements.

**Acceptance Scenarios**:

1. **Given** the bridge node, **When** a standard Python script sends a command, **Then** the bridge publishes the corresponding ROS 2 topic message.
2. **Given** the bridge, **When** ROS 2 sensor data arrives, **Then** the Python script receives it in a non-ROS format (e.g., JSON/dictionary).

### Edge Cases

- **Installation Failures**: If the standard `apt` installation fails (e.g., restricted network, conflicting packages), the module must provide a "Troubleshooting" sidebar or link to the official alternative (e.g., Docker).
- **No GPU/VM Environment**: If RViz2 crashes or fails to render on student VMs without hardware acceleration, the module must provide configuration steps for software rendering (`LIBGL_ALWAYS_SOFTWARE=1`).
- **Version Mismatches**: If students are on a newer Ubuntu (e.g. 24.04) or ROS 2 (Jazzy), the module must explicitly state compatibility limits or provide migration notes (though primarily targeting Humble/Iron on 22.04).
- **Build Errors**: If `colcon build` fails due to missing dependencies, the text must emphasize the usage of `rosdep install` before building.

## Requirements

### Functional Requirements

- **FR-001**: The module MUST provide installation instructions for ROS 2 Humble or Iron on Ubuntu 22.04.
- **FR-002**: The module MUST include Python (rclpy) code examples for creating Publishers, Subscribers, Services, and Action Servers.
- **FR-003**: The module MUST guide the creation of a URDF file describing a humanoid torso, limb (arm/leg), and head with correct joint limits.
- **FR-004**: The system MUST demonstrate visualizing the URDF in RViz2 using `robot_state_publisher`.
- **FR-005**: The module MUST implement a control loop node that runs at a deterministic frequency (e.g., 10Hz+).
- **FR-006**: The module MUST demonstrate publishing `trajectory_msgs/JointTrajectory` commands.
- **FR-007**: The module MUST demonstrate subscribing to sensor topics (simulating IMU or Camera data).
- **FR-008**: The module MUST include an "AI Bridge" node that translates between pure Python objects and ROS 2 messages.
- **FR-009**: All code examples MUST build using `colcon` and pass `rosdep` checks.

### Key Entities

- **Node**: A ROS 2 executable process (e.g., `sensor_reader`, `motion_controller`).
- **Topic**: A named channel for streaming data (e.g., `/joint_states`, `/imu/data`).
- **URDF**: XML description of the robot's physical links and joints.
- **Launch File**: Python-based configuration to start multiple nodes and visualization simultaneously.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can successfully build the provided package on a clean Ubuntu 22.04 VM in under 10 minutes.
- **SC-002**: The URDF model renders in RViz2 without "No tf data" warnings for all defined links.
- **SC-003**: The control loop maintains a target publish frequency (e.g., 50Hz) within 10% tolerance during simulated load.
- **SC-004**: The AI Bridge successfully round-trips a command (send command -> receive status) in under 100ms latency locally.
- **SC-005**: The final project directory structure matches the standard ROS 2 `ament_python` package layout exactly.

### Assumptions

- **A-001**: Students have basic Python knowledge (variables, functions, classes).
- **A-002**: Hardware acceleration for RViz2 is available (or software rendering is sufficient).
- **A-003**: No physical hardware is required for this module; all hardware is mocked/simulated via code.