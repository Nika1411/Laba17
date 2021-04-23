#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 14
# Создать класс Payment (зарплата). В классе должны быть представлены поля: фамилия-
# имя-отчество, оклад, год поступления на работу, процент надбавки, подоходный налог,
# количество отработанных дней в месяце, количество рабочих дней в месяце, начисленная и
# удержанная суммы. Реализовать методы: вычисления начисленной суммы, вычисления
# удержанной суммы, вычисления суммы, выдаваемой на руки, вычисления стажа. Стаж
# вычисляется как полное количество лет, прошедших от года поступления на работу, до теку-
# щего года. Начисления представляют собой сумму, начисленную за отработанные дни, и
# надбавки, то есть доли от первой суммы. Удержания представляют собой отчисления в
# пенсионный фонд (1% от начисленной суммы) и подоходный налог. Подоходный налог
# составляет 13% от начисленной суммы без отчислений в пенсионный фонд.

class Payment:

    def __init__(self, full_name=' ', salary=0, year=0, percent=0, daysworked=0, workingdays=1):
        self.__full_name = str(full_name)
        self.__salary = int(salary)
        self.__year = int(year)
        self.__percent = float(percent)
        self.__days_worked = int(daysworked)
        self.__working_days = int(workingdays)
        # self.amount = 0
        # self.held_amount = 0
        # self.hand_amount = 0
        # self.exp = 0

        # self.accrued_amount()
        # self.withheld_amount()
        # self.handed_amount()
        # self.experience()

    def accrued_amount(self):
        a = self.__salary / self.__working_days
        b = a * self.__days_worked
        percent = self.__percent / 100 + 1
        return b * percent

    def withheld_amount(self):
        b = (self.__salary / self.__working_days) * self.__days_worked

        return b * (0.13 + 0.01)

    def handed_amount(self):
        a = self.__salary / self.__working_days
        b = a * self.__days_worked
        percent = self.__percent / 100 + 1
        return b * percent - (self.__salary / self.__working_days) * self.__days_worked

    def experience(self):
        return 2020 - self.__year

    # def __str__(self):
    #     return f"Experience: {self.exp} years \nCalculations: {self.amount} - {self.held_amount} = {self.hand_amount}"

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __eq__(self, other):
        return self.__salary == other.__salary

    def __ne__(self, other):
        return self.__salary != other.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    def __ge__(self, other):
        return self.__salary >= other.__salary

    def __le__(self, other):
        return self.__salary <= other.__salary

    def __truediv__(self, other):
        if self.__salary >= other.__salary:
            return self.__salary / other.__salary
        else:
            return other.__salary / self.__salary

    def __sub__(self, other):
        if self.__days_worked >= other.__days_worked:
            return self.__days_worked - other.__days_worked
        else:
            return other.__days_worked - self.__days_worked

    def __add__(self, other):
        return self.__working_days + other.__working_days
