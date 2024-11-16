Установка в Debian, Kali Linux, Linux Mint, Ubuntu и их производные:

`sudo apt install tigervnc-standalone-server tigervnc-viewer tigervnc-xorg-extension`

### Настройка сервера TigerVNC  

Для работы сервера TigerVNC требуется файл **~/.vnc/xstartup**. Если этот файл не существует, то TigerVNC пытается его создать. В моих тестах на разных дистрибутивах этот файл обычно приходилось создавать вручную.

Содержимое файла **~/.vnc/xstartup** зависит от вашего окружения рабочего стола! То есть для Cinnamon, XFCE, GNOME и т. д. файлы будут разные!

Дело в том, что TigerVNC не используют текущую X сессию, а создаёт новую. Благодаря такому подходу можно, например, для пользователей выполнивших вход перед компьютером и пользователей, подключившихся по VNC, запускать различные окружения рабочего стола (при условии, что они установлены). Настройка запуска сеанса рабочего стола для VNC выполняется в файле **~/.vnc/xstartup**.

Общая минимальная структура файла **~/.vnc/xstartup** следующая для **<u>linux Mint cinnamon**</u>:

```
#!/bin/sh
# Start up the standard system desktop
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
/usr/bin/cinnamon-session
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
x-window-manager &
```

**Как создать пароль для TigerVNC сервера**

Используйте утилиту:

`vncpasswd`

После неё можно указать файл, в который должен быть сохранён пароль, в противном случае пароль будет сохранён в файл по умолчанию, то есть в **$HOME/.vnc/passwd**.

После ввода пароля программа спросит:
`Would you like to enter a view-only password (y/n)?`

То есть хотите ли вы создать пароль для режима «только просмотр» - если хотите, то введите «**y**», если не хотите, то введите «**n**».

**Как настроить автоматический запуск сервера TigerVNC**

Создайте файл **/etc/systemd/system/vncserver@.service**:

`sudo gedit /etc/systemd/system/vncserver@.service`

Скопируйте в этот файл

```
[Unit]
Description=Remote desktop service (VNC)
After=network.target
[Service]
Type=forking
User=mial
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -localhost no :%i
ExecStop=/usr/bin/vncserver -kill :%i
[Install]
WantedBy=multi-user.target
```

> [!attention] Важно!
> Обратите внимание на строку **User=mial** — впишите в неё имя вашего пользователя вместо **mial**.

Сохраните и закройте этот файл.

Теперь перезагрузите конфигурацию менеджера [systemctl](https://hackware.ru/?p=5460) для чтения свежесозданного файла юнита следующим образом:

`sudo systemctl daemon-reload`

Для запуска службы VNC выполните команду:

`sudo systemctl start vncserver@1`

Обратите внимание, что вместо **1** вы можете указывать любой номер дисплея.

Для проверки статуса службы:

`systemctl status vncserver@1`

Для добавления службы в автозагрузку:

`sudo systemctl enable vncserver@1`

Для остановки службы:

`sudo systemctl stop vncserver@1`

Для удаления службы из автозагрузки:

`sudo systemctl disable vncserver@1`

Источники:
1. https://zalinux.ru/?p=3905
2. https://bytexd.com/how-to-install-configure-vnc-server-on-ubuntu/