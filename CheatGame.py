from pywebio.output import *
from pywebio.input import *

put_text('бокс действий')
box = output()
put_scrollable(box, height=400)

click = 1000000000000000000000000000000000000000000000
add_click = 100000000000000000000000000000000000
evard_list = ['Pulmeshka', 'читер',] 
while True:
    comand = select('Выберете действие', ['клик', 'магазин', 'награды', 'профиль'])
    if comand == 'клик':
        click = click + add_click
    elif comand == 'магазин':
        box.append('Мега клик- 0 кликов\nкастомная награда- 1 кликов')
        shop_comand = select('выберете', ['мега клик', 'кастомная награда', 'назад'])
        if shop_comand == 'мега клик':
            if click == 0 or click > 0:
                click = click - 0
                add_click = add_click + 1000
                box.append('Успешная покупка')
            else:
                box.append('Недостаточно средств')
        elif shop_comand == 'кастомная награда':
            if click == 0 or click > 0:
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
        box.append(f'клики- бесконечно\nмега клик- {add_click}\nкол-во наград- {len(evard_list)}')
    else:
        toast('Error server')
        break