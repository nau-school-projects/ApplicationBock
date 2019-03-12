LOCALHOST = "127.0.0.1"  #defualt local host
HOSTFILE = r"C:\Windows\System32\Drivers\etc\hosts" #default file path for windows host file


def blockWebsite( blockedDict ):
    blocked = True
    with open( HOSTFILE, 'r+') as hostFileOpen:
        hostFileContent = hostFileOpen.read()

        for key in blockedDict:
            if key in hostFileContent:
                pass
            
            else:
                hostFileOpen.write( LOCALHOST + " " + key + "\n" )
                
                blockedDict[key] = blocked

def unblockWebsite( blockedDict):
    blocked = False
    with open( HOSTFILE, 'r+') as hostFileOpen:
       
        hostFileContent = hostFileOpen.readlines()

        hostFileOpen.seek(0)

        for line in hostFileContent:
            for key in blockedDict:
                if not key in line:
                    hostFileOpen.write(line)
                else:
                    blockedDict[key] = False
                    
        hostFileOpen.truncate()

# must be ran as administrator 
