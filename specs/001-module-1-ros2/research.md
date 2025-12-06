# Research: Module 1 - ROS 2 Foundations

**Date**: 2025-12-06
**Scope**: ROS 2 Humble/Iron, Docusaurus v3

## Decisions

### 1. ROS 2 Distribution: Humble/Iron
- **Decision**: Target **ROS 2 Humble Hawksbill** (LTS) on Ubuntu 22.04 as the primary platform, with notes for Iron Irwini.
- **Rationale**: Humble is the current Long Term Support release, ensuring stability for students. Ubuntu 22.04 is the standard tier-1 OS for Humble.
- **Alternatives**: Jazzy (too new/Ubuntu 24.04), Galactic (EOL).

### 2. Documentation Engine: Docusaurus v3
- **Decision**: Use Docusaurus v3.
- **Rationale**: Industry standard for technical documentation, Markdown-first workflow, React-based for custom interactive components if needed later. Confirmed Node 18+ requirement.
- **Alternatives**: MkDocs (simpler but less extensible), Hugo (faster but harder to customize components).

### 3. Build System: colcon
- **Decision**: Standardize on `colcon build --symlink-install`.
- **Rationale**: The standard ROS 2 build tool. Symlink install allows python changes without rebuild, essential for developer velocity in the book's examples.

### 4. URDF vs Xacro
- **Decision**: Start with pure **URDF** for transparency, introduce **Xacro** only if repetition becomes unmanageable in later modules.
- **Rationale**: Beginners learn best by seeing the raw XML structure first. Hiding it behind macros too early causes confusion about what is actually generated.

### 5. Python-first (rclpy)
- **Decision**: Use `rclpy` exclusively for Module 1.
- **Rationale**: Lower barrier to entry than C++. Matches the "AI Engineer" profile of the target audience better than embedded systems engineers.
