# Create the Robot class
class Robot(object):
    # Set default parameters
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    # Print robot information provided by object
    def robot_info(self):
        print('Name: %s\nModel: %s\nColor: %s\n' % (self.name, self.model,
                                                    self.color))

    @classmethod
    # Use hyphen as string delimiter
    def one_string(cls, foo):
        name, model, color = foo.split('-')
        return cls(name, model, color)


def fetch():
    print("Delivering product to target: Shelf")


def sleep():
    print('No action required. Altman returning to backroom to recharge.')
    print("Power = Off")
