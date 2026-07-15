# Model Workflow

This document outlines the planned workflow for the Cyber Bullying Detection and Mitigation project.

## 1. Data Preparation

- Collect or prepare social media text samples.
- Label text as harmful, bullying, neutral, or safe based on the project design.
- Keep the dataset organized and documented.

## 2. Text Preprocessing

Common preprocessing steps:

- Convert text to lowercase
- Remove unnecessary punctuation and symbols
- Remove extra spaces
- Tokenize text
- Remove stop words if needed
- Convert text into features

## 3. Feature Extraction

Possible feature extraction methods:

- Bag of Words
- TF-IDF
- Word embeddings

The selected method should match the model and dataset size.

## 4. Model Training

Train a supervised classification model to identify harmful content.

Possible models:

- Logistic Regression
- Naive Bayes
- Support Vector Machine
- Random Forest

## 5. Evaluation

Track metrics such as:

- Accuracy
- Precision
- Recall
- F1 score
- Confusion matrix

## 6. Mitigation Flow

After text is flagged, the system can support:

- Warning before posting
- Sending flagged text for moderation
- Hiding abusive content
- Suggesting safer wording

## Learning Focus

This mini project connects cybersecurity awareness, online safety, NLP, and machine learning in a practical social media use case.
