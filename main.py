def read_recipes(file_path):

    cook_book = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:

                dish_name = file.readline().strip()
                if not dish_name:
                    break

                ingredient_count = int(file.readline().strip())
                ingredients = []

                for _ in range(ingredient_count):
                    ingredient_data = file.readline().strip().split(' | ')
                    ingredients.append({
                        'ingredient_name': ingredient_data[0],
                        'quantity': int(ingredient_data[1]),
                        'measure': ingredient_data[2]
                    })

                cook_book[dish_name] = ingredients

                file.readline()
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except ValueError as e:
        print(f"Ошибка обработки данных: {e}")
    return cook_book



file_path = 'files/recipes.txt'
cook_book = read_recipes(file_path)

print(cook_book)




