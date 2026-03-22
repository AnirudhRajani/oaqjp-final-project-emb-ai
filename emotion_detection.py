import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = body, headers=header)
    formatted_response = json.loads(response.text)
    return_response = formatted_response['emotionPredictions'][0]['emotion']

    dict_keys = list(return_response.keys())
    dict_values = list(return_response.values())

    dominant_emotion = None
    largest_score = 0
    for i in range(len(dict_values)):
        if dict_values[i] > largest_score:
            return_response['dominant_emotion'] = dict_keys[i]
            largest_score = dict_values[i]

    return return_response