class day:                                      #base class structure - all classes will inherit from this
    def __init__(self):
        self.hour1 = True                       #True = the specified time is available
        self.hour2 = True                       #9am-10am
        self.hour3 = True                       #10am-11am
        self.hour4 = True                       #11am-12pm
        self.hour5 = False                      #12pm-1pm -> Lunch
        self.hour6 = True
        self.hour7 = True
        self.hour8 = True
        self.hour9 = True
        self.hour10 = True                      #5pm-6pm -> last patient
        self.list = [True,True,True,True,False,True,True,True,True,True]

class Monday(day):                              #appointments for monday
    def __init__(self):
        super().__init__()                      #inherits all attributes from day class
        self.day = 'Monday'

class Tuesday(day):                             #appointments for tuesday
    def __init__(self):
        super().__init__()
        self.day = 'Tuesday'


class Wednesday(day):
    def __init__(self):
        super().__init__()
        self.day = 'Wednesday'


class Thursday(day):
    def __init__(self):
        super().__init__()
        self.day = 'Thursday'

class Friday(day):
    def __init__(self):
        super().__init__()
        self.day = 'Friday'


class Saturday(day):                            #last day for doctors to work -> def: !Working on Sunday
    def __init__(self):
        super().__init__()                      
        self.day = 'Saturday'


def main():
    print("Starting up...")

if __name__ == "__main__":
    main()