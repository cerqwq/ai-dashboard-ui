# 📊 AI Dashboard UI

AI仪表板UI工具，支持仪表板设计、数据可视化、交互。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📊 仪表板设计
- 📈 分析仪表板生成
- 🖥️ 管理面板生成
- 📋 统计卡片生成
- 📊 数据表格生成
- 📈 图表组件生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_dashboard_ui import create_tools

tools = create_tools()

# 仪表板设计
dashboard = tools.design_dashboard("销售分析", ["销售额", "订单量"])

# 分析仪表板
analytics = tools.generate_analytics_dashboard("电商", ["转化率", "留存率"])

# 管理面板
admin = tools.generate_admin_panel(["用户管理", "订单管理"], "modern")

# 统计卡片
cards = tools.generate_stats_card(metrics, "modern")

# 数据表格
table = tools.generate_data_table(columns, ["排序", "筛选"])

# 图表组件
charts = tools.generate_chart_widgets(["折线图", "柱状图", "饼图"])
```

## 📁 项目结构

```
ai-dashboard-ui/
├── tools.py       # 仪表板UI工具核心
└── README.md
```

## 📄 许可证

MIT License
