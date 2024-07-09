

import cv2

# مسیر فایل ویدیویی
video_path = r'C:\Users\milad\Desktop\car_park.mp4'

# باز کردن ویدیو
cap = cv2.VideoCapture(video_path)

# بررسی باز شدن موفقیت‌آمیز ویدیو
if not cap.isOpened():
    print("خطا در باز کردن ویدیو")
    exit()

# شماره فریمی که می‌خواهید استخراج کنید (مثلاً فریم 20ام)
frame_number = 20

# تنظیم موقعیت ویدیو به فریم مورد نظر
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# خواندن فریم
ret, frame = cap.read()
if ret:
    # تبدیل فریم به خاکستری
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # استفاده از آستانه‌گذاری تطبیقی برای ایجاد تصویر باینری
    img_threshold = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY_INV, 25, 16)

    # انجام عملیات مورفولوژیکی برای حذف نویز و بهبود تصویر
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    img_morph = cv2.morphologyEx(img_threshold, cv2.MORPH_CLOSE, kernel, iterations=2)
    img_morph = cv2.morphologyEx(img_morph, cv2.MORPH_OPEN, kernel, iterations=2)

    # نمایش تصویر اصلی و تصویر باینری
    cv2.imshow(f"Original Frame {frame_number}", gray_frame)
    cv2.imshow(f"Processed Frame {frame_number}", img_morph)

    # ذخیره تصویر باینری به عنوان یک فایل
    cv2.imwrite(f"frame_{frame_number}_binary.jpg", img_morph)
    print(f"فریم {frame_number} به صورت باینری ذخیره شد.")

    # منتظر ماندن برای فشردن یک کلید
    cv2.waitKey(0)
else:
    print("خطا در خواندن فریم")

# آزادسازی منابع
cap.release()
cv2.destroyAllWindows()



import cv2

# مسیر فایل ویدیویی
video_path = r'C:\Users\milad\Desktop\car_park.mp4'

# باز کردن ویدیو
cap = cv2.VideoCapture(video_path)

# بررسی باز شدن موفقیت‌آمیز ویدیو
if not cap.isOpened():
    print("خطا در باز کردن ویدیو")
    exit()

# شماره فریمی که می‌خواهید استخراج کنید (مثلاً فریم 20ام)
frame_number = 20

# تنظیم موقعیت ویدیو به فریم مورد نظر
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# خواندن فریم
ret, frame = cap.read()
if ret:
    # تبدیل فریم به خاکستری
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # استفاده از تشخیص لبه Canny
    # تنظیم مقادیر آستانه در اینجا ممکن است نیاز به تغییر داشته باشد
    edges = cv2.Canny(gray_frame, 50, 150)

    # نمایش تصویر اصلی و تصویر لبه‌یابی شده
    cv2.imshow(f"Original Frame {frame_number}", gray_frame)
    cv2.imshow(f"Processed Frame {frame_number}", edges)

    # ذخیره تصویر لبه‌یابی شده به عنوان یک فایل
    cv2.imwrite(f"frame_{frame_number}_edges.jpg", edges)
    print(f"فریم {frame_number} با لبه‌یابی ذخیره شد.")

    # منتظر ماندن برای فشردن یک کلید
    cv2.waitKey(0)
else:
    print("خطا در خواندن فریم")

# آزادسازی منابع
cap.release()
cv2.destroyAllWindows()