Добавляем сторонние линтеры для flake8. После того как у нас установлен плагин `Mason` при помощи lazy, мы заходим в командный режим vim и вводим команду `Mason` и устанавливаем утилиты (форматеры и прочее):
- debugpy
- flake8
- isort
- lua-language-server
- luaformatter
- pyright
-  shellcheck
- shfmt

#### Расширяем flake8 дополнительными линтерами
1. переходим в каталог куда Mason установил flake8 и **копируем сюда** файл `requirements_flake8.txt`,  который лежит в корне проекта (на всякий случай дублирую содержание данного файла в конце этой заметки).
	`cd ~/.local/share/nvim/mason/packages/flake8`
2. активируем виртуальное окружение
    `source venv/bin/activate`
3. устанавливаем зависимости
    `pip install -r requirements_flake8.txt`




##### Содержимое файла requirements_flake8.txt
flake8-commas
flake8-builtins
flake8-variables-names
flake8-import-order
flake8-functions
flake8-class-attributes-order
flake8-expression-complexity
flake8-cognitive-complexity
flake8-annotations
flake8-docstrings