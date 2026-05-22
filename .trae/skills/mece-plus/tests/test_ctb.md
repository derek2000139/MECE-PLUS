# MECE+ 测试文件

## 🧪 测试案例

### 测试案例 1：有效输出（应通过验证）

```markdown
## 测试分析输出

### 🧱 MECE 结构树（所选维度：流程法）

```
如何提升用户参与度
 ├── 1️⃣ [获客] (边界描述: 从潜在用户到首次访问)
 │    ├── 渠道拓展
 │    └── 内容吸引
 ├── 2️⃣ [转化] (边界描述: 从访问到注册)
 │    ├── 注册流程优化
 │    └── 价值展示
 └── 3️⃣ [留存] (边界描述: 从注册到活跃)
      └── 持续价值交付
```

> ⚠️ **边缘议题声明**：暂无

### 🔗 割裂点识别
- 割裂点一：获客与转化被人为切分，但在落地页场景下存在强互作用。

# CTB_STATE_START
session:
  original_question: "如何提升用户参与度？"
  current_step: "01_mece"
from_01_mece:
  dimension: "流程法"
  nodes: ["获客", "转化", "留存"]
  fracture_points: ["获客与转化在落地页场景下存在强互作用"]
from_02_system:
  loops: []
  leverage_nodes: []
from_03_dynamic:
  critical_trends: []
from_04_hypothesis:
  core_hypothesis: ""
  experiments: []
from_05_design:
  reframed_hmw: ""
# CTB_STATE_END
```

**预期结果**：✅ 验证通过

---

### 测试案例 2：包含禁用词（应失败）

```markdown
## 测试分析输出

### 🧱 MECE 结构树（所选维度：要素法）

```
如何降低成本
 ├── 1️⃣ [人力成本]
 │    ├── 优化编制
 │    └── 绩效提升
 ├── 2️⃣ [运营成本]
 │    ├── 采购优化
 │    └── 能耗控制
 └── 3️⃣ [其他成本]
      └── 杂项支出
```

# CTB_STATE_START
session:
  original_question: "如何降低成本？"
  current_step: "01_mece"
from_01_mece:
  dimension: "要素法"
  nodes: ["人力成本", "运营成本", "其他成本"]
  fracture_points: []
# CTB_STATE_END
```

**预期结果**：❌ 验证失败（包含禁用词"其他"）

---

### 测试案例 3：大类数量不足（应失败）

```markdown
## 测试分析输出

### 🧱 MECE 结构树（所选维度：主体法）

```
如何提升产品质量
 └── 1️⃣ [研发团队]
      ├── 代码审查
      └── 测试覆盖
```

# CTB_STATE_START
session:
  original_question: "如何提升产品质量？"
  current_step: "01_mece"
from_01_mece:
  dimension: "主体法"
  nodes: ["研发团队"]
  fracture_points: []
# CTB_STATE_END
```

**预期结果**：❌ 验证失败（大类数量为1，要求2-5个）

---

## 🚀 运行测试

```bash
# 测试案例1（应通过）
python scripts/validate_ctb.py tests/test_ctb.md

# 测试案例2和3需要单独创建文件测试
```

## 📋 测试 checklist

| 测试项 | 预期结果 | 状态 |
|--------|----------|------|
| CTB标记存在 | ✅ 通过 | ⏳ |
| YAML格式正确 | ✅ 通过 | ⏳ |
| 无禁用词 | ✅ 通过 | ⏳ |
| 大类数量2-5 | ✅ 通过 | ⏳ |
| 系统阶段有leverage_nodes | ⚠️ 警告（可选） | ⏳ |