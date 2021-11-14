from .models import Plan, AccumulateMoney




def when_goal():
    day = int(Plan.need_money / AccumulateMoney.result())

    return f'You goal need {day} day!'
    