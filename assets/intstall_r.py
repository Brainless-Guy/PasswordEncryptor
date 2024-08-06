import os
import time
def install():
    s = open("assets/temp.txt",'r')
    
    if s.read().strip() == '1':
        os.system("pip install -r requirements")
        with open("assets/temp.txt",'w') as k:
            k.write('')    
    else:
        ''