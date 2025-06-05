import pytest
from lib.owner_pet import Owner, Pet


def test_owner_init():
    owner = Owner("John")
    assert owner.name == "John"


def test_pet_init_valid():
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"
    assert pet.owner is None


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
