---
id: 002
title: Plan Module 4 VLA Robotics LLM
stage: plan
date: 2025-12-06
surface: agent
model: gemini-pro
feature: vla-robotics-llm
branch: 004-vla-robotics-llm
user: user
command: /sp.plan Module 4 — Vision-Language-Action (VLA)

Create:  
- High-level architecture of the complete VLA pipeline:  
  Microphone → Whisper (speech-to-text) → LLM Planner → ROS 2 Action Graph → Navigation + Perception → Manipulation.  
- Section structure for the chapter: theory, pipeline, examples, ROS integration, capstone prep.  
- Research map including latest Whisper, GPT-based planning, and robotics perception models.  
- Quality validation rules for ensuring technical correctness, grounding, and reproducibility.

Decisions needing documentation:  
1. Whisper model selection  
   - Options: tiny, base, small, medium, large  
   - Tradeoffs: accuracy vs. latency vs. Jetson compatibility  
2. LLM planning approach  
   - True hierarchical planning vs. direct ROS action generation  
   - Local vs. cloud LLM inference  
3. Perception grounding  
   - YOLO-based detection vs. Isaac Perception models  
   - Depth-based vs. SLAM-based spatial awareness  
4. ROS 2 action interface  
   - Custom action definitions vs. standard MoveIt/Nav2 actions  
5. Capstone design decision  
   - Single-room environment vs. multi-room exploration  
   - Static vs. dynamic obstacles  
6. Documentation sources pulled through Context7 MCP  
   - Latest ROS 2 Humble/Iron docs  
   - NVIDIA Isaac Sim & Isaac ROS docs  
   - OpenAI Whisper model docs  
   - Unity robotics integration docs

Testing strategy:  
- Whisper validation: test speech variability, accents, ambient noise.  
- Planner validation: ensure natural-language commands produce deterministic ROS plans.  
- Action graph validation: run dry-run simulations in Gazebo + Isaac to verify node connections.  
- Perception validation: test with different lighting, occlusion, and object scale.  
- Safety validation: ensure navigation and manipulation actions avoid collisions.  
- Capstone readiness check: robot must complete voice → plan → navigate → detect → manipulate loop.

Technical details:  
- Use research-concurrent workflow (write and research synchronously).  
- Pull latest Docusaurus docs using Context7 MCP for consistent formatting + linking.  
- Follow citation style defined in /sp.constitution (APA).  
- Organize the chapter into phases:  
  1. Foundations of VLA  
  2. Whisper + Language Understanding  
  3. Cognitive Planning with LLMs  
  4. Vision + Depth Perception  
  5. ROS 2 Action Generation  
  6. Integrated Pipeline Examples  
  7. Capstone Preparation
labels: [plan, vla, robotics, llm, module-4]
links:
  spec: specs/004-vla-robotics-llm/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/004-vla-robotics-llm/plan.md
- specs/004-vla-robotics-llm/research.md
- specs/004-vla-robotics-llm/data-model.md
- specs/004-vla-robotics-llm/quickstart.md
- specs/004-vla-robotics-llm/contracts/
tests:
[]
---

## Prompt

/sp.plan Module 4 — Vision-Language-Action (VLA)

Create:  
- High-level architecture of the complete VLA pipeline:  
  Microphone → Whisper (speech-to-text) → LLM Planner → ROS 2 Action Graph → Navigation + Perception → Manipulation.  
- Section structure for the chapter: theory, pipeline, examples, ROS integration, capstone prep.  
- Research map including latest Whisper, GPT-based planning, and robotics perception models.  
- Quality validation rules for ensuring technical correctness, grounding, and reproducibility.

Decisions needing documentation:  
1. Whisper model selection  
   - Options: tiny, base, small, medium, large  
   - Tradeoffs: accuracy vs. latency vs. Jetson compatibility  
2. LLM planning approach  
   - True hierarchical planning vs. direct ROS action generation  
   - Local vs. cloud LLM inference  
3. Perception grounding  
   - YOLO-based detection vs. Isaac Perception models  
   - Depth-based vs. SLAM-based spatial awareness  
4. ROS 2 action interface  
   - Custom action definitions vs. standard MoveIt/Nav2 actions  
    5. Capstone design decision  
   - Single-room environment vs. multi-room exploration  
   - Static vs. dynamic obstacles  
6. Documentation sources pulled through Context7 MCP  
   - Latest ROS 2 Humble/Iron docs  
   - NVIDIA Isaac Sim & Isaac ROS docs  
   - OpenAI Whisper model docs  
   - Unity robotics integration docs

Testing strategy:  
- Whisper validation: test speech variability, accents, ambient noise.  
- Planner validation: ensure natural-language commands produce deterministic ROS plans.  
- Action graph validation: run dry-run simulations in Gazebo + Isaac to verify node connections.  
- Perception validation: test with different lighting, occlusion, and object scale.  
- Safety validation: ensure navigation and manipulation actions avoid collisions.  
- Capstone readiness check: robot must complete voice → plan → navigate → detect → manipulate loop.

Technical details:  
- Use research-concurrent workflow (write and research synchronously).  
- Pull latest Docusaurus docs using Context7 MCP for consistent formatting + linking.  
- Follow citation style defined in /sp.constitution (APA).  
- Organize the chapter into phases:  
  1. Foundations of VLA  
  2. Whisper + Language Understanding  
  3. Cognitive Planning with LLMs  
  4. Vision + Depth Perception  
  5. ROS 2 Action Generation  
  6. Integrated Pipeline Examples  
  7. Capstone Preparation

## Response snapshot

Created detailed implementation plan for Module 4, including VLA pipeline architecture, chapter structure, and research map. Placeholder files for research, data model, and quickstart, as well as a contracts directory, were also created. Six decisions requiring documentation have been identified for Phase 0 research.

## Outcome

- ✅ Impact: Created detailed plan and initial artifacts for Module 4.
- 🧪 Tests: N/A
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md and contracts/ directory for Module 4.
- 🔁 Next prompts: Conduct Phase 0 research to resolve clarifications in plan.md and populate research.md.
- 🧠 Reflection: The process successfully generated the plan and necessary placeholders according to the workflow. Six clarification points were identified for the research phase.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): None
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): None
