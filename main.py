#!/usr/bin/python

from picamera import PiCamera
from datetime import datetime
from time import sleep


camera = PiCamera()
camera.resolution = (1280, 720)

delay_cnt = 3 * 60 * 12; 
shooting_cnt = 8 * 60 * 12;

while(delay_cnt):
    print('Delay cnd: %d' % delay_cnt);
    delay_cnt = delay_cnt - 1;
    sleep(5)


while(shooting_cnt):
    filename_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    camera.capture('/home/pi/timelapse/' + filename_str + '.jpg')
    shooting_cnt = shooting_cnt - 1;
    print('Cnt: %d' % shooting_cnt);
    sleep(5)
