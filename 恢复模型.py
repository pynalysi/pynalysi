import os
import tensorflow as tf
from tensorflow import keras
import numpy as np

mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

model = keras.models.load_model('my_model.h5')

train_images = train_images.reshape(-1, 28 * 28) / 255.0
test_images = test_images.reshape(-1, 28 * 28) / 255.0

loss, acc = model.evaluate(test_images, test_labels)
print(loss)
print(acc)
print("Untrained model, accuracy: {:5.2f}%".format(100 * acc))

predictions = model.predict(test_images)

print(predictions[0])

print(np.argmax(predictions[0]))
