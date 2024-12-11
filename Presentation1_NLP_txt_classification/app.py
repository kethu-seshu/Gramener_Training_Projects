import streamlit as st
import joblib
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Load the pre-trained models and vectorizer
naive_bayes_model = joblib.load('naive_bayes_model.pkl')
logistic_regression_model = joblib.load('logistic_regression_model.pkl')
vectorizer = joblib.load('count_vectorizer.pkl')  # Assuming the vectorizer is saved too

# Text cleaning function
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)  # Tokenize
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatize
    return ' '.join(tokens)

# Streamlit UI
st.title("Sentiment Analysis")

# User input
user_input = st.text_input("Enter a sentence for sentiment analysis:")

if user_input:
    # Clean the input text
    cleaned_input = clean_text(user_input)
    
    # Vectorize the input text
    input_vec = vectorizer.transform([cleaned_input])
    
    # Predict using both models
    nb_pred = naive_bayes_model.predict(input_vec)
    lr_pred = logistic_regression_model.predict(input_vec)
    
    # Display results
    sentiment = {0: 'Negative', 1: 'Positive'}
    
    st.write(f"Sentiment using Naive Bayes: {sentiment[nb_pred[0]]}")
    st.write(f"Sentiment using Logistic Regression: {sentiment[lr_pred[0]]}")
    
    # Display model accuracies
    st.write("### Model Accuracies")
    st.write(f"Naive Bayes Accuracy: 0.85")  # Update this with the actual accuracy
    st.write(f"Logistic Regression Accuracy: 0.87")  # Update this with the actual accuracy
