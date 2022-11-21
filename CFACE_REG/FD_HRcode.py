# import the opencv library
import cv2

face_cascade = cv2.CascadeClassifier('../DATA / haarcascades / haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../DATA / haarcascades / haarcascade_eye.xml')


def adjusted_detect_face(img):
    face_img = img.copy()
    face_rect = face_cascade.detectMultiScale(face_img,
                                              scaleFactor=1.2,
                                              minNeighbors=3)
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return face_img


# create a function to detect eyes
def detect_eyes(img):
    eye_img = img.copy()
    eye_rect = eye_cascade.detectMultiScale(eye_img,
                                            scaleFactor=1.2,
                                            minNeighbors=5)
    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return eye_img





vid = cv2.VideoCapture(0)
while (True):
    ret, frame = vid.read()
    # cv2.imshow('frame', frame)

    eyes_face = adjusted_detect_face(frame)
    eyes_face = detect_eyes(eyes_face)
    cv2.imshow(eyes_face)
    # cv2.imwrite('face+eyes.jpg', eyes_face)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()