"""
This is a Flask application for an Emotion Detector.
It provides endpoints to analyze text and detect the dominant emotion in the text.

Author: Omeiza Alabi
Date: 7/11/2023
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page() -> str:
    """Render the index page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector() -> str:
    """Detect emotion in the given text and return the result."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    emotions_str = ", ".join(f"'{emotion}': {score}" for emotion, score in response.items())
    system_response_text = f"For the given statement, the system response is {emotions_str}."
    dominant_emotion_text = f"The dominant emotion is {dominant_emotion}."
    return f"{system_response_text} {dominant_emotion_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
