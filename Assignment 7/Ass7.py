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

my_car.accelerate(40)
my_car.accelerate(60)
my_car.accelerate(70)
print(f"Change of speed {my_car.current_speed}")
my_car.accelerate(-200)
print(f"tốc độ hiện tại của xe sau khi phanh khẩn cấp : {my_car.current_speed}")
print("=" * 10, "Task3", "=" * 10)
my_car.drive(1.5)
print(f"Quảng đường xe đã đi được: {my_car.travelled_distance} km ")

# =================Task 4==================
import random

cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(car(reg_number, max_speed))
# Vòng lặp đua xe
race_over = False
while not race_over:
    for c in cars:
        change = random.randint(-10, 15)
        c.accelerate(change)
        c.drive(1)
    # Kiểm tra có xe nào đạt 10,000 km chưa
    for c in cars:
        if c.travelled_distance >= 10000:
            race_over = True
# In bảng kết quả
print(f"{'Biển số':<10} {'Tốc độ tối đa':>15} {'Tốc độ hiện tại':>17} {'Quãng đường':>13}")
print("-" * 60)
for c in cars:
    print(f"{c.registration_number:<10} {c.maximum_speed:>15} {c.current_speed:>17} {c.travelled_distance:>13.1f}")