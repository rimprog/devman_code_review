# Файл search.py

Файл демонстрирует реализацию алгоритма бинарного поиска числа в упорядоченной последовательности элементов.
Для реализации алгоритма в файле создается упорядоченный список длинною в 10 элементов, содержащий рандомную последовательность чисел от 1 до 100, кратные 2.
Пользователь вводит искомое число, после чего при помощи функции, реализующей алгоритм бинарного поиска производится поиск введенного пользователем числа в сгенерированной рандомной последовательности.
Если число было найдено, выводом в консоль дается его индекс в сгенерированной последовательности. Ниже пример сообщения, вывод которого происходит при реализации успешного сценария нахождения индекса искомого числа в случайно сгенерированной последовательности:
```
Pick a number between 0-100: 8
List: [8, 22, 38, 52, 60, 74, 78, 84, 94, 100]
Found 8 in index 0
```
Если же число не было найдено, также осуществляется вывод соответствующего сообщения:
```
Pick a number between 0-100: 4
List: [0, 16, 20, 38, 60, 62, 72, 78, 96, 100]
Cannot find 4 in the list
```
Помимо этого производится проверка на правильность пользовательского ввода. Ожидается ввод целого числа. В случае некорректного ввода выводится сообщение:
`Invalid input`

## s

Функция реализующая непосредственно алгоритм бинарного поиска.
В качестве аргументов, на вход принимает отсортированный список `list_`, и искомое число `target`.
При помощи индекса первого `left` и последнего `right` числа списка, вычисляется индекс серидины списка `middle`.
С помощью конструкции условного выражения `if else` реализуется логика, при которой отбрасывается половина списка в зависимости от положения искомого числа `target` по отношению к середине списка `middle`.
Цикл `while` обеспечивает выполнение поиска по упорядоченной последовательности эллементов, до момента пока число не будет найдено среди элементов списка, либо будет подтверждено его отсутствие.