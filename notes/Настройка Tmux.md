1. Установка: `sudo apt install tmux`
2. Необходимо создать файл `.tmux.conf` в рабочей директории пользователя (об этом говорит знак тильды в пути к файлу`~/.tmux.conf`). Это можно сделать командой `touch .tmux.conf`.
4.  В созданный файл нужно вставить строки:
```
# Заменяем основной префикс ctrl+b на ctrl+g
# set -g prefix C-g

# Поддержка мыши
set -g mouse on

# Устанавливаем максимальное количество записей, хранящиеся в истории
set -g history-limit 15000

# Перемещение между окнами как в vim
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# Ресайз окон на 10 едениц по зажатию заглавных клавиш H J K L
bind -r H resize-pane -L 10
bind -r J resize-pane -D 10
bind -r K resize-pane -U 10
bind -r L resize-pane -R 10
```
В этом репозитории уже  присутствует данный файл так что его можно просто перенести в рабочую директорию пользователя.