#!/usr/bin/env python3

import random

try:
    import settings
except ImportError:
    exit('DO cp setting.py.default setting.py and set token!')

import logging
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

group_id = 220983890
log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler(filename='bot.log', encoding='UTF-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot for vk.com
    Use python 3.11
    """

    def __init__(self, group_id, token):
        """
        :param group_id: group id из группы vk
        :param token: секретный токен
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Запуск бота"""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

    def on_event(self, event):
        """
        Обрабатывает сообщения бота.
        Отправляет сообщение назад, если это текст.

        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug('отправляем сообщение назад')
            self.api.messages.send(
                message=event.message.text,
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.message.peer_id,
            )
        else:
            log.info('такое событие обработать пока не  могу - %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(group_id=settings.GROUP_ID, token=settings.TOKEN)
    bot.run()
