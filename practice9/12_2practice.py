# import os


# def main():
#     # os.mkdir("ducks")
#     # os.mkdir("ducks/real")
#     # os.mkdir("ducks/cartoon")
#     # os.mkdir("ducks/not_ducks")

#     # main()
from datetime import datetime


def main():

    # d = datetime.date(2023, 4, 13)
    # print("date and time", d)
    # now = datetime.now()
    # print("now", now)
    timestamp = datetime.now().time()
    print(timestamp)


main()
