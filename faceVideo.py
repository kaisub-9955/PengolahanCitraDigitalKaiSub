import cv2

#Dibuat oleh Khoironi & Iqbal & Chicken
# Untuk Load Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)
# untuk menangkap video
# cap = cv2.VideoCapture('namafile.mp4')untuk mengambil wajah dari video

while True:
    # Membaca frame
    _, img = cap.read()

    # Konvert ke grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # deteksi wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Membuat persegi disekitar wajah
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop ketika ESC ditekan
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Menampilkan Video
cap.release()
