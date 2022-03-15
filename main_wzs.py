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
from __future__ import print_function
import argparse
import os
from plot_wzs import Plotter
import plot_config
from datetime import datetime
import matplotlib.pyplot as plt

def built_parser(scheme):
    parser = argparse.ArgumentParser()
    '''Task'''
    '''scheme list'''
    parser.add_argument("--scheme", type=int, default=scheme)
    parser.add_argument("--scheme_name", type=dict,
                       default={0: '单变量-曲线图',
                                1: '单变量-散点图',
                                2: '单变量-直方图',
                                3: '相关变量-曲线图',
                                4: '相关变量-散点图',
                                5: '双Y轴-曲线图',
                                6: '双Y轴-散点图',
                                7: '双Y轴-直方图',
                                8: '圆形雷达图',
                                9: '多边形雷达图',
                                10: '规则多幅子图绘制',
                                11: '不规则多幅子图绘制'})

    '''font setting'''
    parser.add_argument("--font", type=str, default='SimSun', help='SimSun or Times New Roman')

    '''figsize setting'''
    parser.add_argument("--figsize", type=dict, default=(12, 8), help='(12, 8) or (8, 8)')

    '''dpi setting'''
    parser.add_argument("--DPI", type=int, default=300, help='300 or 600')

    '''graph setting'''
    parser.add_argument("--graph_color", type=list, default=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])

    '''axes label setting'''
    parser.add_argument("--xlabel", type=str, default='输入数据 x')
    parser.add_argument("--ylabel", type=str, default='输出数据 y')
    parser.add_argument("--y2label", type=str, default='输出数据 y', help='双Y轴右边的y轴标签')
    parser.add_argument("--axes_label_size", type=int, default=20)
    parser.add_argument("--axes_label_color", type=str, default='black')

    '''ticks setting'''
    parser.add_argument("--tick_font", type=str, default='Times New Roman')
    parser.add_argument("--tick_size", type=int, default=15)

    '''title setting'''
    parser.add_argument("--title", type=str, default='图像标题')
    parser.add_argument("--title_size", type=int, default=25)
    parser.add_argument("--title_color", type=str, default='black')

    '''legend setting'''
    parser.add_argument("--legend_size", type=int, default='15')
    return parser.parse_args()

def main(scheme):
    """图像绘制入口"""
    args = built_parser(scheme=scheme)
    draw = Plotter(args)
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
    main(1)





















# 经验：有时候先实现一个小例子，然后再写整体方案反而更加简单。
# 经验：先调研再实现会简单很多。

# 注意；会编程了就千万不要所有的东西都自己写了，现在追求的应该是更高层次的目标，
# 即又好又快的实现目的，而不必在乎用的什么手段，比如抄和改写。
