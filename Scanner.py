import urllib
from urllib.error import URLError
from urllib.error import HTTPError
from urllib.request import urlopen#used to test if a website exsists

def addWebsite( url, websiteList ):

    try:
        connection = urlopen( url )
    except HTTPError:
        print("Not Valid URL") #temporary print outs!
    except URLError:
        print("Not Valid URL")
    except ValueError:
        print("Not Valid URL")
    else:
        websiteList.append( url )
    

def addApplication( filePath, applicationList ):
    try:
        fileAccess = filePath.resolve( strict=True )
        
    except FileNotFoundError:
        print("File Not Found")#temporary print out
        
    else:
        applicationList.append( filePath )

