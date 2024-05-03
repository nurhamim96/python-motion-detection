import cv2
import winsound

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('http://kamera.mikulov.cz:8888/mjpg/video.mjpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
upper_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml")

alarm = False
alarm_mode = False
alarm_counter = 0

# def beep_alarm():
#     global alarm
#     for _ in range(5):
#         if not alarm_mode:
#             break
#         winsound.Beep(2500, 1000)
#     alarm = False


while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)
    upperbodies = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) + len(bodies) + len(upperbodies) > 0:
        if not alarm:
            # alarm = True
            for _ in range(5):
                winsound.Beep(2500, 1000)
                print("Detected")

    for(x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm = not alarm
        alarm_counter = 0
    if key_pressed == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()