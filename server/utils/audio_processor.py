import os
from moviepy.editor import AudioFileClip

def process_audio(video_path):
    """Process video file to extract audio chunks"""
    # Ensure audio directory exists
    base_path = "allaudio"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    else:
        # Delete previously generated audio chunk files
        for file in os.listdir(base_path):
            os.remove(os.path.join(base_path, file))
    
    # Extract audio from video
    audio_clip = AudioFileClip(video_path)
    n = round(audio_clip.duration)
    counter = 0
    start = 0
    audio_clip.close()
    
    # Time interval for each audio clip
    time_interval = 60
    index = time_interval
    flag_to_exit = False
    audio_paths = []
    
    # Split audio into chunks
    while True:
        audio_clip = AudioFileClip(video_path)
        if index >= n:
            flag_to_exit = True
            index = audio_clip.duration
        
        temp = audio_clip.subclip(start, index)
        
        temp_path = os.path.join(base_path, f"temp{counter}.mp3")
        temp.write_audiofile(filename=temp_path)
        temp.close()
        audio_paths.append(temp_path)
        
        counter += 1
        start = index
        index += time_interval
        audio_clip.close()
        
        if flag_to_exit:
            break
    
    return audio_paths