from pywebio.output import *
from pywebio.input import *

put_text('бокс действий')
box = output()
put_scrollable(box, height=400)

click = 0
add_click = 1
evard_list = ['Pulmeshka',] 
while True:
    comand = select('Выберете действие', ['клик', 'магазин', 'награды', 'профиль'])
    if comand == 'клик':
        click = click + add_click
    elif comand == 'магазин':
        box.append('Мега клик- 30 кликов\nкастомная награда- 100 кликов')
        shop_comand = select('выберете', ['мега клик', 'кастомная награда', 'назад'])
        if shop_comand == 'мега клик':
            if click == 30 or click > 30:
                click = click - 30
                add_click = add_click + 1
                box.append('Успешная покупка')
            else:
                box.append('Недостаточно средств')
        elif shop_comand == 'кастомная награда':
            if click == 100 or click > 100:
                custom = input('Введите название награды')
                evard_list.append(custom)
                box.append('Успешная покупка')
            else:
                box.append('недостаточно средств')
        elif shop_comand == 'назад':
            box.append('')
    elif comand == 'награды':
        box.append(evard_list)
    elif comand == 'профиль':
        box.append(f'клики- {click}\nмега клик- {add_click}\nкол-во наград- {len(evard_list)}')
    else:
        toast('Error server')
        break