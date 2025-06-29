Команда **find** – это невероятно мощный инструмент, позволяющий искать файлы не только по названию, но и по:

- Дате добавления.
- Содержимому.
- Регулярным выражениям.

Данная команда будет очень полезна системным администраторам для:

- Управления дисковым пространством.
- Бэкапа.
- Различных операций с файлами.

Команда **find** в Linux производит поиск файлов и папок на основе заданных вами критериев и позволяет выполнять действия с результатами поиска.

Синтаксис команды **find**:

```
$ find directory-to-search criteria action
```

Где:

- directory-to-search (каталог поиска) – это отправной каталог, с которой find начинает поиск файлов по всем подкаталогам, которые находятся внутри. Если не указать путь, тогда поиск начнется в текущем каталоге;
- criteria (критерий) – критерий, по которым нужно искать файлы;
- action (действие) – что делать с каждым найденным файлом, соответствующим критериям.

### Поиск по имени

Следующая команда ищет файл s.txt в текущем каталоге:

```
$ find . -name "s.txt"
./s.txt
```

Где:

- . (точка) – файл относится к нынешнему каталогу
- **-name** – критерии по которым осуществляется поиск. В данном случае поиск по названию файла.

В данном случае критерий **-name** учитывает только символы нижнего регистра и файл S.txt не появиться в результатах поиска. Чтобы убрать чувствительность к регистру необходимо использовать **–iname**.

```
$ find . -iname "s.txt"
./s.txt
./S.txt
```

Для поиска всех изображений c расширением .png нужно использовать шаблон подстановки \*.png:

```
$ find . -name "*.png"
./babutafb.png
./babutafacebook.png
./Moodle2.png
./moodle.png
./moodle/moodle1.png
./genxfacebook.png
```

Можно использовать название каталога для поиска. Например, чтобы с помощью команды **find** найти все **png** изображения в каталоге **home**:

```
$ find /home -name "*.png"
find: `/home/babuta/.ssh': Permission denied
/home/vagrant/Moodle2.png
/home/vagrant/moodle.png
/home/tisha/hello.png
find: `/home/tisha/testfiles': Permission denied
find: `/home/tisha/data': Permission denied
/home/tisha/water.png
find: `/home/tisha/.cache': Permission denied
```

Если выдает слишком много ошибок в отказе разрешения, тогда можно добавить в конец команды – **2> /dev/null**. Таким образом сообщения об ошибках будут перенаправляться по пути **dev/null**, что обеспечит более чистую выдачу.

```
find /home -name "*.jpg" 2>/dev/null
/home/vagrant/Moodle2.jpg
/home/vagrant/moodle.jpg
/home/tisha/hello.jpg
/home/tisha/water.jpg
```

### Ограничение глубины поиска

Поиска файлов по имени в Linux только в этой папке:

```
find . -maxdepth 1 -name "*.php"
```

### Инвертирование шаблона

Найти файлы, которые не соответствуют шаблону:

```
find . -not -name "test*"
```

### Несколько критериев

Поиск командой find в Linux по нескольким критериям, с оператором исключения:

```
find . -name "test" -not -name "*.php"
```

### Исключение папки из поиска

Если нет необходимости производить поиск в той или иной папке, можно исключить её с помощью опций **path, prune** и логического «или».

```
find . -path "./directory_exclude/*" -prune -o -name SEARCH_NAME
```

### Поиск по типу файла

Критерий **-type** позволяет искать файлы по типу, которые бывают следующих видов:

- f – простые файлы;
- d – каталоги;
- l – символические ссылки;
- b – блочные устройства (dev);
- c – символьные устройства (dev);
- p – именованные каналы;
- s – сокеты;

Например, указав критерий **-type d** будут перечислены только каталоги:

```
$ find . -type d
.
./.ssh
./.cache
./moodle
```

### Несколько каталогов

Искать в двух каталогах одновременно:

`find ./test ./test2 -type f -name "*.c"`

### Поиск по размеру файла

Допустим, что вам необходимо найти все большие файлы. Для таких ситуаций подойдет критерий **-size**.

- "+" — Поиск файлов больше заданного размера
- "-" — Поиск файлов меньше заданного размера
- Отсутствие знака означает, что размер файлов в поиске должен полностью совпадать.

В данном случае поиск выведет все файлы более 1 Гб (**+1G**).

```
$ find . -size +1G
./Microsoft_Office_16.29.19090802_Installer.pkg
./android-studio-ide-183.5692245-mac.dmg
```

#### Единицы измерения файлов:

- c — Байт
- k — Кбайт
- M — Мбайт
- G — Гбайт

### Поиск пустых файлов и каталогов

Критерий **-empty** позволяет найти пустые файлы и каталоги.

```
$ find . -empty
./.cloud-locale-test.skip
./datafiles
./b.txt
...
./.cache/motd.legal-displayed
```

### Поиск времени изменения

Критерий **-cmin** позволяет искать файлы и каталоги по времени изменения (в минутах). Для поиска всех файлов, измененных за последний час (менее 60 мин), нужно использовать **-60**:

```
$ find . -cmin -60
.
./a.txt
./datafiles
```

Таким образом можно найти все файлы в текущем каталоге, которые были созданы или изменены в течение часа (менее 60 минут).

Для поиска файлов, которые наоборот были изменены в любое время кроме последнего часа необходимо использовать **+60**.

```
$ find . -cmin +60
```

### Поиск по времени доступа (последнего чтения)

Критерий **-atime** позволяет искать файлы по времени последнего доступа.

```
$ find . -atime +180
```

Таким образом можно найти файлы, к которым не обращались (читали) последние полгода (180 дней).

### Поиск по времени изменения файла / каталога

Критерий **-mtime** позволяет искать файлы по времени (в днях) последнего изменения.
Если нужно вывести файлы, которые открывали за последние 30 дней.

```
$ find . -mtime 30
```

Поиск можно проводить в промежутке дат. Например, чтобы найти файлы, изменённые в промежутке от 30 до 60 дней, подойдёт такой запрос:

```
$ sudo find / -mtime +30 -mtime -60
```

> [!attention] Важно
> Обратите внимание на символы перед числом дней. + означает, что мы ищем файлы, которые редактировались большее количество дней назад, чем мы указали, а символ - указывает на то, что мы ищем файлы, которые редактировались менее указанного количества дней назад.
>
> В нашем случае это файлы, которые редактировались 30 или более дней назад и 60 или менее дней назад.

### Поиск по имени пользователя

Опция **–user username** дает возможность поиска всех файлов и каталогов, принадлежащих конкретному пользователю:

```
$ find /home -user tisha 2>/dev/null
```

Таким образом можно найти все файлы пользователя tisha в каталоге **home**, а **2>/dev/null** сделает выдачу чистой без ошибок в отказе доступа.

### Поиск по набору разрешений

Критерий **-perm** – ищет файлы по определенному набору разрешений.

```
$ find /home -perm 777
```

Поиск файлов с разрешениями **777**.

Поиск файлов доступных владельцу только для чтения только в каталоге **/etc**:

`find /etc -maxdepth 1 -perm /u=r`

### Операторы

Для объединения нескольких критериев в одну команду поиска можно применять операторы:

- -and
- -or / -o
- -not

Например, чтобы найти файлы размером более 1 Гбайта пользователя tisha необходимо ввести следующую команду:

```
$ find /home  -user tisha  -and  -size +1G  2>/dev/null
```

Если файлы могут принадлежать не только пользователю tisha, но и пользователю pokeristo, а также быть размером более 1 Гбайта.

```
$ find /home \( -user pokeristo -or -user tisha \)  -and  -size +1G  2>/dev/null
```

Перед скобками нужно поставить обратный слеш "\\".

### Действия

К команде **find** можно добавить действия, которые будут произведены с результатами поиска.

- -delete — Удаляет соответствующие результатам поиска файлы
- -ls — Вывод более подробных результатов поиска с:
  - Размерами файлов.
  - Количеством inode.
- -print Стоит по умолчанию, если не указать другое действие. Показывает полный путь к найденным файлам.
- -exec Выполняет указанную команду в каждой строке результатов поиска.

#### -delete

Полезен, когда необходимо найти и удалить все пустые файлы, например:

```
$ find . -empty -delete
```

Перед удалением лучше лишний раз себя подстраховать. Для этого можно запустить команду с действием по умолчанию **-print**.

#### -exec:

Данное действие является особенным и позволяет выполнить команду по вашему усмотрению в результатах поиска.

```
-exec command {} \;
или
-exec command {} +
```

Где:

- command – это команда, которую вы желаете выполнить для результатов поиска. Например:
  - rm
  - mv
  - cp
- {} – является результатами поиска.
- \\; — Команда заканчивается точкой с запятой после обратного слеша.

С помощью **–exec** можно написать альтернативу команде **–delete** и применить ее к результатам поиска:

```
$ find . -empty -exec rm {} \;
```

Ограничиваем поиск конкретной директорией + все условия поиска заключаем в скобки для корректной работы exec

```
find ./pandas_study/ -maxdepth 1 \( -name '*.html' -o -name  '*.xls' -o -name '*.h5' -o -name '*.json' -o -name '*.csv' \) -exec ls -l {} +
```

Другой пример использования действия **-exec**:

```
$ find . -name "*.jpg" -exec cp {} /backups/fotos \;
```

Таким образом можно скопировать все .jpg изображения в каталог backups/fotos

### Использование команды xargs

Многие пользователи Linux сталкиваются с необходимостью перенаправления ввода-вывода довольно часто. Но команда exec с цепочкой символов `{} +` кажется им слишком сложной.

И тут на помощь приходит xargs. Нужно просто перенаправить вывод команды find в [команду xargs](https://linuxhandbook.com/xargs-command/) через конвейер.

```
find . -type f -name "*.txt" | xargs ls -l
```

### Сочетание команд find и grep

Теперь вы умеете совмещать команду find с xargs и exec, и пора перейти на следующий уровень — объединить find и grep.

Для разработчиков комбинация команд find и grep — одна из самых распространённых и вместе с тем самых полезных.

Команда find находит файлы с именем, соответствующим шаблону, а затем команда grep выполняет поиск по их содержимому.

Например, вам нужно найти все файлы .txt, в которых есть имя «Alice». Объединить команды find и grep можно так:

```
find . -type f -name "*.txt" -exec grep -i alice {} +
```

А можно с помощью xargs:

```
find . -type f -name "*.txt" | xargs grep -i alice
```

Источники:

1. https://habr.com/ru/companies/alexhost/articles/525394/
2. https://habr.com/ru/companies/first/articles/593669/
