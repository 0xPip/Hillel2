# ДЗ 10. Множини (set) у Python


# ===== Завдання 1 =====
numbers = [10, 20, 10, 30, 20, 40, 10, 50]

unique_numbers = set(numbers)

print("Завдання 1")
print("Початковий список:", numbers)
print("Множина:", unique_numbers)
print("Кількість унікальних чисел:", len(unique_numbers))
print("Число 30 є у множині:", 30 in unique_numbers)
print("Число 100 є у множині:", 100 in unique_numbers)
print()


# ===== Завдання 2 =====
data = [15, "Python", 15, True, "Python", 3.14, False, True]

data_set = set(data)

print("Завдання 2")
print("Множина:", data_set)

data_set.add("Redis")
data_set.add(100)
data_set.remove("Python")

print("Множина після змін:", data_set)
print("True є у множині:", True in data_set)
print("False є у множині:", False in data_set)
print()


# ===== Завдання 3 =====
python_students = {"Anna", "Oleh", "Ivan", "Maria"}
redis_students = {"Oleh", "Maria", "Petro", "Sofia"}

union_operator = python_students | redis_students
union_method = python_students.union(redis_students)

print("Завдання 3")
print("Python або Redis (оператор |):", union_operator)
print("Python або Redis (метод union):", union_method)
print("Результати однакові:", union_operator == union_method)
print()


# ===== Завдання 4 =====
# Дані ті самі, що в завданні 3
intersection_operator = python_students & redis_students
intersection_method = python_students.intersection(redis_students)

print("Завдання 4")
print("Python і Redis (оператор &):", intersection_operator)
print("Python і Redis (метод intersection):", intersection_method)
print()


# ===== Завдання 5 =====
all_students = {"Anna", "Oleh", "Ivan", "Maria", "Petro", "Sofia"}
python_students = {"Anna", "Oleh", "Ivan"}

difference_operator = all_students - python_students
difference_method = all_students.difference(python_students)

print("Завдання 5")
print("Ще не вивчають Python (оператор -):", difference_operator)
print("Ще не вивчають Python (метод difference):", difference_method)
print()


# ===== Завдання 6 =====
numbers = {10, 20, 30}

print("Завдання 6")
print("Початкова множина:", numbers)

numbers.add(40)
print("Після add(40):", numbers)

numbers.add(40)
print("Після повторного add(40) - нічого не змінилось:", numbers)

numbers.update([50, 60, 70])
print("Після update([50, 60, 70]):", numbers)

numbers.remove(20)
print("Після remove(20):", numbers)

numbers.discard(100)
print("Після discard(100) - помилки немає:", numbers)

removed = numbers.pop()
print("Видалений елемент через pop():", removed)

print("Остаточна множина:", numbers)