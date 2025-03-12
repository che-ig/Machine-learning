1. Переходим на [сайт](https://www.nerdfonts.com/font-downloads) и скачиваем понравившийся шрифт (JetBrainsMono Nerd Font)  
2. распаковать архив в каталог (создать если такого каталога нет)
`~/.local/share/fonts/`
3. В настройках терминала выбираем скаченный шрифт (см. рис. ниже)
	![](../images/neovim_font.png)
	4.  Установить `Node.js` смотри [заметку](<../linux/Управление версиями Node.js и NPM с помощью NVM.md>)
	5. Установить`lua` смотри [заметку](<../lua/Установка lua в linux.md>)
	6. Установить `cmake` (потребуется при установке плагинов через Masson)
	```bash		
	sudo apt-get -y install cmake
	```
	7. Установить `ripgrep` - утилита для поиска по строкам и `fd-find`  - утилита для поиска файлов - замена стандартного find (обе утилиты понадобятся для плагина Telescope)
	```bash
	sudo apt install ripgrep
	```
	```bash
	sudo apt install fd-find
	ln -s $(which fdfind) ~/.local/bin/fd
	```