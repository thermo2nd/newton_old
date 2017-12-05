class Market():
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor
    def __str__(self):
        return self.major+'/'+self.minor
