# Create the Robot class
class Robot(object):
    # Set default parameters
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    # Print robot information provided by object
    def robotInfo(self):
        print('Name: %s\nModel: %s\nColor: %s\n' % (self.name, self.model, self.color))

    # Use hyphen as string delimiter
    @classmethod
    def one_string(cls, my_str):
        name, model, color = my_str.split('-')
        return cls(name, model, color)

def fetch():
    print("Delivering product to target: Shelf")

def sleep():
    print('No action required. Altman returning to backroom to recharge.')
    print("\nPower = Off")
