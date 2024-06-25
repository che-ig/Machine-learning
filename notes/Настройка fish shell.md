1. Выполнить команды с официального сайта (https://github.com/fish-shell/fish-shell/)
```
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt update
sudo apt install fish
```
2. Установить менеджер для установки плагинов с оф. сайта (https://github.com/oh-my-fish/oh-my-fish)
`curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish`
3.  Установить нужную тему можно при  помощи команды
 `omf install theme_name` имена тем представлены в репозитории.
4.  Если установлено несколько тем, то можно выбрать интересующую при помощи команды `omf theme theme_name`
5. Если fish не видит nvim, который был установлен как flatpak пакет, то необходимо добавить алиас `alias nvim='flatpak run io.neovim.nvim`
в файл `~/.config/fish/config.fish`