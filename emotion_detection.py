import requests
import json

print("Script started")

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers)
        print("Request sent")  # Debugging
        
        if response.status_code == 200:
            response_dict = response.json()  # Convert response to dictionary
            print("Response received:", response_dict)  # Debugging
            
            # Extract relevant emotions
            emotions = response_dict['emotion_predictions'][0]
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            
            # Find dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return formatted response
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            return {"error": f"Request failed with status code {response.status_code}"}
    
    except Exception as e:
        return {"error": str(e)}

# Take input from user
text = input("Input your statement: ")
result = emotion_detector(text)
print("Function executed")
# print(result)
