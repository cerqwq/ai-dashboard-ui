"""
AI Dashboard UI - AI仪表板UI工具
支持仪表板设计、数据可视化、交互
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDashboardUITools:
    """
    AI仪表板UI工具
    支持：设计、可视化、交互
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_dashboard(self, purpose: str, metrics: List[str]) -> Dict:
        """设计仪表板"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = ", ".join(metrics)

        prompt = f"""请为{purpose}设计仪表板：

指标：{metrics_text}

请返回JSON格式：
{{
    "layout": "布局",
    "widgets": ["组件"],
    "interactions": ["交互"],
    "responsive": "响应式"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"dashboard": content}

    def generate_analytics_dashboard(self, data_source: str, metrics: List[str]) -> str:
        """生成分析仪表板"""
        if not self.client:
            return "LLM客户端未配置"

        metrics_text = ", ".join(metrics)

        prompt = f"""请生成{data_source}分析仪表板：

指标：{metrics_text}

要求：
1. React + TypeScript
2. 多图表布局
3. 筛选器
4. 导出功能"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_admin_panel(self, modules: List[str], style: str = "modern") -> str:
        """生成管理面板"""
        if not self.client:
            return "LLM客户端未配置"

        modules_text = ", ".join(modules)

        prompt = f"""请生成{style}风格的管理面板：

模块：{modules_text}

要求：
1. 侧边栏导航
2. 权限控制
3. 数据表格
4. 响应式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_stats_card(self, metrics: List[Dict], style: str = "modern") -> str:
        """生成统计卡片"""
        if not self.client:
            return "LLM客户端未配置"

        metrics_text = json.dumps(metrics, ensure_ascii=False)

        prompt = f"""请生成{style}风格的统计卡片：

指标：{metrics_text}

要求：
1. 图标
2. 趋势指示
3. 动画效果
4. 响应式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_data_table(self, columns: List[str], features: List[str]) -> str:
        """生成数据表格"""
        if not self.client:
            return "LLM客户端未配置"

        columns_text = ", ".join(columns)
        features_text = ", ".join(features)

        prompt = f"""请生成数据表格组件：

列：{columns_text}
功能：{features_text}

要求：
1. 排序、筛选、分页
2. 行选择
3. 导出
4. 响应式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_chart_widgets(self, chart_types: List[str]) -> str:
        """生成图表组件"""
        if not self.client:
            return "LLM客户端未配置"

        types_text = ", ".join(chart_types)

        prompt = f"""请生成图表组件：

类型：{types_text}

要求：
1. React + Recharts
2. 响应式
3. 主题支持
4. 交互功能"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIDashboardUITools:
    """创建仪表板UI工具"""
    return AIDashboardUITools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Dashboard UI Tools")
    print()

    # 测试
    dashboard = tools.design_dashboard("销售分析", ["销售额", "订单量", "转化率"])
    print(json.dumps(dashboard, ensure_ascii=False, indent=2))
