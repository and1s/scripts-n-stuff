import pyautogui as pa
import os

#spotlight
pa.hotkey('command', 'space')
pa.typewrite('zoom')
pa.hotkey('enter', interval=0.5)

#start meeting
pa.hotkey('command','ctrl', 'v', interval=1)

#open invite window
pa.hotkey('command', 'i')

