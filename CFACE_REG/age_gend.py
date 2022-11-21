import cv2
import os
from datetime import datetime
import csv
from deepface import DeepFace
i = 0
now = datetime.now()
time = now.time()
db = r"E:\CFACE_REG\C_Face"
field_names = ['Name', 'Age', 'Gender', 'Enter_time', 'Leave_time', 'Spent_time']
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

def image_write(data1,image_name):
    os.chdir(db)
    cv2.imwrite(data1, image_name)
    return  print("data inserted")


def age_gender(frame, img_name):
    print(frame, img_name)
    emotRes = DeepFace.analyze(frame, actions=['age', 'gender'], detector_backend=backends[0],enforce_detection=False)
    time = now.time()
    dict = {"Name": img_name, "Age": emotRes['age'], 'Gender': emotRes['gender'], "Enter_time": time}
    with open(r'E:\CFACE_REG\log_book.csv', 'a') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names)
        dict_object.writerow(dict)
    image_write(frame,img_name)





def capturing():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()

        # cv2.putText(frame, 'Press q to quit', (200, 450), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        # cv2.imshow("mvp", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        cv2.imshow("frame",frame)
        print(frame)

        cv2.waitKey()


    cam.release()
    cv2.destroyAllWindows()






capturing()
# def






#
#
# while True:
#     cam = cv2.VideoCapture(0)
#     ret, frame = cam.read()
#     time = now.time()
#     img_name = "image_" + str(i) + '.jpg'
#     limit=5
#     for img in frame:
#         count=len(img)
#         if count!=limit:
#             os.chdir(db)
#             cv2.imwrite(img_name, img)
#         else:
#             print("noframe")
#
#
#
#
#     # cv2.imshow('Frame', frame)
#
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, 'Press q to quit', (200, 450), font, 1, (0, 255, 255), 2, cv2.LINE_4)
#     cv2.imshow("mvp", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#         i = i + 1
# cam.release()
# cv2.destroyAllWindows()
# cv2.waitKey()
# quit()
#

