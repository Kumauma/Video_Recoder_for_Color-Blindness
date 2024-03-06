import cv2 as cv

target_format = "avi"
target_fourcc = "DIVX"

# Read the computer's webcam
video = cv.VideoCapture(0)
assert video.isOpened(), "Cannot read the webcam"

# Get FPS and calculate the waiting time in millisecond
fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)

# Set Recording Parameters
target = cv.VideoWriter()
recording = False

# Set Color-Blindness Parameters
color_blindness = False

while True:
    # Get an image from 'video'
    valid, img = video.read()
    if not valid:
        break

    # Show the image
    img = cv.flip(img, 1)
    img_show = img.copy()
    cv.circle(img_show, (20, 20), 10, (0, 0, 255) if recording else (0, 255, 0), -1)
    cv.putText(
        img_show,
        f"Recording: {'On' if recording else 'Off'}",
        (40, 27),
        cv.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 255) if recording else (0, 255, 0),
        2,
    )
    cv.imshow("Video Player", img_show)

    # Process the key event
    key = cv.waitKey(wait_msec)
    if key == ord(" "):
        recording = not recording
    if key == 27:  # ESC
        break

    if recording:
        if not target.isOpened():
            # Open the target video file
            target_file = "output." + target_format
            h, w, *_ = img.shape
            is_color = (img.ndim > 2) and (img.shape[2] > 1)
            target.open(
                target_file,
                cv.VideoWriter_fourcc(*target_fourcc),
                fps / 1.5,
                (w, h),
                is_color,
            )

        # Add the image to 'target'
        target.write(img)

target.release()

cv.destroyAllWindows()
