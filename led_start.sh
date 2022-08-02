#!/bin/bash
echo "Start"
screen -d -m -S myClock python3 luma.led_matrix/examples/silly_clock_new.py
#^a+d
echo "Done"
