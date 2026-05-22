# MECE+ Thinking Toolkit

<div align="center">

[![中文](https://img.shields.io/badge/语言-中文-red.svg)](./README.md)
[![English](https://img.shields.io/badge/Language-English-blue.svg)](./README_EN.md)

</div>

Enterprise-grade structured thinking suite integrating McKinsey problem-solving, BCG hypothesis trees, system dynamics, and IDEO design thinking.

## 📋 Directory Structure

```
mece-plus/
├── SKILL.md              # Core controller and routing logic
├── scripts/
│   └── validate_ctb.py   # MECE compliance validation script
├── references/           # Underlying tool modules
│   ├── 01_mece_decomposer.md
│   ├── 02_system_mapper.md
│   ├── 03_dynamic_scanner.md
│   ├── 04_hypothesis_driver.md
│   └── 05_design_thinking_bridge.md
└── assets/               # Static resources
```

## 🚀 Quick Start

### 1. Problem Diagnosis

When you pose a question, the system first performs Cynefin complexity diagnosis and outputs the recommended execution path:

```markdown
🧭 MECE+ Problem Diagnosis Report
- Problem Domain: Complex
- Key Variables: Many (>10)
- Project Duration: Short-term (1-3 months)
- Recommended Path: Path C-Short Cycle (skip time dimension scan)
```

Type `start` to confirm the path, or `adjust [path]` to modify.

### 2. Execution Flow (Adaptive by Project Duration)

| Step | Tool | Output | Condition |
|------|------|--------|-----------|
| 01 | MECE Decomposition | SCQA + Structured Issue Tree | All projects |
| 02 | System Mapping | Causal Loop Diagram + Leverage Point Analysis | All projects |
| 03 | Time Dimension Scan | Trend Analysis / Risk Milestones | Project duration > 1 month |
| 04 | Hypothesis-Driven Analysis | Hypothesis Pyramid + MVP Validation | All projects |
| 05 | Design Thinking Bridge | Empathy Insights + HMW Reframing | All projects |

#### ⏰ Time Window Adaptive Rules

| Project Duration | Time Window | Tool 03 Content | Skip? |
|-----------------|-------------|-----------------|-------|
| Ultra-short (<1 month) | <1 month | Key risks + milestones | Optional skip |
| Short-term (1-3 months) | 1-3 months | Risk analysis + milestones | Simplified version |
| Medium-term (3-6 months) | 3-6 months | Full STEEP scan | Full version |
| Long-term (>6 months) | 6-12 months | STEEP + Scenario planning | Full version |

### 3. Validate Output

After completing the analysis, run the validation script to check MECE compliance:

```bash
python scripts/validate_ctb.py <output_file.md>
```

## 📊 Context Transfer Bundle (CTB)

Each round of output automatically includes a CTB at the end, formatted as follows:

```yaml
# CTB_STATE_START
session:
  original_question: "User question"
  current_step: "01_mece"
from_01_mece:
  dimension: "Process Method"
  nodes: ["Acquisition", "Conversion", "Retention"]
  fracture_points: []
# CTB_STATE_END
```

## 🎯 Delivery Standards

1. **Zero Fallback Principle**: Prohibit using "others", "etc." as nodes
2. **Category Count**: First-level categories must be between 2-5
3. **Visualization**: System relationships must be displayed using Mermaid diagrams

## 📚 Reference Frameworks

- **McKinsey**: Pyramid Principle, Issue Tree
- **BCG**: Hypothesis Tree, Day One Answer
- **System Dynamics**: Peter Senge's "The Fifth Discipline", Donella Meadows
- **Design Thinking**: Stanford d.school, Double Diamond Model

## 📝 Example

**Input**: How to increase TRAE community user engagement?

**Output Flow**:
1. Diagnosis → Complex problem, recommended Path C
2. MECE Decomposition → Motivation activation, barrier reduction, experience design, atmosphere building, mechanism guarantee
3. System Diagram → Identify growth flywheels and leverage points
4. Trend Scan → Impact of AI tool普及 on barrier reduction
5. Hypothesis Validation → Design MVP experiments
6. Human-centered Insights → Reframe HMW questions

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).

---

<div align="center">

**[中文版本](./README.md)**

</div>
