def create_file():
    fout = open("users.txt", "w")
    fout.close()


def add_user(user_name):
    fout = open("users.txt", "a")
    fout.write(user_name + "\n")
    fout.close()


def update_user(old_user, new_user):
    fin = open("users.txt", "r")
    lines = fin.read().split("\n")
    fin.close()
    fout = open("users.txt", "w")
    for i in lines:
        if old_user in i:
            i = i.replace(old_user, new_user)
        fout.write(i + "\n")
    fout.close()


def remove_user(name):
    fin = open("users.txt", "r")
    lines = fin.read().split("\n")
    fin.close()
    fout = open("users.txt", "w")
    for i in lines:
        if name != i.strip():
            fout.write(i + "\n")
    fout.close()
