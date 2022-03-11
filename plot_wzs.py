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

font = {'黑体': 'SimHei',
        '微软雅黑': 'Microsoft YaHei',
        '微软正黑体': 'Microsoft JhengHei',

        '新宋体': 'NSimSun',  # 不可用
        '新细明体': 'PMingLiU',
        '细明体': 'MingLiU',
        '标楷体': 'DFKai-SB',

        '仿宋': 'FangSong',
        '楷体': 'KaiTi',

        '仿宋_GB2312': 'FangSong_GB2312',  # 不可用
        '楷体_GB2312': 'KaiTi_GB2312'}

# matplotlib.rcParams['font.sans-serif'] = font['楷体']  # ['SimHei']  # ['KaiTi']  # 解决中文显示的问题 todo:字体列表

matplotlib.rcParams['font.family'] = 'SimSun'  # ['KaiTi']  # 解决中文显示的问题 todo:字体列表

# matplotlib.rcParams['font.sans-serif'] = ['Tahoma']  # ['KaiTi']  # 解决中文显示的问题 todo:字体列表
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决正负号显示的问题

print(matplotlib.matplotlib_fname())

class Plotter():
    """画图"""

    def __init__(self, scheme, color):
        self.scheme = scheme
        self.color = color

    def plot(self):
        if self.scheme == '单变量-曲线图':
            self.single_variable_plot()
        elif self.scheme == '散点图':
            self.scatter()
        elif self.scheme == '单变量-直方图':
            self.hist()
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
        x = np.linspace(-2*np.pi, 2*np.pi, 400)
        sin_y = np.sin(x)
        cos_y = np.cos(x)

        plt.plot(x, sin_y, color=self.color[0], label='sin(x)')  # todo:颜色列表[red blue black]
        plt.plot(x, cos_y, color=self.color[1], label='cos(x)', linestyle='-.')  # todo[: - -. --]
        plt.xlabel('输入数据 x')
        plt.ylabel('sin(x)或者cos(x)')
        plt.title('三角函数图')
        plt.legend()

        # log_dir = './figure/'+datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # os.makedirs(log_dir, exist_ok=True)
        # plt.savefig(fname=log_dir + '/plot.jpg')
        # plt.show()

    def scatter(self):
        """
        绘制散点图
        这是第2个绘图方案
        """
        x = np.random.normal(0, 1, size=10000)
        y = np.random.normal(0, 1, size=10000)

        plt.scatter(x, y, color=self.color[0], marker='o', alpha=0.1, label='二维正态分布的点')
        plt.title('二维正态分布散点图')
        plt.xlabel('正太分布 x')
        plt.ylabel('正态分布 y')
        plt.legend()

        # log_dir = './figure/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # os.makedirs(log_dir, exist_ok=True)
        # plt.savefig(fname=log_dir + '/scatter.jpg')
        # plt.show()

    def hist(self):
        """
        绘制直方图
        这是第3个绘图方案
        """
        np.random.seed(19680801)  # 为了重现固定的随机状态

        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)

        # the histogram of the data
        n, bins, patches = plt.hist(x, 50, density=True, color='green', alpha=0.75)

        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')

        # r是指定它后面的字符串是原始的字符串，然后用$包裹表示中间的是数学表达式，\表示转译具体的数学符号。
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.xlim(40, 160)
        plt.ylim(0, 0.03)
        plt.grid(True)

        # log_dir = './figure/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # os.makedirs(log_dir, exist_ok=True)
        # plt.savefig(fname=log_dir + '/hist.jpg')
        # plt.show()

    def circle_radar(self):
        """
        绘制圆形雷达图
        这是第4个绘图方案
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
        fig = plt.figure(figsize=(8, 6), dpi=100)

        # 新建一个子图
        # ax = plt.subplot(111, polar=True)
        ax = fig.add_subplot(111, projection='polar')

        # 绘制雷达图
        ax.plot(angles, score_a, "o-", color='g')
        ax.plot(angles, score_b, "o-", color='b')

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

        plt.fill(angles, score_a, facecolor='green', alpha=0.2)
        plt.fill(angles, score_b, facecolor='blue', alpha=0.5)

        # log_dir = './figure/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # os.makedirs(log_dir, exist_ok=True)
        # plt.savefig(fname=log_dir + '/circle_radar.jpg')

        # plt.show()

        ##################################################################
        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='polar')  # 创建极坐标的Axes对象
        # # ax = plt.subplot(111, polar=True)
        # ## 创建数据字典
        # p1 = {'经济性': 60, '安全性': 70, '舒适性': 65, '可靠性': 75, '互换性': 80}  # 创建第一个的数据
        # p2 = {'经济性': 70, '安全性': 65, '舒适性': 83, '可靠性': 70, '互换性': 67}  # 创建第二个的数据
        #
        # ## 提取数值信息和标签信息
        # data1 = np.array([i for i in p1.values()]).astype(int)
        # data2 = np.array([i for i in p2.values()]).astype(int)
        # label = np.array([j for j in p1.keys()])
        #
        # theta = np.linspace(0, 2 * np.pi, len(data1), endpoint=False)  # 计算区间角度
        # thetas = np.concatenate((theta, [theta[0]]))  # 添加第一个角度数据，实现闭合
        # data1 = np.concatenate((data1, [data1[0]]))  # 添加第一个指标数据，实现闭合
        # data2 = np.concatenate((data2, [data2[0]]))
        # labels = np.concatenate((label, [label[0]]))  # 添加第一个标签数据，实现闭合
        #
        # ax.set_thetagrids(thetas * 180 / np.pi, labels)  # 设置网格标签，单位转化成度数
        # ax.plot(thetas, data1, "o-", label='产品A')
        # ax.plot(thetas, data2, "o-", label='产品B')
        #
        # ax.set_theta_zero_location('N')  # 设置极坐标0°位置
        # ax.set_rlim(0, 100)  # 设置显示的极径范围
        # ax.fill(thetas, data1, facecolor='g', alpha=0.2)  # 填充颜色
        # ax.fill(thetas, data2, facecolor='r', alpha=0.2)
        # ax.legend(loc=(0.9, 0.9))
        # ax.set_rlabel_position(40)  # 设置极径标签位置
        #
        # # grid_linestyle的解释：每个线段长5，间隔长度5，从线长5的0处开始绘制
        # ax.tick_params(pad=12, grid_color='k', grid_alpha=0.2, grid_linestyle=(0, (5, 5)))
        # plt.tight_layout()
        #
        # log_dir = './figure/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # os.makedirs(log_dir, exist_ok=True)
        # plt.savefig(fname=log_dir + '/circle_radar.jpg')
        #
        # # plt.show()

    def polygon_radar(self):
        """
        绘制多边形雷达图
        这是第5个绘图方案
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

        fig = plt.figure(figsize=(10, 6), dpi=100)
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
            ax[i].plot(angles, data[i], color='b')

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
        # log_dir = './figure/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # os.makedirs(log_dir, exist_ok=True)
        # plt.savefig(fname=log_dir + '/polygon_radar.jpg')

        # plt.show()