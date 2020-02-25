from naivebayes import read_label_data, read_image_data
import numpy as np
import time

def get_pixels(image):
    pix = list()
    for line in image:
        for pixel in line:
            if pixel != ' ':
                pix.append(1)
            else:
                pix.append(0)

    pix.insert(0, 1)
    return pix


# decision function
def f(x):
    return [1 if x > 0 else 0]


def make_feature_vectors(image_data, label_data):
    return [get_pixels(image) for image in image_data]


# 451 training images [0,450]
# 451 training labels [0,450]
def read_image_data(filename, N):
    with open(filename, 'r') as infile:
        lines = [line for line in infile]
    # each image is 70 lines long
    train_image_data = list()
    for i in range(0, N):
        train_image_data.append(lines[i * 70:(i + 1) * 70])
    return train_image_data

def perceptron(X,W,D,Y,n_iter):
    W = np.array(W)
    N = len(list(X))
    # start
    tic = time.clock()
    for i in range(0, n_iter):
        Y[i % N] = f(sum(W.dot(X[i % N])))[0]
        W = W + (D[i % N] - Y[i % N]) * X[i % N]
    toc = time.clock()
    accuracy = sum([1 for (a, b) in zip(Y, D) if a == b]) / N
    return accuracy,toc-tic






