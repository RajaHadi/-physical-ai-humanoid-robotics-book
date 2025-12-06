# Data Model: Module 2 - The Digital Twin

## Glossary Entities

### Core Concepts
- **Digital Twin**: A virtual representation that serves as the real-time digital counterpart of a physical object or process.
- **Physics Engine**: Software that provides an approximate simulation of certain physical systems, such as rigid body dynamics, soft body dynamics, and fluid dynamics.
- **Rigid Body Dynamics**: Analysis of the motion of systems of interconnected bodies that do not deform under the action of forces.

### Simulation Components
- **Collision Mesh**: A simplified geometry used by the physics engine to calculate collisions efficiently (e.g., box, cylinder, convex hull).
- **Visual Mesh**: A high-fidelity 3D model (e.g., DAE, STL, OBJ) used for rendering the robot's appearance.
- **Inertial Tensor**: A matrix describing how an object's mass is distributed relative to its center of mass, crucial for accurate rotational dynamics.
- **TF Tree**: A tree data structure maintained by ROS 2 to keep track of coordinate frames and the transformations between them over time.

## Simulation Configuration Models (SDF/URDF)

### Sensor Configuration (SDF)
- **Type**: `gpu_lidar`, `camera`, `imu`
- **Update Rate**: Frequency of sensor data generation (Hz).
- **Noise**: Configuration for Gaussian noise added to sensor readings.
- **Visual/Collision**: usually sensors have visual representation but simplified collision.

### Environment
- **World File**: Defines the simulation environment (lighting, physics properties, terrain, static objects).
- **Light**: Directional, Point, or Spot lights.
- **Physics**: Gravity vector, time step, real-time update rate.
