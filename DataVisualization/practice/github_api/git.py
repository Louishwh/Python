import os
from time import sleep

filename = 'nam'
os.popen('mkdir '+filename)
sleep(1)
os.popen('cd '+filename)
os.popen('mkdir '+filename)
# os.popen('git clone https://github.com/josephmisiti/awesome-machine-learning.git')
