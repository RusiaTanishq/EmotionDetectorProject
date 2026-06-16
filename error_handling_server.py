from flask import Flask, request, jsonify
from Ta_error_handling_function import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Home route"""
    return "Emotion Detection API is running"


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """API endpoint with blank input error handling"""

    data = request.get_json()

    # Safe extraction of input text
    text_to_analyze = data.get("text", "") if data else ""

    result = emotion_detector(text_to_analyze)

    # 🔴 Handle blank input (400 error case)
    if result.get("status_code") == 400:
        return jsonify({
            "message": "Invalid input! Text cannot be empty.",
            "emotions": result
        }), 400

    # 🟢 Success response
    return jsonify({
        "message": "Emotion analysis successful",
        "emotions": result
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)