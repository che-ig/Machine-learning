# Настройка Flake8

1. Установка flake8 в терминале `pip install flake8`. Затем его нужно запустить (если вдруг он сам не запустится) `ctrl + shift + p` и ввести в строку поиска `run linting`.
2. Делаем симлинк файла `setup.cfg` (это конфигурационный файл для настройки flake8) на одном уровне с проектом.
3. Для нахождения ошибок в коде `pip install flake8-bugbear`
4. Проверяем не переопределили ли мы в своем коде зарезервированныев языке слова (id, len ...) `pip install flake8-builtins`
5. Провера именования переменных, классов и др. `pip install pep8-naming`
6. Проверка на запятые `pip install flake8-commas`
7. Проверка имен переменных будет ругаться на переменные типа a, b, val, result ... (т.е переменные не имеющие осмысленного имени) `pip install flake8-variables-names`
8. Следит за порядком импортов по блокам. Сначала импорты из стандартных библиотек, внешних библиотек и потом из текущего проекта `pip install flake8-import-order`
9. Позволяет следить чтобы функции не были слишком длинные (более 100 строк) и что у функции нет большого количества аргументов (более 6) `pip install flake8-functions`
10. Позволяющее сообщать о неправильном порядке атрибутов класса и логике уровня класса. `pip install flake8-class-attributes-order`. [Источник](https://github.com/best-doctor/flake8-class-attributes-order)
11. Проверяет сложность выражения. Не допускает в условных конструкции большого количества условий `pip install flake8-expression-complexity`
12. Когнитивная сложность является аналогом цикломатической сложности, которая измеряет, насколько сложно понять фрагмент кода. Представленный Г. Энн Кэмпбелл и в настоящее время используется SonarSource, `pip install flake8-cognitive-complexity`


Источники:
1. [Репозиторий с описаниее большого количества плагинов - awesome-flake8-extensions ](https://github.com/DmytroLitvinov/awesome-flake8-extensions)
2. [Видео 1](https://www.youtube.com/watch?v=cdHnEN0Dsm0&list=LL&index=4)
3. [Видео 2](https://www.youtube.com/watch?v=luoFOnOqEGA&list=LL&index=13&t=11s)