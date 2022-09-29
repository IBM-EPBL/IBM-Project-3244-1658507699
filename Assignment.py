import random
while(True):
    TEMPERATURE=random.randrange(0,100)
    if(TEMPERATURE>= 70):
        
        HUMIDITY=random.randrange(0,20)
    else:
        HUMIDITY=random.randrange(21,50)
    print("THE TEMPERATURE OF THE ROOM:",TEMPERATURE)

    print("THE HUMIDITY OF THE ROOM:",HUMIDITY)

    if(TEMPERATURE>70 and HUMIDITY<50):
        print("THE ALARM MUST BE DETECTED")
        break
