# annotation-pipeline/annotations.py

import os
import time

# --- Configuration matching Cloud Build Artifacts ---
# Since the script runs from inside 'annotation-pipeline', paths are relative to it.
FRAMES_DIR = "frames"
PREDICT_DIR = "predict"
INSPECTION_FILE = "inspection.csv"

def create_annotation_artifacts():
    """Simulates the annotation pipeline work."""
    print(f"[{time.ctime()}] Starting Annotation Pipeline execution...")

    # 1. Create necessary output directories
    os.makedirs(FRAMES_DIR, exist_ok=True)
    os.makedirs(PREDICT_DIR, exist_ok=True)
    print(f"[{time.ctime()}] Created output directories: {FRAMES_DIR} and {PREDICT_DIR}")

    # 2. Create mock output files (frames and predictions)
    with open(os.path.join(FRAMES_DIR, "video_frame_001.jpg"), 'w') as f:
        f.write("mock_frame_data")
    
    with open(os.path.join(PREDICT_DIR, "annotated_image_001.png"), 'w') as f:
        f.write("mock_prediction_data")
    
    print(f"[{time.ctime()}] Created mock frame and prediction files.")

    # 3. Create the inspection file
    with open(INSPECTION_FILE, 'w') as f:
        f.write("video_id,annotation_status\nvideo_x,complete\n")
    print(f"[{time.ctime()}] Created inspection CSV file: {INSPECTION_FILE}")


if __name__ == "__main__":
    create_annotation_artifacts()
