# Real-time Object Detection using OpenCV in Python

The Real-time Object Detection project is a computer vision-based application developed in Python using OpenCV. The primary objective of this project is to detect moving objects in a live video stream and highlight them in green while displaying the message "Moving Object Detected" on the video feed. Additionally, the project allows the user to stop the video capture by pressing the 'q' button.

## Key Features

1. **Video Capture**: The project utilizes the OpenCV library to capture a live video stream from a camera or a pre-recorded video file.

2. **Object Detection**: Upon launching the application, the first frame of the video is captured and stored as a reference frame. As the video continues to play, any object that moves within the video frame is detected in real-time using frame differencing techniques.

3. **Object Highlighting**: When a moving object is detected, it is highlighted with a green bounding box or contour, making it easily distinguishable from the static background.

4. **Dynamic Display**: The video feed is dynamically updated to include the message "Moving Object Detected" whenever an object is detected, replacing the normal video stream.

5. **User Interaction**: The project allows the user to stop the video capture by pressing the 'q' button on the keyboard. This feature provides flexibility and control over the execution of the application.

## Usage

1. Clone the repository:

```bash
git clone <https://github.com/ratish-0604/Moving_Object_Detection.git>
