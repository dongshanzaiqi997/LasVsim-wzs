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
            self.single_variable_plot()
        elif self.scheme == '单变量-散点图':
            self.single_variable_scatter()
        elif self.scheme == '单变量-直方图':
            self.single_variable_hist()
        elif self.scheme == '相关变量-曲线图':
            self.correlated_variable_plot()
        elif self.scheme == '相关变量-散点图':
            self.correlated_variable_scatter()
        elif self.scheme == '双Y轴-曲线图':
            self.double_y_plot()
        elif self.scheme == '双Y轴-散点图':
            self.double_y_scatter()
        elif self.scheme == '双Y轴-直方图':
            self.double_y_hist()
        elif self.scheme == '圆形雷达图':
            self.circle_radar()
        elif self.scheme == '多边形雷达图':
            self.polygon_radar()
        else:
            return 0

    def single_variable_plot(self):
        """
        绘制单变量-曲线图
        这是第1个绘图方案
        """
        x = np.arange(10)
        y = np.random.randn(10)

        # 图像尺寸和dpi设置
        plt.figure(figsize=self.figsize, dpi=self.dpi)

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

        plt.figure(figsize=self.figsize, dpi=self.dpi)

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

        plt.figure(figsize=self.figsize, dpi=self.dpi)

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

        # 图像尺寸和dpi设置
        plt.figure(figsize=self.figsize, dpi=self.dpi)

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

        plt.figure(figsize=self.figsize, dpi=self.dpi)
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

        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        ax1 = fig.add_subplot(111)

        plt.title('双Y轴-曲线图', fontsize=20)
        plt.grid(axis='y', color='grey', linestyle='--', lw=0.5, alpha=0.5)
        plt.tick_params(axis='both', labelsize=14)
        plot1 = ax1.plot(x, y1, label='No. of Players Drafted')
        ax1.set_ylabel('Number of Players Drafted', fontsize=18)


        ax2 = ax1.twinx()
        plot2 = ax2.plot(x, y2, 'g', label='Avg WS/48')  # todo:选一个稀有的颜色
        ax2.set_ylabel('Win Shares Per 48 minutes', fontsize=18)

        ax2.tick_params(axis='y', labelsize=14)

        lines = plot1 + plot2
        ax1.legend(lines, [l.get_label() for l in lines])
        ax1.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 9))
        ax2.set_yticks(np.linspace(ax2.get_ybound()[0], ax2.get_ybound()[1], 9))



    def double_y_scatter(self):
        """
        绘制‘双Y轴-散点图’
        这是第7个绘图方案
        """

        pass

    def double_y_hist(self):
        """
        绘制‘双Y轴-直方图’
        这是第8个绘图方案
        """

        pass

    def circle_radar(self):
        """
        绘制圆形雷达图
        这是第9个绘图方案
        """
        results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
                   {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
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

        # 设置图形的大小
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)

        # 新建一个子图
        # ax = plt.subplot(111, polar=True)
        ax = fig.add_subplot(111, projection='polar')

        # 绘制雷达图
        ax.plot(angles, score_a, "o-")
        ax.plot(angles, score_b, "o-")

        # ax.plot(angles, score_a, "o-", color='g')
        # ax.plot(angles, score_b, "o-", color='b')

        # 设置雷达图中每一项的标签显示
        ax.set_thetagrids(angles * 180 / np.pi, labels)

        # 设置雷达图的0度起始位置
        ax.set_theta_zero_location('N')

        # 设置雷达图的坐标刻度范围
        ax.set_rlim(0, 100)

        # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
        ax.set_rlabel_position(270)
        ax.set_title("计算机专业大一（上）")
        plt.legend(["弓长张", "口天吴"], loc='best')
        plt.tight_layout()
        ax.tick_params(pad=12, grid_color='k', grid_alpha=0.2, grid_linestyle=(0, (5, 5)))

        plt.fill(angles, score_a, alpha=0.5)
        plt.fill(angles, score_b, alpha=0.5)

        # plt.fill(angles, score_a, facecolor='green', alpha=0.2)
        # plt.fill(angles, score_b, facecolor='blue', alpha=0.5)

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

        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        fig.suptitle("计算机专业大一（上）")
        ax1 = plt.subplot(121, polar=True)
        ax2 = plt.subplot(122, polar=True)
        ax, data, name = [ax1, ax2], [score_a, score_b], ["弓长张", "口天吴"]

        # 外层for循环的作用是完成两个雷达图的绘制
        for i in range(2):
            # 下面的两个for循环的作用是画雷达底图
            for j in np.arange(0, 100 + 20, 20):  # 画圆
                ax[i].plot(angles, 6 * [j], '-.', lw=0.5, color='black')
            for j in range(5):
                ax[i].plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')

            # 开始在雷达地图上绘制图形
            ax[i].plot(angles, data[i])
            # ax[i].plot(angles, data[i], color='b')

            # 隐藏最外圈的圆
            ax[i].spines['polar'].set_visible(False)

            # 隐藏圆形网格线
            ax[i].grid(False)
            for a, b in zip(angles, data[i]):
                ax[i].text(a, b + 5, '%.00f' % b, ha='right', va='center', fontsize=12, color='b')
            ax[i].set_thetagrids(angles * 180 / np.pi, labels)
            ax[i].set_theta_zero_location('N')
            ax[i].set_rlim(0, 100)
            ax[i].set_rlabel_position(0)
            ax[i].set_title(name[i])
        plt.tight_layout()
