"""
This is the main server for the Emotion Detector application.
It serves the index page and handles requests to analyze text sentiment
using the Emotion Detection API. The app provides an endpoint to 
predict emotions based on the given text.

Dependencies:
- Flask
- EmotionDetection (Emotion detection module)

Usage:
Run this file to start the server, which will be accessible at 
http://0.0.0.0:5000.
"""


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

# Define route for the index page
@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

# Define route for emotion detection
@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the sentiment of the input text and return the results."""
    # Get text from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."

    # Get the emotion prediction response from the emotion detector
    response = emotion_detector(text_to_analyze)

    # Format and return the response
    return (
        f"For the given statement, the system response is "
        f"'anger': {response.get('anger')}, "
        f"'disgust': {response.get('disgust')}, "
        f"'fear': {response.get('fear')}, "
        f"'joy': {response.get('joy')} and "
        f"'sadness': {response.get('sadness')}. "
        f"The dominant emotion is {response.get('dominant_emotion')}."
        )


if __name__ == "__main__":
    # Start the Flask application
    app.run(host="0.0.0.0", port=5000)
