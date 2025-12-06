# Conceptual API Contracts: ROS 2 Interfaces for VLA Pipeline

This document outlines the conceptual API contracts, primarily in terms of ROS 2 interfaces (Actions, Services, Topics), that would facilitate communication and interaction between the various modules of a Vision-Language-Action (VLA) pipeline. These are high-level definitions to illustrate the data flow and functional boundaries between components.

## 1. Speech-to-Text (STT) Service/Action Interface

*   **Purpose**: To transcribe spoken natural language commands into text.
*   **Type**: ROS 2 Service or Action (Action preferred for long audio streams with feedback).
*   **Service/Action Name**: `/vla/stt_service` or `/vla/stt_action`
*   **Goal Message (Conceptual)**:
    ```
    # Goal: Start/stop audio capture and transcription
    bool capture_audio_stream
    float32 audio_duration_limit  # e.g., 5.0 seconds, 0 for continuous
    ```
*   **Result Message (Conceptual)**:
    ```
    # Result: Transcribed text
    string transcribed_text
    float32 confidence_score
    bool success
    string error_message
    ```
*   **Feedback Message (Conceptual - for Action)**:
    ```
    # Feedback: Real-time transcription progress
    float32 current_progress_percentage
    string partial_transcript
    ```
*   **Related Entity**: Whisper

## 2. LLM Planner Service/Action Interface

*   **Purpose**: To interpret a natural language command, integrate with perception data, and generate a structured sequence of robotic actions (an action graph/plan).
*   **Type**: ROS 2 Service or Action (Action preferred for complex planning with intermediate feedback).
*   **Service/Action Name**: `/vla/llm_planner_service` or `/vla/llm_planner_action`
*   **Goal Message (Conceptual)**:
    ```
    # Goal: Generate a plan for a natural language command
    string natural_language_command
    string robot_current_pose_frame_id
    geometry_msgs/PoseStamped robot_current_pose
    perception_msgs/ObjectDetectionArray current_object_detections # From Perception
    # ... other relevant robot state and environmental context
    ```
*   **Result Message (Conceptual)**:
    ```
    # Result: Structured action graph/plan
    vla_msgs/ActionGraph action_plan  # Custom message defining sequential/parallel actions
    string llm_reasoning_trace        # Optional: LLM's thought process
    bool success
    string error_message              # e.g., "Cannot fulfill command", "Ambiguous command"
    ```
*   **Feedback Message (Conceptual - for Action)**:
    ```
    # Feedback: Planning progress, partial plan generated
    float32 planning_progress_percentage
    string current_planning_step
    ```
*   **Related Entities**: LLM/VLM, Natural Language Command, Humanoid Robot, Perception Sensors, Action Graph/Plan

## 3. Navigation Action Interface (Standard)

*   **Purpose**: To command the robot to navigate to a specified pose in the environment.
*   **Type**: ROS 2 Action (Standard Nav2 `NavigateToPose`).
*   **Action Name**: `/navigate_to_pose` (standard Nav2)
*   **Goal Message (Conceptual)**:
    ```
    # Goal: Navigate to a target pose
    geometry_msgs/PoseStamped pose
    string behavior_tree_id # Optional: specific navigation behavior
    ```
*   **Result Message (Conceptual)**:
    ```
    # Result: Navigation outcome
    std_msgs/Empty result # Success/Failure indicated by action status
    ```
*   **Feedback Message (Conceptual)**:
    ```
    # Feedback: Current robot pose, distance to goal, estimated time of arrival
    geometry_msgs/PoseStamped current_pose
    float32 distance_remaining
    builtin_interfaces/Duration estimated_time_remaining
    ```
*   **Related Entities**: Humanoid Robot, Action Graph/Plan, Environment

## 4. Perception Service/Action Interface

*   **Purpose**: To identify objects, estimate their poses, and segment them based on visual and depth data, potentially guided by language.
*   **Type**: ROS 2 Service or Action (Action preferred for complex searches or processing).
*   **Service/Action Name**: `/vla/perception_query_service` or `/vla/object_detection_action`
*   **Goal Message (Conceptual)**:
    ```
    # Goal: Detect/locate objects based on a query
    string object_query               # e.g., "red cup", "person", "table"
    bool return_3d_pose               # Request 3D pose estimation
    geometry_msgs/PointOfInterest roi # Optional: Region of interest for search
    ```
*   **Result Message (Conceptual)**:
    ```
    # Result: Array of detected objects
    perception_msgs/ObjectDetectionArray detections # Custom message type for detections
    bool success
    string error_message              # e.g., "Object not found"
    ```
*   **Feedback Message (Conceptual - for Action)**:
    ```
    # Feedback: Progress of perception task
    float32 search_progress_percentage
    string status_message
    ```
*   **Related Entities**: Perception Sensors, LLM/VLM, Action Graph/Plan, Environment

## 5. Manipulation Action Interface (Standard/Custom)

*   **Purpose**: To perform tasks involving the robot's manipulators, such as grasping, placing, or pushing objects.
*   **Type**: ROS 2 Action (Standard MoveIt `MoveGroup` or custom).
*   **Action Name**: `/move_group` (standard MoveIt) or `/vla/manipulate_object_action` (custom)
*   **Goal Message (Conceptual - for custom action)**:
    ```
    # Goal: Perform a manipulation task on a target object
    string manipulation_task      # e.g., "grasp", "place", "push"
    string target_object_id       # Unique ID for the object (from Perception)
    geometry_msgs/PoseStamped target_pose_in_robot_frame # Target pose for manipulation
    ```
*   **Result Message (Conceptual)**:
    ```
    # Result: Outcome of manipulation task
    bool success
    string error_message
    ```
*   **Feedback Message (Conceptual)**:
    ```
    # Feedback: Gripper state, arm progress, current sub-task
    float32 progress_percentage
    string current_sub_task
    ```
*   **Related Entities**: Humanoid Robot, Action Graph/Plan, Environment

## 6. Robot State Topics

*   **Purpose**: To continuously broadcast the robot's current status and sensor readings for use by other modules (e.g., LLM for context, Navigation for localization).
*   **Type**: ROS 2 Topics (Standard)
*   **Topic Names (Conceptual)**:
    *   `/odom`: `nav_msgs/Odometry` (Robot's pose and velocity)
    *   `/joint_states`: `sensor_msgs/JointState` (Current configuration of robot joints)
    *   `/camera/rgb/image_raw`: `sensor_msgs/Image` (Raw RGB camera feed)
    *   `/camera/depth/image_raw`: `sensor_msgs/Image` (Raw depth camera feed)
    *   `/tf`: `tf2_msgs/TFMessage` (Robot transforms)
*   **Related Entities**: Humanoid Robot, Perception Sensors
