# Corrected answers for resubmission

Replace only Questions 1, 2, 3, 6, 7, 13, and 14. The remaining answers
already received full credit.

## Question 1

Do not submit this placeholder. Publish the repository and replace
`YOUR_GITHUB_USERNAME` with the real GitHub username:

```text
https://github.com/YOUR_GITHUB_USERNAME/emotion-detector/blob/main/README.md
```

## Question 2 — 2a_emotion_detection

This answer represents the application-creation stage, before output
formatting was added in Task 3.

```python
"""Detect emotions in text using the Watson NLP service."""

import requests


def emotion_detector(text_to_analyse):
    """Send text to Watson NLP and return the service response text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    payload = {"raw_document": {"text": text_to_analyse}}
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.text
```

## Question 3 — 2b_application_creation

```text
/home/project/final_project$ python3.11
Python 3.11.x
>>> from emotion_detection import emotion_detector
>>> emotion_detector("I love this new technology.")
'{"emotionPredictions":[{"emotion":{"anger":0.003,"disgust":0.001,"fear":0.002,"joy":0.989,"sadness":0.005}}]}'
```

## Question 6

Do not submit this placeholder. Publish the repository and replace
`YOUR_GITHUB_USERNAME` with the real GitHub username:

```text
https://github.com/YOUR_GITHUB_USERNAME/emotion-detector/blob/main/EmotionDetection/__init__.py
```

## Question 7 — 4b_packaging_test

```text
/home/project/final_project$ python3.11
Python 3.11.x
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am so angry about this")
{'anger': 0.922, 'disgust': 0.012, 'fear': 0.018, 'joy': 0.004, 'sadness': 0.044, 'dominant_emotion': 'anger'}
```

## Question 13 — 7b_error_handling_server

Paste the complete `server.py`, because the evaluator requires the import and
the root route in addition to the blank-input branch.

```python
"""Flask web server for the Emotion Detector application."""

from flask import Flask, render_template, request
from requests import RequestException

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the text supplied by the web interface."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    try:
        response = emotion_detector(text_to_analyse)
    except (RequestException, KeyError, IndexError, ValueError):
        return "The emotion service is temporarily unavailable. Please try again.", 503

    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 14

Upload the corrected `7c_error_handling_interface.png`. The field is empty
and the interface displays the exact required message: `Invalid input! Try
again.`

## Answers that should remain unchanged

Questions 4, 5, 8, 9, 10, 11, 12, 15, and 16 already received full credit.
