import cv2
import dlib

#read img
img = cv2.imread("Hanlun.jpg")
#img = cv2.resize(src=img,dsize=(640, 360))

#convert img  to gray scale
gray=cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)

#dlib: load Face Reg
face_detector=dlib.get_frontal_face_detector()

# load the predictor:
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#use detector to find face landmarks
faces = face_detector(gray)

for face in faces:
    x1 = face.left() #left point
    y1 = face.top() #top point
    x2 = face.right() #right point
    y2 = face.bottom() #bottom point

    #Draw a rectangle
    cv2.rectangle(img=img,pt1=(x1,y1), pt2=(x2,y2), 
        color=(0,0,255), thickness=3)

    face_features=predictor(image=gray, box=face)
    
    #loop through 68 points
    for n in range(0,68):
        x = face_features.part(n).x
        y = face_features.part(n).y

        #draw a dot
        cv2.circle(img = img, center=(x,y), radius=2,
             color=(0,255,0), thickness=3)
    

#show img
cv2.imshow(winname="Face Recognition App", mat=img)

#wait for a key press to exit
cv2.waitKey(delay=0)

#close all windows
cv2.destroyAllWindows()