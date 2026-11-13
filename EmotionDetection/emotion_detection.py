import requests
import json

def emotion_detector(text_to_analyze):
    empty_result = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    if not text_to_analyze or len(text_to_analyze) == 0:
        return empty_result

    # request setup
    api_url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_payload = { "raw_document": { "text": text_to_analyze } }

    # perform request
    response = requests.post(api_url, headers=headers, json=request_payload)

    if response.status_code == 400:
        return empty_result

    return process(response.text)

def process(text_response):
    json_response = json.loads(text_response)

    if "emotionPredictions" not in json_response:
        raise ValueError("expected 'emotionPredictions' object")
    emotion_predictions = json_response["emotionPredictions"]

    if len(emotion_predictions) != 1:
        raise ValueError("expected exactly one 'emotionPrediction' object")
    predictions = emotion_predictions[0]

    if 'emotion' not in predictions:
        raise ValueError("expected 'emotion' object")
    scores = predictions['emotion']

    if len(scores) == 0:
        raise ValueError("expected at least one 'emotion' object")

    if "anger" not in scores:
        raise ValueError("'anger' not found")
    if "disgust" not in scores:
        raise ValueError("'disgust' not found")
    if "fear" not in scores:
        raise ValueError("'fear' not found")
    if "joy" not in scores:
        raise ValueError("'joy' not found")
    if "sadness" not in scores:
        raise ValueError("'sadness' not found")

    anger_score = scores["anger"]
    disgust_score = scores["disgust"]
    fear_score = scores["fear"]
    joy_score = scores["joy"]
    sadness_score = scores["sadness"]

    dominant_emotion, dominant_score = max(scores.items(), key=lambda x: x[1])
    return {"anger": anger_score, "disgust": disgust_score, "fear": fear_score, "joy": joy_score, "sadness": sadness_score, "dominant_emotion": dominant_emotion}
