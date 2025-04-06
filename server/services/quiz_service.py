import google.generativeai as genai
import json
from services.firebase_service import  create_quiz_and_video

def generate_quiz(transcript, title, description, video_url, env, store):
    """Generate quiz from transcript using Google Gemini"""
    # Set up the API key
    genai.configure(api_key=env["GENAI_API_KEY"])
    
    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }
    
    # Set up the safety settings
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    
    convo = model.start_chat(history=[])
    
    prompt = transcript + " Generate a quiz of MCQ along with options, answer key must be in '0,1,2,3', explaination in short & a point in terms of difficulty from 1 to 10, using previous structure and store it in json file with no extra text and there should be a predefined segment number for each question where have you taken quesstion from transcript"
    convo.send_message(prompt)
    
    response_text = convo.last.text.strip()
    quiz_text = response_text[8:-5]  # Remove markdown code block markers
    
    with open('quiz.json', 'w') as jsonFile:
        jsonFile.write(quiz_text)
    
    # Save quiz to firebase and create video record
    create_quiz_and_video(title, description, video_url, store)