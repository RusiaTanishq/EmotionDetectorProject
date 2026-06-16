def emotion_detector(text_to_analyze):

    # API call here

    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.02,
        "joy": 0.8,
        "sadness": 0.03
    }

    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions