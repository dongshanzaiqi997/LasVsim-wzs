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
import csv


# todo:任务(1)细节参数argparse（暂放）；
#                    （2）函数重构（暂放）；
#                    （3）数据接口；
#                          （a）第一步先熟悉数据格式;
#                           (b)然后利用数据。
#                    （4）；
#                     (5)；
#                    （6）。

class Plotter(object):
    """画图"""
    def __init__(self, args):
        super(Plotter, self).__init__()
        self.scheme = args.scheme
        self.font = args.font
        self.figsize = args.figsize
        self.dpi = args.DPI
        self.color = args.graph_color
        self.xlabel = args.xlabel
        self.ylabel = args.ylabel
        self.y2label = args.y2label
        self.axes_label_size = args.axes_label_size
        self.axes_label_color = args.axes_label_color
        self.tick_font = args.tick_font
        self.tick_size = args.tick_size
        self.title = args.title
        self.title_size = args.title_size
        self.title_color = args.title_color
        self.leg_size = args.legend_size

        # 字体及正负号显示设置
        matplotlib.rcParams['font.sans-serif'] = self.font
        matplotlib.rcParams['axes.unicode_minus'] = False  # 解决正负号显示的问题

        # 颜色循环设置
        color_cycler = cycler(color=self.color)
        plt.rc('axes', prop_cycle=color_cycler)  # 设置绘图区属性

    def plot(self):
        """ 各种图像绘制的具体实现 """
        if self.scheme == 0:
            fig = self.prepare_the_canvas()
            self.single_variable_plot(fig, ax=plt.subplot())
        elif self.scheme == 1:
            fig = self.prepare_the_canvas()
            self.single_variable_scatter(fig, ax=plt.subplot())
        elif self.scheme == 2:
            fig = self.prepare_the_canvas()
            self.single_variable_hist(fig, ax=plt.subplot())
        elif self.scheme == 3:
            fig = self.prepare_the_canvas()
            self.correlated_variable_plot(fig, ax=plt.subplot())
        elif self.scheme == 4:
            fig = self.prepare_the_canvas()
            self.correlated_variable_scatter(fig, ax=plt.subplot())
        elif self.scheme == 5:
            fig = self.prepare_the_canvas()
            self.double_y_plot(fig, ax=plt.subplot())
        elif self.scheme == 6:
            fig = self.prepare_the_canvas()
            self.double_y_scatter(fig, ax=plt.subplot())
        elif self.scheme == 7:
            fig = self.prepare_the_canvas()
            self.double_y_hist(fig, ax=plt.subplot())
        elif self.scheme == 8:
            fig = self.prepare_the_canvas()
            self.circle_radar(fig, ax=plt.subplot(polar=True))
        elif self.scheme == 9:
            fig = self.prepare_the_canvas()
            self.polygon_radar(fig, ax=plt.subplot(polar=True))
        elif self.scheme == 10:
            fig = self.prepare_the_canvas()
            self.regular_multiple_subgraph_drawing(fig, ax=plt.subplot())
        elif self.scheme == 11:
            fig = self.prepare_the_canvas()
            self.irregular_multiple_subgraph_drawing(fig, ax=plt.subplot())
        else:
            return 0

    def single_variable_plot(self, fig, ax):  # todo:通过这个函数实现数据的获取（1）
        """
        绘制单变量-曲线图
        这是第1个绘图方案
        """
        ## 从CSV文件加载数据 todo:阅读python文件那部分知识；（2）解决白图像标签显示问题
        # 定义两个空列表
        # x = []
        # y = []
        #
        # # 打开文件
        # with open('test_wzs.csv', 'r') as csvfile:
        #     data = csv.reader(csvfile, delimiter=',')
        #     for row in data:
        #         x.append(row[0])  # 将第一类数据添加到x列表
        #         y.append(row[1])  # 将第二列数据加载到y列表



        x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
        y1 = np.sin(x)
        y2 = np.cos(x)

        ax.plot(x, y1, label='曲线1')
        ax.plot(x, y2, label='曲线2')

        # label字号和颜色设置：20
        ax.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)

        # 刻度字体和字号设置
        x_tick_label = ax.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax.tick_params(axis='x', labelsize=self.tick_size)

        y_tick_label = ax.get_yticklabels()
        [y_tick_label_temp.set_fontname(self.tick_font) for y_tick_label_temp in y_tick_label]
        ax.tick_params(axis='y', labelsize=self.tick_size)

        # title字号和颜色设置
        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)
        ax.legend(fontsize=self.leg_size, loc='best')
        # plt.show()

    def single_variable_scatter(self, fig, ax):
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
        ax.scatter(x, y, marker='o', s=sizes, alpha=0.3, cmap='viridis', label='散点图')
        # plt.colorbar()  # 显示颜色条

        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)

        ax.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)

        # 刻度字体和字号设置
        x_tick_label = ax.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax.tick_params(axis='x', labelsize=self.tick_size)

        y_tick_label = ax.get_yticklabels()
        [y_tick_label_temp.set_fontname(self.tick_font) for y_tick_label_temp in y_tick_label]
        ax.tick_params(axis='y', labelsize=self.tick_size)

        ax.legend(fontsize=self.leg_size, loc='best')

    def single_variable_hist(self, fig, ax):
        """
        绘制’单变量-直方图’
        这是第3个绘图方案
        """
        np.random.seed(19680801)  # 为了重现固定的随机状态

        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)  # 正太分布

        # the histogram of the data
        ax.hist(x, 50, density=True, alpha=0.75, label='正太分布直方图')

        ax.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)

        # r是指定它后面的字符串是原始的字符串，然后用$包裹表示中间的是数学表达式，\表示转译具体的数学符号。
        ax.text(60, .025, r'$\mu=100,\ \sigma=15$')
        ax.set_xlim(40, 160)
        ax.set_ylim(0, 0.03)

        # 刻度字体和字号设置
        x_tick_label = ax.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax.tick_params(axis='x', labelsize=self.tick_size)

        y_tick_label = ax.get_yticklabels()
        [y_tick_label_temp.set_fontname(self.tick_font) for y_tick_label_temp in y_tick_label]
        ax.tick_params(axis='y', labelsize=self.tick_size)

        ax.legend(fontsize=self.leg_size, loc='best')
        ax.grid(True)

    def correlated_variable_plot(self, fig, ax):
        """
        绘制‘相关变量-曲线图’
        这是第4个绘图方案
        """
        x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
        y = np.exp(x)

        ax.plot(x, y, label='exp(x)')

        # label字号和颜色设置：20
        ax.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)

        # 刻度字体和字号设置
        x_tick_label = ax.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax.tick_params(axis='x', labelsize=self.tick_size)

        y_tick_label = ax.get_yticklabels()
        [y_tick_label_temp.set_fontname(self.tick_font) for y_tick_label_temp in y_tick_label]
        ax.tick_params(axis='y', labelsize=self.tick_size)

        # title字号和颜色设置
        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)
        ax.legend(fontsize=self.leg_size, loc='best')

    def correlated_variable_scatter(self, fig, ax):
        """
        绘制‘相关变量-散点图’
        这是第5个绘图方案
        """
        x = np.random.normal(0, 1, size=10000)
        y = np.random.normal(0, 1, size=10000)

        ax.scatter(x, y, marker='o', alpha=0.1, label='二维正态分布的点')

        # 刻度字体和字号设置
        x_tick_label = ax.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax.tick_params(axis='x', labelsize=self.tick_size)

        y_tick_label = ax.get_yticklabels()
        [y_tick_label_temp.set_fontname(self.tick_font) for y_tick_label_temp in y_tick_label]
        ax.tick_params(axis='y', labelsize=self.tick_size)

        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)
        ax.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.legend(fontsize=self.leg_size, loc='best')

    def double_y_plot(self, fig, ax):
        """
        绘制‘双Y轴-曲线图’
        这是第6个绘图方案
        """
        x = np.arange(0.1, np.e, 0.01)
        y1 = np.exp(-x)
        y2 = np.log(x)

        ax1 = ax

        ax1.set_title(self.title, fontsize=self.title_size, color=self.title_color)
        plot1 = ax1.plot(x, y1, label='指数函数')
        ax1.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax1.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)

        # 刻度字体和字号设置
        x_tick_label = ax1.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax1.tick_params(axis='x', labelsize=self.tick_size)

        y1_tick_label = ax1.get_yticklabels()
        [y1_tick_label_temp.set_fontname(self.tick_font) for y1_tick_label_temp in y1_tick_label]
        ax1.tick_params(axis='y', labelsize=self.tick_size)

        ax2 = ax1.twinx()
        plot2 = ax2.plot(x, y2, 'fuchsia', label='对数函数')
        ax2.set_ylabel(self.y2label, fontsize=self.axes_label_size, color=self.axes_label_color)

        y2_tick_label = ax2.get_yticklabels()
        [y2_tick_label_temp.set_fontname(self.tick_font) for y2_tick_label_temp in y2_tick_label]
        ax2.tick_params(axis='y', labelsize=self.tick_size)

        lines = plot1 + plot2
        ax1.legend(lines, [l.get_label() for l in lines], fontsize=self.leg_size, loc='best')

    def double_y_scatter(self, fig, ax):
        """
        绘制‘双Y轴-散点图’
        这是第7个绘图方案
        """
        N = 10
        x = np.random.rand(N)
        y1 = np.random.rand(N)
        y2 = np.random.rand(N)

        ax1 = ax

        ax1.set_title(self.title, fontsize=self.title_size, color=self.title_color)
        s1 = ax1.scatter(x, y1, label='散点1')
        ax1.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax1.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)

        # 刻度字体和字号设置
        x_tick_label = ax1.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax1.tick_params(axis='x', labelsize=self.tick_size)

        y1_tick_label = ax1.get_yticklabels()
        [y1_tick_label_temp.set_fontname(self.tick_font) for y1_tick_label_temp in y1_tick_label]
        ax1.tick_params(axis='y', labelsize=self.tick_size)

        # 利用方法x.twinx()在原来坐标轴上建立第二个坐标轴
        ax2 = ax1.twinx()
        s2 = ax2.scatter(x, y2, c='fuchsia', label='散点2')
        ax2.set_ylabel(self.y2label, fontsize=self.axes_label_size, color=self.axes_label_color)

        # 第二个y轴的设置
        y2_tick_label = ax2.get_yticklabels()
        [y2_tick_label_temp.set_fontname(self.tick_font) for y2_tick_label_temp in y2_tick_label]
        ax2.tick_params(axis='y', labelsize=self.tick_size)

        ax.legend(handles=[s1, s2], fontsize=self.leg_size, loc='best')

    def double_y_hist(self, fig, ax):
        """
        绘制‘双Y轴-直方图’
        这是第8个绘图方案
        """
        np.random.seed(19680801)  # 为了重现固定的随机状态
        mu1, sigma1, mu2, sigma2 = 100, 15, 120, 10
        x1 = mu1 + sigma1 * np.random.randn(10000)  # 正太分布
        x2 = mu2 + sigma2 * np.random.randn(10000)  # 正太分布

        ax1 = ax


        plt.title(self.title, fontsize=self.title_size, color=self.title_color)
        ax1.hist(x1, 50, density=True, alpha=0.75, label='直方图1')
        ax1.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax1.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        plt.xticks(fontproperties=self.tick_font, size=self.tick_size)
        plt.yticks(fontproperties=self.tick_font, size=self.tick_size)
        ax2 = ax1.twinx()
        ax2.hist(x2, 50, density=True, alpha=0.75, color='fuchsia', label='直方图2')
        ax2.set_ylabel(self.y2label, fontsize=self.axes_label_size, color=self.axes_label_color)
        plt.yticks(fontproperties=self.tick_font, size=self.tick_size)

        fig.legend(loc='upper right',
                   bbox_to_anchor=(1, 1),
                   bbox_transform=ax1.transAxes,
                   fontsize=self.leg_size)

    def circle_radar(self, fig, ax):
        """
        绘制圆形雷达图
        这是第9个绘图方案
        """
        results = [{"安全性": 87, "合规性": 79, "舒适性": 95, "效率性": 92, "节能性": 85},
                   {"安全性": 80, "合规性": 99, "舒适性": 81, "效率性": 85, "节能性": 61}]
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

        # 绘制雷达图
        ax.plot(angles, score_a, "o-")
        ax.plot(angles, score_b, "o-")

        # 设置雷达图中每一项的标签显示
        ax.set_thetagrids(angles * 180 / np.pi, labels, size=self.axes_label_size, color=self.axes_label_color)

        # 设置雷达图的0度起始位置
        ax.set_theta_zero_location('N')

        # 设置雷达图的坐标刻度范围
        ax.set_rlim(0, 100)

        # 极径网格线和标签显示(这个方法类似plt.yticks())
        ax.set_rgrids(np.arange(0, 120, 20),
                      labels=np.arange(0, 120, 20),
                      fontproperties=self.tick_font,
                      size=self.tick_size)

        # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
        ax.set_rlabel_position(270)
        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)
        ax.legend(["算法1", "算法2"], loc='best', fontsize=self.leg_size)

        # 图像在画布上充分填充
        # plt.tight_layout()

        # 指标标签的属性配置
        ax.tick_params(pad=20, grid_color='k', grid_alpha=0.2, grid_linestyle=(0, (5, 5)), size=10)

        # 雷达图的填充
        ax.fill(angles, score_a, alpha=0.5)
        ax.fill(angles, score_b, alpha=0.5)
        plt.tight_layout()

    def polygon_radar(self, fig, ax):
        """
        绘制多边形雷达图
        这是第10个绘图方案
        """
        results = [{"安全性": 87, "合规性": 79, "舒适性": 95, "效率性": 92, "节能性": 85},
                   {"安全性": 80, "合规性": 90, "舒适性": 91, "效率性": 85, "节能性": 88}]
        data_length = len(results[0])
        angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)

        labels = [key for key in results[0].keys()]
        score = [[v for v in result.values()] for result in results]

        # 数据封闭处理
        score_a = np.concatenate((score[0], [score[0][0]]))
        score_b = np.concatenate((score[1], [score[1][0]]))
        angles = np.concatenate((angles, [angles[0]]))
        labels = np.concatenate((labels, [labels[0]]))

        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)

        # 下面的两个for循环的作用是画雷达底图
        for j in np.arange(0, 100 + 20, 20):  # 画圆
            ax.plot(angles, 6 * [j], '-.', lw=0.5, color='black')
        for j in range(5):  # 绘制雷达图的极径骨架
            ax.plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')

        # 开始在雷达地图上绘制图形
        ax.plot(angles, score_a, label='算法（一）')
        ax.plot(angles, score_b, label='算法（二）')

        # 隐藏最外圈的圆
        ax.spines['polar'].set_visible(False)

        # 隐藏圆形网格线
        ax.grid(False)

        for a, b, c in zip(angles, score_a, score_b):  # 将每一项指标的数值显示在雷达图上其应在的位置
            ax.text(a, b + 5, '%.00f' % b, ha='right', va='top', fontsize=15, color='b')
            ax.text(a, c + 5, '%.00f' % c, ha='right', va='top', fontsize=15, color='g')

        ax.set_thetagrids(angles * 180 / np.pi, labels, size=self.axes_label_size,
                             color=self.axes_label_color)

        # 设置极坐标零度朝向
        ax.set_theta_zero_location('N')

        # 设置极径刻度范围
        ax.set_rlim(0, 100)

        # 极径标签的字体和字号设置
        r_tick_label = ax.get_yticklabels()
        [r_tick_label_temp.set_fontname(self.tick_font) for r_tick_label_temp in r_tick_label]
        ax.tick_params(axis='y', labelsize=self.tick_size)

        # 极径标签的角度（相对极坐标的初始零度）位置
        ax.set_rlabel_position(358)

        # 指标标签的属性配置
        ax.tick_params(pad=10, grid_color='k', grid_alpha=0.2, grid_linestyle=(0, (5, 5)), size=10)

        ax.legend(loc='best', fontsize=self.leg_size)

        # 雷达图的填充
        ax.fill(angles, score_a, alpha=0.5)
        ax.fill(angles, score_b, alpha=0.5)

        plt.tight_layout()  # ax无此方法

    def regular_multiple_subgraph_drawing(self, fig, ax):
        """ 在同一画布上绘制规则的多幅子图 """
        # 画第1个图：折线图
        # x = np.arange(1, 100)

        ax1 = plt.subplot(221)
        self.double_y_hist(fig, ax1)

        # 画第2个图：散点图
        ax2 = plt.subplot(222)
        self.single_variable_scatter(fig, ax2)

        # 画第3个图：直方图
        ax3 = plt.subplot(223)
        self.single_variable_plot(fig, ax3)

        # 画第4个图：雷达图
        ax4 = plt.subplot(224, polar=True)
        self.circle_radar(fig, ax4)
        plt.tight_layout()

    def irregular_multiple_subgraph_drawing(self, fig, ax):
        """ 在同一画布上绘制不规则的多幅子图 """
        # x = np.arange(1, 100)

        # 画第1个图：直方图
        ax1 = plt.subplot(211)
        self.double_y_hist(fig, ax1)

        # 画第2个图：散点图
        ax2 = plt.subplot(223)
        self.single_variable_scatter(fig, ax2)

        # 画第3个图：雷达图
        ax3 = plt.subplot(224, polar=True)
        self.polygon_radar(fig, ax3)
        # 第一个图占了211的位置，如果想在下面放两个图，得把第二行当成2列，剩下的两个图像将占据223和224的位置

        plt.tight_layout()

    def prepare_the_canvas(self):
        """ 画布准备 """
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        return fig
