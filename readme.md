🚗 Driver Drowsiness Detection System
📌 Overview

    This project is a real-time Driver Drowsiness Detection System that uses computer vision and facial landmark detection to monitor a driver’s eye movements and detect signs of fatigue.

When drowsiness is detected, the system :-
    Triggers alerts
    Sends notifications via Telegram
    Communicates with external hardware (e.g., Arduino)


🎯 Features :-
    👁️ Real-time eye tracking using webcam
    📉 Eye Aspect Ratio (EAR) based drowsiness detection
    🔔 Alert system when driver is sleepy
    📲 Telegram notifications for remote alerting
    🔌 Serial communication with Arduino for hardware response
    🧠 Facial landmark detection using pre-trained model


🛠️ Technologies Used :-

    Python
    OpenCV (cv2)
    dlib
    imutils
    SciPy
    Requests (for Telegram API)
    Serial Communication (Arduino integration)


📂 Project Structure :-

        Drowsiness_Detection/
        │── main.py                     # Main execution file
        │── Drowsiness_Detection.py    # Core detection logic
        │── serial_rx_tx.py            # Serial communication module
        │── terminal.py                # Serial terminal helper
        │── models/
        │   └── shape_predictor_68_face_landmarks.dat
        │── assets/                    # Sample eye images
        │── driver_drowsiness_robot_april_24/
        │   └── .ino file (Arduino code)
        │── Documents/                 # Reports, PPTs, screenshots


⚙️ How It Works :-

    Webcam captures live video feed
    Face is detected using dlib
    Facial landmarks (eyes) are extracted
    Eye Aspect Ratio (EAR) is calculated
    If EAR falls below threshold for a certain number of frames:
    Driver is considered drowsy
    Alert is triggered
    Telegram message is sent
    Signal is sent to Arduino


📊 Key Algorithm :-

    Eye Aspect Ratio (EAR):

    EAR = (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
    Low EAR → Eyes closed → Drowsiness
    High EAR → Eyes open
    🚀 Installation & Setup
    1️⃣ Clone the Repository
    git clone <your-repo-link>
    cd Drowsiness_Detection
    2️⃣ Install Dependencies
    pip install opencv-python dlib imutils scipy requests
    3️⃣ Download Model File

Ensure this file exists:

    models/shape_predictor_68_face_landmarks.dat
        ▶️ Running the Project
            python main.py

        🔌 Hardware Setup (Optional)
            Connect Arduino to system
            Update COM port in main.py:
            comport = 'COM15'
            baudrate = '9600'
            Upload .ino file to Arduino
        📲 Telegram Integration

            Update your credentials in main.py:

            BOT_TOKEN = "YOUR_BOT_TOKEN"
            CHAT_ID = "YOUR_CHAT_ID"

            ⚠️ Important: Never upload your real bot token publicly.

            ⚠️ Parameters You Can Tune
            thresh = 0.25       # EAR threshold
            frame_check = 20    # Frames to confirm drowsiness
            
🧪 Output
    Live webcam feed with detection
    Alert when drowsiness detected
    Telegram notification sent
    Hardware trigger activated

    📸 Sample Use Cases
        Driver safety systems
        Smart vehicles
        Fleet monitoring
        Accident prevention systems

    🚧 Limitations
        Works best in good lighting conditions
        Requires clear face visibility
        Performance depends on webcam quality
        May not work well with sunglasses

    🔮 Future Enhancements
        Mobile app integration
        AI-based fatigue prediction
        Cloud monitoring dashboard
        Multi-face detection
        Voice alert system

About the Project :-
    Developed as part of an academic project on Driver Safety & AI-based Monitoring Systems.