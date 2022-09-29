import random
while(True):
    TEMPERATURE=random.randrange(0,90)
    if(TEMPERATURE>= 60):
        
        HUMIDITY=random.randrange(0,20)
    else:
        HUMIDITY=random.randrange(20,60)
    print("THE TEMPERATURE OF THE ROOM:",TEMPERATURE)

    print("THE HUMIDITY OF THE ROOM:",HUMIDITY)

    if(TEMPERATURE>60 and HUMIDITY<50):
        print("THE ALARM MUST BE DETECTED")
        break
