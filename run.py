# run.py

import os
import json
import time
from PIL import Image

# --- Configuration matching Cloud Build Artifacts ---
OUTPUT_DIR = "frame_data"
FRAMES_DIR = os.path.join(OUTPUT_DIR, "frames")
PREDICT_DIR = os.path.join(OUTPUT_DIR, "predict")
RESULT_JSON = "result.json"

def create_mock_files():
    """Simulates the pipeline by creating output directories and files."""
    print(f"[{time.ctime()}] Starting PoC execution...")

    # 1. Create necessary output directories
    os.makedirs(FRAMES_DIR, exist_ok=True)
    os.makedirs(PREDICT_DIR, exist_ok=True)
    print(f"[{time.ctime()}] Created output directories: {FRAMES_DIR} and {PREDICT_DIR}")

    # 2. Create mock image files in frames and predict directories
    try:
        # Create a mock black image (to simulate a video frame)
        img = Image.new('RGB', (100, 100), color = 'black')
        
        frame_path = os.path.join(FRAMES_DIR, "frame_001.jpg")
        predict_path = os.path.join(PREDICT_DIR, "prediction_001.png")
        
        img.save(frame_path)
        img.save(predict_path)
        print(f"[{time.ctime()}] Created mock frame: {frame_path}")
        print(f"[{time.ctime()}] Created mock prediction: {predict_path}")
    except Exception as e:
        print(f"[{time.ctime()}] Could not create mock images (Pillow issue): {e}")

    # 3. Create the result.json file (Secondary Artifact)
    result_data = {
        "pipeline_run": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success",
        "total_frames_processed": 1,
        "artifact_location_check": "gs://demo-artifact-bucket/videoFrames/"
    }
    
    with open(RESULT_JSON, 'w') as f:
        json.dump(result_data, f, indent=4)
    print(f"[{time.ctime()}] Created secondary artifact: {RESULT_JSON}")
    
    # 4. Create an inspection file matching the other artifact path
    with open(os.path.join(OUTPUT_DIR, "inspection.csv"), 'w') as f:
        f.write("id,result\n1,success\n")
    print(f"[{time.ctime()}] Created main artifact check file: {os.path.join(OUTPUT_DIR, 'inspection.csv')}")


if __name__ == "__main__":
    create_mock_files()
