class Manager:
    def __init__(self):
        self.actions = {}

    def assing(self, name):
        def decorate(callback):
            self.actions[name] = callback
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)


manager = Manager()

@manager.assing("print_yes")
def printyes(manager):
    print("yes")


manager.execute("print_yes")