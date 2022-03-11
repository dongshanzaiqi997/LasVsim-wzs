"""
功能：放置plot模块的配置参数
时间：2022.03.09
作者：TsingHua-iDLab-王左帅
"""
SCHEME = {0: '单变量-曲线图',
          1: '散点图',
          2: '单变量-直方图',
          3: '圆形雷达图',
          4: '多边形雷达图'}  # 本模块提供的图像种类选择
GRAPH_COLOR = [{0: 'lightseagreen'},
               {0: 'deepskyblue'},
               {0: 'blue'},
               {0: 'yellow'},
               {0: 'pink', 1: 'cyan'},
               {0: 'olive', 1: 'cyan'},
               {0: 'red', 1: 'blue', 2: 'black'}]  # 不同个数图形的颜色选择
