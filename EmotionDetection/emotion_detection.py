"""
Emotion detector 
"""
# Import the requests library
import requests, json

# Define the "emotion_detector" function, which receives as an argument "text_to_analyze"
def emotion_detector(text_to_analyze):
    """
    emotion_detector function
    Input: text_to_analyze
    Output: response.text
    """
    # Define the Watdon NLP URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Define the headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Create a request and store the response in "response" variable
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    emotion_scores  = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    formatted_data = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    # Return the response as text
    return formatted_data
