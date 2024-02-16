class Pet:
    
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    
    def __init__(self, name, pet_type, owner=""):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type=pet_type
        else:
            raise Exception
        self.owner = owner

    # @property
    # def pet_type(self):
    #     return self._pet_type

    # @pet_type.setter
    # def pet_type(self, pet_type):
    #     if pet_type in Pet.PET_TYPES:
    #         self._pet_type=pet_type
    #     else:
    #         raise Exception
       
class Owner:
    def __init__(self, name):
        self.name = name