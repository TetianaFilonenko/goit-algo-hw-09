## Порівняння жадібного алгоритму та динамічного програмування для задачі видачі решти

### Жадібний алгоритм

Жадібний підхід обирає найбільші доступні номінали монет, що призводить до швидкого знаходження рішення. Однак цей підхід не завжди оптимальний. Цей підхід обирає найбільший можливий номінал на кожному кроці, не враховуючи глобальний контекст, що не гарантує оптимального рішення для всіх наборів монет.

### Динамічне програмування

Метод динамічного програмування шукає мінімальну кількість монет для досягнення заданої суми, зберігаючи проміжні результати. Це забезпечує оптимальне рішення, але потребує більше часу та пам'яті.

### Часова складність

- Жадібний алгоритм: O(n), де n — кількість номіналів монет.
- Динамічне програмування: O(n \* m), де n — кількість номіналів монет, а m — сума.

### Висновок

Жадібний алгоритм підходить для швидких і простих рішень, але може не бути оптимальним для всіх наборів номіналів монет. Алгоритм динамічного програмування гарантує оптимальне рішення, але є більш вимогливим до ресурсів. Для великих сум і нестандартних наборів монет алгоритм динамічного програмування є кращим вибором, оскільки гарантує оптимальне рішення.
