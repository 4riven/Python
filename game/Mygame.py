import random


inventory = []
opened_doors = set()
solved_puzzles = set()
game_over = False

levels = {
    1: {
        'description': "Ты в холодной комнате с единственной дверью. На полу лежит старый ключ.",
        'actions': ['осмотреться', 'взять ключ', 'открыть дверь', 'открыть инвентарь',],
        'hint': "Используй ключ.",
        'item': 'ключ'
    },
    2: {
        'description': "В комнате есть лестница вниз и дверь с кодовым замком.",
        'actions': ['спуститься', 'ввести код'],
        'puzzle': "Сколько будет 2 + 3 + 5 (сумма первых трех простых чисел)?",
        'answer': '10'
    },
    3: {
        'description': "Комната с инструментами. Один из них - ломик.",
        'actions': ['осмотреться', 'взять ломик', 'открыть дверь'],
        'item': 'ломик'
    },
    4: {
        'description': "Перед тобой три двери, одна ведет на следующий уровень, остальные - ловушки.",
        'actions': ['открыть дверь 1', 'открыть дверь 2', 'открыть дверь 3'],
        'options': {
            'открыть дверь 1': 'Ловушка! Ты погиб.',
            'открыть дверь 2': 'Ты нашел лестницу вверх и прошёл на следующий уровень',
            'открыть дверь 3': 'Яма! Ты погиб.'
        }
    },
    5: {
        'description': "На пути решетка, которая закрыта на код.",
        'actions': ['ввести код'],
        'puzzle': "Сколько будет 2^3?",
        'answer': '8'
    },
    6: {
        'description': "Перед тобой три туннеля. Похоже, что только один безопасный.",
        'actions': ['идти направо', 'идти налево', 'идти прямо'],
        'options': {
            'идти направо': 'Ты погиб',
            'идти налево': 'Ты нашел выход на следующий уровень.',
            'идти прямо': 'Ты попал в ловушку и погиб.'
        }
    },
    7: {
        'description': "Ты нашел тайную комнату, внутри дробовик.",
        'actions': ['взять дробовик', 'идти дальше'],
        'item': 'дробовик'
    },
    8: {
        'description': "Ты встречаешь охранника, он готов атаковать.",
        'actions': ['использовать дробовик', 'попытаться сбежать'],
        'options': {
            'использовать дробовик': 'Ты победил охранника и прошел дальше.',
            'попытаться сбежать': 'Охранник тебя поймал, ты погиб.'
        }
    },
    9: {
        'description': "Ты видишь перед собой две двери - железную и деревянную.",
        'actions': ['открыть железную дверь', 'открыть деревянную дверь'],
        'options': {
            'открыть железную дверь': 'Ты нашел тайный выход на следующий уровень.',
            'открыть деревянную дверь': 'Ты попал в ловушку и погиб.'
        }
    },
    10: {
        'description': "Перед тобой комната с натянутыми проволоками.",
        'actions': ['пройти медленно', 'пробежать быстро'],
        'options': {
            'пройти медленно': 'Ты смог пройти безопасно.',
            'пробежать быстро': 'Ты зацепил проволоку и погиб.'
        }
    },
    11: {
        'description': "Просто открой дверь тут нет никакого подвоха.",
        'actions': ['открыть дверь'],
        'puzzle': "Ключ спрятан под предметом, который начинается на 'л'. Что это за предмет?",
        'answer': 'ломик'
    },
    12: {
        'description': "Твоя последняя задача: открыть тяжелую дверь, ведущую к свободе.",
        'actions': ['использовать ломик', 'попробовать открыть дверь'],
        'item_needed': 'ломик'
    },
    13: {
        'description': "Поздравляем! Ты выбрался из дома маньяка! Открой последюю дверь и заверши игру.",
        'actions': ['открыть дверь']
    }
}




def show_inventory():
    print("Твой инвентарь:", ', '.join(inventory) if inventory else "пусто")


def process_command(level, command):
    global game_over
    level_info = levels[level]

    if command == 'осмотреться' and 'item' in level_info:
        print(f"Ты нашел предмет: {level_info['item']}.")
    elif command.startswith('взять') and 'item' in level_info:
        item = level_info['item']
        if item not in inventory:
            print(f"Ты взял {item}.")
            inventory.append(item)
    elif command == 'открыть дверь' or command == 'идти дальше' :
        if level == 1 or 'ключ' in inventory or 'ломик' in inventory or 'дробовик' in inventory:
            print("Дверь открыта! Переходишь на следующий уровень.")
            solved_puzzles.add(level)
        else:
            print("Дверь заперта, и у тебя нет ключа.")
    elif command == 'спуститься':
        print("Вы аккуратно спускаетесь, но вдруг старая лестница рушится, и вы падаете в темный подвал и теряете сознание. Вас находит маньяк и убивает.")
        game_over = True
    elif command == 'ввести код':
        answer = input(f"Реши задачу: {level_info['puzzle']} ")
        if answer == level_info['answer']:
            print("Верно! Дверь открыта.")
            solved_puzzles.add(level)
        else:
            print("Неверный код.")
    elif command in level_info.get('options', {}):
        outcome = level_info['options'][command]
        print(outcome)
        if 'погиб' in outcome:
            game_over = True
        else:
            solved_puzzles.add(level)
    elif command == 'использовать ломик' and 'ломик' in inventory:
        print("Ломик помог открыть дверь. Ты прошел уровень.")
        solved_puzzles.add(level)
    elif command == 'открыть инвентарь':
        show_inventory()
    else:
        print("Неверная команда. Попробуй снова.")

def play_level(level):
    global game_over
    level_info = levels[level]
    print(f"\n{level_info['description']}")

    while level not in solved_puzzles and not game_over:
        print("Доступные действия:", ', '.join(level_info['actions']))
        command = input("Ваши действия: ").strip().lower()
        process_command(level, command)

    if game_over:
        print("Ты погиб. Игра окончена.")
    elif level in solved_puzzles:
        print(f"Ты успешно прошел уровень {level}!\n")


def start_game():
    print("Ты очнулся в доме маньяка. Твоя цель - выбраться, избегая ловушек и решая головоломки!")
    for level in range(1, 14):
        if game_over:
            break
        play_level(level)
    if not game_over:
        print("Поздравляем! Ты нашел выход и сбежал из дома маньяка!")


start_game()