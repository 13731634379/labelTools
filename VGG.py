# -*- coding: utf-8 -*-
# @Time    : 2024/5/13 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : VGG.py
# @Software: PyCharm
# 作用      :
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, optimizers, metrics, Sequential
import numpy as np
import os

tf.random.set_seed(0)
np.random.seed(0)
os.environ['TF_CPP_MIN_LEVEL'] = '2'
assert tf.__version__.startswith('2.')


batch_size = 128
epochs = 50
optimizer = optimizers.Adam(0.0001)

class VGG_13(keras.Model):
    def __init__(self):
        super(VGG_13, self).__init__()

        # unit1 [b,32,32,3] => [b,16,16,64]
        self.conv1 = layers.Conv2D(64, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv2 = layers.Conv2D(64, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool1 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit2 [b,16,16,64] => [b,8,8,128]
        self.conv3 = layers.Conv2D(128, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv4 = layers.Conv2D(128, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool2 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit3 [b,8,8,128] => [b,4,4,256]
        self.conv5 = layers.Conv2D(256, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv6 = layers.Conv2D(256, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool3 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit4 [b,4,4,256] => [b,2,2,512]
        self.conv7 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv8 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool4 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit5 [b,2,2,512] => [b,1,1,512]
        self.conv9 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv10 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool5 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        self.fc1 = layers.Dense(256, activation=tf.nn.relu)
        self.fc2 = layers.Dense(128, activation=tf.nn.relu)
        self.fc3 = layers.Dense(10)

    def call(self, inputs, training=None):
        x = inputs
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.pool1(out)
        # print(out.shape)

        out = self.conv3(out)
        out = self.conv4(out)
        out = self.pool2(out)
        # print(out.shape)

        out = self.conv5(out)
        out = self.conv6(out)
        out = self.pool3(out)
        # print(out.shape)

        out = self.conv7(out)
        out = self.conv8(out)
        out = self.pool4(out)
        # print(out.shape)

        out = self.conv9(out)
        out = self.conv10(out)
        out = self.pool5(out)
        # print(out.shape)

        out = tf.reshape(out, (-1, 512))

        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out
# 测试网络输出shape
model = VGG_13()
x = tf.random.normal((1, 32, 32, 3))
out = model(x)
print(out.shape)

# 查看网络
model.build(input_shape=(None, 32, 32, 3))
model.summary()

# 数据预处理
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32)/255.
    y = tf.cast(y, dtype=tf.int32)
    return x, y

# 导入数据集
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
print('train_shape:', x_train.shape, y_train.shape)
y_train = tf.squeeze(y_train, axis=1)
y_test = tf.squeeze(y_test, axis=1)
train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_db = train_db.map(preprocess).shuffle(50000).batch(batch_size)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_db = test_db.map(preprocess).batch(batch_size)

def main():
    for epoch in range(epochs):
        for step, (x, y) in enumerate(train_db):
            with tf.GradientTape() as tape:
                logits = model(x)
                y_onehot = tf.one_hot(y, depth=10)
                loss = tf.losses.categorical_crossentropy(y_onehot, logits, from_logits=True)
                loss = tf.reduce_mean(loss)
            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

            if step % 10 == 0:
                print('epoch:', epoch, 'step:', step, 'loss:', float(loss))

            # test
            if step % 100 == 0:
                total_correct = 0
                total_num = 0
                for step, (x, y) in enumerate(test_db):
                    logits = model(x)
                    prob = tf.nn.softmax(logits, axis=1)
                    pred = tf.cast(tf.argmax(prob, axis=1), dtype=tf.int32)
                    correct = tf.reduce_sum(tf.cast(tf.equal(pred, y), dtype=tf.int32))

                    total_correct += correct
                    total_num += x.shape[0]
                acc = total_correct / total_num
                print(epoch, step, 'acc:', float(acc))
                model.save_weights('./checkpoint/weights.ckpt')
                print('save weights')

if __name__ == "__main__":
    main()
# 简写方式，不需要自己写向后传播和test:
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, optimizers, metrics, Sequential
import numpy as np
import os

tf.random.set_seed(0)
np.random.seed(0)
os.environ['TF_CPP_MIN_LEVEL'] = '2'
assert tf.__version__.startswith('2.')


batch_size = 128
epochs = 50
optimizer = optimizers.Adam(0.0001)

class VGG_13(keras.Model):
    def __init__(self):
        super(VGG_13, self).__init__()

        # unit1 [b,32,32,3] => [b,16,16,64]
        self.conv1 = layers.Conv2D(64, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv2 = layers.Conv2D(64, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool1 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit2 [b,16,16,64] => [b,8,8,128]
        self.conv3 = layers.Conv2D(128, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv4 = layers.Conv2D(128, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool2 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit3 [b,8,8,128] => [b,4,4,256]
        self.conv5 = layers.Conv2D(256, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv6 = layers.Conv2D(256, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool3 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit4 [b,4,4,256] => [b,2,2,512]
        self.conv7 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv8 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool4 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        # unit5 [b,2,2,512] => [b,1,1,512]
        self.conv9 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.conv10 = layers.Conv2D(512, (3, 3), strides=1, padding='same', activation=tf.nn.relu)
        self.pool5 = layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

        self.fc1 = layers.Dense(256, activation=tf.nn.relu)
        self.fc2 = layers.Dense(128, activation=tf.nn.relu)
        self.fc3 = layers.Dense(10)

    def call(self, inputs, training=None):
        x = inputs
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.pool1(out)
        # print(out.shape)

        out = self.conv3(out)
        out = self.conv4(out)
        out = self.pool2(out)
        # print(out.shape)

        out = self.conv5(out)
        out = self.conv6(out)
        out = self.pool3(out)
        # print(out.shape)

        out = self.conv7(out)
        out = self.conv8(out)
        out = self.pool4(out)
        # print(out.shape)

        out = self.conv9(out)
        out = self.conv10(out)
        out = self.pool5(out)
        # print(out.shape)

        out = tf.reshape(out, (-1, 512))

        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out
# 测试网络输出shape
model = VGG_13()
x = tf.random.normal((1, 32, 32, 3))
out = model(x)
print(out.shape)

# 查看网络
model.build(input_shape=(None, 32, 32, 3))
model.summary()

# 数据预处理
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32)/255.
    y = tf.cast(y, dtype=tf.int32)
    y = tf.one_hot(y, depth=10)
    return x, y

# 导入数据集
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
print('train_shape:', x_train.shape, y_train.shape)
y_train = tf.squeeze(y_train, axis=1)
y_test = tf.squeeze(y_test, axis=1)
train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_db = train_db.map(preprocess).shuffle(50000).batch(batch_size)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_db = test_db.map(preprocess).batch(batch_size)

def main():
    model.compile(optimizer=optimizers.Adam(lr=0.0001),
                  loss=tf.losses.CategoricalCrossentropy(from_logits=True),
                  metrics=['acc'])
    model.fit(train_db, epochs=epochs, validation_data=test_db, validation_freq=2)
　　 model.evaluate(test_db)


if __name__ == "__main__":
    main()