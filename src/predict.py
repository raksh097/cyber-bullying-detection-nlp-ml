import argparse

from preprocess import clean_text
from train_model import build_pipeline, load_dataset


def main():
    parser = argparse.ArgumentParser(description="Run a demo cyber bullying prediction.")
    parser.add_argument("text", help="Comment text to classify.")
    parser.add_argument("--data", default="data/sample_comments.csv", help="Path to CSV dataset.")
    args = parser.parse_args()

    texts, labels = load_dataset(args.data)
    model = build_pipeline()
    model.fit(texts, labels)

    cleaned = clean_text(args.text)
    prediction = model.predict([cleaned])[0]
    print(f"Prediction: {prediction}")

    if prediction == "bullying":
        print("Mitigation: flag for review and suggest safer wording.")
    else:
        print("Mitigation: no action needed.")


if __name__ == "__main__":
    main()
