import pytest
import message_formatter

# Test on generate_training_description


def test_single_ex_basic_data():
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


def test_single_ex_no_data():
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

# TODO test_single_ex_full_data

# TODO test_multiple_ex


# TODO Test on generate_execution_history_description and remove example from docstring
