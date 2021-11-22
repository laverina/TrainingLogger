import sqlite3


def update_lists_to_len(list, desired_length):
    len_diff = desired_length - len(list)
    for i in range(len_diff):
        list.append('')
    return list


def add_exercise_records(user_id, training_date, exercise_num, exercise_name, exercise_details,
                         execution_details=['', '', '', '', '']):
    cursorobj = con.cursor()
    exercise_details = update_lists_to_len(exercise_details, 5)
    execution_details = update_lists_to_len(execution_details, 5)
    cursorobj.execute("""
                    INSERT INTO exercises VALUES(
                        """ + str(user_id) + """,
                        '""" + str(training_date) + """',
                        """ + str(exercise_num) + """,
                        '""" + str(exercise_name) + """',
                        '""" + str(exercise_details[0]) + """',
                        '""" + str(exercise_details[1]) + """',
                        '""" + str(exercise_details[2]) + """',
                        '""" + str(exercise_details[3]) + """',
                        '""" + str(exercise_details[4]) + """',
                        '""" + str(execution_details[0]) + """',
                        '""" + str(execution_details[1]) + """',
                        '""" + str(execution_details[2]) + """',
                        '""" + str(execution_details[3]) + """',
                        '""" + str(execution_details[4]) + """'
                    )
                    """)
    con.commit()


con = sqlite3.connect('data\exercises.db')
