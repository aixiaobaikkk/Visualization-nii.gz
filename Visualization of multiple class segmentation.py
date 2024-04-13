import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from scipy.ndimage import gaussian_filter
# 读取.nii.gz文件
nii_file = r'your_predict_nii_file_path'
nii_img = nib.load(nii_file)

# 获取图像数据
nii_data = nii_img.get_fdata()

# 可以根据需要选择特定的切片进行显示
slice_index = 0 # 选择第50个切片
slice_data = nii_data[:, :, slice_index]
# 创建自定义颜色映射
colors = ['black', 'purple', 'green', 'blue']  # 每个类别对应的颜色
cmap = ListedColormap(colors)
# 将边缘像素值设置为背景像素值
background_value = 0
slice_data[np.where(slice_data == background_value)] = background_value
# 使用高斯滤波器平滑边缘
sigma = 0# 高斯滤波器的标准差
smoothed_data = gaussian_filter(slice_data, sigma=sigma)
# 显示图像，使用bilinear插值方法平滑图像
plt.imshow(smoothed_data, cmap=cmap, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
# 根据原始文件名保存图像
save_path = nii_file.replace('.nii.gz', '.png')
plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

plt.show()
