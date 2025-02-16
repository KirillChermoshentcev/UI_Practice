from faker import Faker
faker = Faker()
class UserData:
    name = faker.first_name()
    email = faker.email()
    current_address = faker.administrative_unit()
    permanent_address = faker.city()