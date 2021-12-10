class Dog:
    def __init__(self, dog_name):
        self.dog_name = dog_name
        self.trick_list = []
    def get_name(self):
        return self.dog_name
    def sit(self):
        print(self.dog_name, "sits")
        self.trick_list.append("sits courteously")
    def roll_over(self):
        print(self.dog_name, "rolls over")
        self.trick_list.append("rolls over amazingly")
    def shake_hand(self):
        print(self.dog_name, "shakes your hand")
        self.trick_list.append("shakes your hand professionally")
    def print_trick_list(self):
        if len(self.trick_list) == 0:
            print(self.dog_name, "hasn't preformed any tricks yet")
        else:
            print(self.dog_name, "has performed the following tricks:", self.trick_list)
