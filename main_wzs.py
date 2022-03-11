"""
功能：绘图
时间：2022.03.08
作者：TsingHua-iDLab-王左帅
"""
# todo: 今天下午的任务：形成完善的整体框架（主要是处理好关于参数的接口问题）。
#                    具体包括：
#                    （1）确定matplotlib提供的图形颜色种类；
#                    （2）确定matplotlib他的字体种类；
#                    （3）阅读海桐的画图代码，了解其画图思想和实现手段；
#                    （4）画直方图；
#                    （5）画雷达图；
#                    （6）将昨天开会的要求实现；
#                    （7）画动态图像；
#                    （8）根据李老师的指导方针完善本模块的功能。


# todo: 下午看海桐的画图代码，
#  明天上午的任务是完善文档。
# todo:模块开发宗旨：让使用者只修改接口就可完成期待图像的绘制，不需要关注plot模块中的具体代码操作。

# 注意；会编程了就千万不要所有的东西都自己写了，现在追求的应该是更高层次的目标，
# 即又好又快的实现目的，而不必在乎用的什么手段，比如抄和改写。

import os

import matplotlib.font_manager

from plot_wzs import Plotter
import plot_config
from matplotlib import font_manager
from datetime import datetime
import matplotlib.pyplot as plt


def main(scheme, color):
    """图像绘制入口"""
    draw = Plotter(scheme, color)
    draw.plot()

    # 图像保存
    log_dir = './figure/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    os.makedirs(log_dir, exist_ok=True)
    plt.savefig(fname=log_dir + '/polygon_radar.jpg')




    # for font in font_manager.fontManager.ttflist:
    #     # 查看字体名以及对应的字体文件名
    #     # print(font.name, '   ==||==   ', font.fname)
    #     print(font.name)

    # # matplotlib 查看所有可设置字体及设置中文字体
    # a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
    # for i in a:
    #     print(i)





if __name__ == '__main__':
    os.environ["OMP_NUM_THREADS"] = "1"
    print('--欢迎来到LasVSim的绘图世界！永远记得实力捍卫尊严！')
    main(plot_config.SCHEME[0], plot_config.GRAPH_COLOR[4])























# 经验：有时候先实现一个小例子，然后再写整体方案反而更加简单。
# 经验：先调研再实现会简单很多。
