# import necessary modules
import os

from BlockedList import *
from MD5Encryptor import *

# initialize constants


# Simple storage class that holds the user's name, password, and their list
# of applications/websites they want to block. Used only while the program is
# running, with data being save to an encrypted file at shutdown and then loaded
# at startup.
class UserProfile( object ):

    def __init__( self, name, password, blockedList ):
        # initialize instance variables
        self.name = name

        self.password = password
        
        self.blockedList = blockedList

# Class that stores a list of user profiles and manages the creation of new
# users, the process of logging in, and the saving and loading of user profiles
# to/from a file.
class UserManager( object ):

    # NOTE, in the future this method will probably make use of the load data
    # method so that the UserManager can be initialized with all user profiles
    # that were previously saved.
    def __init__( self ):
        # initialize instance variables

        # Dictionary of users, with usernames as keys and UserProfiles as values
        self.usersDict = {}

    # algorithm: creates a new user and adds it to the dictionary if the entered
    # username is not taken
    # precondition: passed username, password, and BlockedList
    # postcondition: if name is not taken, new UserProfile instance is created
    # with these values, added to dictionary and True is returned; if name is
    # returns False
    def newUserProfile( self, name, password, blockedList ):
        # initialize function/variables
        

        # check if name is taken
        for user in self.usersDict:
            if( self.usersDict[ user ].name == name ):
                return False;
            
        newUser = UserProfile( name, password, blockedList )
        self.usersDict[ name ] = newUser
        return True;

    # algorithm: checks if a username password pair matches, and returns the
    # associated BlockedList if they do
    # precondition: passed username and password
    # postcondition: if username and password match, return that UserProfile's
    # BlockedList, otherwise returns None
    def checkPassword( self, name, password ):
        # initialize function/variables
        targetProfile = self.usersDict[ name ]

        if( targetProfile.password == password ):
            return targetProfile.blockedList

        return None

    # TODO: Implement writing to and reading from a file.
    # save data

    # load data
    

