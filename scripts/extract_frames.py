import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    """
    Extracts frames from a video at a specified rate and saves them as images.
    
    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder where frames will be saved.
        frame_rate (int): Interval of frames to save (e.g., every 'nth' frame).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cap = cv2.VideoCapture(video_path)
    count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save frame every 'frame_rate' interval
        if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % frame_rate == 0:
            cv2.imwrite(f"{output_folder}/frame_{count:04d}.jpg", frame)
            count += 1
    
    cap.release()
    print(f"Extracted {count} frames to {output_folder}")