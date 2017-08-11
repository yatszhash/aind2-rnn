import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import re


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    series_size = series.shape[0]
    X = [series[i:i + window_size] for i in range(series_size - window_size)]
    y = [series[i] for i in range(window_size, series_size)]

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()

    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1, activation="sigmoid"))
    return model

### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']

    replace_pattern = r"[^a-z\!,\.:;\? ]"
    # compiled_pattern = re.compile(replace_pattern)
    # text.lower()
    replaced_text = re.sub(replace_pattern, ' ', text)

    return replaced_text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    text_size = len(text)
    inputs = [list(text[i:i + window_size]) for i in range(0, text_size - window_size, step_size)]
    outputs = [text[i] for i in range(window_size, text_size, step_size)]

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    pass
