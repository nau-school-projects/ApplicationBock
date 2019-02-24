import os
import winreg


class Registry_Editor():

    def __init__(self):
        self.blocked_apps = {}
        self.mainKey = None



    # This method is the initial setup of the registry to ensure that we have the right keys available to block apps.
    # It goest through the steps detailed in: https://www.technipages.com/prevent-users-from-running-certain-programs
    # With the extra addition of creating the Explorer key within Policies as that key was not already created in my
    # Registry
    def registry_setup(self):

        hkey = winreg.HKEY_CURRENT_USER
        Policies_Dir = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"
        Explorer_Dir = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer"
        DisallowRun_Dir = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun"
    
        try: 
            Policies_Key = winreg.OpenKey(hkey, "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies", 0, winreg.KEY_WRITE)
        except WindowsError as error:
            print("Error opening policy key")
            print(error)
            
        try:
            Explorer_Key = winreg.CreateKey(hkey, Explorer_Dir)
        except WindowsError as error:
            print("Error creating Explorer key")
            print(error)
            
        try:
            winreg.SetValueEx( Explorer_Key, "DisallowRun", 0, winreg.REG_DWORD, 1 )
        except WindowsError as error:
            print("Error setting value")
            print(error)
            
        try:
            DisallowRun_Key = winreg.CreateKey( hkey, DisallowRun_Dir )
            mainKey = DisallowRun_Key
        except WindowsError as error:
            print("Error creating DisallowRun")
            print(error)        



    # This method will add a new app to block
    # Param:
    #   app_to_add: String name of format app.exe
    #   registry_num: String number to order blocked apps
    def add_new_app( app_to_add, registry_num ):

        try:
            winreg.SetValueEx( mainKey, registry_num, 0, winreg.REG_SZ, app_to_add )
            blocked_apps[registry_num] = app_to_add
        except WindowsError:
            print("Unable to add new value")



    # This will delete values that correspond with a specific app within the Key DisallowRun
    # Search dictionary for the access key of the app_to_del
    def delete_app( app_to_del ):
        
        for num_val in blocked_apps:
            if blocked_apps[num_val] == app_to_del:
                registry_num = num_val
                
        try:
            winreg.DeleteValue( mainKey, registry_num )
        except WindowsError:
            print("Unable to delete new value")

        

    def block_pop_up():
        # When an application is blocked via the registry, and it is clicked to be opened a
        # dialogue pops up to tell the user that the user doesn't have the permission to open the app
        # We need a way to either edit or block this popup to replace it with our own.
        print("Hiya")
