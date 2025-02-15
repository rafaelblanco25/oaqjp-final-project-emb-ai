import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed

    response = requests.post(url, json = myobj, headers=headers)  # Send a POST request to the API with the text and headers

    responseJson = response.json()  # Convert the response to JSON

    setOfEmotions = responseJson

    return setOfEmotions  # Return the response text from the API