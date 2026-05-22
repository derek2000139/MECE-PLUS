# MECE+ 思维工具链

<div align="center">

[![中文](https://img.shields.io/badge/语言-中文-red.svg)](./README.md)
[![English](https://img.shields.io/badge/Language-English-blue.svg)](./README_EN.md)

</div>

企业级结构化思维套件，整合麦肯锡问题解决、BCG假设树、系统动力学与IDEO设计思维。

## 📋 目录结构

```
mece-plus/
├── SKILL.md              # 核心控制器与路由逻辑
├── scripts/
│   └── validate_ctb.py   # MECE合规性验证脚本
├── references/           # 底层工具模块
│   ├── 01_mece_decomposer.md
│   ├── 02_system_mapper.md
│   ├── 03_dynamic_scanner.md
│   ├── 04_hypothesis_driver.md
│   └── 05_design_thinking_bridge.md
└── assets/               # 静态资源
```

## 🚀 快速开始

### 1. 问题诊断

当您提出问题时，系统首先进行 Cynefin 复杂度诊断，输出推荐执行路径：

```markdown
🧭 MECE+ 问题诊断报告
- 问题域: Complex
- 关键变量: 多 (>10)
- 项目周期: 短期 (1-3月)
- 推荐路径: 路径 C-短周期（跳过时间维度扫描）
```

输入 `开始` 确认路径，或 `调整 [路径]` 修改。

### 2. 执行流程（自适应项目周期）

| 步骤 | 工具 | 输出 | 条件 |
|------|------|------|------|
| 01 | MECE结构拆解 | SCQA + 结构化议题树 | 所有项目 |
| 02 | 系统关系图 | 因果回路图 + 杠杆点分析 | 所有项目 |
| 03 | 时间维度扫描 | 趋势分析 / 风险里程碑 | 项目周期>1月 |
| 04 | 假设驱动分析 | 假设金字塔 + MVP验证 | 所有项目 |
| 05 | 设计思维桥接 | 同理心洞察 + HMW重构 | 所有项目 |

#### ⏰ 时间窗口自适应规则

| 项目周期 | 时间窗口 | 工具03内容 | 是否跳过 |
|---------|---------|-----------|---------|
| 超短期 (<1月) | <1月 | 关键风险 + 里程碑 | 可选跳过 |
| 短期 (1-3月) | 1-3月 | 风险分析 + 里程碑 | 执行简化版 |
| 中期 (3-6月) | 3-6月 | 完整STEEP扫描 | 执行完整版 |
| 长期 (>6月) | 6-12月 | STEEP + 情景规划 | 执行完整版 |

### 3. 验证输出

完成分析后，可运行验证脚本检查MECE合规性：

```bash
python scripts/validate_ctb.py <output_file.md>
```

## 📊 上下文传递包 (CTB)

每轮输出末尾自动附带 CTB，格式如下：

```yaml
# CTB_STATE_START
session:
  original_question: "用户问题"
  current_step: "01_mece"
from_01_mece:
  dimension: "流程法"
  nodes: ["获客", "转化", "留存"]
  fracture_points: []
# CTB_STATE_END
```

## 🎯 交付标准

1. **零兜底原则**：禁止使用"其他"、"等等"作为节点
2. **分类数量**：第一层大类必须在 2-5 个之间
3. **可视化**：系统关系必须使用 Mermaid 图表展示

## 📚 参考框架

- **McKinsey**：金字塔原理、Issue Tree
- **BCG**：假设树、Day One Answer
- **系统动力学**：彼得·圣吉《第五项修炼》、Donella Meadows
- **设计思维**：斯坦福 d.school、双钻石模型

## 📝 示例

**输入**：如何提升TRAE社区用户参与度？

**输出流程**：
1. 诊断 → Complex问题，推荐路径C
2. MECE拆解 → 动机激发、门槛降低、体验设计、氛围营造、机制保障
3. 系统图 → 识别增长飞轮和杠杆点
4. 趋势扫描 → AI工具普及对门槛的影响
5. 假设验证 → 设计MVP实验
6. 人本洞察 → 重构HMW问题

## 📄 许可证

本项目采用 [Apache License 2.0](LICENSE) 开源许可证。

---

<div align="center">

**[English Version](./README_EN.md)**

</div>
