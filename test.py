"""
功能：对一些代码片段进行测试
时间：2022.03.13
作者：Tsinghua-iDLab-王左帅
"""

# ## cycler方法的测试
# from cycler import cycler
# import matplotlib.pyplot as plt
#
# color_cycle = cycler(color=['r', 'g', 'b'])
# m_cycle = cycler(marker=['s', 'o'])
# m_c = m_cycle * color_cycle
# for i, j in enumerate(m_c):
#     print(i, j)
#     # print(j)
#     # print(*j)
#     # print([i, i])
#
#     plt.plot([i + 2, i], **j)
#
# plt.show()


#  ################################ 迭代器测试 #############################################
from collections.abc import Iterator
from cycler import cycler

color_cycler = cycler(color=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
print(color_cycler)
x = isinstance(color_cycler, Iterator)
print(x)
print('经测试，cycler对象不是一个迭代器！')
