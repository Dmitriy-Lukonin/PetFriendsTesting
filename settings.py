import random

valid_email = "lukonin.dv@gmail.com"
valid_password = "POSTman"
no_valid_email = "lukonin.d.v@gmail.com"
no_valid_password = "POSTman1"

images = ["150.jpg", "151.jpg", "152.jpeg", "153.jpeg", "154.jpeg", "155.jpg", "156.jpg", "157.jpg", "158.jpeg",
          "cat1.jpg", "P1040103.jpeg"]

print(random.choice(images))


authorization_data = {
    "valid_email": "lukonin.dv@gmail.com", "valid_password": "POSTman",
    "no_valid_email": "lukonin.d.v@gmail.com", "no_valid_password": "POSTman1"}

