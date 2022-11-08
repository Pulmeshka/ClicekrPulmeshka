from pywebio.output import *
from pywebio.input import *
from pywebio import start_server

def main():
    choose = select('Выберете режим игры', ['новая игра', 'чит режим'])
    if choose == 'новая игра':
        import NewGame
    elif choose == 'чит режим':
        import CheatGame
    else:
        toast('Error server')
start_server(main, debug=True, port=8080)