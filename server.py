from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    emotions_str = ", ".join(f"'{emotion}': {score}" for emotion, score in response.items())

    return f"For the given statement, the system response is {emotions_str}. The dominant emotion is {response['dominant_emotion']}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)