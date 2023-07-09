from faker import Faker

def print_name():
    faker=Faker("nl_NL")
    name=faker.name()
    print(name)

def main():
    print_name()