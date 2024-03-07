# Video_Recoder_for_Color-Blindness
A simple video recorder that records images of a computer's webcam for color-blindness using OpenCV

Mode
-
* Recording Mode
By pressing the spacebar, you can enter and exit the recording mode. In this case, a red mark appears on the preview screen to confirm that it is recorded.
In addition, the recorded video is saved as an output.avi file in the same directory as the executable. If you already have another output.avi file, the newly recorded video will be overwritten.
<br>
* Color-Blindness Mode
By pressing the tap key, you can enter and exit color-blindness mode. Just like in recording mode, a blue indication will appear to confirm that you are in colorblind mode.
The image can be recorded while in color blind mode.


For the colorblind mode's algorithm, the following research paper was referenced.

    Hyun-Ji Kim, Jae-Young Cho, and Sung-Jea Ko.
    "Re-coloring Methods using the HSV Color Space for people with the Red-green Color Vision Deficiency,"
    Journal of The Institute of Electronics Engineers of Korea, Vol. 50(3), pp. 616-619, 2013.
    https://koreascience.kr/article/JAKO201310837317613.page