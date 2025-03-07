import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed

    response = requests.post(url, json = myobj, headers=headers)  # Send a POST request to the API with the text and headers

    if response.status_code == 400:
        requiredSetOfEmotions = { "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None , "dominant_emotion": None}  # If the response is not successful, set all emotions to 0
    else:
        formatted_response = json.loads(response.text)  # Convert the response to JSON
        requiredSetOfEmotions = formatted_response['emotionPredictions'][0]['emotion']  # Extract the emotions from the response  
        requiredSetOfEmotions['dominant_emotion'] = max(requiredSetOfEmotions, key=requiredSetOfEmotions.get)  # Find the dominant emotion

    return requiredSetOfEmotions  # Return the response text from the API