import json

def create_quiz_and_video(title, description, video_url, store):
    """Create quiz in Firestore and link to video"""
    with open('quiz.json') as f:
        quiz_json = json.load(f)
    
    # Create quiz document in Firestore
    doc_ref = store.collection("quizzes")
    result = doc_ref.add({
        "questions": quiz_json
    })
    
    quiz_id = result[1].id
    print("Quiz created successfully", quiz_id)
    
    # Create video document with reference to quiz
    create_video(title, description, video_url, quiz_id, store)
    
    return result

def create_video(title, description, video_url, quiz_id, store):
    """Create video document in Firestore"""
    print("Creating video document in database")
    
    doc_ref = store.collection("videos")
    result = doc_ref.add({
        "title": title,
        "description": description,
        "video_url": video_url,
        "quizId": quiz_id
    })
    
    print("Video created successfully", result[1].id)
    return result