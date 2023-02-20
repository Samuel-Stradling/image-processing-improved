import cv2
import pygame
from numpy import average


def frame_color(frame):

    # using numpy to get average color from the frame
    # note cv2 uses BGR color (inverse rgb) hence [::-1]

    avg_color_per_row = average(frame, axis=0)
    avg_color = average(avg_color_per_row, axis=0)[::-1]
    print(avg_color)

    screen.fill(avg_color)
    pygame.display.flip()


def play_video():

    videoPath = "test.mp4"
    # 0 for video, or "videopath/video.mp4"

    cap = cv2.VideoCapture(videoPath)
    while cap.isOpened():
        ret, frame = cap.read()

        # if cap.read() is returning:
        if ret:
            # display that frame
            cv2.imshow("Video", frame)
            # the parameter of waitkey affects speed of playing
            if cv2.waitKey(25) & 0xFF == ord("q"):
                exit()

            frame_color(frame)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Average Color")
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    play_video()
