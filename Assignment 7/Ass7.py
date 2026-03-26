class car:
    def __init__(self, registration_number, speed_limit):
        self.registration_number = registration_number
        self.speed_limit = speed_limit
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = self.current_speed + change
        if self.current_speed > self.speed_limit:
            self.current_speed = self.speed_limit
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

my_car = car("ABC-123", 142)

print(f"Registration number: {my_car.registration_number}")
print(f"Speed limit: {my_car.speed_limit}")
print(f"Current speed: {my_car.current_speed}")
print(f"Travelled distance: {my_car.travelled_distance}")
print(f"Current speed: {my_car.current_speed}")

my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"Current speed: {my_car.current_speed}")
my_car.accelerate(-200)
print(f"Speed after break: {my_car.current_speed}")

my_car.drive(1.5)
print(f"Travelled distance: {my_car.travelled_distance} km")

import random

cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(car(reg_number, max_speed))

race_over = False
while not race_over:
    for c in cars:
        change = random.randint(-10, 15)
        c.accelerate(change)
        c.drive(1)

    for c in cars:
        if c.travelled_distance >= 10000:
            race_over = True

print(f"{'Registration number':<10} {'Max speed':>15} {'Current speed':>17} {'Distance':>13}")

for c in cars:
    print(f"{c.registration_number:<10} {c.speed_limit:>15} {c.current_speed:>17} {c.travelled_distance:>13.1f}")