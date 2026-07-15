import argparse
import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from preprocess import clean_text


def load_dataset(path: Path):
    texts = []
    labels = []

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            texts.append(clean_text(row["text"]))
            labels.append(row["label"])

    return texts, labels


def build_pipeline():
    return Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )


def main():
    parser = argparse.ArgumentParser(description="Train a cyber bullying text classifier.")
    parser.add_argument("--data", default="data/sample_comments.csv", help="Path to CSV dataset.")
    args = parser.parse_args()

    texts, labels = load_dataset(Path(args.data))

    train_x, test_x, train_y, test_y = train_test_split(
        texts,
        labels,
        test_size=0.3,
        random_state=42,
        stratify=labels,
    )

    model = build_pipeline()
    model.fit(train_x, train_y)

    predictions = model.predict(test_x)
    print(classification_report(test_y, predictions, zero_division=0))


if __name__ == "__main__":
    main()
