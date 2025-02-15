from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"
    
    return (f"For the given statement, the system response is 'anger': {response.get("anger")}, 'disgust': {response.get("disgust")}, 'fear': {response.get("fear")}, 'joy': {response.get("joy")} and 'sadness': {response.get("sadness")}. The dominant emotion is {response.get("dominant_emotion")}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
