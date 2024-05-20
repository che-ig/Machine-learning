#ranger
**Проблема:**  При наведении курсора на файл с расширением djvuf происходит полная загрузка процессора и памяти - происходит полное зависание системы.

**Решение:**  Необходимо внести правку в файл .config/ranger/scope.sh.  В данном файле в обработчике события `handle_image` добавить код
```bash 
image/vnd.djvu)
	ddjvu -format=tiff -quality=90 -page=1 -size="${DEFAULT_SIZE}" \
	- "${IMAGE_CACHE_PATH}" < "${FILE_PATH}" \
	&& exit 6 || exit 1;;

