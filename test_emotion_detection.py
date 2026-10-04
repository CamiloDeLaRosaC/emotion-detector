"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify all five supported dominant emotions and invalid input."""

    @staticmethod
    def _service_response(dominant_emotion):
        scores = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
        }
        scores[dominant_emotion] = 0.96
        response = Mock(status_code=200)
        response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        response.raise_for_status.return_value = None
        return response

    def _assert_dominant_emotion(self, text, expected):
        with patch("EmotionDetection.emotion_detection.requests.post") as post:
            post.return_value = self._service_response(expected)
            result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], expected)

    def test_joy(self):
        """A joyful statement is classified as joy."""
        self._assert_dominant_emotion("I am glad this happened", "joy")

    def test_anger(self):
        """An angry statement is classified as anger."""
        self._assert_dominant_emotion("I am really mad about this", "anger")

    def test_disgust(self):
        """A disgusted statement is classified as disgust."""
        self._assert_dominant_emotion("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        """A sad statement is classified as sadness."""
        self._assert_dominant_emotion("I am so sad about this", "sadness")

    def test_fear(self):
        """A fearful statement is classified as fear."""
        self._assert_dominant_emotion("I am really afraid that this will happen", "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, post):
        """A 400 response returns the standardized empty result."""
        post.return_value = Mock(status_code=400)
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])
        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()
