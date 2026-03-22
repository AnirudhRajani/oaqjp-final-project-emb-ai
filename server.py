from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_submit():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Blank inputs are invalid."

    return_str = 'For the given statement, the system response is '
    
    return_str += f"\'anger\': {response['anger']}, "
    return_str += f"\'disgust\': {response['disgust']}, "
    return_str += f"\'fear\': {response['fear']}, "
    return_str += f"\'joy\': {response['joy']} and "
    return_str += f"\'sadness\': {response['sadness']}. "
    
    return_str += f"The dominant emotion is {response['dominant_emotion']}."

    return return_str

@app.route("/")
def main_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)