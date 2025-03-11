### Установка NVM

`nvm` управляет версиями node.js и npm. Он устанавливается для конкретного пользователя и может быть вызван отдельно для каждой оболочки. `nvm` работает с любой POSIX-совместимой оболочкой (sh, dash, ksh, zsh, bash), в том числе на платформах: unix, macOS и windows WSL.  
  
`nvm` можно установить с помощью команд wget:  

```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```
  
Скрипт `install.sh` клонирует репозиторий nvm в `~/.nvm` и пытается добавить исходные строки из приведенного ниже фрагмента в нужный файл профиля (`~/.bash_profile`, `~/.zshrc`, `~/.profile` или `~/.bashrc`).  

```
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```
  
В `~/.bash_profile` мы видим, что строки добавлены:  

```
export NVM_DIR="/Users/fuje/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

### Использование NVM

Итак, мы установили nvm. Теперь используем данную команду для установки последней версии node.js:  

```
$ nvm install node
```

Источники:
https://habr.com/ru/companies/timeweb/articles/541452/