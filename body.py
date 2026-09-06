import cv2
xml="haarcascade_fullbody.xml"
cas=cv2.CascadeClassifier(xml)
# img=cv2.imread("body/b3.jpg",0)
# b=cas.detectMultiScale(img,1.1,3)
# print(b)

# for (x,y,w,h) in b:
#     r=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
# cv2.imshow("i",img)
# cv2.waitKey(0)
# vid=cv2.VideoCapture("walking.mp4")
vid=cv2.VideoCapture("videos/walking2.mp4")
cv2.namedWindow("i", cv2.WINDOW_NORMAL)
cv2.resizeWindow("i", 960, 540)
while vid.isOpened():
    ret,frame=vid.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    b=cas.detectMultiScale(img,1.1,2)
    for (x,y,w,h) in b:
        r=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
    cv2.imshow("i",img)
    key=cv2.waitKey(20)
    if key==27:
        break