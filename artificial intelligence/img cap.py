import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import json

# Step 1: Extract Image Features (ResNet)

def extract_image_features(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Load pre-trained ResNet model without the top layer
    base_model = ResNet50(weights='imagenet', include_top=False)
    model = Model(inputs=base_model.input, outputs=base_model.layers[-1].output)

    # Extract features
    features = model.predict(img_array)
    features = np.reshape(features, (1, features.shape[1]))

    return features

# Step 2: Build Captioning Model (LSTM-based)

def build_captioning_model(vocab_size, max_len, embedding_dim=256, lstm_units=512):
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_len))
    model.add(LSTM(lstm_units, return_sequences=False))
    model.add(Dense(vocab_size, activation='softmax'))

    optimizer = Adam(learning_rate=0.001)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    return model

# Step 3: Train the Captioning Model

def prepare_data(data_path, vocab_size, max_len):
    # Load your preprocessed data (replace with your data loading logic)
    # For simplicity, let's assume you have image paths and corresponding captions in a JSON file
    with open(data_path, 'r') as file:
        data = json.load(file)

    # Process the data and create input sequences and target sequences (replace with your data preparation logic)
    # For simplicity, let's assume you have a function prepare_data() to do that
    X_train, y_train = prepare_data(data, vocab_size, max_len)

    return X_train, y_train

# Assuming you have a tokenizer and vocabulary size
vocab_size = 1000  # Replace with the actual vocabulary size
max_len = 20  # Replace with the actual maximum caption length

# Load your preprocessed data
X_train, y_train = prepare_data('path/to/train_data.json', vocab_size, max_len)

# Build and compile the captioning model
captioning_model = build_captioning_model(vocab_size, max_len)

# Train the model
captioning_model.fit(X_train, y_train, epochs=10, batch_size=32)

# Step 4: Generate Captions for Images

def generate_caption(image_path, tokenizer, idx_to_word, max_len, captioning_model):
    # Extract features from the image
    image_features = extract_image_features(image_path)

    # Initialize the caption with a start token
    caption = ['<start>']

    # Generate the caption word by word
    for _ in range(max_len):
        # Convert the current caption to a sequence of word indices
        seq = tokenizer.texts_to_sequences([caption])[0]
        # Pad the sequence to the max length
        seq = pad_sequences([seq], maxlen=max_len, padding='post')

        # Predict the next word
        next_word_idx = np.argmax(captioning_model.predict([image_features, seq]))

        # Convert the index to the corresponding word
        next_word = idx_to_word[next_word_idx]

        # Break if the end token is predicted
        if next_word == '<end>':
            break

        # Append the predicted word to the caption
        caption.append(next_word)

    # Join the words to form the final caption
    generated_caption = ' '.join(caption[1:])
    return generated_caption
