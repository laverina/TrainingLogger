DROP TABLE IF EXISTS exercises;

CREATE TABLE IF NOT EXISTS exercises(
	user_id integer,
	date text,
	exercise_num integer,
	exercise_name text,
	sets integer,
	reps integer,
	details text,
	execution_weight integer,
	execution_details text
);