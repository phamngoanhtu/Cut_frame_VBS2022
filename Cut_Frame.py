# #Get info of start frame and end frame of each shot
# #For every 15 frame, extract 1 pictures and save in folder <Frame/shot> -> Shot1_1
import pandas as pd
import cv2
import os
for file in os.listdir("V3C1_Sample/videos"):

    path_to_index = "V3C1_Cut_Frame/" + file
    if os.path.isdir(path_to_index) == False:
        os.mkdir(path_to_index)

    df = pd.read_csv("V3C1_Sample/msb/" + file +".tsv", sep='\t')
    cap = cv2.VideoCapture('V3C1_Sample/videos/' + file + "/" + file + ".mp4")
    print(df)
    count = 0
    while count < df.shape[0]:
        start_frame =   df["startframe"][count]
        end_frame   =   df["endframe"][count]

        print("Start Frame of Shot", count, ":" , start_frame)
        print("End Frame of Shot", count, ":", end_frame)

        path = "V3C1_Cut_Frame/" + file + "/Shot" + str(count)
        if os.path.isdir(path) == False:
            os.mkdir(path)

        for i in range(start_frame, end_frame + 1):
            ret, frame = cap.read()
            current_frame = i - start_frame

            if i == end_frame:
                cv2.imwrite("V3C1_Cut_Frame/" + file + "/Shot" + str(count) + "/" + str(i) + '.jpg', frame)
                break

            if  current_frame % 15 != 0:
                continue

            elif ret == False:
                break

            cv2.imwrite("V3C1_Cut_Frame/" + file + "/Shot" + str(count) + "/" + str(i) + '.jpg', frame)
            i += 1
        count += 1
    cap.release()
    cv2.destroyAllWindows()



