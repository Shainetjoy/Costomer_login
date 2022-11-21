import face_recognition
from deepface import DeepFace
models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]
#face verification
verification = DeepFace.verify("img1.jpg", "img2.jpg", model_name = models[1])
#face recognition
recognition = DeepFace.find(img_path = "img.jpg", db_path = “C:/facial_db", model_name = models[1])
