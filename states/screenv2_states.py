from aiogram.dispatcher.filters.state import StatesGroup, State

class screenv2_states(StatesGroup):
    #количество стейтов = количеству максимально возможных вопросов, мы все равно делаем state.finish(следовательно все обрывается)
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()
    Q11 = State()
    Q12 = State()
