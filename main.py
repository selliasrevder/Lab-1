RED='\u001b[41m'
WHITE='\u001b[47m'
END='\u001b[0m'
for i in range(7):
    if i==0 or i==6:
        print(f'{RED}{" "*29}{END}')
    else:
        if i==3:
            print(f'{RED}{" "*7}{WHITE}{" "*15}{RED}{" "*7}{END}')
        else:
            print(f'{RED}{" "*13}{WHITE}{" "*3}{RED}{" "*13}{END}')

print('\n')


a=f'{" "*2}{WHITE}{" "*7}{END}{" "*2}'
b=f'{" "}{WHITE}{" "}{END}{" "*7}{WHITE}{" "}{END}{" "}'
c=f'{WHITE}{" "}{END}{" "*9}{WHITE}{" "}{END}'
for i in range(8):
    print(a*8)
    print(b*8)
    print(c*8)
    print(c*8)
    print(b*8)

print('\n')



def draw_line(offset=0,length=3):
    line=" "*length
    print('|',' '*offset, '*'*length)

offset=24    
for i in range(9):
    draw_line(offset,3)
    offset-=3
print('- '*22)
    
print('\n')



f=open('sequence.txt', 'r')
three=0
notthree=0
k=0
for number in f:
    k+=1
    if -3<=float(number)<=3:
        three+=1
    else: notthree+=1
perc3=round(three/k*100)
percn3=round(notthree/k*100)
print(f"{WHITE}{' '*perc3}{END}")
print(f"{RED}{' '*percn3}{END}")



import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_frame(frame_num):
    clear_console()
    if frame_num == 1:
        print(f'{" "}{WHITE}{" "*3}{END}{" "}')
        print(f'{WHITE}{" "*5}{END}')
        print(f'{WHITE}{" "*5}{END}')
        print(f'{" "}{WHITE}{" "*3}{END}{" "}')
    elif frame_num == 2:
        print(f'{" "*2}{WHITE}{" "*1}{END}{" "*2}')
        print(f'{" "}{WHITE}{" "*3}{END}{" "}')
        print(f'{" "}{WHITE}{" "*3}{END}{" "}')
        print(f'{" "*2}{WHITE}{" "*1}{END}{" "*2}')
    elif frame_num == 3:
        print(f'{" "*2}{WHITE}{" "*1}{END}{" "*2}')
        print(f'{" "*2}{WHITE}{" "*1}{END}{" "*2}')
        print(f'{" "*2}{WHITE}{" "*1}{END}{" "*2}')
        print(f'{" "*2}{WHITE}{" "*1}{END}{" "*2}')
    elif frame_num == 4:
        print(f'{" "*2}{RED}{" "*1}{END}{" "*2}')
        print(f'{" "}{RED}{" "*3}{END}{" "}')
        print(f'{" "}{RED}{" "*3}{END}{" "}')
        print(f'{" "*2}{RED}{" "*1}{END}{" "*2}')
    elif frame_num == 5:
        print(f'{" "}{RED}{" "*3}{END}{" "}')
        print(f'{RED}{" "*5}{END}')
        print(f'{RED}{" "*5}{END}')
        print(f'{" "}{RED}{" "*3}{END}{" "}')


for i in range(1, 6):
  draw_frame(i)
  time.sleep(0.5)