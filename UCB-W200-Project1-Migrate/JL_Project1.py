import operator
import sys
import time

# Relocation Happiness Score Program Project by C.S. John Lee

# Start by defining the data classes
class Person:
    """Class person will store the characteristics of the user.
       It will store weights of different attributes in the location
       class which will be used to calculate the happiness score.       
       """

    def __init__(self, name, sunw = 'fluctuating', climatew = 'cold', 
                 popw = 'high'):
        self.name = name
        self.sunw = sunw
        self.climatew = climatew
        self.salaryw = 'high'
        self.popw = popw
        self.homew = 'low'        
        self.crimew = 'low'
    
    def __str__(self):
        msg1 = "Name: " + str(self.name)
        msg2 = "Daylight Throughout the Year Preference: " + str(self.sunw)
        msg3 = "Temperature Preference: " + str(self.climatew)
        msg4 = "Population Preference: " + str(self.popw) + " density"
        statement = msg1+'\n'+msg2+'\n'+msg3+'\n'+msg4
        return statement


class Location:
    """Class location will store the characterstics of each location.
       These characteristics will be used in the Happiness class and can 
       be returned to the user.
       """

    def __init__(self, city, sun, climate, salary, pop, home, crime):
        self.city = city
        self.sun = sun              # low number is steady sunlight hours
        self.climate = climate      # Ratio of heating-to-cooling throughout year
        self.salary = salary        # median salary in $/hr
        self.pop = pop              # population per square mile
        self.home = home            # median home price
        self.crime = crime          # Property crime rate per 100,000 people

    def __str__(self):
        return str(self.city)

    def __repr__(self):
        return repr(self.city)
    
    def get_details(self):        
        msg1 = "City name: " + str(self.city)
        msg2 = "Annual max and min daylight fluctuations: " + str(self.sun) + " minutes"
        msg3 = "Heat-to-Cool Degree-Day Ratio: " + str(self.climate)
        msg4 = "Median Salary: " + "$" + str(self.salary) + "/hr"
        msg5 = "Population density: " + str(self.pop) + " per sq. mile"
        msg6 = "Median Home Value: $" + str(self.home)
        msg7 = "Property Crime: " + str(self.crime) + " per 100,000 people per year"
        statement = msg1+'\n'+msg2+'\n'+msg3+'\n'+msg4+'\n'+msg5+'\n'+msg6+'\n'+msg7
        return statement    
    
    
"""Declaring a few standard locations for this program
   (City, Sunlight, Climate, Salary, Pop. Density, Home Value, Crime)
   1. Sunlight = longest daylight of the year minus shortest daylight of the year
      Source: https://www.timeanddate.com/sun/usa/albuquerque
   2. Climate = Heating-Degree-Day : Cooling-Degree-Day
      Source: 2017 ASHRAE Fundamentals Chapter 14
   3. Salary = median salary
      Source: https://www.payscale.com/research/US/Location=Albuquerque-NM/Salary
   4. Pop. Density = population per square mile
      Source: https://en.wikipedia.org/wiki/Albuquerque,_New_Mexico
   5. Home Value = median home value
      Source: https://www.kiplinger.com/tool/real-estate/T010-S003-home-prices-in-100-top-u-s-metro-areas/index.php
   6. Crime = total property crime per 100,000 people
      Source: https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate
   """
location1 = Location('AlbuquerqueNM',283 ,2.75 ,16.79 ,2900 ,167000 ,7366)
location2 = Location('NewyorkNY',348 ,4.71 ,20.28 ,27751 ,410000, 1449)
location3 = Location('PhoenixAZ',264 ,0.20 ,17.89 ,3207 ,252000 ,3671)
location4 = Location('AtlantaGA',269 ,1.90 ,17.93 ,3547 ,210000 ,4776)
location5 = Location('AustinTX',234 ,0.54 ,18.33 ,3182 ,290000 ,3190)
location6 = Location('BatonrougeLA',236 ,0.58 ,16.85 ,2650 ,168000 ,5594)
location7 = Location('BakersfieldCA',236 ,0.884 ,17.31 ,2562 ,215000 ,4068)
location8 = Location('SanfranciscoCA',314 ,17.06 ,25.57 ,18838 ,860000 ,6168)
location9 = Location('SeattleWA',454 ,24.00 ,22.2 ,7251 ,430000 ,5259)
location10 = Location('HonoluluHI',156 ,0.00 ,19.17 ,5791 ,600000 ,2774)
location11 = Location('MiamiFL',193 ,0.04 ,17.09 ,11136 ,255000 ,4014)
location12 = Location('SandiegoCA',258 ,1.64 ,20.05 ,4326 ,545000 ,1843)
location13 = Location('TulsaOK',295 ,1.64 ,16.54 ,2074 ,146000 ,5456)
location14 = Location('DetroitMI',372 ,6.77 ,18.29 ,4852 ,157000 ,4541)
location15 = Location('BostonMA',372 ,7.1 ,22.38 ,14344 ,410000 ,2089)
location16 = Location('AverageCity',286 ,4.65 ,19.1 ,7627 ,341000 ,4151)

listoflocations=[location1,location2,location3,location4,location5,
                 location6,location7,location8,location9,location10,
                 location11,location12,location13,location14,location15,
                 location16]
dictoflocations={'AlbuquerqueNM':location1, 'NewyorkNY':location2, 
                'PhoenixAZ':location3, 'AtlantaGA':location4, 
                'AustinTX':location5, 'BatonRougeLA':location6,
                'BakersfieldCA':location7, 'SanfranciscoCA':location8,
                'SeattleWA':location9, 'HonoluluHI':location10,
                'MiamiFL':location11, 'SandiegoCA':location12,
                'TulsaOK':location13, 'DetroitMI':location14,
                'BostonMA':location15, 'AverageCity':location16}

def location_verification(loc):
    "Verifies if location is in default list"
    lis=list(dictoflocations.values())
    p=[str(i).lower() for i in lis]
    if loc.lower() not in p:
        raise InvalidLocationError
      

class Happiness:
    """Class happiness will calculate the happiness index of each location
       based on user's input/preferences and location characteristics.
       """
       
    def __init__(self):
        self.index=0
        self.indexlist=[0,0,0,0,0,0]
        self.locations=[]
        self.locationsum=[0,0,0,0,0,0]
        self.locationavg=[0,0,0,0,0,0]
        self.locationmax=[0,0,0,0,0,0]
        self.locationmin=[1000,10,50,100000,1000000,10000]
        self.locationscount=0

    def addtolist(self,location):
        """Adds location into a list of locations for use in other methods"""
        name=location.city
        sun=location.sun
        climate=location.climate
        salary=location.salary
        pop=location.pop
        home=location.home
        crime=location.crime
        self.locations.append([name,sun,climate,salary,pop,home,crime])
        self.locationscount += 1
       
    def statslocation(self):
        """Calculates basic statistics of all location characteristics."""
        for location in self.locations:
            for i in range(0,6):
                self.locationsum[i] += location[i+1]   #calculating sums                
                if self.locationmax[i] < location[i+1]:
                    self.locationmax[i]=location[i+1]  #finding maximum                
                if self.locationmin[i] > location[i+1]:
                    self.locationmin[i]=location[i+1]  #finding minimum                
        for i in range(0,6):
            self.locationavg[i] = self.locationsum[i]/self.locationscount #finding average

    def hindex(self,loc,per):
        """Calculates happiness index based on location and user characteristics.
           
           Equation is essentially sum((1/6)*each attribute)*100.
           
           Each attribute is the specified location's value relative to all 
           of the other location's value.
           Each attribute = [location's attribute value - min of attribute values] 
                            / [max of attribute values - min of attribute values]
           
           User characteristic flips each attribute depending on input. If high
           population density is preferred, we would prioritize the cities with 
           higher population density meaning cities with population density
           closest to the max population density value.
           If low population density is preferred, we would prioritize the cities 
           with lower population density meaning cities with population density
           closest to the min population density value, therefore, we would do 
           absolute value of (1 minus equation).  
           """
        if per.sunw == 'steady':
            self.indexlist[0] = (abs(1-((loc.sun-self.locationmin[0])/
                                    (self.locationmax[0]-self.locationmin[0]))))
        if per.sunw == 'fluctuating':
            self.indexlist[0] = ((loc.sun-self.locationmin[0])/
                                 (self.locationmax[0]-self.locationmin[0]))
        if per.climatew == 'hot':        
            self.indexlist[1] = (abs(1-((loc.climate-self.locationmin[1])/
                                 (self.locationmax[1]-self.locationmin[1]))))
        if per.climatew == 'cold':        
            self.indexlist[1] = ((loc.climate-self.locationmin[1])/
                                 (self.locationmax[1]-self.locationmin[1]))
        if per.popw == 'high':
            self.indexlist[3] = ((loc.pop-self.locationmin[3])/
                                 (self.locationmax[3]-self.locationmin[3]))
        if per.popw == 'low':
            self.indexlist[3] = (abs(1-((loc.pop-self.locationmin[3])/
                                     (self.locationmax[3]-self.locationmin[3]))))
        self.indexlist[2] = ((loc.salary-self.locationmin[2])/
                             (self.locationmax[2]-self.locationmin[2]))
        self.indexlist[4] = (abs(1-((loc.home-self.locationmin[4])/
                             (self.locationmax[4]-self.locationmin[4]))))
        self.indexlist[5] = (abs(1-((loc.crime-self.locationmin[5])/
                             (self.locationmax[5]-self.locationmin[5]))))       
        self.index=0
        for j in range(0,6):
            self.index += 1/len(self.indexlist)*self.indexlist[j]*100
        return self.index

"""Declare a happiness class to incorporate all locations into Happiness Class.
   Do not use more than once to avoid duplicating cities"""
root=Happiness()
for l in listoflocations:
    root.addtolist(l) 
root.statslocation()  


class Action(Happiness):
    """Class Action will do all the actions. Methods include move, traveled,
       and Fhome.
       
       1. Move calculates a location's happiness index based on user input.
       2. Traveled stores list of all placed the user selected to move.
       3. Fhome shows all locations ranked from highest to lowest Happiness
          Index. 
       """
    
    def __init__(self):
        self.whereyoubeen=[]
        self.allplaces={}

    def move(self, mloc, c,p):
        self.whereyoubeen.append([mloc,c.hindex(mloc,p)])
        return mloc, 'Happiness Index: {:.1f}'.format(c.hindex(mloc,p))

    def moveavg(self, mloc, c,p):
        return mloc, 'Happiness Index: {:.1f}'.format(c.hindex(mloc,p))
   
    def traveled(self):
        print("Places where you've moved:")
        for l in self.whereyoubeen:
            print(l[0])
        
    def Fhome(self, listoflocations, c,p):
        i=0
        for l in listoflocations:
            self.allplaces[l]=c.hindex(l,p)
            i+=1
        return self.allplaces


"Error catching classes, handles errors during user inputs"
class InvalidLocationError(Exception):
    pass;
    
class InvalidResponseError(Exception):
    pass;

class InvalidCommandError(Exception):
    pass;


class CommToTheEndUser:
    """Class to communicate with end user. Minimizes complexity of prompt. 
       Includes error catching to raise exception classes.
       """
    
    q="\nWhat is your name?"
    q1="""\nDo you prefer 'steady' or 'fluctuating' daylight \
throughout a year?"""
    q2="\nDo you prefer 'cold' or 'hot' weather?"
    q3="\nDo you prefer 'high' or 'low' population density?"
    q4="\nWhat would you like to do?"

    def commIntro1(self):
        print("\nWelcome to the Location Happiness Score Program")
        print("Happiness Score ranges from 100 (best) to 0 (worse)")
    
    def commUserIntro2(self):
        print("\nLet's start by inputting your preferences...")
        #time.sleep(1)

    def commUserIntro3(self):
        print("\nUser characteristics saved!\n")
    
    def commUserAct1(self):
        print("""\nEnter a command: [m]ove, [f]orever home, [h]elp, [q]uit""")
 
    def commUserAct2(self):
        print("""\nEnter a command: [S]elect location or [R]eturn \
list of places moved.""")    
    
    def commUserAct2_1(self,y):
        sorted_y=sorted(y.items(), key=operator.itemgetter(0))
        print("\nList of locations:")
        for z in sorted_y:
            print(z[0])        

    def commUserAct2_2(self):
        print("Please type in the location you wish to move to: ")

    def commUserAct2_3(self):
        print("Calculating Happiness Index...""")
        time.sleep(1)
        print("Calculating...")
        time.sleep(1)
        print("")        
    
    def commUserAct3(self,x):
        sorted_x=sorted(x.items(), key=operator.itemgetter(1),reverse=True)       
        print("\nCities ranked from highest to lowest happiness index: \n")
        print("Calculating Happiness Index...""")
        time.sleep(1)
        count=0
        for z in sorted_x:
            if z[0] != 'Average':
                count+=1
                print('{}. {} has happiness index of {:.1f}'.format(count,z[0],z[1]))
                time.sleep(0.1)  
    
    def commUserAct4(self):
        print("""[m]ove - choose a location to move to or show list of \
locations user have moved.""")
        print("""[f]orever home - returns a list of locations to move \
ranked by highest to lowest happiness score.""")        
        print("[q]uit - quits program.")
    
    def sunweight(self,ans):
        if ans != 'steady' and ans != 'fluctuating':
            raise InvalidResponseError 

    def climateweight(self,ans):
        if ans != 'cold' and ans != 'hot':
            raise InvalidResponseError 
    
    def popweight(self,ans):
        if ans != 'high' and ans != 'low':
            raise InvalidResponseError 

    def cmd1(self,ans):
        if ans not in ['m','move','f','forever home','h','help','q','quit']:
            raise InvalidCommandError       
    
    def cmd2(self,ans):
        if ans not in ['s','select','r','return']:
            raise InvalidCommandError


############# Main Prompt To User starts here #################################
def Main():
    #-----------declaring variables for later use---------------#
    s=CommToTheEndUser()
    m=Action()
    sunw = None
    climatew = None
    popw = None 
    
    #-----------introduction to get user attributes-------------#
    s.commIntro1()
    print(s.q)
    name = input()
    print("\nHi {}!".format(name))
    s.commUserIntro2()
   
    while sunw != 'steady' and sunw != 'fluctuating':
        print(s.q1)
        sunw = input().lower()
        try:
            s.sunweight(sunw)
        except InvalidResponseError as err:
            print("\nInvalid Response! Enter 'steady' or 'fluctuating'")

    while climatew != 'cold' and climatew != 'hot':     
        print(s.q2)
        climatew = input().lower()
        try:
            s.climateweight(climatew)
        except InvalidResponseError as err:
            print("\nInvalid Response! Enter 'cold' or 'hot'")
   
    while popw != 'high' and popw != 'low':
        print(s.q3)
        popw = input().lower()
        try:
            s.popweight(popw)
        except InvalidResponseError as err:
            print("\nInvalid Response! Enter 'high' or 'low'")
        
    user = Person(name, sunw, climatew, popw)
    s.commUserIntro3()
    print(user)
    time.sleep(1.5)
    print(s.q4)    
    
    #-----------actions in the program--------------------------#
    while True:
        s.commUserAct1()
        cmd1 = input().lower()
        try:
            s.cmd1(cmd1)   
            if cmd1 == 'm' or cmd1 == 'move':
                s.commUserAct2()
                cmd2 = input().lower()
                try:
                    s.cmd2(cmd2)
                    if cmd2 == 's' or cmd2 == "select" or cmd2 == "select location":
                        s.commUserAct2_1(dictoflocations)                
                        s.commUserAct2_2()  
                        mloc=input()                
                        try:
                            location_verification(mloc)
                            s.commUserAct2_3()
                            mloc1=mloc[0].upper()+mloc[1:]
                            mloc2=mloc1[:-2]+mloc[-2:].upper()
                            a=dictoflocations[mloc2].get_details()
                            b=m.move(dictoflocations[mloc2], root, user)
                            c=m.moveavg(dictoflocations['AverageCity'], root, user)
                            print(a,"\n")
                            print("{}'s {}".format(b[0],b[1]))
                            print("{}'s {}".format(c[0],c[1]))
                        except InvalidLocationError as err:
                            print("Invalid Location inputted!")         
                    elif cmd2 == 'r' or cmd2 == "return":
                        print("")
                        m.traveled()
                except InvalidCommandError as err:
                    print("Invalid Command Inputted!")
            elif cmd1 == 'f' or cmd1 == 'forever home':
                x=m.Fhome(listoflocations, root, user)
                s.commUserAct3(x)
            elif cmd1 == 'h' or cmd1 == 'help':
                s.commUserAct4()        
            elif cmd1 == 'q' or cmd1 == 'quit':
                sys.exit()
        except InvalidCommandError as err:
            print("Invalid Command Inputted!")             

############# Initializes Program #############################################
Main()
