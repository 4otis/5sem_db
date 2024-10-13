from faker import Faker
import csv
import random as r
from parser import parse_vehicles

fake = Faker("ru_RU")

services_data = [
    "оклейка пленкой",
    "полировка",
    "детейлинг/химчистка",
    "арматурные работы"
]

specialization_data = [
    "кузов",
    "салон",
    "стекла",
    "полировка"
]

vehicles_classification = parse_vehicles()
vehicles_brands = list(vehicles_classification.keys())

base_table_size = 1000

def generate_valid_phone():
    mobile_operator = r.choice(list(["916", "985", "915", "925"]))
    return str(f"8{mobile_operator}{r.randint(10**6,  10**7 - 1)}")


# vehicleClass

with open("./data/vehicleClass.csv", mode="w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    writer.writerow(("id", "class"))

    for i in range(5):
        writer.writerow((i, f"{i} класс"))


# vehicle

with open("./data/vehicle.csv", mode="w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    writer.writerow(("id", "brand", "model", "vehicleClassId", "urgent"))

    for i in range(base_table_size):
        brand = r.choice(vehicles_brands)
        model = r.choice(vehicles_classification[brand])
        vehicleClass = model[0]
        model = model[1]
        urgent = r.choice([True, False])

        writer.writerow(((97, brand, model, vehicleClass, urgent)))

vehicles = [i + 1 for i in range(base_table_size)]


# client

with open("./data/client.csv", mode="w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    writer.writerow(("id", "name", "surname", "email", "phone", "vehicleId"))

    for i in range(base_table_size):

        match r.choice(["male", "female", "male", "male"]):
            case "male":
                name = fake.first_name_male()
                surname = fake.last_name_male()
            case "female":
                name = fake.first_name_female()
                surname = fake.last_name_female()

        email = fake.ascii_email()
        phone = generate_valid_phone()

        vehicleId = r.choice(vehicles)
        vehicles.remove(vehicleId)

        writer.writerow((i + 1, name, surname, email, phone, vehicleId))

clients = [i + 1 for i in range(base_table_size)]


# specialization

with open("./data/specialization.csv", mode="w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    writer.writerow(("id", "name"))

    for i in range(len(specialization_data)):
        writer.writerow((i + 1, specialization_data[i]))


# employee

with open("./data/employee.csv", mode="w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    writer.writerow(("id", "name", "surname", "specializationId"))

    for i in range(base_table_size):
        
        match r.choice(["male", "female", "male", "male"]):
            case "male":
                name = fake.first_name_male()
                surname = fake.last_name_male()
            case "female":
                name = fake.first_name_female()
                surname = fake.last_name_female()

        specializationId = r.randint(1, len(specialization_data))
        
        writer.writerow((i + 1, name, surname, specializationId))


# serviceType

with open("./data/serviceType.csv", mode="w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    writer.writerow(("id", "name"))

    for i in range(len(services_data)):
        writer.writerow((i + 1, services_data[i]))


# service

with open("./data/service.csv", mode="w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    writer.writerow(("id", "clientId", "employeeId", "serviceTypeId", "cost"))

    for i in range(base_table_size):
        clientId = r.choice(clients)
        clients.remove(clientId)
        employeeId = r.randint(1, base_table_size - 1)
        serviceTypeId = r.randint(1, len(services_data))
        cost = r.randint(3000, 500000)

        writer.writerow((i + 1, clientId, employeeId, serviceTypeId, cost))