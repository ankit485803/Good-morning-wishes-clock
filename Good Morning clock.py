 
/* Method: 1 */

print("24:00 clock")
time=0
time= int(input('Enter time'))
if(time>=1 and time<=12):
    print("Good morning 🌅🌄 sir")
elif(time>12 and time<=17):
    print("Hey,Good Afternoon sir")
else:
    print("Good night  🌉🌃 dear!")


/* Method: 2 by importing time library */

import time

tiemstap=time.strftime('%H:%M:%S')
print(tiemstap)

hours=int(time.strftime('%H'))
print(hours)

mint=int(time.strftime('%M'))
print(mint)

scnd=int(time.strftime('%S'))
print(scnd)


if(hours>=0 and hours<12):
       print("Good morning")

elif(hours>=12 and hours<=17):
       print("Good afternoon")

elif(hours>=18 and hours<=22):
       print("Good evening")
 
else:
       print("good night")
