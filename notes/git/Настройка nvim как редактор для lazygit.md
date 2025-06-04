Т.к мы не устанавливаем nvim, а используем портативное решение nvim-linux-x86_64.appimage
то нам необходимо сделать симлинк nvim для того, чтобы lazgit воспринял его.
ln -sfvi /home/che/nvim-linux-x86_64.appimage /usr/bin/nvim
