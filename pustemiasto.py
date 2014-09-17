class PusteMiasto(object):
    def __init__(self):
        self.nazwa = "-"
    def __cmp__(self, other):
        if self.nazwa == other.nazwa:
            return 0
        return 1
    