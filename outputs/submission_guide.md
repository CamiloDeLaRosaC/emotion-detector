# Emotion Detector — Submission Guide

This checklist maps every rubric item to the prepared evidence. Replace
`YOUR_GITHUB_URL` after publishing the repository.

## Task 1 — Repository URL (1 point)

Submit the public URL that opens `README.md`:

`YOUR_GITHUB_URL/blob/main/README.md`

## Task 2 — Watson NLP application (2 points)

- Activity 1: copy the `emotion_detector` implementation from
  `EmotionDetection/emotion_detection.py`.
- Activity 2: use the package import section in `terminal_outputs.txt`.

## Task 3 — Formatted output (2 points)

- Activity 1: copy the `scores` dictionary, `max(...)`, and return statement
  from `EmotionDetection/emotion_detection.py`.
- Activity 2: use the successful test output in `terminal_outputs.txt`, or run:

  ```bash
  .venv/bin/python -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am glad this happened'))"
  ```

  The public Watson course endpoint must be available for this live command.

## Task 4 — Package validation (2 points)

- Activity 1: submit
  `YOUR_GITHUB_URL/blob/main/EmotionDetection/__init__.py`.
- Activity 2: use the successful package import in `terminal_outputs.txt`.

## Task 5 — Unit tests (2 points)

- Activity 1: copy `test_emotion_detection.py`.
- Activity 2: use the six passing tests in `terminal_outputs.txt`.

## Task 6 — Flask deployment (2 points)

- Activity 1: copy `server.py`.
- Activity 2: upload `6b_deployment_test.png`.

## Task 7 — Error handling (3 points)

- Activity 1: copy the `response.status_code == 400` branch and
  `_empty_result` from `EmotionDetection/emotion_detection.py`.
- Activity 2: copy the `dominant_emotion is None` branch from `server.py`.
- Activity 3: upload `7c_error_handling_interface.png`.

## Task 8 — Static analysis (2 points)

- Activity 1: submit `server.py`, including its module and function docstrings.
- Activity 2: use the `pylint` result of `10.00/10` in
  `terminal_outputs.txt`.

## Final pre-submission check

- Confirm that the GitHub repository is public.
- Confirm that the default branch is `main`.
- Open both GitHub file links in a private/incognito browser window.
- Upload the two PNG files without renaming them.
- Paste each code or terminal section into its matching rubric field.
