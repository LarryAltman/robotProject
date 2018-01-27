# Create the Robot class
class Robot(object):
    # Set default parameters
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    # Use hyphen as string delimiter
    @classmethod
    def one_string(cls, my_str):
        name, model, color = my_str.split('-')
        return cls(name, model, color)

    # Print robot information provided by object
    def robotInfo(self):
        print('Name: %s\nModel: %s\nColor: %s' % (self.name, self.model, self.color))

    # Methods called from main
    @classmethod
    def check(cls):
        state = input("Is the shelf full? Enter 'Y\' for yes or 'N\' for no: ").upper()
        return state

    @classmethod
    def fetch(cls):
        stockExists = input("Is there product available in the backroom? Enter 'Y\' for yes or 'N\' for no: ").upper()
        if stockExists == 'Y':
            print("\nAltman will stock the product on the shelf. Will return to backroom to sleep when finished.")
        elif stockExists == 'N':
            print("\nNo product available to stock. Returning to backroom to sleep.")
        else:
            print("\nInvalid percepts. Please try again.")

    @classmethod
    def sleep(cls):
        print('\nShelves full. Altman returning to backroom to sleep.')
