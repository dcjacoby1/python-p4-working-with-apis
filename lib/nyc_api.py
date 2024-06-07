
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    #returns response in JSON
    return response.content
  
  #used to build out a formatted response
  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted dictionary
        programs_list = []
        #json.loads parses data into Python dictionary
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])
        #returns a list of the agency fields for all the programs
        return programs_list


#this line creates a GetPrograms instance and stores it in programs
programs = GetPrograms()
#calls the program_agencies function on the programs data and stores it in agencies
agencies = programs.program_agencies()

#prints each agency on a seperate line
#we use set to remove duplicates
for agency in set(agencies):
    print(agency)
  