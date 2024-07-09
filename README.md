This Python program is designed to detect the status of parking spots (empty or occupied) in a video using image processing techniques with OpenCV.

Video File Usage: The program uses a video file named "car_park.mp4" located at "C:\Users\milad\Desktop". It analyzes this video to determine the status of parking spots in each frame.

Loading Parking Spot Positions: The coordinates of parking spots are loaded from a pickle file named "car_parkPos". If the file is not found, an empty list is used.

Image Processing: For each frame of the video, it converts the image to grayscale and applies Gaussian Blur and Thresholding to process the image and detect parking spots.

Displaying Results: For each parking spot, a colored rectangle (green for empty and red for occupied) is drawn, and its status is displayed as text. The number of empty parking spots in each frame is also displayed.

This position_picker program allows you to select parking spot positions interactively using mouse clicks and store them in a pickle file named "car_parkPos".

Using the Frame Image: The program uses a frame from the video that was previously saved (named "frame_{frame_number}.jpg").

Parking Spot Positions: By clicking on the image, you select positions of rectangles representing parking spots. Right-clicking on a rectangle deletes it.

Changing Rectangle Sizes: You can increase or decrease the size of selected rectangles using the "+" and "-" keys.

Clearing All Rectangles: Pressing the "c" key clears all selected rectangles and empties the pickle file.

Adaptive Thresholding: This method is used for thresholding images where the threshold value is calculated based on local image properties.

Morphology: These operations include closing and opening operations, which are used to remove noise and enhance the shape of objects in the image.
Canny Edge Detection: This method is used to detect edges in the image based on intensity gradients.
