#!/usr/bin/env python
"""
Trains a simple deep NN on the MNIST dataset.
Gets to 98.90% test accuracy after 30 epochs
"""
import numpy  as np
import pandas as pd

from keras.datasets import mnist

from keras.models       import Sequential
from keras.layers       import Dense
from keras.layers.noise import GaussianNoise
from keras.optimizers   import Adam 
from keras.utils        import to_categorical

def main():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype('float32') / 255.0
    x_test  = x_test .reshape(10000, 784).astype('float32') / 255.0
    y_train = to_categorical(y_train, 10)
    y_test  = to_categorical(y_test , 10)

    model = Sequential()
    model.add(GaussianNoise(stddev=0.4, input_shape=(x_train.shape[1],)))
    model.add(Dense(512, activation="relu"))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(10 , activation="softmax"))

    model.summary()

    model.compile(optimizer=Adam(), 
                  loss="categorical_crossentropy", 
                  metrics=["accuracy"])

    model.fit(x_train, y_train,
              batch_size=128, epochs=30, validation_data=(x_test,y_test))

    print(model.evaluate(x_test, y_test))


if __name__ == '__main__':
    main()