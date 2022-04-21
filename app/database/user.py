"""Database functions for user table."""
from app.database import get_db


def output_formatter(results):              # results will be a tuple of tuples
    out = []                                # empty list
    for result in results:                  # For each loop.
        result_dict = {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "hobbies": result[3],
            "active": result[4]
        }
        out.append(result_dict)
    return out


def insert(user_dict):
    """This function creates a user in our user table."""
    value_tuple = (
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies")
    )
    statement = """
        INSERT INTO user (
            first_name,
            last_name,
            hobbies
        ) VALUES (?, ?, ?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db().execute("SELECT * FROM user WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db().execute("SELECT * FROM user WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, user_data):              # user_data (parameter) is a dictionary (dict type)
    value_tuple = (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        pk
    )
    statement = """
        UPDATE user
        SET first_name=?,
        last_name=?,
        hobbies=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()
