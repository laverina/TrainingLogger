import sqlite3


def add_exercise_records(user_id, training_date, exercise_num, exercise_name, exercise_details):
    cursorobj = con.cursor()
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
                        '""" + str(exercise_details[4]) + """'
                    )
                    """)
    con.commit()


con = sqlite3.connect('data\exercises.db')
