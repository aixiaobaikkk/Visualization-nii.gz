import nibabel as nib
import matplotlib.pyplot as plt

# 读取.nii.gz文件
nii_file = r'your_nii_file_path'
nii_img = nib.load(nii_file)

# 获取图像数据
nii_data = nii_img.get_fdata()

# 可以根据需要选择特定的切片进行显示
slice_index = 100 # 选择第100个切片
slice_data = nii_data[:, :, slice_index]

# 显示图像
plt.imshow(slice_data, cmap='gray')
plt.axis('off')  # 不显示坐标轴
save_path = nii_file.replace('.nii.gz', '.png')
plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

plt.show()
