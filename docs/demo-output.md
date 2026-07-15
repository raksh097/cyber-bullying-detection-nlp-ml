# Demo Output

This document shows example outputs from the rebuilt sample implementation.

The sample model uses safe demo comments from `data/sample_comments.csv`. The examples below are for demonstration only and are not from a private dataset.

## Workflow Diagram

```text
User Comment
     |
     v
Text Preprocessing
     |
     v
TF-IDF Feature Extraction
     |
     v
ML Classification
     |
     v
Prediction: safe / bullying
     |
     v
Mitigation Action
```

## Example 1: Safe Comment

Command:

```bash
python src/predict.py "you are doing great"
```

Expected output:

```text
Prediction: safe
Mitigation: no action needed.
```

Explanation:

The comment is supportive and does not contain harmful or abusive language.

## Example 2: Bullying Comment

Command:

```bash
python src/predict.py "nobody wants you here"
```

Expected output:

```text
Prediction: bullying
Mitigation: flag for review and suggest safer wording.
```

Explanation:

The comment is hostile and may harm the receiver, so the system flags it for review.

## Example 3: Disagreement Without Abuse

Command:

```bash
python src/predict.py "I disagree, but I respect your opinion"
```

Expected output:

```text
Prediction: safe
Mitigation: no action needed.
```

Explanation:

The comment expresses disagreement respectfully, so it should not be treated as cyber bullying.

## Mitigation Flow

If the model predicts `bullying`, possible actions include:

- Flag the comment for moderation
- Warn the user before posting
- Suggest rewriting the message
- Hide the comment until review
- Record the incident for safety monitoring

## Notes

- This is a small demonstration model.
- The real project can be improved with a larger dataset.
- Accuracy depends on dataset quality, preprocessing, and model choice.
- The system should support human review for sensitive decisions.
