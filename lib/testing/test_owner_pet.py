from lib import Owner, Pet

def test_owner_init():
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

def test_has_pet_types():
    assert Pet.PET_TYPES == ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

def test_pet_has_all():
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Tweety", "bird")
    assert pet1 in Pet.all
    assert pet2 in Pet.all

def test_owner_has_pets():
    owner = Owner("Ben")
    pet = Pet("Rex", "dog")
    owner.add_pet(pet)
    assert pet in owner.pets()

def test_owner_adds_pets():
    owner = Owner("Ben")
    pet = Pet("Luna", "cat")
    owner.add_pet(pet)
    assert owner.pets() == [pet]

def test_add_pet_checks_isinstance():
    owner = Owner("Jim")
    try:
        owner.add_pet("not a pet")
    except Exception as e:
        assert str(e) == "Can only add Pet instances."

def test_get_sorted_pets():
    owner = Owner("John")
    pet1 = Pet("Zebra", "exotic")
    pet2 = Pet("Alpha", "cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    sorted_pets = owner.get_sorted_pets()
    assert sorted_pets[0].name == "Alpha"
    assert sorted_pets[1].name == "Zebra"
