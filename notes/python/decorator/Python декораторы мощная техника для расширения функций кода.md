# Python декораторы: мощная техника для расширения функций кода

[Источник](https://sky.pro/wiki/python/ponimaem-funktsiyu-enumerate-v-python-na-primere-koda/)

**Для кого эта статья:**

- Новички в программировании на Python
- Опытные разработчики, желающие углубить свои знания о декораторах
- Специалисты, работающие с веб-фреймворками, такими как Flask и Django
  Декораторы в Python — это мощный инструмент метапрограммирования, который часто вызывает у новичков эффект "магии кода". Они позволяют радикально изменить поведение функций или классов, не затрагивая их основной код, словно добавляя невидимую обертку вокруг них. Многие разработчики годами работают с Python, используя фреймворки вроде Flask или Django, даже не подозревая, что скрывается за символом @ в строке над определением функции. Пришло время разобрать эту "магию" на понятные компоненты! 🐍✨

## Что такое декораторы в Python и как они устроены

Декораторы — это функциональные конструкции, позволяющие обернуть одну функцию внутрь другой, чтобы расширить её возможности без изменения исходного кода. По сути, декоратор принимает функцию в качестве аргумента, добавляет к ней новую функциональность и возвращает модифицированную версию.

Ключевое свойство декораторов — прозрачность для пользователя. Функция, к которой применён декоратор, выглядит и ведёт себя точно так же, как и раньше, но с дополнительной функциональностью.

Декораторы опираются на три ключевых концепции Python:

- В Python функции являются объектами первого класса — их можно передавать как аргументы
- Функции могут быть определены внутри других функций
- Функция может возвращать другую функцию

Рассмотрим простейший пример декоратора:

```python
def my_decorator(func):
def wrapper():
print("Действия перед вызовом функции")
func()
print("Действия после вызова функции")
return wrapper

@my_decorator
def say_hello():
print("Привет!")

# При вызове say_hello() получим:
# Действия перед вызовом функции
# Привет!
# Действия после вызова функции
```

В этом примере функция `my_decorator` принимает другую функцию, определяет внутри себя новую функцию `wrapper`, которая вызывает исходную функцию, обрамляя её дополнительными действиями, и возвращает эту обёртку.

Важно понимать, что синтаксис `@my_decorator` — это лишь удобное сокращение для:

```python
def say_hello():
print("Привет!")

say_hello = my_decorator(say_hello)
```

Именно эта особенность делает декораторы таким мощным инструментом — мы буквально переопределяем функцию, заменяя её на декорированную версию.

**Python-разработчик с 8-летним опытом**

В начале карьеры я считал декораторы чем-то сложным и экзотическим. Всё изменилось, когда мне поручили создать API с авторизацией. Я писал код проверки токена в каждом методе, и это выглядело ужасно. Мой наставник показал, как решить эту проблему одним декоратором:

```python
def require_auth(func):
def wrapper(request, *args, **kwargs):
if not request.headers.get('Authorization'):
return {'error': 'Unauthorized'}, 401
return func(request, *args, **kwargs)
return wrapper

@require_auth
def get_user_data(request):
# Логика метода
return {'user': 'data'}
```

Это изменило моё понимание чистого кода. Теперь я мог добавить проверку авторизации к любому методу одной строкой. Декораторы из "сложной концепции" превратились в мой любимый инструмент рефакторинга.

## Синтаксис и механизм работы декораторов в Python

Механизм работы декораторов основан на концепции замыканий и функций высшего порядка. Замыкание — это функция, запоминающая окружение, в котором она была создана. Функция высшего порядка — это функция, которая принимает другие функции как аргументы или возвращает их как результат.

Полный синтаксис декоратора можно представить в нескольких вариациях:

| **Тип декоратора**      | **Синтаксис**                                | **Эквивалентный код**                |
| ----------------------- | -------------------------------------------- | ------------------------------------ |
| Базовый декоратор       | `@decorator<br>def func(): pass`             | `func = decorator(func)`             |
| Декоратор с аргументами | `@decorator(arg1, arg2)<br>def func(): pass` | `func = decorator(arg1, arg2)(func)` |
| Несколько декораторов   | `@dec1<br>@dec2<br>def func(): pass`         | `func = dec1(dec2(func))`            |
| Декорирование класса    | `@decorator<br>class MyClass: pass`          | `MyClass = decorator(MyClass)`       |

Рассмотрим более подробно, как работает механизм декорирования:

1. Интерпретатор Python встречает функцию, отмеченную декоратором `@decorator`
2. Функция определяется как обычно
3. Определенная функция передается декоратору как аргумент
4. Декоратор возвращает новую функцию (обертку)
5. Оригинальное имя функции присваивается этой новой обертке

Вот пример, демонстрирующий, как Python обрабатывает функцию с декоратором:

```python
def timing_decorator(func):
def wrapper(*args, **kwargs):
import time
start_time = time.time()
result = func(*args, **kwargs)
end_time = time.time()
print(f"Функция {func.__name__} выполнялась {end_time – start_time:.4f} секунд")
return result
return wrapper

@timing_decorator
def slow_function(delay):
import time
time.sleep(delay)
return "Функция выполнена"

# Вызов функции
slow_function(1) # Выведет: "Функция slow_function выполнялась 1.0005 секунд"
```

В этом примере `timing_decorator` принимает функцию `func`, создает функцию-обертку `wrapper`, которая измеряет время выполнения `func`, а затем возвращает `wrapper`.

Важно отметить, что декорированная функция теряет свои метаданные (имя, документацию, сигнатуру), заменяясь на метаданные обертки. Для решения этой проблемы используется декоратор `@functools.wraps` из стандартной библиотеки:

```python
import functools

def timing_decorator(func):
@functools.wraps(func) # Сохраняет метаданные оригинальной функции
def wrapper(*args, **kwargs):
import time
start_time = time.time()
result = func(*args, **kwargs)
end_time = time.time()
print(f"Функция {func.__name__} выполнялась {end_time – start_time:.4f} секунд")
return result
return wrapper
```

Такая структура позволяет сохранить исходные метаданные декорируемой функции, что особенно важно для интроспекции и документации кода. 🔍

## Базовые способы использования декораторов в коде

Декораторы могут решить множество практических задач, существенно улучшая читаемость и поддерживаемость кода. Рассмотрим наиболее распространенные способы их применения.

| **Тип использования**        | **Что решает**                                         | **Примеры в экосистеме Python**          |
| ---------------------------- | ------------------------------------------------------ | ---------------------------------------- |
| Логирование                  | Отслеживание вызовов функций, параметров и результатов | Собственные декораторы, `logging` модуль |
| Измерение производительности | Анализ времени выполнения функций                      | `timeit`, профилировщики                 |
| Кэширование                  | Сохранение результатов для идентичных входных данных   | `functools.lru_cache`, `memoization`     |
| Валидация аргументов         | Проверка входных данных перед выполнением функции      | `pydantic`, `schema` библиотеки          |
| Управление доступом          | Авторизация и аутентификация                           | Декораторы в Flask, Django, FastAPI      |

Рассмотрим несколько практичных примеров, которые вы можете адаптировать для своих проектов:

**1. Декоратор для ретрая функции при возникновении исключения**

```python
def retry(max_attempts=3, delay=1):
def decorator(func):
def wrapper(*args, **kwargs):
attempts = 0
while attempts < max_attempts:
try:
return func(*args, **kwargs)
except Exception as e:
attempts += 1
if attempts == max_attempts:
raise e
import time
time.sleep(delay)
return None
return wrapper
return decorator

@retry(max_attempts=5, delay=2)
def unstable_network_call(url):
# Имитация ненадежного сетевого вызова
import random
if random.random() < 0.7: # 70% шанс ошибки
raise ConnectionError("Сетевая ошибка")
return "Данные получены"
```

**2. Декоратор для кэширования результатов функции**

```python
def simple_cache(func):
cache = {}
def wrapper(*args, **kwargs):
# Создаем ключ на основе аргументов
key = str(args) + str(kwargs)
if key not in cache:
cache[key] = func(*args, **kwargs)
return cache[key]
return wrapper

@simple_cache
def fibonacci(n):
if n <= 1:
return n
return fibonacci(n-1) + fibonacci(n-2)

# Теперь вычисление fibonacci(100) будет очень быстрым
# благодаря кэшированию промежуточных результатов
```

**3. Декоратор для добавления поддержки контекстного менеджера**

```python
def contextmanager(func):
def wrapper(*args, **kwargs):
generator = func(*args, **kwargs)
class ContextManager:
def __enter__(self):
return next(generator)

def __exit__(self, exc_type, exc_val, exc_tb):
try:
next(generator)
except StopIteration:
pass
return ContextManager()
return wrapper

@contextmanager
def file_opener(filename, mode='r'):
f = open(filename, mode)
try:
yield f
finally:
f.close()

# Использование
with file_opener('example.txt') as f:
content = f.read()
```

Эти примеры демонстрируют, как декораторы позволяют отделить сквозную функциональность (логирование, кэширование, обработку ошибок) от основной бизнес-логики. Такой подход соответствует принципу единственной ответственности и делает код более модульным и тестируемым. 🧩

## Продвинутые техники применения декораторов Python

Освоив базовые декораторы, можно переходить к более сложным техникам, которые раскрывают всю мощь этого инструмента. Продвинутые техники включают работу с классами-декораторами, декораторы с параметрами и композицию декораторов.

**Классы как декораторы**

Python позволяет использовать не только функции, но и классы в качестве декораторов. Для этого класс должен реализовать метод `__call__`, который вызывается, когда экземпляр класса используется как функция.

```python
class CountCalls:
def __init__(self, func):
self.func = func
self.count = 0

def __call__(self, *args, **kwargs):
self.count += 1
print(f"Функция {self.func.__name__} вызвана {self.count} раз")
return self.func(*args, **kwargs)

@CountCalls
def hello(name):
return f"Привет, {name}!"

hello("Alice") # Функция hello вызвана 1 раз
hello("Bob") # Функция hello вызвана 2 раз
```

Классы-декораторы удобны, когда нужно хранить состояние между вызовами декорированной функции или когда логика декоратора становится сложной.

**Декораторы с сохранением сигнатуры функции**

Декораторы могут "маскировать" оригинальную функцию, что приводит к проблемам с интроспекцией и документацией. Для решения этой проблемы используется встроенный декоратор `functools.wraps`:

```python
import functools

def debug(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
print(f"Вызов {func.__name__} с аргументами: {args}, {kwargs}")
result = func(*args, **kwargs)
print(f"Результат: {result}")
return result
return wrapper

@debug
def multiply(a, b):
"""Умножает два числа и возвращает результат."""
return a * b

# Теперь help(multiply) покажет оригинальную документацию функции multiply,
# а не документацию обертки wrapper
```

**Композиция декораторов**

Декораторы можно комбинировать, применяя несколько к одной функции. Они применяются в порядке снизу вверх:

```python
def bold(func):
def wrapper(*args, **kwargs):
return "<b>" + func(*args, **kwargs) + "</b>"
return wrapper

def italic(func):
def wrapper(*args, **kwargs):
return "<i>" + func(*args, **kwargs) + "</i>"
return wrapper

@bold
@italic
def format_text(text):
return text

print(format_text("Python")) # Выводит: <b><i>Python</i></b>
```

**Lead Backend Developer**

Мой проект страдал от проблемы N+1 запросов — наши API делали слишком много обращений к базе данных. Оптимизация каждого метода вручную требовала бы огромных усилий.

Я создала два декоратора: один для профилирования SQL-запросов и другой для автоматического джойна связанных данных:

```python
@profile_queries
@prefetch_related('author', 'comments')
def get_articles(self, request):
articles = Article.objects.all()
return ArticleSerializer(articles, many=True).data
```

После применения этих декораторов к ключевым эндпоинтам, количество запросов сократилось на 70%, а отзывчивость API выросла в 3 раза. Особенно впечатляло, что решение было неинвазивным — мы не переписывали основную логику API, а просто добавили декораторы.

Теперь декораторы — первый инструмент, к которому я обращаюсь, когда нужно применить сквозную функциональность без загрязнения бизнес-логики.

**Параметризованные декораторы**

Создание декораторов, принимающих параметры, требует добавления дополнительного уровня вложенности:

```python
def repeat(times=1):
def decorator(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
result = None
for _ in range(times):
result = func(*args, **kwargs)
return result
return wrapper
return decorator

@repeat(times=3)
def greet(name):
print(f"Привет, {name}!")

greet("Мир") # Выведет "Привет, Мир!" три раза
```

Здесь `repeat` — это не сам декоратор, а фабрика декораторов, создающая декоратор с заданными параметрами.

**Декораторы методов с доступом к экземпляру класса**

При декорировании методов класса, первым аргументом метода обычно является `self` — экземпляр класса. Декораторы методов могут использовать это для доступа к состоянию объекта:

```python
def check_auth(method):
@functools.wraps(method)
def wrapper(self, *args, **kwargs):
if not self.is_authenticated:
raise PermissionError("Требуется аутентификация")
return method(self, *args, **kwargs)
return wrapper

class User:
def __init__(self, name, is_authenticated=False):
self.name = name
self.is_authenticated = is_authenticated

@check_auth
def view_profile(self):
return f"Профиль пользователя: {self.name}"

user = User("Alice", is_authenticated=False)
try:
user.view_profile() # Вызовет PermissionError
except PermissionError as e:
print(str(e))
```

Эти продвинутые техники демонстрируют гибкость декораторов в Python и их способность решать сложные архитектурные задачи. Умелое применение декораторов может значительно улучшить структуру кода и упростить его поддержку. 🚀

## Практические задачи и решения с использованием декораторов

Лучший способ освоить декораторы — применить их к решению реальных задач. Рассмотрим несколько практических проблем и их элегантные решения с использованием декораторов.

**Задача 1: Ограничение частоты вызовов функции (rate limiting)**

Ограничение частоты вызовов API или функций — распространенная задача для защиты от DoS-атак или перегрузки системы.

```python
import time
import functools

def rate_limit(max_calls, period=60):
"""Ограничивает функцию до max_calls вызовов в течение period секунд."""
calls = []

def decorator(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
current_time = time.time()
# Удаляем устаревшие записи о вызовах
while calls and current_time – calls[0] > period:
calls.pop(0)

if len(calls) >= max_calls:
raise Exception(f"Превышен лимит вызовов: {max_calls} за {period} секунд")

calls.append(current_time)
return func(*args, **kwargs)
return wrapper
return decorator

@rate_limit(max_calls=3, period=10)
def fetch_data():
print("Данные получены")

# Тестирование
for _ in range(4):
try:
fetch_data()
time.sleep(1) # Небольшая пауза между вызовами
except Exception as e:
print(f"Ошибка: {e}")
```

**Задача 2: Автоматическая сериализация/десериализация данных**

При работе с API часто требуется преобразование данных между форматами JSON, XML и Python-объектами.

```python
import json
import functools

def json_response(func):
"""Автоматически сериализует результат функции в JSON."""
@functools.wraps(func)
def wrapper(*args, **kwargs):
result = func(*args, **kwargs)
return json.dumps(result)
return wrapper

def parse_json_request(parameter_name):
"""Десериализует JSON из указанного параметра."""
def decorator(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
if parameter_name in kwargs:
kwargs[parameter_name] = json.loads(kwargs[parameter_name])
return func(*args, **kwargs)
return wrapper
return decorator

@json_response
@parse_json_request('data')
def process_data(data):
data['processed'] = True
return data

# Пример использования
result = process_data(data='{"name": "Test", "value": 42}')
print(result) # Выводит: {"name": "Test", "value": 42, "processed": true}
```

**Задача 3: Валидация входных параметров функций**

Проверка типов и значений аргументов функций — частая задача для обеспечения надежности кода.

```python
def validate_types(**expected_types):
"""Проверяет соответствие типов аргументов функции ожидаемым типам."""
def decorator(func):
@functools.wraps(func)
def wrapper(*args, **kwargs):
# Получаем словарь аргументов функции
func_args = func.__code__.co_varnames[:func.__code__.co_argcount]
all_args = dict(zip(func_args, args))
all_args.update(kwargs)

# Проверяем типы
for arg_name, expected_type in expected_types.items():
if arg_name in all_args:
actual_value = all_args[arg_name]
if not isinstance(actual_value, expected_type):
raise TypeError(
f"Аргумент '{arg_name}' должен быть типа {expected_type.__name__}, "
f"получен {type(actual_value).__name__}"
)
return func(*args, **kwargs)
return wrapper
return decorator

@validate_types(name=str, age=int)
def register_user(name, age, email=None):
return f"Пользователь {name}, возраст {age} зарегистрирован"

# Корректный вызов
print(register_user("Alice", 30))

# Вызов с некорректными типами
try:
print(register_user("Bob", "двадцать пять"))
except TypeError as e:
print(f"Ошибка: {e}")
```

**Задача 4: Асинхронная обработка и управление потоками**

Декораторы могут помочь в работе с асинхронными операциями и многопоточностью.

```python
import threading
import functools

def run_async(func):
"""Запускает функцию в отдельном потоке."""
@functools.wraps(func)
def wrapper(*args, **kwargs):
thread = threading.Thread(target=func, args=args, kwargs=kwargs)
thread.daemon = True
thread.start()
return thread
return wrapper

@run_async
def long_running_task(name, duration):
import time
print(f"Задача '{name}' запущена")
time.sleep(duration)
print(f"Задача '{name}' завершена после {duration} секунд")

# Запускаем несколько задач асинхронно
thread1 = long_running_task("Task 1", 2)
thread2 = long_running_task("Task 2", 1)

# Основной поток продолжает работу
print("Основной поток продолжает выполнение")

# Ждем завершения всех задач
thread1.join()
thread2.join()
```

Эти примеры демонстрируют, как декораторы позволяют элегантно решать сложные задачи, отделяя инфраструктурный код от бизнес-логики. Использование декораторов делает код более чистым, модульным и легко расширяемым. 🛠️

Каждый из приведенных примеров можно адаптировать под конкретные нужды проекта. Создание собственных декораторов для решения специфических задач — это навык, который отличает опытных Python-разработчиков и позволяет писать более элегантный и поддерживаемый код.

> Декораторы в Python — это не просто синтаксический сахар, а фундаментальный инструмент, меняющий подход к структурированию кода. Они позволяют реализовать принцип "Разделяй и властвуй", отделяя инфраструктурную логику от бизнес-логики. Начните с простых примеров из этой статьи, экспериментируйте с ними в своих проектах, и вскоре вы обнаружите, что декораторы становятся неотъемлемой частью вашего инструментария, помогая создавать более чистый, модульный и выразительный код. Помните: лучший способ освоить декораторы — это применять их для решения реальных проблем.
