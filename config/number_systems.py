class Convert:
    def __init__(self, first_num, second_num):
        self.fn = first_num
        self.sn = second_num

    def convert_1(self):
        stroka = ''
        while self.fn > 0:
            stroka += str(self.fn % self.sn)
            self.fn //= self.sn
        return int(stroka[::-1])
