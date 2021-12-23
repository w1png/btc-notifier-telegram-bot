import sqlite3
from sys import argv
from argparse import ArgumentParser

conn = sqlite3.connect("data.db")
c = conn.cursor()


class User:
    def __init__(self, user_id):
        self.user_id = user_id

        if not does_user_exist(self.get_id()):
            c.execute(f"INSERT INTO users VALUES(?, ?)", [user_id, 0])
            conn.commit()

    def get_id(self):
        return self.user_id

    def __clist(self):
        c.execute(f"SELECT * FROM users WHERE user_id={self.get_id()}")
        return list(c)[0]

    def is_subscribed(self):
        return self.__clist()[1] == 1
    
    def set_subscribed(self, value):
        c.execute(f"UPDATE users SET notification=? WHERE user_id=?", [value, self.get_id()])
        conn.commit()


def does_user_exist(user_id):
    c.execute(f"SELECT * FROM users WHERE user_id=\"{user_id}\"")
    return len(list(c)) != 0


def get_notif_list():
    c.execute(f"SELECT * FROM users WHERE notification=1")
    return list(map(User, [user[0] for user in list(c)]))


def get_user_login(message):
    return message.from_user.username


def get_user_list():
    c.execute("SELECT * FROM users")
    return list(map(User, [user[0] for user in list(c)]))


# Arguments for debugging
if __name__ == "__main__":
    # only used to create -h because it's way faster than doing it manually
    parser = ArgumentParser(description="Allows you to interact with the \"users\" talbe in the database.")
    parser.add_argument("-a", "--all", help="allows you to see all the users.", required=False)
    parser.add_argument("-s", "--subscribed", help="allows you to see all the subscribed users.", required=False)

    if argv:
        for arg in argv:
            if arg in ["-a", "--all"]:
                print("There are no users for now." if len(get_user_list()) == 0 else "\n".join(map(str, [user.get_id() for user in get_user_list()])))
            elif arg in ["-s", "--subscribed"]:
                print("There are no subscribed users for now." if len(get_notif_list()) == 0 else "\n".join(map(str, [user.get_id() for user in get_notif_list()])))
                
    else:
        print(parser.print_help())