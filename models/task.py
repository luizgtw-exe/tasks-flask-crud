class Task:
    def __init__(self,id, tittle, description, completed =False):
        self.id = id
        self.tittle = tittle
        self.description = description
        self.completed = completed

    def to_dict(self):
        return{
            "id":self.id,
            "title": self.tittle,
            "description":self.description,
            "completed":self.completed

        }
        