# Imports
from keras.datasets import mnist
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Input, Reshape
from keras import Model

# Constants definition
numClasses = 10
inputShape = (28, 28)

# Dataset import
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Model definition
inputs = Input(shape=inputShape)
x = Reshape((28, 28, 1))(inputs)
x = Conv2D(4, 3, activation='relu', padding='same')(x)
x = MaxPool2D()(x)
x = Conv2D(4, 3, activation='relu', padding='same')(x)
x = MaxPool2D()(x)
x = Conv2D(8, 3, activation='relu', padding='same')(x)
x = MaxPool2D()(x)
x = Conv2D(8, 3, activation='relu', padding='same')(x)
x = MaxPool2D()(x)
x = Flatten()(x)
y = Dense(32, activation='relu')(x)
out = Dense(numClasses, activation='softmax')(y)
model = Model(inputs=inputs, outputs=out)

# Print model detail
model.summary()

# Configure model optimizer and metrics
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate model
loss = model.evaluate(x_test, y_test, batch_size=32)
print(loss)
print("Loss: %.4f\tAccuracy: %.4f" % loss)