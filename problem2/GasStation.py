def gasStation(strArr):
    tank = 0
    gsn = int(strArr[0][1])
    lenArr = len(strArr)
    for startPoint in range(1, lenArr):
        enoughFuel = 1
        index = startPoint
        interactions = 0
        print "ponto inicial: " + str(startPoint)
        while enoughFuel==1:
            gasOnStation = strArr[index][1]
            gasToNext = strArr[index][3]
            print(gasToNext)
            tank += int(gasOnStation) - int(gasToNext)
            print "tanque: " +str(tank)
            print "indice "+ str(index)
            interactions += 1
            if tank < 0:
                enoughFuel = 0
                tank = 0
            else:
                index +=1
                if interactions == (lenArr - startPoint):
                    if index > lenArr-1:
                        index = 1
            
                if interactions==(lenArr-1):
                    return startPoint
                
    return "impossivel"


















            
