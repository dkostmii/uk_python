# uk_python (Українська адаптація пітону)

> [!IMPORTANT]
> Хоч проект має ряд обмежень, ми
> раді розглянути Ваші пропозиції у PR та issues🙏❤️

Репозиторій містить бібліотеку Python, що служить українською
адаптацією цієї мови програмування.

## Встановлення бібліотеки

Встановіть пакет з репозиторію PyPi за допомогою
пакетного менеджера `pip`, що надається Python.

```sh
pip install uk_python
```

## Приклад коду

Нижче наведено приклад коду для виведення
кольорами українського прапору🇺🇦

```python
from пітон import *

надрукувати("Привіт!", стиль="жовтий")
надрукувати("Світ!", стиль="блакитний")
```

Більше прикладів застосування можна
знайти у каталозі [`приклади/`](./приклади).

## Обмеження проекту

Оскільки проект реалізовано у вигляді бібліотеки,
а не середовища запуску чи компілятора,
виконання повного перекладу є неможливим.
Це не означає, що бібліотека не знайде свого застосування:
=======
### Адаптовані бібліотеки
   - import argparse = from пітон.стд import аргпарсер [опис]()
   - import time = from пітон.стд import час
   - import thread = rom пітон.стд import багатопочність

> [!IMPORTANT]
> **Допоможіть нам знайти його, пропонуючи зміни або знаходячи баги**🙏❤️.
