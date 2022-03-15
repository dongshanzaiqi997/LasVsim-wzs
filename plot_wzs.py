"""
功能：图像绘制的具体实现
时间：2022.03.08
作者：Tsinghua-iDLab-王左帅
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from datetime import datetime
from cycler import cycler
# import pandas
# import constants as cst


print(matplotlib.matplotlib_fname())

class Plotter():
    """画图"""
    def __init__(self, scheme, font, figsize, dpi, color, label, ticks, title, legend):
        self.scheme = scheme
        self.font = font
        self.figsize = figsize
        self.dpi = dpi
        self.color = color
        self.label = label
        self.ticks = ticks
        self.title = title
        self.legend = legend

        # 字体及正负号显示设置
        matplotlib.rcParams['font.sans-serif'] = self.font
        matplotlib.rcParams['axes.unicode_minus'] = False  # 解决正负号显示的问题

        # 颜色循环设置
        color_cycler = cycler(color=color)
        plt.rc('axes', prop_cycle=color_cycler)  # 设置绘图区属性

    def plot(self):
        """ 各种图像绘制的具体实现 """
        if self.scheme == '单变量-曲线图':
            self.prepare_the_canvas()
            self.single_variable_plot()
        elif self.scheme == '单变量-散点图':
            self.prepare_the_canvas()
            self.single_variable_scatter()
        elif self.scheme == '单变量-直方图':
            self.prepare_the_canvas()
            self.single_variable_hist()
        elif self.scheme == '相关变量-曲线图':
            self.prepare_the_canvas()
            self.correlated_variable_plot()
        elif self.scheme == '相关变量-散点图':
            self.prepare_the_canvas()
            self.correlated_variable_scatter()
        elif self.scheme == '双Y轴-曲线图':
            self.prepare_the_canvas()
            self.double_y_plot()
        elif self.scheme == '双Y轴-散点图':
            self.prepare_the_canvas()
            self.double_y_scatter()
        elif self.scheme == '双Y轴-直方图':
            self.double_y_hist()
        elif self.scheme == '圆形雷达图':
            self.prepare_the_canvas()
            self.circle_radar()
        elif self.scheme == '多边形雷达图':
            self.prepare_the_canvas()
            self.polygon_radar()
        elif self.scheme == '多幅子图绘制':
            self.regular_multiple_subgraph_drawing()
        else:
            return 0

    def single_variable_plot(self):
        """
        绘制单变量-曲线图
        这是第1个绘图方案
        """
        x = np.arange(10)
        y = np.random.randn(10)

        plt.plot(x, y, label='y')

        # label字号和颜色设置：20
        plt.xlabel('输入数据 x', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.ylabel('输出数据 y', fontsize=self.label['label_size'], color=self.label['label_color'])

        # 刻度字体和字号设置
        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        # title字号和颜色设置
        plt.title('单变量-曲线图', fontsize=self.title['font_size'], color=self.title['font_color'])
        plt.legend(fontsize=self.legend['leg_size'], loc='best')

    def single_variable_scatter(self):
        """
        绘制'单变量-散点图'
        这是第2个绘图方案
        """
        rng = np.random.RandomState(0)  # 产生伪随机数，类似numpy.random.seed()的作用
        x = range(10)
        y = rng.randn(10)  # 从标准正太分布中返回10个样本值

        colors = rng.rand(10)  # 产生10个介于[0，1]之间的数值，用于颜色映射的数值
        sizes = 700 * rng.rand(10)  # 用于改变散点面积的数值

        # plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
        plt.scatter(x, y, marker='o', s=sizes, alpha=0.3, cmap='viridis', label='散点图')
        # plt.colorbar()  # 显示颜色条

        plt.title('单变量-散点图', fontsize=self.title['font_size'], color=self.title['font_color'])

        plt.xlabel('输入数据 x', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.ylabel('随机数据 y', fontsize=self.label['label_size'], color=self.label['label_color'])

        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        plt.legend(fontsize=self.legend['leg_size'], loc='best')

    def single_variable_hist(self):
        """
        绘制’单变量-直方图’
        这是第3个绘图方案
        """
        np.random.seed(19680801)  # 为了重现固定的随机状态

        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)  # 正太分布

        # the histogram of the data
        plt.hist(x, 50, density=True, alpha=0.75, label='正太分布直方图')

        plt.xlabel('Smarts', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.ylabel('Probability', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.title('Histogram of IQ', fontsize=self.title['font_size'], color=self.title['font_color'])

        # r是指定它后面的字符串是原始的字符串，然后用$包裹表示中间的是数学表达式，\表示转译具体的数学符号。
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.xlim(40, 160)
        plt.ylim(0, 0.03)

        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        plt.legend(fontsize=self.legend['leg_size'], loc='best')
        plt.grid(True)

    def correlated_variable_plot(self):
        """
        绘制‘相关变量-曲线图’
        这是第4个绘图方案
        """
        x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
        sin_y = np.sin(x)

        plt.plot(x, sin_y, label='sin(x)')

        # label字号和颜色设置：20
        plt.xlabel('输入数据 x', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.ylabel('sin(x)', fontsize=self.label['label_size'], color=self.label['label_color'])

        # 刻度字体和字号设置
        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        # title字号和颜色设置
        plt.title('相关变量曲线图', fontsize=self.title['font_size'], color=self.title['font_color'])
        plt.legend(fontsize=self.legend['leg_size'], loc='best')

    def correlated_variable_scatter(self):
        """
        绘制‘相关变量-散点图’
        这是第5个绘图方案
        """
        x = np.random.normal(0, 1, size=10000)
        y = np.random.normal(0, 1, size=10000)

        plt.scatter(x, y, marker='o', alpha=0.1, label='二维正态分布的点')

        # plt.scatter(x, y, color=self.color[0], marker='o', alpha=0.1, label='二维正态分布的点')
        # 刻度字体和字号设置
        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        plt.title('相关变量-散点图', fontsize=self.title['font_size'], color=self.title['font_color'])
        plt.xlabel('正太分布 x', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.ylabel('正态分布 y', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.legend(fontsize=self.legend['leg_size'], loc='best')

    def double_y_plot(self):
        """
        绘制‘双Y轴-曲线图’
        这是第6个绘图方案
        """
        x = np.arange(0.1, np.e, 0.01)
        y1 = np.exp(-x)
        y2 = np.log(x)

        ax1 = plt.subplot(111)

        plt.title('双Y轴-曲线图', fontsize=self.title['font_size'], color=self.title['font_color'])
        plot1 = ax1.plot(x, y1, label='指数函数')
        ax1.set_xlabel('输入数据 x', fontsize=self.label['label_size'], color=self.label['label_color'])
        ax1.set_ylabel('指数函数', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        ax2 = ax1.twinx()
        plot2 = ax2.plot(x, y2, 'fuchsia', label='对数函数')
        ax2.set_ylabel('对数函数', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        lines = plot1 + plot2
        ax1.legend(lines, [l.get_label() for l in lines], fontsize=self.legend['leg_size'], loc='best')

    def double_y_scatter(self):
        """
        绘制‘双Y轴-散点图’
        这是第7个绘图方案
        """
        x = np.arange(0.1, np.e, 0.1)
        y1 = np.exp(-x)
        y2 = np.log(x)

        ax1 = plt.subplot(111)

        plt.title('双Y轴-散点图', fontsize=self.title['font_size'], color=self.title['font_color'])
        s1 = ax1.scatter(x, y1, label='指数函数')
        ax1.set_xlabel('输入数据 x', fontsize=self.label['label_size'], color=self.label['label_color'])
        ax1.set_ylabel('指数函数', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        # 利用方法x.twinx()在原来坐标轴上建立第二个坐标轴
        ax2 = ax1.twinx()
        s2 = ax2.scatter(x, y2, c='fuchsia', label='对数函数')
        ax2.set_ylabel('对数函数', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.legend(handles=[s1, s2], fontsize=self.legend['leg_size'], loc='best')

    def double_y_hist(self):
        """
        绘制‘双Y轴-直方图’
        这是第8个绘图方案
        """
        np.random.seed(19680801)  # 为了重现固定的随机状态

        mu1, sigma1, mu2,  sigma2 = 100, 15, 120, 10
        x1 = mu1 + sigma1 * np.random.randn(10000)  # 正太分布
        x2 = mu2 + sigma2 * np.random.randn(10000)  # 正太分布

        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        ax1 = plt.subplot(111)

        plt.title('双Y轴-直方图', fontsize=self.title['font_size'], color=self.title['font_color'])
        ax1.hist(x1, 50, density=True, alpha=0.75, label='指数函数')
        ax1.set_xlabel('输入数据 x', fontsize=self.label['label_size'], color=self.label['label_color'])
        ax1.set_ylabel('指数函数', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.xticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        ax2 = ax1.twinx()
        ax2.hist(x2, 50, density=True, alpha=0.75, color='fuchsia', label='对数函数')
        ax2.set_ylabel('对数函数', fontsize=self.label['label_size'], color=self.label['label_color'])
        plt.yticks(fontproperties=self.ticks['tick_font'], size=self.ticks['tick_size'])

        fig.legend(loc='upper right',
                   bbox_to_anchor=(1, 1),
                   bbox_transform=ax1.transAxes,
                   fontsize=self.legend['leg_size'])

    def circle_radar(self, ax):
        """
        绘制圆形雷达图
        这是第9个绘图方案
        """
        results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
                   {"大学英语": 80, "高等数学": 99, "体育": 81, "计算机基础": 85, "程序设计": 61}]
        data_length = len(results[0])

        # 将极坐标根据数据长度进行等分
        angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
        labels = [key for key in results[0].keys()]
        score = [[v for v in result.values()] for result in results]

        # 使雷达图数据封闭
        score_a = np.concatenate((score[0], [score[0][0]]))
        score_b = np.concatenate((score[1], [score[1][0]]))
        angles = np.concatenate((angles, [angles[0]]))
        labels = np.concatenate((labels, [labels[0]]))

        # ax = plt.subplot(111, polar=True)  # todo:看看怎么解决这行语句问题

        # 绘制雷达图
        ax.plot(angles, score_a, "o-")
        ax.plot(angles, score_b, "o-")

        # 设置雷达图中每一项的标签显示
        ax.set_thetagrids(angles * 180 / np.pi, labels, size=self.label['label_size'], color=self.label['label_color'])

        # 设置雷达图的0度起始位置
        ax.set_theta_zero_location('N')

        # 设置雷达图的坐标刻度范围
        ax.set_rlim(0, 100)

        # 极径网格线和标签显示(这个方法类似plt.yticks())
        ax.set_rgrids(np.arange(0, 120, 20),
                      labels=np.arange(0, 120, 20),
                      fontproperties=self.ticks['tick_font'],
                      size=self.ticks['tick_size'])

        # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
        ax.set_rlabel_position(270)
        ax.set_title("圆形雷达图", fontsize=self.title['font_size'], color=self.title['font_color'])
        plt.legend(["弓长张", "口天吴"], loc='best', fontsize=self.legend['leg_size'])

        # 图像在画布上充分填充
        # plt.tight_layout()

        # 指标标签的属性配置
        ax.tick_params(pad=20, grid_color='k', grid_alpha=0.2, grid_linestyle=(0, (5, 5)), size=10)

        # 雷达图的填充
        plt.fill(angles, score_a, alpha=0.5)
        plt.fill(angles, score_b, alpha=0.5)

    def polygon_radar(self):
        """
        绘制多边形雷达图
        这是第10个绘图方案
        """
        results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
                   {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
        data_length = len(results[0])
        angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)

        labels = [key for key in results[0].keys()]
        score = [[v for v in result.values()] for result in results]

        # 数据封闭处理
        score_a = np.concatenate((score[0], [score[0][0]]))
        score_b = np.concatenate((score[1], [score[1][0]]))
        angles = np.concatenate((angles, [angles[0]]))
        labels = np.concatenate((labels, [labels[0]]))

        plt.suptitle("多边形雷达图", fontsize=self.title['font_size'], color=self.title['font_color'])

        ax1 = plt.subplot(121, polar=True)
        ax2 = plt.subplot(122, polar=True)
        ax, data, name = [ax1, ax2], [score_a, score_b], ["弓长张", "口天吴"]

        # 外层for循环的作用是完成两个雷达图的绘制
        for i in range(2):
            # 下面的两个for循环的作用是画雷达底图
            for j in np.arange(0, 100 + 20, 20):  # 画圆
                ax[i].plot(angles, 6 * [j], '-.', lw=0.5, color='black')
            for j in range(5):  # 绘制雷达图的极径骨架
                ax[i].plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')

            # 开始在雷达地图上绘制图形
            ax[i].plot(angles, data[i])
            # ax[i].plot(angles, data[i], color='b')

            # 隐藏最外圈的圆
            ax[i].spines['polar'].set_visible(False)

            # 隐藏圆形网格线
            ax[i].grid(False)
            for a, b in zip(angles, data[i]):  # 将每一项指标的数值显示在雷达图上其应在的位置
                ax[i].text(a, b + 5, '%.00f' % b, ha='right', va='center', fontsize=15, color='b')
            ax[i].set_thetagrids(angles * 180 / np.pi, labels, size=self.label['label_size'], color=self.label['label_color'])

            # 设置极坐标零度朝向
            ax[i].set_theta_zero_location('N')

            # 设置极径刻度范围
            ax[i].set_rlim(0, 100)

            # 极径网格线和标签显示(这个方法类似plt.yticks())
            ax[i].set_rgrids(np.arange(0, 120, 20),
                          labels=np.arange(0, 120, 20),
                          fontproperties=self.ticks['tick_font'],
                          size=self.ticks['tick_size'])

            # 极径标签的角度（相对极坐标的初始零度）位置
            ax[i].set_rlabel_position(0)

            # 设置每一个单独的子图的标题（注意：不是整幅图像的标题）
            ax[i].set_title(name[i])

            # 指标标签的属性配置
            ax[i].tick_params(pad=20, grid_color='k', grid_alpha=0.2, grid_linestyle=(0, (5, 5)), size=10)
        # plt.legend(loc='best', fontsize=self.legend['leg_size'])  # 这种不需要再画图例了
        plt.tight_layout()

    def regular_multiple_subgraph_drawing(self):
        """ 在同一画布上绘制规则多幅子图 """
        # 画第1个图：折线图
        # x = np.arange(1, 100)
        plt.subplot(221)
        self.single_variable_plot()  # todo:要进行代码重构，完成类似此处这个函数的调用。即第一步完成代码重构，第二步实现多子图绘制的开发。
        # plt.plot(x, x * x)

        # 画第2个图：散点图
        plt.subplot(222)
        self.single_variable_scatter()
        # plt.scatter(np.arange(0, 10), np.random.rand(10))

        # 画第3个图：直方图
        plt.subplot(223)
        self.single_variable_hist()

        # 画第4个图：雷达图
        ax = plt.subplot(224, polar=True)
        self.circle_radar(ax)

        plt.show()
        # todo:明天上午的任务是：(1)替换成ax的形式；
        #                    （1）画不规则多子图；
        #                    （3）子图中属性缩放等；
        #                    （4）按陈晨说的修改。

    def prepare_the_canvas(self):
        """ 画布准备 """
        plt.figure(figsize=self.figsize, dpi=self.dpi)
