from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import time
import datetime
import cv2
import serial_rx_tx
import requests
import os

# ---------------- TELEGRAM SETTINGS ----------------
BOT_TOKEN = "8587332127:AAFUIZvQxQ7c0JQR-dIFfttdZkOOiUhaC3M"
CHAT_ID = "5607096547"

def send_telegram_alert(message):
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload, timeout=5)
        print("Telegram alert sent")
    except:
        print("Telegram error")

# ---------------- SERIAL COMMUNICATION -------------
serialPort = serial_rx_tx.SerialPort()

def OpenCommand():
    comport = 'COM15'
    baudrate = '9600'
    serialPort.Open(comport, baudrate)

def SendDataCommand(cmd):
    message = str(cmd)
    if serialPort.IsOpen():
        serialPort.Send(message)

OpenCommand()
time.sleep(2)

# ---------------- EYE ASPECT RATIO -----------------
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# ---------------- PARAMETERS -----------------------
thresh = 0.25
frame_check = 20
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

cap = cv2.VideoCapture(0)
flag = 0
alert_sent = False

print("Drowsiness detection started")

# ---------------- MAIN LOOP ------------------------
while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)

    for subject in subjects:
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < thresh:
            flag += 1
            print(flag)

            if flag >= frame_check:
                cv2.putText(frame, "ALERT DROWSINESS DETECTED", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                SendDataCommand("1")

                if not alert_sent:
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    message = (
                        "DROWSINESS ALERT\n"
                        "Driver is drowsy\n"
                        "Time: " + current_time
                    )
                    send_telegram_alert(message)
                    alert_sent = True
        else:
            flag = 0
            alert_sent = False

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
