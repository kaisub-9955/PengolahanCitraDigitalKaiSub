import cv2

#Dibuat oleh Khoironi & Iqbal & Chicken
# Untuk load Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# menginput gambar
img = cv2.imread('test.jpg')

# Konvert ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Deteksi Wajah
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Menggambar persegi disekitar wajah
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display output
cv2.imshow('img', img)
cv2.waitKey()
