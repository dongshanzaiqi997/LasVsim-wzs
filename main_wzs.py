"""
功能：绘图
时间：2022.03.08
作者：TsingHua-iDLab-王左帅
"""
# todo:
#                    （1）画动态图像；
#                    （2）根据李老师的指导方针完善本模块的功能。


# todo:完善文档。
# todo:模块开发宗旨：让使用者只修改接口就可完成期待图像的绘制，不需要关注plot模块中的具体代码操作。
from __future__ import print_function
import argparse
import os
from plot_wzs import Plotter
import plot_config
from datetime import datetime
import matplotlib.pyplot as plt

SCHEME_NAME = {0: '单变量-曲线图',
               1: '单变量-散点图',
               2: '单变量-直方图',
               3: '相关变量-曲线图',
               4: '相关变量-散点图',
               5: '双Y轴-曲线图',
               6: '双Y轴-散点图',
               7: '双Y轴-直方图',
               8: '圆形雷达图',
               9: '多边形雷达图'}


def built_parser():
    parser = argparse.ArgumentParser()

    '''data file setting'''
    parser.add_argument("--filename", type=str, default='test_wzs.csv')

    '''drawing setting'''
    parser.add_argument("--drawing_scheme", type=list, default=[0])
    parser.add_argument("--data_name", type=dict, default={0: ['time', 'x']})
    parser.add_argument("--figure_location_parameter", type=list, default=[111])
    parser.add_argument("--title", type=list, default=['标题'])
    parser.add_argument("--axes_label", type=dict, default={0: ['x', 'y1']})
    parser.add_argument("--legend_label", type=dict, default={0: ['位置x坐标的变化']})

    # parser.add_argument("--drawing_scheme", type=list, default=[7, 3, 5])
    # parser.add_argument("--data_name", type=dict, default={0: ['time', 'y'], 1: ['x', 'y'], 2: ['time', 'x', 'y']})
    # parser.add_argument("--figure_location_parameter", type=list, default=[221, 222, 212])
    # parser.add_argument("--title", type=list, default=['标题1', '标题2', '标题3'])
    # parser.add_argument("--axes_label", type=dict, default={0: ['x', 'y1', 'y2'],
    #                                                         1: ['x', 'y'],
    #                                                         2: ['x', 'y1', 'y2']})
    # parser.add_argument("--legend_label", type=dict, default={0: ['直方图1', '直方图2'],
    #                                                           1: ['行驶轨迹'],
    #                                                           2: ['位置x坐标的变化', '位置y坐标的变化']})

    '''font setting'''
    parser.add_argument("--font", type=str, default='SimSun', help='SimSun or Times New Roman')

    '''figsize setting'''
    parser.add_argument("--figsize", type=tuple, default=(8, 6), help='(12, 7) or (8, 8)')

    '''dpi setting'''
    parser.add_argument("--DPI", type=int, default=300, help='300 or 600')

    '''graph setting'''
    parser.add_argument("--graph_color", type=list, default=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
    parser.add_argument("--axes_label_size", type=int, default=20)
    parser.add_argument("--axes_label_color", type=str, default='black')

    '''ticks setting'''
    parser.add_argument("--tick_font", type=str, default='Times New Roman')
    parser.add_argument("--tick_size", type=int, default=15)

    '''title setting'''
    parser.add_argument("--title_size", type=int, default=25)
    parser.add_argument("--title_color", type=str, default='black')

    '''legend setting'''
    parser.add_argument("--legend_size", type=int, default='15')

    '''default variables drawing setting'''
    parser.add_argument("--default_variables", type=list,
                        default=['x', 'y', 'phi', 'u', 'v', 'w', 'acc_lon', 'acc_lat', 'eng_speed',
                                 'fuel_total', 'fuel_rate', 'acce_des', 'theta_des'])
    parser.add_argument("--default_units_of_the_default_variables", type=list,
                        default=['m', ' m', 'rad', 'm/s', 'm/s','rad/s','m/s^2','m/s^2','rpm','L','g/s','m/s^2','rad'])

    return parser.parse_args()

def main():
    """图像绘制入口"""
    args = built_parser()
    draw = Plotter(args)
    draw.default_variables_drawing()
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
    main()





















# 经验：有时候先实现一个小例子，然后再写整体方案反而更加简单。
# 经验：先调研再实现会简单很多。

# 注意；会编程了就千万不要所有的东西都自己写了，现在追求的应该是更高层次的目标，
# 即又好又快的实现目的，而不必在乎用的什么手段，比如抄和改写。
