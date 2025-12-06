# Quickstart: Module 2 - The Digital Twin

## Prerequisites
- **Documentation Build**: Same as Module 1 (Node.js 18+, `npm install` in `website/`).
- **Conceptual**: Completion of Module 1 (Basic ROS 2 knowledge).

## 1. Accessing the Content
1. Navigate to the book's website directory: `cd website`.
2. Start the local server: `npm run start`.
3. Open your browser to `http://localhost:3000`.
4. Navigate to the "Digital Twin" section in the sidebar.

## 2. Running Examples (Conceptual)
*Note: This module is primarily conceptual documentation. However, code snippets provided in the chapters can be tested if Gazebo is installed.*

**Example: Verifying an SDF snippet**
If you have Gazebo installed, you can save an SDF snippet to `model.sdf` and run:
```bash
ign sdf -k model.sdf
```
*(Note: `ign` might be `gz` depending on version).*

## 3. Visualizing Logic
Review the diagrams in `01-intro-digital-twins.md` to understand the data flow between the Physics Engine, Sensor Models, and the Robot Control System (ROS 2).
