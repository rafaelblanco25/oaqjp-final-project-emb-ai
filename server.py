""" 
Server function.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """ 
    Index page.

    Args:

    Returns:

        str: html file to display to user.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """ 
    Emotion detector route function.

    Args:

    Returns:

        str: result to be displayed to the user.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"
    anger_response = f"'anger': {response.get('anger')}"
    disgust_response = f"'disgust': {response.get('disgust')}"
    fear_response = f"'fear': {response.get('fear')}"
    joy_response = f"'joy': {response.get('joy')}"
    sadness_response = f"'sadness': {response.get('sadness')}"
    dominant_emotion_response = f"The dominant emotion is {response.get('dominant_emotion')}"
    response_part_1 = f"For the given statement, the system response is {anger_response}, "
    response_part_2 = f", {disgust_response}, {fear_response}, "
    response_part_3 = f"{joy_response} and {sadness_response}. {dominant_emotion_response}."
    return f"{response_part_1} {response_part_2} {response_part_3}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
