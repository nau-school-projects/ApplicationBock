from urllib.error import URLError
from urllib.error import HTTPError
from urllib.request import urlopen #used to test if a website exsists

from os.path import exists

BLOCKED = False
EXECUTABLE = "exe"

def addWebsite( url, websiteDict ):

    try:
        connection = urlopen( url )
    except HTTPError:
        print("Not Valid URL1")
    except URLError:
        print("Not Valid URL2")
    except ValueError:
        print("Not Valid URL3")
    else:
        websiteDict[url.split('/')[2]] = BLOCKED
    

def addApplication( filePath, applicationDict ):
    if exists( filePath ):
        if filePath[-3:] == EXECUTABLE:
            applicationDict[filePath] = BLOCKED
        else:
            print("File not an executable")
    else:
        print("file not found")
