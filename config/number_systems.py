from tkinter import messagebox
class Convert:
    def __init__(self, number, first_system, second_system):
        self.num = number # тип строка

        self.fs = first_system
        self.ss = second_system

        self.d = {10: 'A', 11: 'B', 12: 'C',
                  13: 'D', 14: 'E', 15: 'F'}

    def convert_1(self, num): # конверация из 10 в другую
        stroka = ''
        while num > 0:
            val = num % self.ss
            if self.ss == 16 and 16 > val > 9:
                stroka += self.d[val]
            else:
                stroka += str(num % self.ss)
            num //= self.ss
        print(stroka[::-1])
        return stroka[::-1]

    def convert_2(self): # конвертация из другой в 10
        stroka = str(self.num)
        print(stroka)
        l = len(stroka) - 1
        res = 0
        for i in range(len(stroka)):
            if self.fs == 16 and stroka[i].upper() in self.d.values():
                key = get_key(self.d, stroka[i].upper())
                print(key)
                res += key * self.fs ** l
            else:
                res += int(stroka[i]) * self.fs ** l
            l -= 1
        return res

    def convert(self):
        if self.fs == self.ss:
            return self.num
        elif self.fs == 10:
            return self.convert_1(self.num) # конверация из 10 в другую
        elif self.ss == 10:
            return self.convert_2() # конвертация из другой в 10
        else:
            number_one = self.convert_2()
            return self.convert_1(number_one)

# ищем ключ по значению
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

# Число может содержать только цифры 0 - 7
def number_check(number, system):
    if system == 2:
        for i in number:
            if int(i) >= system:
                print(i)
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 1')
                return True
    elif system == 3:
        for i in number:
            if int(i) >= system:
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 2')
                return True
    elif system == 4:
        for i in number:
            if int(i) >= system:
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 3')
                return True
    elif system == 5:
        for i in number:
            if int(i) >= system:
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 4')
                return True
    elif system == 6:
        for i in number:
            if int(i) >= system:
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 5')
                return True
    elif system == 7:
        for i in number:
            if int(i) >= system:
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 6')
                return True
    elif system == 8:
        for i in number:
            if int(i) >= system:
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 7')
                return True
    elif system == 9:
        for i in number:
            if int(i) >= system:
                messagebox.showerror('Ошибка', 'Число может содержать \nтолько цифры: 0 - 8')
                return True


