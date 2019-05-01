import os
import tensorflow as tf
from tensorflow import keras

#tf.enable_eager_execution()


(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels
test_labels = test_labels

train_images = train_images.reshape(-1, 28 * 28) / 255.0
test_images = test_images.reshape(-1, 28 * 28) / 255.0

# Returns a short sequential model
def create_model():
    model = tf.keras.models.Sequential([
      keras.layers.Dense(512, activation=tf.nn.relu, input_shape=(784,)),
      keras.layers.Dropout(0.2),
      keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])

    return model

# Create a basic model instance
model = create_model()


loss, acc = model.evaluate(test_images, test_labels)
print("Untrained model, accuracy: {:5.2f}%".format(100*acc))


checkpoint_path = "training_1/cp.ckpt"
model.load_weights(checkpoint_path)
loss,acc = model.evaluate(test_images, test_labels)
print(loss)
print(acc)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))
