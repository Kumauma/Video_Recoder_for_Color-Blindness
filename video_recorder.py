import cv2 as cv


# 색약 시각화를 위한 함수
def adjust_hsv_for_cvd(image):
    # 이미지를 RGB에서 HSV 색상 공간으로 변환
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # 색상과 명도 조정
    hsv_image[:, :, 0] = (hsv_image[:, :, 0] + 10) % 180  # 색상 조정
    hsv_image[:, :, 2] = cv.min(hsv_image[:, :, 2] * 1.1, 255)  # 명도 조정

    # 조정된 이미지를 다시 RGB 색상 공간으로 변환
    adjusted_rgb_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

    return adjusted_rgb_image


target_format = "avi"
target_fourcc = "DIVX"

# 컴퓨터 웹캡에서 비디오를 읽어옴
video = cv.VideoCapture(0)
assert video.isOpened(), "Cannot read the webcam"

# FPS를 얻고 밀리초 단위의 대기 시간을 계산
fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)

# 녹화 파라미터 설정
target = cv.VideoWriter()
recording = False

# 색약 파라미터 설정
color_blindness = False

while True:
    # 'video'에서 이미지를 읽어옴
    valid, img = video.read()
    if color_blindness:
        img = adjust_hsv_for_cvd(img)
    if not valid:
        break

    # 이미지 보여주기
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
    cv.putText(
        img_show,
        f"Color Blindness: {'On' if color_blindness else 'Off'}",
        (40, 55),
        cv.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 0, 0) if color_blindness else (0, 255, 0),
        2,
    )
    cv.imshow("Video Player", img_show)

    # 키보드 입력 처리
    key = cv.waitKey(wait_msec)
    if key == ord(" "):
        recording = not recording
    elif key == 27:  # ESC
        break
    elif key == ord("\t"):
        color_blindness = not color_blindness

    if recording:
        if not target.isOpened():
            # 타깃 비디오 파일 열기
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

        # 'target'에 이미지를 쓰기
        target.write(img)

target.release()

cv.destroyAllWindows()
