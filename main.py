import configparser
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import messagee_parser
import training_formatter

config = configparser.ConfigParser()
config.read('config.ini')
token = config['VK']['token']
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.from_user and event.to_me:

        received_message = event.text

        if received_message.startswith('распарси') or received_message.startswith('запиши'):
            training = messagee_parser.parse_training(received_message)
            response_massage = training_formatter.generate_training_description(training)

            if received_message.startswith('запиши'):
                # todo сохранение в БД
                response_massage += '\n\nтренировка записана'

        elif received_message.startswith('подбери'):
            training = messagee_parser.parse_training(received_message)
            # todo чтение упражнений из БД, отбор последних записей
            # todo генерация ответа - training_formatter с деталями
            response_massage = 'тут будет подбор весов и параметров'

        else:
            response_massage = 'команда не распознана'

        vk.messages.send(
                user_id=event.user_id,
                random_id=randrange(10000),
                message=response_massage
            )
