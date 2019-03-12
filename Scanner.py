import urllib
from urllib.error import URLError
from urllib.error import HTTPError
from urllib.request import urlopen          #used to test if a website exists

from os.path import exists                  # used to test if a file exists

def addWebsite( url, websiteList ):

    try:
        connection = urlopen( url )
    except HTTPError:
        print("Not Valid URL1")
    except URLError:
        print("Not Valid URL2")
    except ValueError:
        print("Not Valid URL3")
    else:
        websiteList.append( url )
    

def addApplication( filePath, applicationList ):
    if exists( filePath ):
        applicationList.append( filePath )
    else:
        print("file not found")




