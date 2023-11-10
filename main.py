from forestSample import ForestSample
import os
import time
import streamlit as st

f = ForestSample(size=25, initial_fire_pos={(0,0), (10,9)}, initial_monkey_pos=(24,24))

while f.isMonkeyAlive():
    os.system('clear')
    step = f.bfs()
    str_ = f.renderFrame(step)
    print(str_)
    time.sleep(1)
