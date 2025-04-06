import whisper
import os

def generate_transcript(audio_paths):
    """Generate transcript from audio files"""
    final_text = ""
    counter = 0
    
    # Load whisper model
    model = whisper.load_model("base", device="cpu")
    
    # Process each audio chunk
    for index, path in enumerate(audio_paths):
        result = model.transcribe(path, fp16=False)
        final_text += result['text']
        print("Progress: ", (index+1)/len(audio_paths)*100, "%")
    
    print("Transcript generation completed")
    return final_text