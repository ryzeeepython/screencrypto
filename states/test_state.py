from aiogram.dispatcher.filters.state import StatesGroup, State

class test_states(StatesGroup):
    #количество стейтов = количеству максимально возможных вопросов, мы все равно делаем state.finish(следовательно все обрывается)
    Q1 = State()
    Q2 = State()
