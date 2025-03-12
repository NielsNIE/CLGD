from ultralytics import YOLO
import torch
import cv2
import numpy as np

def test_environment():
    # 测试CUDA是否可用
    print(f"CUDA is available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA device: {torch.cuda.get_device_name(0)}")
    
    # 测试YOLOv8
    try:
        model = YOLO('yolov8n.pt')
        print("YOLOv8 model loaded successfully")
    except Exception as e:
        print(f"Error loading YOLOv8 model: {e}")
    
    # 测试OpenCV
    try:
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imshow('test', img)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        print("OpenCV working correctly")
    except Exception as e:
        print(f"Error testing OpenCV: {e}")

if __name__ == "__main__":
    print("Starting environment test...")
    test_environment() 