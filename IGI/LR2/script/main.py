import os
import importlib
#import time

shape = os.getenv("SHAPE", "circle").lower()
size = os.getenv("SIZE", "10")

available_shapes = ["circle", "square"]

if shape not in available_shapes:
    print(f"Ошибка: Фигура '{shape}' не поддерживается. Доступны: {available_shapes}")
    exit(1)

module = importlib.import_module(f"geometric_lib.{shape}")

area = module.area(float(size))
perimeter = module.perimeter(float(size))

print(f"Фигура: {shape}")
print(f"Размер: {size}")
print(f"Площадь: {area}")
print(f"Периметр: {perimeter}")

#time.sleep(3600)