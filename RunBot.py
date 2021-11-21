import configparser

config = configparser.ConfigParser()
config.read('config.ini')
token = config['VK']['token']


from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.from_user and event.to_me:

        vk.messages.send(
                user_id=event.user_id,
                random_id=randrange(10000),
                message='текст ответа'
            )
