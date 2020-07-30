from api import PetFriends
from settings import *


class TestPetFriends:
    def setup(self):
        self.pf = PetFriends()

    def test_get_API_keyForValidUser(self, email=valid_email, password=valid_password):
        status, result = self.pf.get_API_key(email, password)
        assert status == 200
        assert 'key' in result

    def test_getAllPetsWithValidKey(self, filter=''):  # filter available values : my_pets
        _, auth_key = self.pf.get_API_key(valid_email, valid_password)
        status, result = self.pf.get_list_of_pets(auth_key, filter)
        assert status == 200
        assert len(result['pets']) > 0

    def test_addNewPetWithValidData(self, name='Барбоскин', animal_type='двортерьер', age='4',
                                    pet_photo='images/cat1.jpg'):

        _, auth_key = self.pf.get_API_key(valid_email, valid_password)

        status, result = self.pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
        assert result['name'] == name

    def test_successfulDeleteSelfPet(self):
        _, auth_key = self.pf.get_API_key(valid_email, valid_password)
        _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

        if len(myPets['pets']) == 0:
            self.pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
            _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

        pet_id = myPets['pets'][0]['id']
        status, _ = self.pf.delete_pet(auth_key, pet_id)
        _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200
        assert pet_id not in myPets.values()

    def test_successfulUpdateSelfPetInfo(self, name='Мурзик', animal_type='Котэ', age=5):
        _, auth_key = self.pf.get_API_key(valid_email, valid_password)
        _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

        if len(myPets['pets']) > 0:
            status, result = self.pf.update_pet_info(auth_key, myPets['pets'][0]['id'], name, animal_type, age)
            assert status == 200
            assert result['name'] == name
        else:
            raise Exception("There is no my pets")
