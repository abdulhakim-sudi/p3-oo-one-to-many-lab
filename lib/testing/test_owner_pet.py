 
from lib import Owner, Pet

import pytest
from lib.owner_pet import Owner, Pet
d0945c5 (Complete One-to-many Owner-Pet lab with passing tests)

def test_owner_init():
    owner = Owner("John")
    assert owner.name == "John"
def test_pet_init():
def test_pet_init_valid():
 d0945c5 (Complete One-to-many Owner-Pet lab with passing tests)
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"
    assert pet.owner is None


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


def test_pet_init_invalid_type():
    with pytest.raises(Exception):
        Pet("Fluffy", "dinosaur")


def test_pet_owner_assignment():
    owner = Owner("Alice")
    pet = Pet("Mittens", "cat")
    owner.add_pet(pet)
    assert pet.owner == owner


def test_owner_pets_method():
    owner = Owner("Bob")
    pet1 = Pet("Spot", "dog", owner)
    pet2 = Pet("Whiskers", "cat", owner)
    pet3 = Pet("Nibbles", "rodent")
    pets = owner.pets()
    assert pet1 in pets
    assert pet2 in pets
    assert pet3 not in pets


def test_get_sorted_pets():
    owner = Owner("Carol")
    pet1 = Pet("Zorro", "dog", owner)
    pet2 = Pet("Buddy", "cat", owner)
    sorted_pets = owner.get_sorted_pets()
    assert sorted_pets == [pet2, pet1]  # Buddy, Zorro sorted alphabetically


def test_add_pet_invalid():
    owner = Owner("Dave")
    with pytest.raises(Exception):
        owner.add_pet("not a pet")
d0945c5 (Complete One-to-many Owner-Pet lab with passing tests)
