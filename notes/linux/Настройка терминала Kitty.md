1. `curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin` Бинарные файлы будут установлены в `~/.local/kitty.app`
2.  Для того чтобы kitty можно было вызывать как из терминала так и из меню приложений, необходимо выполнить команды:

```bash
# Create symbolic links to add kitty and kitten to PATH (assuming ~/.local/bin is in
# your system-wide PATH)
ln -sf ~/.local/kitty.app/bin/kitty ~/.local/kitty.app/bin/kitten ~/.local/bin/
# Place the kitty.desktop file somewhere it can be found by the OS
cp ~/.local/kitty.app/share/applications/kitty.desktop ~/.local/share/applications/
	```
3. Для того чтобы осуществлять поиск без учета регистра необходимо выполнить команду: 
```bash
echo 'set completion-ignore-case On' >> ~/.inputrc
````



Источники:
- https://sw.kovidgoyal.net/kitty/binary/
- https://askubuntu.com/questions/87061/can-i-make-tab-auto-completion-case-insensitive-in-bash