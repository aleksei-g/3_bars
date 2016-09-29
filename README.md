# 3_bars

#Бары

Скрипт анализирует загруженную из json-файла информацию о барах и выводит самый маленький, самый большой бар, а так же, в зависимости от переданных ему gps-координат, самый ближайший бар.
Список баров в json-формате можно скачать по [ссылке] (http://data.mos.ru/opendata/7710881420-bary).

**Параметры скрипта:**
* **-f ФАЙЛ (--file ФАЙЛ):** обязательный параметр, путь до файла json.
* **-s (--smallest):** необязательный параметр, вывести самый маленький бар.
* **-b (--biggest):** необязательный параметр, вывести самый большой бар.
* **-с ШИРОТА ДОЛГОТА (--coordinates ШИРОТА ДОЛГОТА):** необязательный параметр, вывести самый большой бар.

**Пример использования:**
```
python bars.py -f bar.json -s -b -c 37.621099 55.753525
```
Данная команда передает в скрипт файл ***bar.json*** и координаты ***37.621099 55.753525***. Скрипт на основе полученной информации выведет самый маленький бар, самый большой бар, а так же ближайший бар.
