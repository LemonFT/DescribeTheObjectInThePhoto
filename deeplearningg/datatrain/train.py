import os

import keras
import numpy as np
import tensorflow

# # Tải dữ liệu từ tập dữ liệu MNIST
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# 
# # Tạo một thư mục để lưu dữ liệu
# save_dir = "./mnist_data"
# if not os.path.exists(save_dir):
#     os.makedirs(save_dir)
# 
# # Lưu dữ liệu xuống đĩa cục bộ
# train_data_path = os.path.join(save_dir, "train_data.npz")
# test_data_path = os.path.join(save_dir, "test_data.npz")
# if not os.path.exists(train_data_path):
#     with open(train_data_path, "wb") as f:
#         np.savez(f, x_train=x_train, y_train=y_train)
# if not os.path.exists(test_data_path):
#     with open(test_data_path, "wb") as f:
#         np.savez(f, x_test=x_test, y_test=y_test)

file_path = "mnist_data/train_data.npz"

# Đọc dữ liệu từ tập tin
with np.load(file_path) as data:
    x_train = data['x_train']
    y_train = data['y_train']

# Kiểm tra dữ liệu đã đọc được
print("Shape of x_train:", x_train.shape)
print("Shape of y_train:", y_train.shape)
