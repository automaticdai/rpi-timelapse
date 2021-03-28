#!/usr/bin/python

from picamera import PiCamera
from datetime import datetime
from time import sleep


camera = PiCamera()

# set the desired resoultion
camera.resolution = (1280, 720)

# delay before start (in seconds)
delay_s = 3; 

# interval between images (in seconds)
interval_s = 5;

# overall number of photos to take
shooting_cnt = 8 * 60 * int(60 / interval_s);

while(delay_cnt):
    print('Delay cnd: %d' % delay_cnt);
    delay_cnt = delay_cnt - 1;
    sleep(1)


while(shooting_cnt):
    filename_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    camera.capture('/home/pi/timelapse/' + filename_str + '.jpg')
    shooting_cnt = shooting_cnt - 1;
    print('Cnt: %d' % shooting_cnt);
    sleep(interval_s)
