import cv2
import numpy as np
from picamera2 import Picamera2

# 初始化
picam2 = Picamera2()
# 配置摄像头：RGB格式、分辨率（
picam2.configure(picam2.create_preview_configuration(
    main={"format": 'RGB888', "size": (1920,1080)}
))
picam2.start() 


WINDOW_NAME = "raspi_实时处理画面"
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)  # 允许窗口缩放

try:
    print("开始实时显示，按 'q' 键退出...")
    while True:
        # 1. 读取官方摄像头帧（RGB格式）
        frame = picam2.capture_array()
        
        # 图像实时处理逻辑
      
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # Picamera2是RGB格式，注意和USB摄像头的区别
        edges = cv2.Canny(gray, 50, 150)                # 边缘检测
        processed_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # 转回BGR供imshow显示
        
        # 在VNC窗口里实时显示处理后的画面
        cv2.imshow(WINDOW_NAME, processed_frame)
        cv2.resizeWindow(WINDOW_NAME, 1280, 1020)
  
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # 程序结束后清理资源（必加，避免摄像头占用）
    picam2.stop()         
    cv2.destroyAllWindows()
    print("程序已退出，资源已释放")
