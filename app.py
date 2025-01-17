import nltk
import streamlit as st
import pickle 
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the stemmer
ps = PorterStemmer()

# Text Preprocessing Function
def transform_text(text):
    text = text.lower()  # Convert text to lowercase
    text = nltk.word_tokenize(text)  # Tokenize the text

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load pre-trained model and vectorizer
tk = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Streamlit UI setup
st.set_page_config(page_title="SMS Spam Detection", page_icon="📱", layout="wide")

# Title and header with improved styling
st.markdown("<h1 style='text-align: center; color: #ff6347;'>SMS Spam Detection Model</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4CAF50;'>*Made with love by Chaitanya Ashish Kelkar*</h3>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# Add a stylish input box for the SMS text
input_sms = st.text_area("Enter the SMS Message Below:", height=150, max_chars=500, 
                         placeholder="Type your SMS message here... 📝", key="sms_input", 
                         label_visibility="collapsed", 
                         help="Input the message you want to check if it's spam or not.")

# Custom Button with styling
if st.button("Check Spam Status", key="predict_button", use_container_width=True):
    if input_sms != "":
        # Preprocess the input
        transformed_sms = transform_text(input_sms)
        # Vectorize the preprocessed input
        vector_input = tk.transform([transformed_sms])
        # Predict the class of the SMS (Spam or Ham)
        result = model.predict(vector_input)[0]

        # Display result with enhanced styling
        if result == 1:
            st.markdown("<h3 style='text-align: center; color: red;'>🚨 Spam Message Detected! 🚨</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='text-align: center; color: green;'>✅ This is a Safe Message! ✅</h3>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a message to check.", icon="⚠️")

# Add Footer with social links (if desired)
st.markdown("""
    <br><br>
    <footer style='text-align: center; color: #BDBDBD;'>
        <p>Chaitanya Kelkar | &copy; 2025 All Rights Reserved.</p>
    </footer>
""", unsafe_allow_html=True)
