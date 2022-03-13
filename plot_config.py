"""
功能：放置plot模块的配置参数
时间：2022.03.09
作者：TsingHua-iDLab-王左帅
"""
# 图像种类选择
SCHEME = {0: '单变量-曲线图',
          1: '散点图',
          2: '单变量-直方图',
          3: '圆形雷达图',
          4: '多边形雷达图'}

# 图像中字体选择
FONT = {0: 'SimSun',
        1: 'Times New Roman'}

# 图像尺寸选择
FIG_SIZE = {0: (12, 8),      # figsize=(a,b) 设置图形的大小，a为图形的宽，b为图形的高，单位为英寸
            1: (8, 8)}

# 图像每英寸点数选择
DPI = {0: 300,                # dpi 为设置图像每英寸的点数
       1: 600}

# 图形颜色选择
GRAPH_COLOR = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

# 轴标签字号和颜色设置
LABEL = {'label_size': 20, 'label_color': 'black'}

# 轴刻度字体和字号设置
TICKS = {'tick_font': 'Times New Roman', 'tick_size': 15}

# 图像标题字号和颜色设置
TITLE = {'font_size': 25, 'font_color': 'black'}

# 图例字号设置
LEGEND = {'leg_size': 20}
