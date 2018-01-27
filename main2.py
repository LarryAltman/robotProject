# Import Robot class to use the methods within
from Robot import *

# Create Robot1 object with arguments
Robot1 = Robot.one_string('Altman-X27-Cobalt')

# Call the robotInfo function using the Robot2 object
Robot1.robotInfo()

# Set state variable equal to return value from check class
state = Robot.check()

# Call methods depending on value of state
if state == 'Y':
    Robot.sleep()
elif state == 'N':
    Robot.fetch()
else:
    print('\nInvalid percepts. Please try again.')
