
#opens an image and allows the user to click on the image to find the coordinates of potential parking spots
import cv2
import pickle
import os

width, height = 60, 20  # مستطیل‌ها را کمی بزرگتر کردیم

# مسیر فایل ویدیویی
video_path = r'C:\Users\milad\Desktop\car_park.mp4'

# باز کردن ویدیو و استخراج فریم
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("خطا در باز کردن ویدیو")
    exit()

frame_number = 20
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
ret, frame = cap.read()
if not ret:
    print("خطا در خواندن فریم")
    exit()

image_path = f"frame_{frame_number}.jpg"
cv2.imwrite(image_path, frame)
print(f"فریم {frame_number} با موفقیت ذخیره شد.")
cap.release()

try:
    with open("car_parkPos", "rb") as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    global posList, width, height
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    with open('car_parkPos', "wb") as f:
        pickle.dump(posList, f)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouseClick)

while True:
    img = cv2.imread(image_path)
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)  # ضخامت خط را به 2 افزایش دادیم
    cv2.imshow('Image', img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):  # پاک کردن همه مستطیل‌ها
        posList.clear()
        with open('car_parkPos', "wb") as f:
            pickle.dump(posList, f)
        print("تمام مستطیل‌ها پاک شدند.")
    elif key == ord('+'):  # افزایش اندازه مستطیل‌ها
        width += 2
        height += 1
    elif key == ord('-'):  # کاهش اندازه مستطیل‌ها
        width = max(10, width - 2)
        height = max(5, height - 1)

cv2.destroyAllWindows()