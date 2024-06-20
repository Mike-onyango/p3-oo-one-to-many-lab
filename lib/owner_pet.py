class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f'{pet_type} is not a valid pet type.')
            raise Exception(f'{pet_type} is not a valid pet type.')
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if pet.owner is not None:
            raise Exception(f'The pet {pet.name} has an owner.')
        pet.owner = self
        self._pets.append(pet)
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
    pass