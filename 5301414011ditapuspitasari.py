import numpy as np
import cv2

capture = cv2.VideoCapture(0) 
#inisialisasi webcam. angka "0" berarti webcam internal. 
#capture merupakan inisialisasi dari gambar yang ditangkap oleh webcam.

while (1):
#while merupakan kondisi dimana:
	
	val, frame = capture.read()
#val, frame artinya nilai dari frame diperoleh dari pembacaan capture pada baris 4.
	sepia = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#nilai dari sepia diperoleh dari hasil frame dan diberi efek keabu-abuan atau gray COLOR_BGR2GRAY
	negative = (255 - sepia)
#nilai dari negative diperoleh dari 225 dikurangi gambar keabu-abuan.
	changebright = (1 + sepia)
#nilai dari changebright diperoleh dari 1 ditambah sepia
	cv2.imshow('Original Capture',frame)
#cv2.imshow merupakan syntax untuk menampilkan gambar dengan tittle Original Capture, 
#dan yang ditampilkan adalah hasil dari frame.
	cv2.imshow('Sepia Effect',sepia)
#menampilkan gambar dengan tittle Sepia Effect, dan yang ditampilkan adalah hasil dari sepia.
	cv2.imshow('Negative Effect',negative)
#menampilkan gambar dengan tittle Negative Effect, dan yang ditampilkan adalah hasil dari negative.
	cv2.imshow('Change Bright',changebright)
#menampilkan gambar dengan tittle Change Bright, dan yang ditampilkan adalah hasil dari changebrigt.
	if cv2.waitKey(1) & 0xFF == ord('k'):
		break
#waitkey(1) merupakan fungsi untuk menampilkan video dalam satuan milidetik
#break untuk menjalankan perintah-perintah setelah blok while
		

#destroyAllWindows untuk membuka semua jendela yang kita buat
cv2.destroyAllWindows()
capture.release()
#ketika semua selesai, maka membuka semua program yang telah ditangkap.