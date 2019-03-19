# Minist Tutorial

Use [Keras.io](https://keras.io/) to code a simple CNN network for tutorial purpose.

## Result

After 5 epochs of training on MNIST training dataset and evaluating using MNIST test dataset:

    Loss: 0.1663	Accuracy: 0.9476

## Before Start

1. Make sure you have properly installed TensorFlow as Keras uses it for backend computation
2. Make sure you have installed Keras: `pip install keras`
3. If you are on a Mac and encounter problem when trying to download the MNIST dataset, go to `~/Application/YOUR-PYTHON` in finder and double click `Install Certificates.command` to properly install SSL certificate

## Neural Network Structure

    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    input_1 (InputLayer)         (None, 28, 28)            0         
    _________________________________________________________________
    reshape_1 (Reshape)          (None, 28, 28, 1)         0         
    _________________________________________________________________
    conv2d_1 (Conv2D)            (None, 28, 28, 4)         40        
    _________________________________________________________________
    max_pooling2d_1 (MaxPooling2 (None, 14, 14, 4)         0         
    _________________________________________________________________
    conv2d_2 (Conv2D)            (None, 14, 14, 4)         148       
    _________________________________________________________________
    max_pooling2d_2 (MaxPooling2 (None, 7, 7, 4)           0         
    _________________________________________________________________
    conv2d_3 (Conv2D)            (None, 7, 7, 8)           296       
    _________________________________________________________________
    max_pooling2d_3 (MaxPooling2 (None, 3, 3, 8)           0         
    _________________________________________________________________
    conv2d_4 (Conv2D)            (None, 3, 3, 8)           584       
    _________________________________________________________________
    max_pooling2d_4 (MaxPooling2 (None, 1, 1, 8)           0         
    _________________________________________________________________
    flatten_1 (Flatten)          (None, 8)                 0         
    _________________________________________________________________
    dense_1 (Dense)              (None, 32)                288       
    _________________________________________________________________
    dense_2 (Dense)              (None, 10)                330       
    =================================================================
    Total params: 1,686
    Trainable params: 1,686
    Non-trainable params: 0
    _________________________________________________________________