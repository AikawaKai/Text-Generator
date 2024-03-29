from numpy import array
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from pickle import dump


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


# load
in_filename = 'sequences.txt'
raw_text = load_doc(in_filename)
lines = raw_text.split('\n')
print(lines)

chars = sorted(list(set(raw_text)))
mapping = dict((c, i) for i, c in enumerate(chars))

sequences = list()
for line in lines:
    # integer encode line
    encoded_seq = [mapping[char] for char in line]
    # store
    sequences.append(encoded_seq)

# vocabulary size
vocab_size = len(mapping)
print('Vocabulary Size: %d' % vocab_size)


for i in range(len(sequences)):
    if len(sequences[i]) < 11:
        sequences[i] = sequences[i].append(1)

new_sequences = []
for seq in sequences:
    if seq is not None:
        new_sequences.append(seq)
sequences = array(new_sequences)
print(sequences.shape)
X, y = sequences[:, :-1], sequences[:, -1]

sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
X = array(sequences)
y = to_categorical(y, num_classes=vocab_size)

print(X.shape)
# define model
model = Sequential()
model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=110, verbose=2)

# save the model to file
model.save('model.h5')

# save the mapping
dump(mapping, open('mapping.pkl', 'wb'))
