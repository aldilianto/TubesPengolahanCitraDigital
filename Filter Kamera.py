import cv2
import numpy as np
from pynput import keyboard

# Ialisnisiasi variabel global
current_filter = 0  # Filter warna saat ini 
filters = [None, lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_JET),
           lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_INFERNO),
           lambda frame: cv2.applyColorMap(frame, cv2.COLORMAP_AUTUMN)]

# Fungsi untuk mengubah filter saat tombol panas ditekan
def on_key_release(key):
    global current_filter
    if key == keyboard.Key.esc:  # Tekan Esc untuk keluar dari aplikasi
        cap.release()
        cv2.destroyAllWindows()
        exit()
    elif key == keyboard.Key.space:  # Tekan spasi untuk mengubah filter
        current_filter = (current_filter + 1) % len(filters)

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Membuat listener untuk hotkeys
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

while True:
    ret, frame = cap.read()

    # Terapkan filter saat ini
    if filters[current_filter] is not None:
        filtered_frame = filters[current_filter](frame)
        cv2.imshow("Filtered Camera", filtered_frame)
    else:
        cv2.imshow("Filtered Camera", frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bebaskan sumber daya dan tutup jendela ketika selesai
cap.release()
cv2.destroyAllWindows()
