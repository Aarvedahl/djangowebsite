import json

class Todo:
    def __init__(self,description,done):
        self.description = description
        self.done = done
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        