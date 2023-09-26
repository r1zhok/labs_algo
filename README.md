# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Стріжик Олексій Богданович (Група ІР-24)

### Лабораторна робота №1 (Варіант 3 Рівень 3)
'''Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає довжину найдовшої пікової підпослідовностію Для формування пікової підпослідовності необхідно мінімум 3 числа. Пікова підпослідовність визначається як послідовність чисел, яка починається з меншого числа, після чого наступне число строго більше попереднього, поки вони не досягнуть вершини (максимального значення у підпослідовності). Всі значення після досягнення вершини мають бути завжди меншими від попередника. Наприклад, пікова послідовність може мати вигляд:
​
1 7 2
Де 7 - є вершиною послідовності
​
1 2 3 - не є піковою послідовністю (немає лівої частки)
3 2 1 - також не є піковою полідовністю (немає правої частки)
-1 -5 -1 - теж не є піковою послідовністю (необхідно знайти вершину, а не впадину)
​
У масиві може бути декілька пікових підпослідовностей, необхідно знайти довжину максимальної
​
Приклад
Для вхідного масиву: 1, 3, 5, 4, 2, 8, 3, 7,  знайдена найдовша пікова підпослідовність має довжину 5 - 1, 3, 5, 4, 2
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити сценарії коли: 
всі елементи масиву посортовані за зростанням, 
посортовані за спаданням, 
масив з 2х елементів, 
не містять пікових підпослідовностей, 
містять 3 пікові послідовності'''

