"""
功能：图像绘制的具体实现
时间：2022.03.08
作者：Tsinghua-iDLab-王左帅
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from cycler import cycler
import csv
import copy

# from matplotlib.legend_handler import HandlerTuple
# from pylab import *


# todo:任务(1)细节参数argparse（暂放）；
#                    （2）绘图函数重构（暂放）；
#                    （3）；
#                    （4）；
#                     (5)；
#                    （6）。

class Plotter(object):
    """画图"""
    def __init__(self, args):
        super(Plotter, self).__init__()
        self.args = args
        self.filename = args.filename
        self.scheme = args.drawing_scheme
        self.data_name = args.data_name
        self.fig_loc_param = args.figure_location_parameter
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
        """ 图像绘制 """
        # 绘图数据准备
        init_all_the_data_for_drawing = self.prepare_all_the_data_for_drawing()

        fig = self.prepare_the_canvas()
        for i in range(len(self.scheme)):
            scheme = self.scheme[i]
            data = init_all_the_data_for_drawing[i][i]
            ax = plt.subplot(self.fig_loc_param[i])
            self.scheme_select(scheme, fig, data, ax)

    def scheme_select(self, scheme, fig, data, ax):
        """绘图方案选择"""
        # 开始绘图
        if scheme == 0:
            self.single_variable_plot(fig, data, ax=ax)
        elif scheme == 1:
            self.single_variable_scatter(fig, data, ax=ax)
        elif scheme == 2:
            self.single_variable_hist(fig, data, ax=ax)
        elif scheme == 3:
            self.correlated_variable_plot(fig, data, ax=ax)
        elif scheme == 4:
            self.correlated_variable_scatter(fig, data, ax=ax)
        elif scheme == 5:
            self.double_y_plot(fig, data, ax=ax)
        elif scheme == 6:
            self.double_y_scatter(fig, data, ax=ax)
        elif scheme == 7:
            self.double_y_hist(fig, data, ax=ax)
        elif scheme == 8:  # todo: 数据未定，暂时未做
            self.circle_radar(fig, ax=plt.subplot(polar=True))
        elif scheme == 9:
            self.polygon_radar(fig, ax=plt.subplot(polar=True))
        else:
            return 0

    def single_variable_plot(self, fig, data, ax):
        """单变量-曲线图绘制"""
        # 数据准备
        x, y = data[0], data[1]

        # 开始画图
        ax.plot(x, y, label='曲线1')

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

        plt.tight_layout()
        # plt.show()

    def single_variable_scatter(self, fig, data, ax):
        """单变量-散点图绘制"""
        # 数据准备
        x, y = data[0], data[1]

        # 颜色映射
        rng = np.random.RandomState(0)  # 产生伪随机数，类似numpy.random.seed()的作用
        colors = rng.rand(len(x))  # 产生10个介于[0，1]之间的数值，用于颜色映射的数值
        sizes = 700 * rng.rand(len(x))  # 用于改变散点面积的数值

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
        plt.tight_layout()
        # plt.show()

    def single_variable_hist(self, fig, data, ax):
        """单变量-直方图绘制"""
        # 数据准备
        x = data

        # the histogram of the data
        ax.hist(x, 50, density=False, alpha=0.75, label='正太分布直方图')

        ax.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax.set_title(self.title, fontsize=self.title_size, color=self.title_color)

        # r是指定它后面的字符串是原始的字符串，然后用$包裹表示中间的是数学表达式，\表示转译具体的数学符号。
        # ax.text(60, .25, r'$\mu=100,\ \sigma=15$')
        # ax.set_xlim(40, 160)
        # ax.set_ylim(0, 0.03)

        # 刻度字体和字号设置
        x_tick_label = ax.get_xticklabels()
        [x_tick_label_temp.set_fontname(self.tick_font) for x_tick_label_temp in x_tick_label]
        ax.tick_params(axis='x', labelsize=self.tick_size)

        y_tick_label = ax.get_yticklabels()
        [y_tick_label_temp.set_fontname(self.tick_font) for y_tick_label_temp in y_tick_label]
        ax.tick_params(axis='y', labelsize=self.tick_size)

        ax.legend(fontsize=self.leg_size, loc='best')
        ax.grid(True)
        plt.tight_layout()
        # plt.show()

    def correlated_variable_plot(self, fig, data, ax):
        """相关变量-曲线图"""
        # 数据准备
        x, y = data[0], data[1]

        # 开始绘图
        ax.plot(x, y, label='行驶轨迹')

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

    def correlated_variable_scatter(self, fig, data, ax):
        """相关变量-散点图"""
        # 数据准备
        x, y = data[0], data[1]

        # 开始绘图
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

    def double_y_plot(self, fig, data, ax):
        """双Y轴-曲线图绘制"""
        # 数据准备
        x, y1, y2 = data[0], data[1], data[2]

        # 开始绘图
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
        plt.tight_layout()

    def double_y_scatter(self, fig, data, ax):
        """双Y轴-散点图绘制"""
        # 数据准备
        x, y1, y2 = data[0], data[1], data[2]

        # 开始绘图
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

    def double_y_hist(self, fig, data, ax):  # todo:对于变量里面都是同一个数怎么画直方图 ? 因为 竖条个数Num=max-min/bins.
        """双Y轴-直方图绘制"""
        # 数据准备
        x1, x2 = data[0], data[1]

        # 开始绘图
        ax1 = ax
        plt.title(self.title, fontsize=self.title_size, color=self.title_color)
        plt.hist(x1, 50, density=False, alpha=0.75, label='直方图1')
        ax1.set_xlabel(self.xlabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        ax1.set_ylabel(self.ylabel, fontsize=self.axes_label_size, color=self.axes_label_color)
        plt.xticks(fontproperties=self.tick_font, size=self.tick_size)
        plt.yticks(fontproperties=self.tick_font, size=self.tick_size)
        ax2 = ax1.twinx()
        plt.hist(x2, 50, density=False, alpha=0.75, color='fuchsia', label='直方图2')
        ax2.set_ylabel(self.y2label, fontsize=self.axes_label_size, color=self.axes_label_color)
        plt.yticks(fontproperties=self.tick_font, size=self.tick_size)

        # todo：暂放图例设置
        # todo:要么从更宏大的方面入手来解决问题，比如更换直方图函数，更改外层更大的实现架构。要么沿着当前操作方法往深层挖掘。
        ax1.legend(fontsize=self.leg_size, loc=2)
        ax2.legend(fontsize=self.leg_size, loc=1)

        plt.tight_layout()
        # plt.show()

    def circle_radar(self, fig, ax):
        """圆形雷达图绘制"""
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
        """多边形雷达图绘制"""
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

    def prepare_the_canvas(self):
        """ 画布准备 """
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        return fig

    def prepare_all_the_data_for_drawing(self):
        """
        功能：为绘图准备所有所有的数据
        input:
        output: 输出所有绘图所需的数据
        """
        # 数据x、 y
        data_name = self.data_name
        mid_variable_for_per_subplot = []
        output_all_the_data_for_plot = []
        for i in range(len(data_name)):
            for j in range(len(data_name[i])):
                per_data_name = data_name[i][j]
                mid_variable_for_per_subplot.append(self.get_data_for_per_variable(per_data_name))
            copy_data_for_return = copy.deepcopy(dict(zip([i], [mid_variable_for_per_subplot])))

            # 为了构建对应data_name的变量字典而清空列表
            del mid_variable_for_per_subplot[:]

            # 为了返回数据而存储数据
            output_all_the_data_for_plot.append(copy_data_for_return)

        return output_all_the_data_for_plot

    def get_data_for_per_variable(self, variable_name):
        """
        文件加载和指定数据获取
        input:
             variable_name: csv第一行变量名
        output:
              output1: variable_name对应的数据
        """
        output = []
        # todo:用切片实现中间一段数据的获取
        filename = self.filename
        try:
            with open(filename) as csvfile:
                data = csv.reader(csvfile, delimiter=',')  # data是一个生成器
                # 读取第一行表头
                head = next(data)
                try:
                    if variable_name in head:
                        index_x = head.index(variable_name)
                    for column in data:
                        # 判断某一列的数据类型
                        data_type_x = type(eval(column[index_x]))
                        # todo：如果是list，则下面一段代码要根据需要进行调整
                        output.append(data_type_x(column[index_x]))
                except UnboundLocalError:
                    print('请检查您输入的变量名是否正确！')
        except FileNotFoundError:
            msg = "Sorry, the file " + filename + " does not exist."
            print(msg)

        return output

