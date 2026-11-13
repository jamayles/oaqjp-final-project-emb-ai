from flask import Flask, render_template
import EmotionDetection

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/emotionDetector')
def run_emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = EmotionDetection.emotion_detection.emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
