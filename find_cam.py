import cv2

def find_cameras(max_cameras_to_check=5):
    available_cameras = []
    for i in range(max_cameras_to_check):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

print(find_cameras())