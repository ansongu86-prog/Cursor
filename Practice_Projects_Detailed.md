# ETF Markets 实践项目详细说明

## 项目1: ETF折溢价监控系统

### 项目目标
构建一个自动化系统，监控多只ETF的折溢价情况，识别异常并生成报告。

### 技术栈
- Python 3.8+
- Pandas
- yfinance 或 pandas_datareader
- Matplotlib/Seaborn
- 可选: Streamlit (Web界面)

### 详细功能要求

#### 1. 数据获取模块
```python
# 需要实现的功能
- 获取ETF实时价格
- 获取ETF NAV数据
- 处理多个ETF (至少10-20只)
- 处理不同市场的数据 (港股、A股、美股等)
- 错误处理和重试机制
```

#### 2. 折溢价计算模块
```python
# 计算公式
Premium/Discount = (Market Price - NAV) / NAV * 100

# 需要计算
- 实时折溢价
- 历史折溢价统计
- 折溢价波动率
- 异常折溢价识别 (例如 >2% 或 <-2%)
```

#### 3. 可视化模块
```python
# 需要创建的图表
- 折溢价时间序列图
- 折溢价分布直方图
- 多只ETF对比图
- 异常折溢价警报图
```

#### 4. 报告生成模块
```python
# 报告内容
- 当前折溢价情况汇总
- 异常ETF列表
- 历史趋势分析
- 建议和洞察
```

### 实施步骤

#### 步骤1: 环境设置 (1天)
```bash
# 创建虚拟环境
python -m venv etf_env
source etf_env/bin/activate  # Linux/Mac
# 或 etf_env\Scripts\activate  # Windows

# 安装依赖
pip install pandas numpy matplotlib seaborn yfinance
```

#### 步骤2: 数据获取 (2-3天)
```python
# 示例代码框架
import yfinance as yf
import pandas as pd

def get_etf_data(ticker, period="1mo"):
    """
    获取ETF价格数据
    """
    etf = yf.Ticker(ticker)
    hist = etf.history(period=period)
    return hist

def get_nav_data(ticker):
    """
    获取NAV数据 (可能需要从其他数据源)
    注意: yfinance可能不直接提供NAV，需要查找其他数据源
    """
    # 实现NAV获取逻辑
    pass
```

#### 步骤3: 计算模块 (2-3天)
```python
def calculate_premium_discount(market_price, nav):
    """
    计算折溢价
    """
    if nav == 0:
        return None
    return (market_price - nav) / nav * 100

def identify_anomalies(premium_discount, threshold=2.0):
    """
    识别异常折溢价
    """
    anomalies = []
    if abs(premium_discount) > threshold:
        anomalies.append({
            'ticker': ticker,
            'premium_discount': premium_discount,
            'severity': 'high' if abs(premium_discount) > 5 else 'medium'
        })
    return anomalies
```

#### 步骤4: 可视化 (2-3天)
```python
import matplotlib.pyplot as plt
import seaborn as sns

def plot_premium_discount_history(df):
    """
    绘制折溢价历史图
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['premium_discount'])
    plt.axhline(y=2, color='r', linestyle='--', label='Upper Threshold')
    plt.axhline(y=-2, color='r', linestyle='--', label='Lower Threshold')
    plt.axhline(y=0, color='g', linestyle='-', alpha=0.3)
    plt.title('ETF Premium/Discount Over Time')
    plt.xlabel('Date')
    plt.ylabel('Premium/Discount (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
```

#### 步骤5: 报告生成 (2-3天)
```python
def generate_report(etf_data, anomalies):
    """
    生成HTML或PDF报告
    """
    # 实现报告生成逻辑
    pass
```

### 扩展功能 (加分项)
- 添加邮件警报功能
- 创建Web仪表板 (使用Streamlit)
- 添加机器学习异常检测
- 支持实时数据流
- 添加数据库存储历史数据

### 预期成果
- 完整的Python项目代码
- 可以运行的演示
- 项目文档和README
- 可以展示给面试官

---

## 项目2: ETF流动性分析工具

### 项目目标
分析ETF的流动性指标，评估市场质量，识别流动性风险。

### 技术栈
- Python
- Pandas
- 市场数据API (需要获取tick数据或订单簿数据)
- Matplotlib/Plotly

### 详细功能要求

#### 1. 流动性指标计算
```python
# 需要计算的指标

# 1. 买卖价差 (Bid-Ask Spread)
spread = ask_price - bid_price
relative_spread = spread / mid_price * 100

# 2. 市场深度 (Market Depth)
# 需要订单簿数据，计算不同价格水平的累计数量

# 3. 交易量指标
- 日均交易量 (ADV)
- 交易量波动率
- 交易量集中度

# 4. 价格影响 (Price Impact)
# 衡量大额交易对价格的影响

# 5. 流动性比率
- Amihud Illiquidity Ratio
- Roll Measure
```

#### 2. 数据获取挑战
```python
# 注意: 获取tick数据或订单簿数据可能需要付费API
# 替代方案:
# 1. 使用公开的日度数据计算部分指标
# 2. 使用模拟数据演示
# 3. 使用免费API获取有限数据
```

#### 3. 可视化需求
```python
# 需要创建的图表
- 买卖价差时间序列
- 市场深度可视化 (订单簿热力图)
- 交易量分析图
- 流动性指标对比图
- 流动性风险仪表板
```

### 实施步骤

#### 步骤1: 数据准备 (3-5天)
- 研究可用的数据源
- 设计数据获取方案
- 处理数据质量问题

#### 步骤2: 指标计算 (5-7天)
```python
def calculate_bid_ask_spread(bid, ask):
    """计算买卖价差"""
    return ask - bid

def calculate_amihud_ratio(returns, volume):
    """
    Amihud Illiquidity Ratio
    = |Return| / Volume
    值越大，流动性越差
    """
    return abs(returns) / volume

def calculate_roll_measure(prices):
    """
    Roll Measure - 基于价格序列的流动性指标
    """
    # 实现Roll Measure计算
    pass
```

#### 步骤3: 分析和可视化 (3-5天)
- 创建各种分析图表
- 设计流动性仪表板
- 添加交互式功能

### 预期成果
- 流动性分析工具
- 多只ETF的流动性对比
- 可视化报告
- 流动性风险评估

---

## 项目3: ETF交易数据分析系统

### 项目目标
分析ETF交易数据，提取市场洞察，支持决策制定。

### 技术栈
- Python
- Pandas
- SQL (如果需要数据库)
- Jupyter Notebook (用于分析)
- 可选: PostgreSQL/MySQL

### 详细功能要求

#### 1. 数据模型设计
```sql
-- 示例数据库schema
CREATE TABLE etf_trades (
    trade_id SERIAL PRIMARY KEY,
    etf_ticker VARCHAR(10),
    trade_date DATE,
    trade_time TIMESTAMP,
    price DECIMAL(10, 4),
    volume INTEGER,
    trade_type VARCHAR(10), -- 'BUY' or 'SELL'
    market VARCHAR(20)
);

CREATE TABLE etf_holdings (
    holding_id SERIAL PRIMARY KEY,
    etf_ticker VARCHAR(10),
    date DATE,
    constituent_ticker VARCHAR(10),
    weight DECIMAL(5, 4),
    shares DECIMAL(15, 2)
);
```

#### 2. 分析功能
```python
# 需要实现的分析

# 1. 交易模式分析
- 日内交易模式
- 周内交易模式
- 季节性模式

# 2. 投资者行为分析
- 大额交易识别
- 交易集中度
- 投资者类型推断

# 3. 市场质量分析
- 执行质量
- 滑点分析
- 市场冲击

# 4. 相关性分析
- ETF与基准的相关性
- ETF之间的相关性
- 跨市场相关性
```

#### 3. SQL查询示例
```sql
-- 每日交易量统计
SELECT 
    etf_ticker,
    trade_date,
    SUM(volume) as daily_volume,
    AVG(price) as avg_price,
    COUNT(*) as trade_count
FROM etf_trades
GROUP BY etf_ticker, trade_date
ORDER BY trade_date DESC;

-- 大额交易识别
SELECT 
    etf_ticker,
    trade_date,
    price,
    volume,
    price * volume as trade_value
FROM etf_trades
WHERE price * volume > 1000000  -- 大于100万
ORDER BY trade_value DESC;

-- 交易时间分布
SELECT 
    EXTRACT(HOUR FROM trade_time) as hour,
    COUNT(*) as trade_count,
    AVG(volume) as avg_volume
FROM etf_trades
GROUP BY EXTRACT(HOUR FROM trade_time)
ORDER BY hour;
```

#### 4. Python分析代码
```python
import pandas as pd
import numpy as np

def analyze_trading_patterns(df):
    """
    分析交易模式
    """
    # 日内模式
    df['hour'] = pd.to_datetime(df['trade_time']).dt.hour
    hourly_pattern = df.groupby('hour')['volume'].sum()
    
    # 周内模式
    df['day_of_week'] = pd.to_datetime(df['trade_date']).dt.dayofweek
    daily_pattern = df.groupby('day_of_week')['volume'].sum()
    
    return hourly_pattern, daily_pattern

def identify_large_trades(df, threshold_percentile=95):
    """
    识别大额交易
    """
    threshold = df['trade_value'].quantile(threshold_percentile / 100)
    large_trades = df[df['trade_value'] > threshold]
    return large_trades

def calculate_correlation(etf_prices, benchmark_prices):
    """
    计算ETF与基准的相关性
    """
    returns_etf = etf_prices.pct_change().dropna()
    returns_benchmark = benchmark_prices.pct_change().dropna()
    correlation = returns_etf.corrwith(returns_benchmark)
    return correlation
```

### 实施步骤

#### 步骤1: 数据准备 (5-7天)
- 设计数据库schema
- 准备模拟数据或获取真实数据
- 数据清洗和验证

#### 步骤2: 数据库设置 (2-3天)
- 安装和配置数据库
- 创建表结构
- 导入数据

#### 步骤3: SQL分析 (3-5天)
- 编写常用查询
- 优化查询性能
- 创建视图和存储过程

#### 步骤4: Python分析 (5-7天)
- 实现各种分析功能
- 创建可视化
- 生成洞察报告

### 预期成果
- 完整的数据库和分析系统
- SQL查询库
- Python分析脚本
- 分析报告和可视化

---

## 项目4: 风险监控仪表板

### 项目目标
创建实时风险监控工具，识别异常情况，自动生成警报。

### 技术栈
- Python
- Streamlit 或 Dash (Web框架)
- Pandas
- Plotly (交互式图表)
- 可选: 数据库 (实时数据存储)

### 详细功能要求

#### 1. 实时监控指标
```python
# 需要监控的指标

# 1. 价格异常
- 价格波动超过阈值
- 异常价格跳跃
- 价格与NAV偏离过大

# 2. 交易量异常
- 交易量突然增加/减少
- 异常大额交易
- 交易量集中度异常

# 3. 流动性异常
- 买卖价差扩大
- 市场深度下降
- 流动性指标恶化

# 4. 折溢价异常
- 折溢价超过正常范围
- 折溢价快速变化
```

#### 2. 警报系统
```python
def check_price_anomaly(current_price, historical_prices, threshold=3):
    """
    检查价格异常 (使用Z-score)
    """
    mean_price = historical_prices.mean()
    std_price = historical_prices.std()
    z_score = abs(current_price - mean_price) / std_price
    
    if z_score > threshold:
        return {
            'alert': True,
            'severity': 'high' if z_score > 5 else 'medium',
            'message': f'Price anomaly detected: Z-score = {z_score:.2f}'
        }
    return {'alert': False}

def check_volume_spike(current_volume, avg_volume, threshold=2):
    """
    检查交易量异常
    """
    if current_volume > avg_volume * threshold:
        return {
            'alert': True,
            'severity': 'high',
            'message': f'Volume spike: {current_volume/avg_volume:.1f}x average'
        }
    return {'alert': False}
```

#### 3. 仪表板设计
```python
# Streamlit示例框架
import streamlit as st
import plotly.express as px

st.title('ETF Risk Monitoring Dashboard')

# 侧边栏 - ETF选择
etf_ticker = st.sidebar.selectbox('Select ETF', ['2800.HK', '510050.SS', ...])

# 主界面
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('Current Price', price, delta=price_change)

with col2:
    st.metric('Premium/Discount', f'{premium:.2f}%', 
              delta=premium_change, delta_color='inverse')

with col3:
    st.metric('Volume', volume, delta=volume_change)

with col4:
    st.metric('Bid-Ask Spread', f'{spread:.2f}%')

# 图表区域
st.subheader('Price Trend')
fig = px.line(price_data, x='date', y='price')
st.plotly_chart(fig, use_container_width=True)

# 警报区域
st.subheader('Alerts')
for alert in alerts:
    if alert['severity'] == 'high':
        st.error(alert['message'])
    else:
        st.warning(alert['message'])
```

### 实施步骤

#### 步骤1: 数据获取和存储 (3-5天)
- 设置数据获取机制
- 设计数据存储方案
- 实现数据更新逻辑

#### 步骤2: 监控逻辑 (5-7天)
- 实现各种异常检测算法
- 设计警报规则
- 测试监控准确性

#### 步骤3: 仪表板开发 (5-7天)
- 学习Streamlit或Dash
- 设计用户界面
- 实现交互功能

#### 步骤4: 测试和优化 (3-5天)
- 功能测试
- 性能优化
- 用户体验改进

### 预期成果
- 可运行的Web仪表板
- 实时监控功能
- 警报系统
- 可视化展示

---

## 项目5: 市场质量分析报告生成器

### 项目目标
自动化生成ETF市场质量分析报告，支持决策制定。

### 技术栈
- Python
- Pandas
- ReportLab 或 WeasyPrint (PDF生成)
- Jinja2 (模板引擎)
- Matplotlib/Plotly

### 详细功能要求

#### 1. 报告内容结构
```markdown
# ETF市场质量分析报告

## 执行摘要
- 关键指标概览
- 主要发现
- 建议

## 1. 价格表现
- 价格走势
- 收益率分析
- 波动率分析

## 2. 流动性分析
- 买卖价差
- 市场深度
- 交易量分析

## 3. 折溢价分析
- 折溢价趋势
- 异常情况
- 套利机会

## 4. 交易质量
- 执行质量
- 市场冲击
- 滑点分析

## 5. 风险指标
- 风险指标汇总
- 异常风险点
- 风险趋势

## 6. 市场比较
- 与同类ETF比较
- 与基准比较
- 市场排名
```

#### 2. 数据分析和计算
```python
def calculate_market_quality_metrics(df):
    """
    计算市场质量指标
    """
    metrics = {}
    
    # 价格指标
    metrics['return'] = df['price'].pct_change().mean() * 252  # 年化
    metrics['volatility'] = df['price'].pct_change().std() * np.sqrt(252)
    
    # 流动性指标
    metrics['avg_spread'] = df['spread'].mean()
    metrics['avg_volume'] = df['volume'].mean()
    
    # 折溢价指标
    metrics['avg_premium'] = df['premium'].mean()
    metrics['premium_volatility'] = df['premium'].std()
    
    return metrics

def generate_insights(metrics, historical_data):
    """
    生成洞察和建议
    """
    insights = []
    
    if metrics['avg_premium'] > 1:
        insights.append({
            'type': 'warning',
            'message': 'ETF consistently trading at premium. Monitor closely.'
        })
    
    if metrics['avg_spread'] > 0.5:
        insights.append({
            'type': 'concern',
            'message': 'Wide bid-ask spread indicates lower liquidity.'
        })
    
    return insights
```

#### 3. 报告生成
```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(metrics, insights, charts, filename):
    """
    生成PDF报告
    """
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # 标题
    story.append(Paragraph("ETF Market Quality Report", styles['Title']))
    story.append(Spacer(1, 12))
    
    # 执行摘要
    story.append(Paragraph("Executive Summary", styles['Heading1']))
    # ... 添加内容
    
    # 添加图表
    # ... 插入图表
    
    doc.build(story)
```

### 实施步骤

#### 步骤1: 数据准备和分析 (5-7天)
- 收集所需数据
- 实现分析函数
- 计算所有指标

#### 步骤2: 报告模板设计 (3-5天)
- 设计报告结构
- 创建模板
- 设计图表样式

#### 步骤3: 自动化生成 (5-7天)
- 实现报告生成逻辑
- 集成所有组件
- 测试报告质量

### 预期成果
- 自动化报告生成系统
- 示例报告
- 可配置的报告模板
- 文档和使用说明

---

## 项目选择建议

### 如果你是初学者
**推荐顺序：**
1. 项目1 (折溢价监控) - 相对简单，数据易获取
2. 项目3 (交易数据分析) - 巩固SQL和Python技能
3. 项目4 (风险监控仪表板) - 学习Web开发

### 如果你有编程经验
**推荐顺序：**
1. 项目4 (风险监控仪表板) - 展示综合能力
2. 项目2 (流动性分析) - 展示专业深度
3. 项目5 (报告生成器) - 展示实用价值

### 时间分配建议
- **项目1**: 2-3周
- **项目2**: 3-4周
- **项目3**: 3-4周
- **项目4**: 4-5周
- **项目5**: 3-4周

### 项目组合建议
选择2-3个项目组合，展示不同方面的能力：
- **技术能力**: 项目1 + 项目4
- **专业深度**: 项目2 + 项目5
- **综合展示**: 项目3 + 项目4

---

## GitHub项目展示建议

### 项目结构
```
etf-analysis-projects/
├── README.md
├── requirements.txt
├── project1_premium_discount/
│   ├── README.md
│   ├── src/
│   ├── data/
│   └── notebooks/
├── project2_liquidity/
│   └── ...
└── project4_dashboard/
    └── ...
```

### README要求
- 项目描述
- 功能列表
- 技术栈
- 安装说明
- 使用示例
- 截图/演示
- 未来改进计划

### 代码质量
- 清晰的代码结构
- 详细的注释
- 文档字符串
- 错误处理
- 单元测试 (加分项)

---

**记住**: 项目的质量比数量更重要。完成1-2个高质量的项目比完成5个粗糙的项目更有价值。
