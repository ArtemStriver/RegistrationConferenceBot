#!/usr/bin/env python3

import random
from _token import token
import vk_api
import vk_api.bot_longpoll
from vk_api.utils import get_random_id

group_id = 220983890


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=group_id)

        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('получено событие')
            try:
                self.on_event(event)
            except Exception as exc:
                print(exc)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.message.text)
            print(event.message.peer_id)
            self.api.messages.send(
                message=event.message.text,
                random_id=random.randint(0, 2**20),
                peer_id=event.message.peer_id,
            )
        else:
            print('такое событие обработать пока не  могу - ', event.type)


if __name__ == '__main__':
    bot = Bot(group_id=group_id, token=token)
    bot.run()
