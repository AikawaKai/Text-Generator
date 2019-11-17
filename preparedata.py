import os


def gen_sequences(raw_text, sequences, length=10):
    # organize into sequences of characters
    for i in range(length, len(raw_text)):
        # select sequence of tokens
        seq = raw_text[i - length:i + 1]
        # store
        sequences.append(seq)
    print('Total Sequences: %d' % len(sequences))


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()


if __name__ == '__main__':
    path_ = "../corpus/"
    files = [path_ + f for f in os.listdir(path_)]
    sequences = []
    for file_ in files:
        raw_text = load_doc(file_)
        tokens = raw_text.split(" ")
        raw_text = ' '.join(tokens)
        print(raw_text)
        gen_sequences(raw_text, sequences)
    save_doc(sequences, "sequences.txt")
# from keras.models import Sequential
# from keras.layers import Dense, LSTM
#
# model = Sequential()
# model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
# model.add(Dense(vocab_size, activation='softmax'))
# model.compile(loss = 'categorical_crossentropy',
#               optimizer = 'adam',
#               metrics = ['accuracy'])
# model.fit(X, y, epochs = 100, verbose = 2)
#
