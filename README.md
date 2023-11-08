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
### Лабораторна робота №2 (Варіант 3 Рівень 3)
'''Фермер Джон побудував новий довгий загін для худоби, з N (2 <= N <= 100,000) секцій. Секції розташовуються уздовж прямої лінії в положеннях x1, ..., xN (0 <= x-i <= 1 000 000 000).

Його C (2 <= C <= N) корів не люблять нову будівлю і стають агресивними одна до одної, коли вони поставлені в сусідні стійла. Щоб уникнути ситуації, коли корови можуть заподіяти шкоду одна одній, фермер хоче розташувати агресивних корів у стійлах таким чином, щоб мінімальна відстань між будь-якими з них була настільки великою, наскільки це можливо. Яка найбільша мінімальна відстань?

Вхідні дані функції:
N = 5 С = 3
free_sections = `[1, 2, 8, 4, 9]

Результат 3

Пояснення:  У фермера є 5 корів, з яких 3 агресивні. Їх можна роташувати в стійлах 1, 4 та 8 або 1,4, 9. Таким чином мінімальне значення максимальної дистанції становить 3

Підказка:

Оскільки у нас є щонайменше дві корови, найкраще, що ми можемо зробити, це розташувати їх у загоні у першому вільному стійлі і в кінці

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище'''
### Лабораторна робота №3 (Варіант 3 Рівень 3)
'''Для заданого бінарного дерева реалізуйте функцію, яка обчислює та повертає значення максимального діаметра у бінарному дереві - найвіддаленішу відстань між двома листками. Максимальний діаметр у бінарному дереві визначає найбільшу відстань між будь-якою парою листків (кінцевих вузлів) у дереві. Діаметр вимірюється як кількість ребер, які потрібно пройти, щоб дістатися одного листка від іншого. Максимальний діаметр не обов'язково має включати в себе кореневий вузол

Нехай у вас задане бінарне дерево такого вигляду:

        1
       /  \
      3    2
     / \
    7   4
   /     \
  8       5
 /         \
9           6
Для даного дерева максимальний діаметр становить 6: 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6 - для проходження від листка 9 до листка 6 слід пройти 6 ребер.

Реалізована вами функція binary_tree_diameter(tree: BinaryTree) -> int отримує на вхід корінь бінарного дерева та повертає максимальний діаметр дерева.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)'''
### Лабораторна робота №4 (Варіант 2 Рівень 3)

'''Дано шахівницю, знайдіть найкоротшу відстань (мінімальна кількість ходів), яку пройшов кінь, щоб досягти заданого пункту призначення з заданого джерела.

Наприклад,

Вхідні дані:
 
N = 8 (дошка 8 × 8)
Джерело = (7, 0)
Пункт призначення = (0, 7)
 
Результат: мінімальна необхідна кількість кроків – 6 (див рисунок, червоними хрестиками позначено 



Кінь може ходити у восьми можливих напрямках від даної клітини, як показано на наступному малюнку:




Ми можемо знайти всі можливі місця, куди лицар може переміститися з даного місця, використовуючи масив, який зберігає відносну позицію руху лицаря з будь-якого місця. Наприклад, якщо поточне розташування (x, y), ми можемо перейти до (x + row[k], y + col[k]) для 0 <= k <= 7 за допомогою такого масиву:

row[] = [ 2, 2, -2, -2, 1, 1, -1, -1 ]
col[] = [ -1, 1, 1, -1, 2, -2, 2, -2 ]

З позиції (x,y) кінь може рухатись на клітинки з координатами:

(x + 2, y – 1)
(x + 2, y + 1)
(x – 2, y + 1)
(x – 2, y – 1)
(x + 1, y + 2)
(x + 1, y – 2)
(x – 1, y + 2)
(x – 1, y – 2)

Вхідні дані містяться у файлі input.txt:
 
8	# розмір поля
7, 0	# стартова точка
0, 7     # точка призначення

Результуючий файл має містити кількість ходів


Результуючий файл має містити значення найкоротшого шляху від початкової точки до точки призначення'''




### Лабораторна робота №2 (Варіант 3 Рівень 3)
​
Фермер Джон побудував новий довгий загін для худоби, з N (2 <= N <= 100,000) секцій. Секції розташовуються уздовж прямої лінії в положеннях x1, ..., xN (0 <= x-i <= 1 000 000 000).
​
Його C (2 <= C <= N) корів не люблять нову будівлю і стають агресивними одна до одної, коли вони поставлені в сусідні стійла. Щоб уникнути ситуації, коли корови можуть заподіяти шкоду одна одній, фермер хоче розташувати агресивних корів у стійлах таким чином, щоб мінімальна відстань між будь-якими з них була настільки великою, наскільки це можливо. Яка найбільша мінімальна відстань?
​
​
Вхідні дані функції:  
N = 5
С = 3  
free_sections = `[1, 2, 8, 4, 9]
​
Результат
3
​
Пояснення: 
У фермера є 5 корів, з яких 3 агресивні. Їх можна роташувати в стійлах 1, 4 та 8 або 1,4, 9. Таким чином мінімальне значення максимальної дистанції становить 3
​
Підказка:
​
Оскільки у нас є щонайменше дві корови, найкраще, що ми можемо зробити, це розташувати їх у загоні у першому вільному стійлі і в кінці


