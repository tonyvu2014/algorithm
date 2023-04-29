from keras.datasets import imdb
import numpy as np
from keras import models, layers, optimizers
import matplotlib.pyplot as plt

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# print(train_data[0])

def decode_review(data):
    word_indices = imdb.get_word_index()
    reverse_word_index = dict((value, key) for (key, value) in word_indices.items())
    decoded_review = ' '.join(reverse_word_index.get(i-3, '?') for i in data)
    return decoded_review

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

print(x_train[0])

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000, )))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# x_val = x_train[:10000]
# partial_x_train = x_train[10000:]

# y_val = y_train[:10000]
# partial_y_train = y_train[10000:]

history = model.fit(x_train,
                    y_train,
                    epochs=40,
                    batch_size=512)
                    # validation_data=(x_val, y_val))

# history_dict = history.history
# loss_values = history_dict['loss']
# val_loss_values = history_dict['val_loss']

# epochs = range(1, 21)

# plt.plot(epochs, loss_values, 'bo', label = 'Training Loss')
# plt.plot(epochs, val_loss_values, 'b', label = 'Validation Loss')
# plt.title('Training and validation loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()

# results = model.evaluate(x_test, y_test)
# print(results)

prediction = model.predict(x_test)
print(prediction)

decoded_review = decode_review(test_data[2])
print(decoded_review)




