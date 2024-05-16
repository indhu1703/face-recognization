from random import randint
import cv2
      
CASCADE="Face_cascade.xml"
FACE_CASCADE=cv2.CascadeClassifier(CASCADE)

def detect_faces(image_path,display=True):
    image=cv2.imread(image_path)
    image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)
    for x,y,w,h in faces:
        sub_img=image[y-10:y+h+10,x-10:x+w+10]
        cv2.imwrite(str(randint(0,10000))+".jpg",sub_img)
        cv2.imwrite("H:\MINI-PROJECT\OUTPUT\Faces\output.jpeg",sub_img)
        cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)
        cv2.imshow("Faces Found",image)
        print("Face has been saved to the directory")
    if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
        cv2.destroyAllWindows()
if __name__ == "__main__":
        path="Dem.jpg"
        detect_faces(path)
