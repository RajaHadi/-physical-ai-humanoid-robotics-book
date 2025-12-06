# Research: Module 2 - The Digital Twin (Gazebo & Unity)

**Date**: 2025-12-06
**Scope**: Docusaurus v3, Gazebo (Fortress/Harmonic), Unity Robotics

## Decisions

### 1. Documentation Structure (Docusaurus v3)
- **Decision**: Use `website/docs/digital-twin/` for Module 2 content.
- **Rationale**: Aligns with Docusaurus file-system based routing. Keeps modules distinct.
- **Alternatives**: Single huge file (bad DX), separate repo (overkill).

### 2. Gazebo Version Reference
- **Decision**: Reference **Gazebo Harmonic** (latest LTS) but note Fortress compatibility.
- **Rationale**: Harmonic is the current recommendation for ROS 2 Jazzy, though Humble uses Fortress. We will note differences where critical, but focus on general SDF concepts.
- **Alternatives**: Gazebo Classic (EOL), Ignition (Renamed).

### 3. Unity Integration Reference
- **Decision**: Focus on **Unity Robotics Hub** patterns (URDF Importer).
- **Rationale**: Standard workflow for bringing ROS 2 robots into Unity.
- **Alternatives**: Custom C# scripts (too complex for this module).

### 4. Diagramming
- **Decision**: Use Mermaid.js for simple flowcharts (Docusaurus supported) and ASCII for quick in-text structures.
- **Rationale**: Mermaid renders natively in Docusaurus v3. ASCII is universally readable.

### 5. Sensor Models
- **Decision**: Focus on **Ideal vs. Noisy** models.
- **Rationale**: Critical for "Sim-to-Real" gap education. Students must understand that simulation without noise is unrealistic.
