import json

def load(self, name):
    f = open(name)
    info = json.load(f)
    f.close()

    self.__dict__.update(info) 
