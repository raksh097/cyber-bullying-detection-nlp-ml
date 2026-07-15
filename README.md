# Cyber Bullying Detection and Mitigation on Social Media

Cyber bullying detection and mitigation system using NLP and machine learning for safer social media.

## Overview

This 3rd year mini project was completed with my project partner. It focuses on detecting harmful or bullying content in social media text using Natural Language Processing and Machine Learning. The project also considers mitigation steps for flagged content to support safer online communication.

This repository now includes a small rebuilt sample implementation based on the original project concept. The sample uses safe demo comments and is meant to show the project workflow without exposing private datasets or personal social media content.

## Objectives

- Detect cyber bullying or harmful text from social media content
- Apply NLP preprocessing techniques
- Train and evaluate machine learning classification models
- Support mitigation workflows for flagged text
- Build awareness of online safety and responsible technology

## Project Workflow

1. Collect or prepare text data
2. Clean and preprocess text
3. Convert text into machine-readable features
4. Train a classification model
5. Evaluate model performance
6. Flag harmful content
7. Suggest mitigation actions for safer interaction

## NLP Steps

- Lowercasing text
- Removing noise such as punctuation and unnecessary symbols
- Tokenization
- Stop word removal
- Feature extraction
- Text classification

## Machine Learning Focus

- Supervised learning
- Classification
- Model evaluation
- Accuracy and performance comparison
- Practical use of ML for online safety

## Mitigation Ideas

- Flag harmful comments for review
- Warn users before posting harmful text
- Hide or limit abusive content
- Support moderation workflows
- Encourage safer communication

## Tech and Skills

- Python
- NLP
- Machine Learning
- Text preprocessing
- Classification models
- Cyber safety awareness

## Sample Implementation

Included files:

- `data/sample_comments.csv` - small safe demo dataset
- `src/preprocess.py` - text cleaning helper
- `src/train_model.py` - TF-IDF and Logistic Regression training demo
- `src/predict.py` - quick prediction demo for one comment
- `requirements.txt` - Python dependency list

Install dependencies:

```bash
pip install -r requirements.txt
```

Train and evaluate the sample model:

```bash
python src/train_model.py
```

Predict one comment:

```bash
python src/predict.py "you are doing great"
```

Private datasets, model files, virtual environments, and generated outputs are intentionally excluded from GitHub.

## Learning Outcome

This project helped me understand how NLP and ML can be used to identify harmful online behavior and support safer social media environments.

## Future Improvements

- Add dataset details
- Add model comparison results
- Include confusion matrix and accuracy metrics
- Build a simple web interface
- Add multilingual detection support

## Author

Rakshitha N P  
4th Year Cybersecurity Student  
Portfolio: <https://raksh097.github.io/raksh097-portfolio/>
