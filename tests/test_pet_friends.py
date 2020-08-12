from api import PetFriends
from settings import *


class TestPetFriends:
    def setup(self):
        self.pf = PetFriends()

    def test_get_api_key_for_valid_user(self, email=valid_email, password=valid_password):
        status, result = self.pf.get_api_key(email, password)
        assert status == 200
        assert 'key' in result

    def test_get_all_pets_with_valid_key(self, filter=''):  # filter available values : my_pets
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.get_list_of_pets(auth_key, filter)
        assert status == 200
        assert len(result['pets']) > 0

    def test_add_new_pet_with_valid_data(self, name='Барбоскин', animal_type='двортерьер',
                                         age='4', pet_photo='images/cat1.jpg'):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)

        status, result = self.pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        assert status == 200
        assert result['name'] == name

    def test_successful_delete_self_pet(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

        if len(my_pets['pets']) == 0:
            self.pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
            _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

        pet_id = my_pets['pets'][0]['id']
        status, _ = self.pf.delete_pet(auth_key, pet_id)
        _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200
        assert pet_id not in my_pets.values()

    def test_successful_update_self_pet_info(self, name='Мурзик', animal_type='Котэ', age=5):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

        if len(my_pets['pets']) > 0:
            status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
            assert status == 200
            assert result['name'] == name
        else:
            raise Exception("There is no my pets")
