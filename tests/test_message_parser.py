import message_parser
from datetime import datetime


def test_training_parser_1_ex_min_data():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               0,
            'reps':               0,
            'details':            '',
            'execution_weight':   0,
            'execution_details': ''
        }
    ]


def test_training_parser_1_ex_sets_reps():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
4 по 8
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               '4',
            'reps':               '8',
            'details':            '',
            'execution_weight':   0,
            'execution_details': ''
        }
    ]


def test_training_parser_1_ex_details():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
детали
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               0,
            'reps':               0,
            'details':            'детали',
            'execution_weight':   0,
            'execution_details': ''
        }
    ]


def test_training_parser_1_ex_mult_details():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
детали
и еще детали
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               0,
            'reps':               0,
            'details':            'детали; и еще детали',
            'execution_weight':   0,
            'execution_details': ''
        }
    ]


def test_training_parser_1_ex_weight():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
--40
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               0,
            'reps':               0,
            'details':            '',
            'execution_weight':   '40',
            'execution_details': ''
        }
    ]


def test_training_parser_1_ex_exec_details():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
--с гирей 24 кг
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               0,
            'reps':               0,
            'details':            '',
            'execution_weight':   0,
            'execution_details': 'с гирей 24 кг'
        }
    ]


def test_training_parser_1_ex_mult_exec_details():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
--с гирей 24 кг
--сложно
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               0,
            'reps':               0,
            'details':            '',
            'execution_weight':   0,
            'execution_details': 'с гирей 24 кг; сложно'
        }
    ]


def test_training_parser_1_ex_max():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
4 по 8
детали
еще детали
--40
--сложно
--еще детали
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               '4',
            'reps':               '8',
            'details':            'детали; еще детали',
            'execution_weight':   '40',
            'execution_details': 'сложно; еще детали'
        }
    ]


def test_training_parser_2_ex():
    assert message_parser.parse_training(
        """распарси
Приседания со штангой
4 по 8
детали
еще детали
--40
--сложно
--еще детали

еще упражнение
1 по 2
детали
еще детали
--10
--сложно
--еще детали
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               '4',
            'reps':               '8',
            'details':            'детали; еще детали',
            'execution_weight':   '40',
            'execution_details': 'сложно; еще детали'
        },
        {
            'name': 'еще упражнение',
            'num': 2,
            'sets': '1',
            'reps': '2',
            'details': 'детали; еще детали',
            'execution_weight': '10',
            'execution_details': 'сложно; еще детали'
        }
    ]


def test_date_parser_date_provided():
    assert message_parser.parse_date(
        """запиши 2021-11-11
упражнение
детали

упражнение
детали

упражнение
детали
"""
    ) == '2021-11-11'


def test_date_parser_date_not_provided():
    assert message_parser.parse_date(
        """запиши
упражнение
детали

упражнение
детали

упражнение
детали
"""
    ) == datetime.today().strftime('%Y-%m-%d')
