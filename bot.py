#!/usr/bin/env python3

from _token import token
import vk_api
import vk_api.bot_longpoll
group_id = 220983890


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=group_id)

    def run(self):
        pass


if __name__ == '__main__':
    bot = Bot(group_id=group_id, token=token)
    bot.run()
