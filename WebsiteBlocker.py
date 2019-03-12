import socket #needed to find the local hose IP
import shutil #used to copy the duplicate the host_file needed for windows 
import os     #needed to delete the duplicate host_file


redirct = socket.gethostbyname(socket.gethostname())
hostFile = r"C:\Windows\System32\Drivers\etc\hosts"

duplicateHostFile = r"C:\Windows\System32\Drivers\etc\hostsD"

def duplicateHostFile ():
    shutil.copy(hostFile, duplicateHostFile )
    
def blockWebsite( blockedList ):
    duplicateHostFile()
    
    with open( duplicateHostFile, 'r+'):
        hostFileContent = file.read()
    
    for website in blockList:
        if website in hostFileContent:
            pass
        else:
            file.write( redirect + " " + website + "\n" )

def unblockWebsite( blockedList ):
    if os.path.exists( duplicateHostFile ):
        os.remove( duplicateHostFile )
    else:
        pass
                
    
# Havent tested this fully yet, can not test on school computer which i am using to code! will test later today
