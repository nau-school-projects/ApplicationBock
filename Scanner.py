import requests #used to test if a website exsists

def addWebsite( url, websiteList ):
    connection = requests.get( url )

    if connection.status_code == 404: #404 is the code of not found
        print("Website Doesn't Exsist") #temporary print out
        
    else:
         websiteList.append( url )

def addApplication( filePath, applicationList ):
    try:
        fileAccess = filePath.resolve( strict=True )
        
    except FileNotFoundError:
        print("File Not Found")#temporary print out
        
    else:
        applicationList.append( filePath )
        
    
#tested and works. Testing if the file or website exsists and then adding them to the lists.
