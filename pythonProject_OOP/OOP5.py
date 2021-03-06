# self
class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):  # instance method # ธรรมเนียมมม เป็นตัวแปรตัวอื่นได้
        return self.gold + self.silver + self.bronze

    def dummy(self, a, b):
        return a + b


if __name__ == '__main__':
    th = Medal("Thailand", 5, 3, 2)
    print(th.country)
    print(th.total())  # same Medal.total(th) 16 = 17
    print(Medal.total(th))  # th = self

    print(th.dummy(1, 2))
    print(Medal.dummy(th, 1, 2))
