from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock
from vk_api.bot_longpoll import VkBotMessageEvent

import settings
from bot import Bot


class Test1(TestCase):
    RAW_EVENT = {'group_id': 220983890,
                 'type': 'message_new', 'event_id': '23f650e33d5d7f12b27932535f8fbf2fc03b479f', 'v': '5.131',
                 'object': {
                     'message': {'date': 1686813143, 'from_id': 270344325, 'id': 95, 'out': 0, 'attachments': [],
                                 'conversation_message_id': 94, 'fwd_messages': [], 'important': False,
                                 'is_hidden': False,
                                 'peer_id': 270344325, 'random_id': 0, 'text': 'Проба 2'},
                     'client_info': {
                         'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback',
                                            'intent_subscribe', 'intent_unsubscribe'],
                         'keyboard': True, 'inline_keyboard': True, 'carousel': True, 'lang_id': 0
                     }}}

    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count  # [obj, obj, ...]
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    # старый тест для эхо-функции, сейчас не актуален

    # def test_on_event(self):
    #     event = VkBotMessageEvent(raw=self.RAW_EVENT)
    #
    #     send_mock = Mock()
    #
    #     with patch('bot.vk_api.VkApi'):
    #         with patch('bot.VkBotLongPoll'):
    #             bot = Bot('', '')
    #             bot.api = Mock()
    #             bot.api.messages.send = send_mock
    #
    #             bot.on_event(event=event)
    #
    #     send_mock.assert_called_once_with(
    #         message=self.RAW_EVENT['object']['message']['text'],
    #         random_id=ANY,
    #         peer_id=self.RAW_EVENT['object']['message']['peer_id'],
    #     )

    INPUTS = [
        'Привет!',
        'А когда?',
        'Где будет конференция?',
        'Зарегистрируй меня.',
        'Веник',
        'мой адрес email@mail',
        'email@mail.ru'
    ]
    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.INTENTS[1]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Веник', email='email@mail.ru')
    ]

    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotMessageEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mock
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        assert real_outputs == self.EXPECTED_OUTPUTS
