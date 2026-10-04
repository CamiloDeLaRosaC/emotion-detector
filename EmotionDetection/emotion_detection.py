"""Detect emotions in English text using the Watson NLP service."""

from typing import Dict, Union

import requests


SERVICE_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

EmotionScore = Union[float, str, None]
EmotionResult = Dict[str, EmotionScore]


def emotion_detector(text_to_analyse: str) -> EmotionResult:
    """Return emotion scores and the dominant emotion for the supplied text."""
    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(
        SERVICE_URL,
        json=payload,
        headers=HEADERS,
        timeout=15,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores


def _empty_result() -> EmotionResult:
    """Return the standardized response used for invalid text."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
