def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat)

            return cats_info

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []

    except (ValueError, IndexError):
        print("Помилка: файл має неправильний формат.")
        return []


cats_info = get_cats_info("cats_file.txt")

print(cats_info)