import requests

def emotion_detector(text_to_analyze):
    # request setup
    api_url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyze } }

    # perform request
    response = requests.post(api_url, headers=headers, json=json)

    return response.text
