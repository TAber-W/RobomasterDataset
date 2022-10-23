'''
Opencv-python needed
Author:Taber-W
Date:2022-10-23

Save frame from video
'''


import argparse
import cv2


def run(video_pth='',frame_pth='',frame_len=1):
    cap = cv2.VideoCapture(video_pth[0])
    flag = 0
    num =0
    while(1):
        ret,frame = cap.read()
        flag = flag+1
        if flag == frame_len:
            #print("正在保存第"+str(num)+"张图片")
            cv2.imwrite(frame_pth[0]+"/"+str(num)+".jpg", frame)
            num = num+1
            flag = 0
    print("共输出"+str(num)+"张图片")



def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_pth', nargs='+', type=str, default='', help='Video path')
    parser.add_argument('--frame_pth', nargs='+', type=str, default='', help='Frame path for save')
    parser.add_argument('--frame_len', nargs='+', type=int, default=1, help='Stride for frame')

    opt = parser.parse_args()
    return opt

def main(opt):
    run(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)