# import the opencv library
import os
import cv2
from datetime import datetime
import face_recognition
import shutil

# check version of keras_vggface
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
DatabaseA = r"C:\Users\Amal\Downloads\CFACE_REG\CFACE_REG\A"
DatabaseB = r"C:\Users\Amal\Downloads\CFACE_REG\CFACE_REG\B"


def adjusted_detect_face(img):
    face_img = img.copy()
    face_rect = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=3)
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return face_img


# create a function to detect eyes
def detect_eyes(img):
    eye_img = img.copy()
    eye_rect = eye_cascade.detectMultiScale(eye_img, scaleFactor=1.2, minNeighbors=3)
    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return eye_img


vid = cv2.VideoCapture(0)
i = 1


def com(frame):
    b = frame
    A = r"C:/Users/Amal/Downloads/CFACE_REG/CFACE_REG/B"
    di = os.listdir(A)
    re = []
    for i in di:
        if i.endswith(".jpg"):
            # print(A + "/" + l)

            known_image = face_recognition.load_image_file(A + "/" + i)
            unknown_image = face_recognition.load_image_file(b)
            try:
                biden_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                # results = DeepFace.verify(known_image, unknown_image)
                print(results, "-------------------------------------")
                # re.append(results[0])
            except:
                print("IndexError: list index out of range")
    print(re)
    if "True" not in re:
        return False
    else:
        return True
    # if re is None or "False":
    #     return False
    # else:
    #     return True


while (True):
    ret, frame = vid.read()
    # cv2.imshow('frame', frame)
    eyes_face = adjusted_detect_face(frame)
    eyes_face = detect_eyes(eyes_face)
    cv2.imshow("mvp", eyes_face)
    now = datetime.now()
    time = now.time()
    img_name = "image_" + str(i) + '.jpg'
    os.chdir(r"C:\Users\Amal\Downloads\CFACE_REG\CFACE_REG\k")
    cv2.imwrite("img.jpg", eyes_face)
    # print(len(os.listdir(DatabaseB)))
    if len(os.listdir(DatabaseB)) <= 3:
        # print("first f")
        os.chdir(DatabaseB)
        cv2.imwrite(img_name, eyes_face)

        # else:
        #
        # count = 0
        # os.chdir("C:/Users/Amal/Downloads/CFACE_REG/CFACE_REG/k")
        # cv2.imwrite("frame%d.jpg" % count, eyes_face)
        # count = count + 1
        # k_image = os.listdir("C:/Users/Amal/Downloads/CFACE_REG/CFACE_REG/k")
        # print(type(k_image))
        # # comp_img = com(k_image)
        # # print(comp_img)

    else:
        if com(r"C:\Users\Amal\Downloads\CFACE_REG\CFACE_REG\k\img.jpg"):
            a = r"C:\Users\Amal\Downloads\CFACE_REG\CFACE_REG\A"
            if len(os.listdir(a)) <= 3:
                os.chdir(a)
                cv2.imwrite(img_name, eyes_face)

    # a = r"C:\Users\Amal\Downloads\CFACE_REG\CFACE_REG\A"
    # x = os.listdir(a)
    # if len(x) == 3:
    #
    #     source = 'C:/Users/Amal/Downloads/CFACE_REG/CFACE_REG/A'
    #     destination = 'C:/Users/Amal/Downloads/CFACE_REG/CFACE_REG/B'
    #     allfiles = os.listdir(source)
    #     for f in allfiles:
    #         src_path = os.path.join(source, f)
    #         dst_path = os.path.join(destination, f)
    #         shutil.move(src_path, dst_path)

    i = i + 1
    cv2.waitKey(1)

vid.release()
cv2.destroyAllWindows()
