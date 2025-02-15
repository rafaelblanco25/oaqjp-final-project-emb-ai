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

    return "For the given statement, the system response is 'anger': {}, \
        'disgust': {}, \
        'fear': {}, \
        'joy': {} \
        and 'sadness': {}. \
        The dominant emotion is {}."\
        .format(response.get("anger"), response.get("disgust"), response.get("fear"), \
                response.get("joy"), response.get("sadness"), response.get("dominant_emotion"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)