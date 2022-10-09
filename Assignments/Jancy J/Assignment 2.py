'''ASSIGNMENT 2
    Build a python code,assume you get temperature and humidity values(generated with random function to a variable)
    and write a condition to continuously detect alarm in case of high temperature
'''
def weatherStatus():
    import random as r
    #Get the temperature value
    temperatureValue=r.randint(1,80)
    print("Temperature is",temperatureValue,"degrees Celsius")
    #Get the humidity value based on temperature value and then print Weather Status
    if(temperatureValue>=40):                       
        humidityValue=r.randint(10,20)
        print("Humidity is",humidityValue,"%")
        print("Temperature is very HIGH")
        print("Alarm in ON condition")
    elif((temperatureValue>=15)):                   
        if((temperatureValue>=15)and(temperatureValue<=25)):
             humidityValue=r.randint(20,60)
             print("Humidity is",humidityValue,"%")
             print("Comfortable Weather")
        else:
            humidityValue=r.randint(20,60)
            print("Humidity is",humidityValue,"%")
            print("Weather is Hot")

        print("Alarm in OFF condition")
    else:
         humidityValue=r.randint(60,70)
         print("Humidity is",humidityValue,"%")
         print("Temperature is very low")
         print("Cold Weather")
         print("There's a strong possibility of rain")

         print("Alarm in OFF condition")
    
#while(1): #Use this condition when you need to run this code infinite times 
weatherStatus()
print("***********************************************************")


