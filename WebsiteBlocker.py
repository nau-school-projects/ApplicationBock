localHost = "127.0.0.1"  #defualt local host
hostFile = r"C:\Windows\System32\Drivers\etc\hosts" #default file path for windows host file

    
def blockWebsite( blockedList ):
    with open( hostFile, 'r+') as hostFileOpen:
        hostFileContent = hostFileOpen.read()

        for website in blockedList:
            if website in hostFileContent:
                pass
            else:
                hostFileOpen.write( localHost + " " + website + "\n" )

def unblockWebsite( blockedList):
    with open( hostFile, 'r+') as hostFileOpen:
       
        hostFileContent = hostFileOpen.readlines()

        hostFileOpen.seek(0)

        for line in hostFileContent:
            if not any (website in line for website in blockedList):
                hostFileOpen.write(line)
                    
        hostFileOpen.truncate()
        
# must be ran as administrator


    
