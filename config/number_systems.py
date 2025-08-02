from tkinter import messagebox
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

    def convert_2(self):
        stroka = str(self.fn)
        l = len(stroka) - 1
        res = 0
        for i in range(len(stroka)):
            res += int(stroka[i]) * self.sn ** l
            l -= 1
        print(res)
        return res


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


