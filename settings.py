import random

valid_email = "lukonin.dv@gmail.com"
valid_password = "POSTman"
no_valid_email = "lukonin.d.v@gmail.com"
no_valid_password = "POSTman1"

images = ["150.jpg", "151.jpg", "152.jpeg", "153.jpeg", "154.jpeg", "155.jpg", "156.jpg", "157.jpg", "158.jpeg",
          "160.jpg", "162.jpeg", "163.jpeg", "164.jpeg"]

print(random.choice(images))

# Необходимо доработать работу тестов со списком авторизации
authorization_data = {
    "valid_email": "lukonin.dv@gmail.com", "valid_password": "POSTman",
    "no_valid_email": "lukonin.d.v@gmail.com", "no_valid_password": "POSTman1"
}
