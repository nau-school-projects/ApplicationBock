from urllib.error import URLError
from urllib.error import HTTPError
from urllib.request import urlopen #used to test if a website exsists

BLOCKED = False      # sets to websites to not blocked when added to the list
EXECUTABLE = "exe"   # used to check if the file is an executible


class Scanner:       # creates Scanner class 

    # takes in a websites hostname and creates a full
    # URL and then adds the website to the blocked list
    # if the website exsists
    def addWebsite( hostName, websiteDict ):
        
    url = "https://" + hostName           # creates the url from the hostname 
    
    try:
        connection = urlopen( url )       # opens a connection with the websites and grabs the response
        
    except HTTPError:                     # checks for a HTTP error 
        print("Not Valid WEBSITE")
        
    except URLError:                      # checks for a URL error
        print("Not Valid WEBSITE")
        
    except ValueError:                    # checks for a value error
        print("Not Valid WEBSITE")
        
    else:                                 # if there are no errors 
        websiteDict[hostName] = BLOCKED   # adds the blocked dictionary


    # takes an application file path and then adds it
    # to the application dictionary if the its and
    # executible 
    def addApplication( filePath, applicationDict ):
        if filePath[-3:] == EXECUTABLE:                            # if the file name is an executible
            applicationDict[filePath] = BLOCKED    # add the file name to the blocked list
        else:
             print("File not an executable")                        # otherwise its not an executible


