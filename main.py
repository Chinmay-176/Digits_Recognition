import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflowjs as tfjs
import tensorflow as tf
import keras

(x_train, y_train), (x_test, y_test) =tf.keras.datasets.mnist.load_data(path="mnist.npz")
x_train = x_train.reshape([-1, 28, 28, 1])
x_test = x_test.reshape([-1, 28, 28, 1])
x_train = x_train/255.0
x_test = x_test/255.0

train_label = tf.keras.utils.to_categorical(x_train)
test_label = tf.keras.utils.to_categorical(x_test)

model = keras.Sequential([
    keras.layers.Conv2D(32, (5, 5), padding="same", input_shape=[28, 28, 1]),
    keras.layers.MaxPool2D((2,2)),
    keras.layers.Conv2D(64, (5, 5), padding="same"),
    keras.layers.MaxPool2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(1024, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train,y_train,epochs=5)

loss,accuracy=model.evaluate(x_test,y_test)
print(accuracy)
print(loss)

model.save('Digit.model')


# for x in range(5,6):
#     img= cv.imread(f'{x}.png')[:,:,0]
#     img=np.invert(np.array([img]))
#     prediction=model.predict(img)
#     print("The digit is probably ",np.argmax(prediction))
#     plt.imshow(img[0],cmap=plt.cm.binary)
#     plt.show()


tfjs.converters.save_keras_model(model,"models")
