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
#                           下一步的目标是想想有没有更好的实现方法。
#                           再下一个目标是将其它图像以及还没有实现的图像完整的做好
#                    （7）画动态图像；
#                    （8）根据李老师的指导方针完善本模块的功能。


# todo:完善文档。
# todo:模块开发宗旨：让使用者只修改接口就可完成期待图像的绘制，不需要关注plot模块中的具体代码操作。

import os
from plot_wzs import Plotter
import plot_config
from datetime import datetime
import matplotlib.pyplot as plt


def main(scheme, font, figsize, dpi, color, label, ticks, title, legend):
    """图像绘制入口"""
    draw = Plotter(scheme, font, figsize, dpi, color, label, ticks, title, legend)
    draw.plot()

    # 图像保存
    figure_dir = './Figures'
    os.makedirs(figure_dir, exist_ok=True)
    log_dir = './Figures/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    os.makedirs(log_dir, exist_ok=True)
    plt.savefig(fname=log_dir + '/polygon_radar.jpg')
    plt.savefig(fname=log_dir + '/polygon_radar.pdf')
    plt.savefig(fname=log_dir + '/polygon_radar.svg')



if __name__ == '__main__':
    os.environ["OMP_NUM_THREADS"] = "1"
    print('--欢迎来到LasVSim的绘图世界！成功！')
    main(plot_config.SCHEME[10],       # 画图方案
         plot_config.FONT[0],         # 字体
         plot_config.FIG_SIZE[0],     # 图像尺寸
         plot_config.DPI[0],          # 打印分辨率 todo:这种一个的可以直接写在这里
         plot_config.GRAPH_COLOR,     # 图形颜色
         plot_config.LABEL,           # 轴标签字号和颜色配置
         plot_config.TICKS,           # 轴刻度字体和字号配置
         plot_config.TITLE,           # 图像标题
         plot_config.LEGEND)          # 图例字号设置  # todo:思考是否可用argparse的方式实现会更简洁和清晰























# 经验：有时候先实现一个小例子，然后再写整体方案反而更加简单。
# 经验：先调研再实现会简单很多。

# 注意；会编程了就千万不要所有的东西都自己写了，现在追求的应该是更高层次的目标，
# 即又好又快的实现目的，而不必在乎用的什么手段，比如抄和改写。
