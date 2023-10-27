class Workable:
    def work(self):
        pass

class Breakable:
    def take_break(self):
        pass

class Worker(Workable, Breakable):
    def work(self):
        pass

class Robot(Workable):
    def work(self):
        pass