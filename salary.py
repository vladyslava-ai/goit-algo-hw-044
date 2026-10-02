def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            total = 0

            for line in lines:
                name, salary = line.strip().split(",")
                salary = int(salary)
                total += salary

            average = total / len(lines)

            return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0

    except (ValueError, IndexError):
        print("Помилка: файл має неправильний формат.")
        return 0, 0

total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")

