# SMS Spam Detection using NLTK

## 📌 Overview

### This project implements an SMS spam detection system using Natural Language Processing (NLP) with the NLTK library. The model is trained to classify SMS messages as either Spam or Ham (Not Spam) based on text analysis.

## 🛠️ Features

 1. Preprocesses SMS messages (tokenization, stopword removal, stemming)

 2. Extracts features using TF-IDF vectorization
 
 3. Trains a classification model (e.g., Naive Bayes, Logistic Regression, etc.)

 4. Predicts whether a given SMS is spam or not

## 🚀 Technologies Used

 * Python

 * NLTK (Natural Language Toolkit)

 * Scikit-learn

 * Pandas

 * NumPy

 * Matplotlib (for visualization)
   
## 📊 Dataset

The dataset consists of SMS messages labeled as spam or ham. A common dataset used for this task is the SMS Spam Collection dataset.

## 🔧 Installation & Setup

  1. Clone this repository:

  ```sh
  git clone https://github.com/yourusername/sms-spam-detection.git
  cd sms-spam-detection
  ```
  
  2. Install dependencies:

  ```sh
  pip install -r requirements.txt
  ```

  3. Run the training script:

  ```sh
  python src/train_model.py
  ```

  4. Make predictions using:

  ```sh
  python src/predict.py "Your message here"
  ```

## 🖥️ Usage

  * Train the model using train_model.py.
  
  * Use predict.py to check if a message is spam.
  
  * Optionally, run app.py to start a simple web interface for classification.
