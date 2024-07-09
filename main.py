
#I tried the lines of code, but the Python script didn't open the video. Another challenge was that the waikey attribute of cv2 used to be in the past, but now it's waitkey
import cv2
import os
import pickle

# مسیر صحیح فایل ویدیویی را تنظیم کنید
file_path = r'C:\Users\milad\Desktop\car_park.mp4'

# بررسی وجود فایل
if not os.path.exists(file_path):
    print(f"فایل ویدیو در مسیر مشخص شده یافت نشد: {file_path}")
    exit()

# تلاش برای باز کردن فایل ویدیویی
cap = cv2.VideoCapture(file_path)
if not cap.isOpened():
    print("خطا در باز کردن ویدیو")
    exit()

frame_count = 0

# بارگذاری موقعیت‌های جای پارک از فایل pickle
try:
    with open("car_parkPos", "rb") as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []
    print("فایل موقعیت جای پارک یافت نشد. لیست خالی استفاده خواهد شد.")

width, height = 60, 20
threshold = 400  # آستانه برای شمارش پیکسل‌های سفید

def car_parkcheck(img, thresh_img):
    empty_spots = 0
    for pos in posList:
        x, y = pos
        carpark_img = thresh_img[y:y+height, x:x+width]

        # شمارش پیکسل‌های سفید
        count = cv2.countNonZero(carpark_img)

        if count < threshold:  # مقدار آستانه برای تشخیص جای پارک خالی
            color = (0, 255, 0)  # سبز
            status = "Empty"
        else:
            color = (0, 0, 255)  # قرمز
            status = "Occupied"
        
        # رسم مستطیل‌ها در مکان‌های مشخص شده
        cv2.rectangle(img, (x, y), (x + width, y + height), color, 2)

        # نمایش وضعیت مستطیل به صورت متنی
        cv2.putText(img, f"{status} ({count})", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

        # نمایش وضعیت هر جای پارک به صورت متنی در کنار مستطیل
        cv2.putText(img, f"{status}", (x, y + height + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

        if status == "Empty":
            empty_spots += 1

    return empty_spots

while True:
    ret, frame = cap.read()
    if ret:
        frame_count += 1

        # تبدیل فریم به سیاه و سفید برای پردازش
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # اعمال Gaussian Blur برای کاهش نویز
        blurred_frame = cv2.GaussianBlur(gray_frame, (7, 7), 0)

        # تغییر به آستانه‌گذاری ساده
        _, thresh_frame = cv2.threshold(blurred_frame, 100, 255, cv2.THRESH_BINARY_INV)

        # بررسی جای پارک‌ها در تصویر
        empty_spots = car_parkcheck(frame, thresh_frame)

        # نمایش تعداد جای‌های پارک خالی
        cv2.putText(frame, f'Empty Spots: {empty_spots}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # نمایش فریم پردازش شده
        cv2.imshow("Video", frame)

        # بررسی کلیدهای ورودی
        key = cv2.waitKey(30) & 0xFF
        if key == ord('q'):
            print("کلید 'q' فشرده شد. خروج از برنامه.")
            break
    else:
        print("پایان ویدیو یا خطا در خواندن فریم")
        break

print(f"تعداد فریم‌های خوانده شده: {frame_count}")

cap.release()
cv2.destroyAllWindows() 
