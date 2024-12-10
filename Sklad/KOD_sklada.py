users = [
    {'username': 'admin', 'password': 'admin123', 'role': 'admin'},
    {'username': 'user1', 'password': 'user123', 'role': 'user'}
]

exhibits = [
    {'title': 'Мона Лиза', 'category': 'Живопись', 'year': 1503, 'rating': 4.9},
    {'title': 'Давид', 'category': 'Скульптура', 'year': 1504, 'rating': 4.8},
    {'title': 'Звёздная ночь', 'category': 'Живопись', 'year': 1889, 'rating': 4.7},
]


def validate_string(prompt):
    while True:
        value = input(prompt).strip()
        if value.isalpha():
            return value
        print("Ошибка: значение должно содержать только буквы.")

def validate_year(prompt):
    while True:
        try:
            year = int(input(prompt))
            if year > 0:
                return year
            print("Ошибка: год должен быть положительным числом.")
        except ValueError:
            print("Ошибка: введите корректное целое число для года.")

def validate_rating(prompt):
    while True:
        try:
            rating = float(input(prompt))
            if 1.0 <= rating <= 5.0:
                return rating
            print("Ошибка: рейтинг должен быть числом от 1 до 5.")
        except ValueError:
            print("Ошибка: введите корректное число для рейтинга.")


def login():
    print("Добро пожаловать в Музейный каталог!")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Успешный вход! Ваша роль: {user['role']}")
            return user
    print("Неверный логин или пароль.")
    return None


def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Добавить экспонат")
        print("2. Удалить экспонат")
        print("3. Редактировать экспонат")
        print("4. Просмотреть экспонаты")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            add_exhibit()
        elif choice == '2':
            delete_exhibit()
        elif choice == '3':
            edit_exhibit()
        elif choice == '4':
            view_exhibits()
        elif choice == '5':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


def user_menu():
    while True:
        print("\nМеню пользователя:")
        print("1. Просмотреть экспонаты")
        print("2. Сортировать экспонаты по рейтингу")
        print("3. Фильтровать экспонаты по категории")
        print("4. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            view_exhibits()
        elif choice == '2':
            sort_exhibits_by_rating()
        elif choice == '3':
            filter_exhibits_by_category()
        elif choice == '4':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


def add_exhibit():
    title = input("Введите название экспоната: ").strip()
    if not title:
        print("Ошибка: название не может быть пустым.")
        return
    category = validate_string("Введите категорию экспоната (только буквы): ")
    year = validate_year("Введите год создания (целое положительное число): ")
    rating = validate_rating("Введите рейтинг экспоната (от 1 до 5): ")
    exhibits.append({'title': title, 'category': category, 'year': year, 'rating': rating})
    print(f"Экспонат '{title}' добавлен.")

def delete_exhibit():
    title = input("Введите название экспоната для удаления: ").strip()
    for exhibit in exhibits:
        if exhibit['title'].lower() == title.lower():
            exhibits.remove(exhibit)
            print(f"Экспонат '{title}' удалён.")
            return
    print("Экспонат не найден.")

def edit_exhibit():
    title = input("Введите название экспоната для редактирования: ").strip()
    for exhibit in exhibits:
        if exhibit['title'].lower() == title.lower():
            exhibit['title'] = input("Введите новое название: ").strip()
            exhibit['category'] = validate_string("Введите новую категорию (только буквы): ")
            exhibit['year'] = validate_year("Введите новый год создания (целое положительное число): ")
            exhibit['rating'] = validate_rating("Введите новый рейтинг (от 1 до 5): ")
            print(f"Экспонат '{title}' обновлён.")
            return
    print("Экспонат не найден.")

def view_exhibits():
    if not exhibits:
        print("Список экспонатов пуст.")
    else:
        print("\nСписок экспонатов:")
        for exhibit in exhibits:
            print(f"{exhibit['title']} ({exhibit['category']}, {exhibit['year']}) - Рейтинг: {exhibit['rating']}")

def sort_exhibits_by_rating():
    sorted_exhibits = sorted(exhibits, key=lambda x: x['rating'], reverse=True)
    print("\nЭкспонаты, отсортированные по рейтингу:")
    for exhibit in sorted_exhibits:
        print(f"{exhibit['title']} - Рейтинг: {exhibit['rating']}")

def filter_exhibits_by_category():
    category = validate_string("Введите категорию для фильтрации (только буквы): ")
    filtered_exhibits = list(filter(lambda x: x['category'].lower() == category.lower(), exhibits))
    if not filtered_exhibits:
        print(f"Экспонаты в категории '{category}' не найдены.")
    else:
        print(f"\nЭкспонаты в категории '{category}':")
        for exhibit in filtered_exhibits:
            print(f"{exhibit['title']} ({exhibit['year']}) - Рейтинг: {exhibit['rating']}")


def main():
    user = login()
    if user:
        if user['role'] == 'admin':
            admin_menu()
        elif user['role'] == 'user':
            user_menu()

if __name__ == "__main__":
    main()