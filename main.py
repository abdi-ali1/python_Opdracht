
# Online Python - IDE, Editor, Compiler, Interpreter

measuredTempaturesJune = [17.2, 18.9, 19.1, 19, 25.3, 26.8, 24.9, 25.9, 16.1, 19, 19.3, 18.9, 19.1, 19, 25.3, 26.8, 24.9, 24.9, 18.5, 19, 17.2, 18.9, 19.1, 26, 26, 29.1, 31.2, 31.5, 27.5, 27.1]
measuredTempaturesJuly = [28, 28.5, 29, 29.1, 23.1, 24.3, 19.1, 18.6, 20.3, 19.9, 19.9, 24, 26, 26, 29.8, 22.2, 21.4, 22, 23.1, 21, 27.2, 28.9, 29.2, 26.6, 27.9, 27.1, 32.1, 30.1, 29.9, 25 ]


easyway = True 

def highesTemperature(temperatures, easyCode):
    highestnumber = 0    
    if easyCode:
        return max(temperatures); 
    else:
        for temp in temperatures:
            
            if highestnumber < temp :
                highestnumber = temp
        
    return highestnumber

def lowestTemperature(temperatures, easyway):
    lowestNumber = 50
    if easyway:
        return min(temperatures);
    else:   
        for temp in temperatures:
            if lowestNumber > temp:
                lowestNumber = temp
    return lowestNumber

def calculateRange(temperatures):
    return abs((highesTemperature(temperatures,easyway)) - (lowestTemperature(temperatures,easyway)))

def calculateAverageTempature(temperatures):
      averagenumber = 0
      for temp in temperatures:
        averagenumber += temp 
      return averagenumber / len(temperatures)
    

def calculateHeateDays(temperatures):
        heatDays = 0
        for temp in temperatures:
            if temp >= 25:
                heatDays+= 1
            else:
                heatDays = 0
        return heatDays            
          
    
def calculateHighestJump(temperatures):
    HighestJump = 0
    day1= 0
    day2= 0
    listdata = []
    for i in range(1, len(temperatures) - 1):
  
        diff = temperatures[i] - temperatures[i + 1]
      
        if HighestJump <= diff:
                HighestJump = diff
                day1 = temperatures.index(temperatures[i - 3])
                day2 = temperatures.index(temperatures[i + 1 - 3])
                
                
                
    listdata.append(round(HighestJump, 1))
    listdata.append(day1)
    listdata.append(day2)
    
    return listdata





# ORIENTING: Assessment assignment part 1
print("ORIENTING: Assessment assignment part 1 ")
print(f'June: highest {highesTemperature(measuredTempaturesJune,easyway)} degrees, lowest {lowestTemperature(measuredTempaturesJune,easyway)} degrees')
print(f'July: highest {highesTemperature(measuredTempaturesJuly,easyway)} degrees, lowest {lowestTemperature(measuredTempaturesJuly,easyway)} degrees \n')

#ORIENTING: Assessment assignment part 2
print("ORIENTING: Assessment assignment part 2 ")
print(f'The monthly temperature range in June was {calculateRange(measuredTempaturesJune)}')
print(f'The average temperature in July was {calculateRange(measuredTempaturesJuly)} \n')



#ORIENTING: Assessment assignment part 3
print("ORIENTING: Assessment assignment part 3 ")
print(f'The average temperature in June was {calculateAverageTempature(measuredTempaturesJune)}')
print(f'The average temperature in July was {calculateAverageTempature(measuredTempaturesJuly)} \n')


#ORIENTING: Assessment assignment part 4
print("ORIENTING: Assessment assignment part 4 ")
print(f'There was a heat wave in June ({calculateHeateDays(measuredTempaturesJune)} days)')
print(f'There was a heat wave in June ({calculateHeateDays(measuredTempaturesJuly)} days) \n')


#ORIENTING: Assessment assignment part 5
print("ORIENTING: Assessment assignment part 4 ")
print(f'The biggest jump in June was {calculateHighestJump(measuredTempaturesJune)[0]} degrees. It occurred from  day {calculateHighestJump(measuredTempaturesJune)[1]}  to day {calculateHighestJump(measuredTempaturesJuly)[2]}')
print(f'The biggest jump in July was {calculateHighestJump(measuredTempaturesJuly)[0]} degrees. It occurred from day {calculateHighestJump(measuredTempaturesJuly)[1]} to day {calculateHighestJump(measuredTempaturesJuly)[2]} ')


