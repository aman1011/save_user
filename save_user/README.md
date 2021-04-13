# Utility methods
There are 2 utility methods for writing and reading the sensor info in the text files, databases.txt.(which acts as database, since lambda is stateless)
 - write_movement_to_file:- This takes the data from the event['movement'] and writes the sensor movement data in the file in the following manner:-
    user 1,2 2021-05-13T04:22:01.002Z
    occupant room co-ordinates time
    The information is space separated.
 - get_room:- get_room method takes the occupant as the input and looks for the latest entries in the text file and returns the room co-ordinates for the given occupant. The possible values for occupants are:- user and beast.
 
 
# EscapeFromBeast Main class
There is a main calls EscapeFromBeast which have two attributes.
- user_room
- beast_room

These are the room co-ordinates for the user and beast.
The core logic resides in the method **user_is_safe** which checks whether the user is in adjacent room to the beast.
    
    
    
 # Assumptions
 - The sensor payload will have 2 possible values of occupants:- beast or user
 - If either user's or beast's room is not set yet, the method will assume that the user is safe.