import pytest
import message_formatter

# Test on generate_training_description


def test_training_formatter_single_ex_basic_data():
    assert message_formatter.generate_training_description([
        {
            'num': 1,
            'name': 'приседания со штангой',
            'sets': 4,
            'reps': 8,
            'details': '',
            'execution_weight': 40,
            'execution_details': ''
        }
    ]) == """Тренировка состоит из упражнений:

1. приседания со штангой
 -  4 по 8
 -- 40 кг

"""


def test_training_formatter_single_ex_no_data():
    assert message_formatter.generate_training_description([
        {
            'num': 1,
            'name': 'приседания со штангой',
            'sets': 0,
            'reps': 0,
            'details': '',
            'execution_weight': 0,
            'execution_details': ''
        }
    ]) == """Тренировка состоит из упражнений:

1. приседания со штангой

"""


def test_training_formatter_single_ex_full_data():
    assert message_formatter.generate_training_description([
        {
            'num': 1,
            'name': 'приседания со штангой',
            'sets': 4,
            'reps': 8,
            'details': 'детали',
            'execution_weight': 40,
            'execution_details': 'подробности выполнения'
        }
    ]) == """Тренировка состоит из упражнений:

1. приседания со штангой
 -  4 по 8
 - детали
 -- 40 кг
 -- подробности выполнения

"""


def test_training_formatter_multiple_ex():
    assert message_formatter.generate_training_description([
        {
            'num': 1,
            'name': 'приседания со штангой',
            'sets': 4,
            'reps': 8,
            'details': '',
            'execution_weight': 40,
            'execution_details': ''
        },
        {
            'num': 2,
            'name': 'жим штанги лежа',
            'sets': 5,
            'reps': 5,
            'details': '',
            'execution_weight': 25,
            'execution_details': ''
        }
    ]) == """Тренировка состоит из упражнений:

1. приседания со штангой
 -  4 по 8
 -- 40 кг

2. жим штанги лежа
 -  5 по 5
 -- 25 кг

"""

# TODO split test to several: 1 ex 1 rec min data, 1 ex 1 rec full data, 1 ex mult rec, multiple ex
def test_history_formatter():
    assert message_formatter.generate_execution_history_description(
        [
            {
                'exercise_name': 'приседания со штангой',
                'execution_history': [
                    {
                        'date': '2021-11-21',
                        'sets': '4',
                        'reps': '10',
                        'details': '',
                        'execution_weight': '35',
                        'execution_details': '',
                    },
                    {
                        'date': '2021-11-14',
                        'sets': '5',
                        'reps': '5',
                        'details': '',
                        'execution_weight': '40',
                        'execution_details': 'последний подход тяжело',
                    },
                ]
            },
            {
                'exercise_name': 'выпады (ходьба)',
                'execution_history': [
                    {
                        'date': '2021-11-21',
                        'sets': '0',
                        'reps': '0',
                        'details': '16 (8+8) 3 подхода; носок передней ноги внутрь смотрит',
                        'execution_weight': '0',
                        'execution_details': 'с 2мя гантелями по 10 кг',
                    }
                ]
            },
        ]
    ) == """Последние записи об упражнениях:

приседания со штангой
2021-11-21
 - 4 по 10
 --35 кг
2021-11-14
 - 5 по 5
 --40 кг [последний подход тяжело]

выпады (ходьба)
2021-11-21
 - 0 по 0 [16 (8+8) 3 подхода; носок передней ноги внутрь смотрит]
 --0 кг [с 2мя гантелями по 10 кг]

"""
# TODO fix "0 по 0"
# TODO fix "0 кг"
