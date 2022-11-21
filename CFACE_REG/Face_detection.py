# Importing all necessary libraries
import cv2
import os
from datetime import datetime
import csv
from deepface import DeepFace

now = datetime.now()
time = now.time()
field_names = ['Name', 'Age', 'Gender', 'Enter_time', 'Leave_time', 'Spent_time']
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

# Read the video from specified path
cam = cv2.VideoCapture(0)
db = r"E:\CFACE_REG\C_Face"
# frame
i = 0


def age_gender(frame, img_name):
    # print(frame, img_name)
    emotRes = DeepFace.analyze(frame, actions=['age', 'gender'], detector_backend=backends[0],
                                   enforce_detection=False)
    os.chdir(db)
    cv2.imwrite(img_name, frame)
    time = now.time()
    dict = {"Name": img_name, "Age": emotRes['age'], 'Gender': emotRes['gender'], "Enter_time": time}
    with open(r'E:\CFACE_REG\log_book.csv', 'a') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names)
        dict_object.writerow(dict)
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    time = now.time()
    img_name = "image_" + str(i) + '.jpg'
    os.chdir(db)
    if len(os.listdir(db)) == 0:
        cv2.imwrite(img_name, frame)
        age_gender(frame, img_name)
    else:
        df = DeepFace.find(frame, db_path=db, enforce_detection=False)
        print(df)
        if len(df) == 0:
            age_gender(frame, img_name)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Press q to quit', (200, 450), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    cv2.imshow("mvp", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        i = i + 1
cam.release()
cv2.destroyAllWindows()
cv2.waitKey()
quit()

