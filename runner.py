import config
from functions import meow
from likert import likert
import time
from multiprocessing import Process


def func1():
    for i in range(config.actionCount):
        meow.twt()
        time.sleep(config.timeBetweenTweets)


def func2():
    likert()


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()
