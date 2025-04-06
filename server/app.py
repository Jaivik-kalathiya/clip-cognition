from flask import Flask, jsonify, request
from flask_cors import CORS
import os

from config.config import load_environment
from utils.video_processor import download_video
from utils.audio_processor import process_audio
from utils.transcript import generate_transcript
from services.quiz_service import generate_quiz

from utils.transcript import generate_transcript




app = Flask(__name__)
CORS(app)

# Load environment
env, store = load_environment()

@app.route('/getTranscript', methods=['POST'])
def getTranscript():
    data = request.json
    video_url = data['url']
    title = data['title']
    description = data['description']

    # Download video
    filename = "downloaded_video.mp4"
    success = download_video(video_url, filename)
    if not success:
        return jsonify({'error': 'Failed to download video'}), 400

    # Process audio
    audio_paths = process_audio(filename)
    
    # Generate transcript
    transcript = generate_transcript(audio_paths)
    
    # Save transcript
    with open('transcript.txt', 'w', encoding="utf-8", errors='ignore') as textFile:
        textFile.write(transcript)
    
    # Generate quiz
    generate_quiz(transcript, title, description, video_url, env, store)
    
    success_message = {'message': 'Operation was successful'}
    return jsonify(success_message), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)