"""
功能：放置备用资料
时间：2022.03.14
作者：Tsinghua-iDLab-王左帅
"""

# ########################################### 图例的四种实现方法 #########################################################
# fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes, fontsize=self.legend['leg_size'])
# fig.legend(labels=('exp', 'log'), loc='upper left')
# ax1.legend(fontsize=self.legend['leg_size'])
# plt.legend(handles=[s1, s2], fontsize=self.legend['leg_size'], loc='best')


# ########################################### 使图像扩展 #########################################################
# plt.tight_layout()


# ########################################### 雷达图的另一种建立形式 ####################################################
# 新建一个子图
# ax = plt.subplot(111, polar=True)


# ########################################### 饼图和条形图 ####################################################
# # 画第3个图：饼图
# plt.subplot(223)
# plt.pie(x=[15, 30, 45, 10], labels=list('ABCD'), autopct='%.0f', explode=[0, 0.05, 0, 0])
# # 画第4个图：条形图
# plt.subplot(224)
# plt.bar([20, 10, 30, 25, 15], [25, 15, 35, 30, 20], color='b')

