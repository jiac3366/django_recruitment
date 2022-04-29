import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR' + BASE_DIR)
print(__name__)
logger = logging.getLogger(__name__)
print(os.path.join(os.path.dirname(BASE_DIR), 'meetingroom.performance.log'))

li = ['1', '2', '3']
li.remove('1')
print(li)
