import json
import string
import random


symbols = string.ascii_letters + string.digits + "!_"


def load_db(filename):
    with open(filename) as file:
        db = json.load(file)

    return db


def save_db(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file, indent=2)

def add_pass(db):
    site = input("Введите название сайта : ")
    login = input("Введите логин : ")
    password = input("Введите пароль : ")

    db.append(
        {
            "login": login,
            "password": password,
            "site": site
        },

    )

def change(subject, prev):
    t = input(f"Введите {subject} ({prev}):")
    if t == "":
        return prev
    else:
        return t



def change_pass(info):
    info["site"] = change("название сайта", info["site"])
    info["login"] = change("логин", info["login"])
    info["password"] = change("пароль", info["password"])

def compare(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)

    inter = s1_set.intersection(s2_set)

    return len(inter) > 0

def gen_pass(L):
    while True:
        res = ""
        for i in range(L):
            res += random.choice(symbols)

        bools = [
            compare(res, string.ascii_letters),
            compare(res, string.ascii_uppercase),
            compare(res,string.digits),
            compare(res, "!_"),
            res[0], not string.ascii_uppercase,
        ]

        if all(bools):
            return res


def add_and_gen(db):
    site = input("Введите название сайта : ")
    login = input("Введите логин : ")
    L = int(input("Введите длину пароля : "))
    password = gen_pass(L)

    db.append(
        {
            "login": login,
            "password": password,
            "site": site
        },

    )

db = []

add_and_gen(db)
print(db)

