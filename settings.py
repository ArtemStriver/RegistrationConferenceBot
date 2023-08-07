GROUP_ID = 220983890
TOKEN = "vk1.a.EVxwXnNvngMA8ls66GAUjsgk-BJOCuyYvpziyzn_5Cvl8druJld-YpPKvDnSquLXpwG2lycmtUQCxdbVY57nZ4jbSsb51nJa1Tk4hXB4tY-RHjBTLqdAXZCQUzRgebqdKDG4qSSs4wvczjCUI6ze86n_vUrJuQO-8hr8mavusVC77ZNBkghB4wUkq7yxiWVwCsFhS21Potml_Q6K_M-SAQ"

INTENTS = [
    {
        'name': 'Дата проведения',
        'tokens': ("когда", "сколько", "дата", "дату"),
        'scenario': None,
        'answer': 'Конференция проводится 13 мая, регистрация начинается в 10 утра.'
    },
    {
        'name': 'Место проведения',
        'tokens': ('где', 'место', 'локация', 'адрес', 'метро'),
        'scenario': None,
        'answer': 'Конференция пройдет на набережной, в амфитеатре.'
    },
    {
        'name': 'Регистрация',
        'tokens': ("регистр", "добав"),
        'scenario': 'registration',
        'answer': None
    }
]

SCENARIOS = {
    'registration': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Чтобы зарегистрироваться, введите ваше имя. Оно будет написано на бейджике.',
                'failure_text': 'Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще раз.',
                'handler': 'handler_name',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введите email. Мы отправим на него все данные.',
                'failure_text': 'Во введенном адресе ошибка. Попробуйте еще раз.',
                'handler': 'handler_email',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Спасибо за регистрацию, {name}! Мы отправили на {email} билет, распечатайте его.',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }
    }
}

DEFAULT_ANSWER = 'Не знаю как на это ответить. ' \
                 'Могу сказать когда и где пройдет конференция, а также зарегистрировать вас. Просто спросите.'

DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='qwerty',
    host='localhost',
    database='vk_chat_bot')
