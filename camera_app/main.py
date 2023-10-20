from ultralytics import YOLO
import cv2
from datetime import date, datetime
import os
import asyncio

frames_to_save = []
empty_frame_counter = 0
detection = False
path = os.path.abspath(os.path.dirname(__file__))

#model_path = path + '/weights/best.pt'
model_path = '/home/moreau/.pyenv/runs/detect/train2/weights/best.pt'
save_path = path[0:(len(path)-10)]+'video_archive/'

model = YOLO(model_path)
cap = cv2.VideoCapture(0)

async def save_video(frames_to_save, width, height):
    today = date.today()
    today_save_path = save_path + today.strftime("%d_%m_%Y") + '/'
    
    if not os.path.isdir(today_save_path):
        os.mkdir(today_save_path)

    current_date = datetime.now()
    video_name = os.path.join(today_save_path,current_date.strftime("%d_%m_%Y_%H_%M_%S") + '.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #out = cv2.VideoWriter(video_name, fourcc, 10.0, (640, 480))
    out = cv2.VideoWriter(video_name, fourcc, 10.0, (width, height))

    for frames in frames_to_save:
        out.write(frames)

    await asyncio.sleep(10)

    #TODO 
    #save to django model

async def main():

    frames_to_save = []
    empty_frame_counter = 0
    detection = False

    while cap.isOpened():

        success, frame = cap.read()
        height, width, channels = frame.shape

        if success:
            results = model(frame,conf=0.5) 
            if results[0]:
                empty_frame_counter = 0
                detection = True
                annotated_frame = results[0].plot()            
            else:
                if detection:
                    empty_frame_counter += 1
                annotated_frame = frame

            cv2.imshow("YOLOv8 Inference", annotated_frame)

            if detection:
                frames_to_save.append(annotated_frame)

            if empty_frame_counter > 20 and detection == True:
                asyncio.create_task(save_video(frames_to_save[:], width, height))
            
                frames_to_save = []
                detection = False
                #break

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

asyncio.run(main())
"""
while cap.isOpened():

    success, frame = cap.read()
    height, width, channels = frame.shape

    if success:
        results = model(frame,conf=0.5) 
        if results[0]:
            empty_frame_counter = 0
            detection = True
            annotated_frame = results[0].plot()            
        else:
            if detection:
                empty_frame_counter += 1
            annotated_frame = frame

        cv2.imshow("YOLOv8 Inference", annotated_frame)

        if detection:
            frames_to_save.append(annotated_frame)

        if empty_frame_counter > 20 and detection == True:
            asyncio.run(save_video(frames_to_save[:]))
            
            frames_to_save = []
            detection = False
            print('THE END')
            break

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:

        break
"""
cap.release()
cv2.destroyAllWindows()