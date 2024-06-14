import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemy = 100

    def run(self):
        day = 0
        while self.enemy > 0:
            day += 1
            self.enemy -= self.skill
            print(f'День {day}.....{self.name} уничтожил {self.skill} врагов, ещё осталось {self.enemy} врагов', flush=True)

            time.sleep(2)

        print(f'{self.name} защитил королевство за {day} дн.', flush=True)


knight_1 = Knight('Sir Lion Heart', 33)
knight_2 = Knight('Sir Black Prince', 10)

knight_1.start()
knight_2.start()

knight_1.join()
knight_2.join()
