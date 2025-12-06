# Deliverable Structure: Module 2

The module deliverables adhere to the following file hierarchy and contracts.

## 1. Documentation Modules (`website/docs/digital-twin/`)

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
1. `01-intro-digital-twins.md`: Defining the concept and scope.
2. `02-physics-basics.md`: Rigid body dynamics, gravity, friction.
3. `03-sensor-simulation.md`: LiDAR, Camera, IMU modeling.
4. `04-humanoid-modeling.md`: Specifics of simulating bipedal robots (inertia, balancing).
5. `05-environment-interaction.md`: Terrain, static/dynamic obstacles.
6. `06-unity-visualization.md`: Unity Robotics Hub, visual fidelity.
7. `07-best-practices.md`: Common errors, optimization, "Sim-to-Real".
8. `08-linking-modules.md`: Bridge to Module 3 (Isaac Sim) and from Module 1 (ROS 2).

## 2. Content Contracts

**Diagrams:**
- All diagrams must be either Mermaid code blocks or clear ASCII art.
- Image references must point to `website/static/img/module2/` (if external images are used, though preferred generated).

**Code Snippets:**
- SDF examples must be valid XML.
- URDF examples must align with Module 1 standards.
- Python/C# snippets must be syntactically correct.

**Glossary:**
- Terms defined in `data-model.md` must be explained in context within the chapters.
