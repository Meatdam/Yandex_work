# Тестовое Yandex Plus

## Блок 1. Сегментация
### Задание 1.
Вам необходимо построить дерево сегмента по следующим параметрам:<br>
- пользователи с активной подпиской
- смотрели сериал «Конец света», одну серию и более на Кинопоиске или смотрели
фильм «Интерстеллар» более 10 минут на Кинопоиске
- не слушали подкаст «В предыдущих сериях» на Яндекс Музыке
### Задание 2.
Проверьте собранный сегмент на логику и дополните параметрами, которые мы упустили (вводных по доступности параметров нет, напишите все, что посчитаете нужным).<br>
Если считаете, что этих параметров для отправки достаточно, то напишите об этом.<br>
_____
## Блок 2. Верстка
### Задание 1.
Внесите следующие изменения в верстку письма
- замените картинки на те, которые находятся в архиве 2
- замените текст (будет ниже)
- расставьте неразрывные пробелы, ссылки (где считаете нужным по тексту), ютм-метки
- символ рубля, длинное тире и кавычки необходимо вставить html-тегами<br>
Текст:<br>
прехедер: И новые вкусные задания текст на баннере: Неделя гастрономии и
новые задания заголовок: Всё вкусное с Плюсом текст 1 блок: На этой неделе предлагаем стать настоящими гастроэнтузиастами!<br>
Заказывайте новую посуду на Маркете, слушайте подкасты на Музыке, пока готовите, и отправляйтесь на ужин на такси в тарифах Комфорт и выше текст 2 блок:<br>
Пользуйтесь сервисами как обычно и выполняйте еженедельные задания. А мы – подарим один из подарков: баллы Плюса, опции и скидки до 1000 ₽ в сервисах Яндекса кнопка:<br>
Открыть задания дисклеймер: Срок проведения акции с 02.11.2022 до 31.12.2022 г. Подробности (ссылка на https://yandex.ru/legal/plus_activity) об организаторе акции,<br>
правилах ее проведения, количестве подарков, сроках, месте и порядке их получения. Условия программы лояльности «Яндекс Плюс Кешбэк» (ссылка на https://yandex.ru/legal/plus_loyalty).
### Задание 2 (дополнительное).
К уже готовому письму из задания 1 добавьте подстановку данных о баллах пользователя (через текстовый шаблонизатор Jinja) Данные о баллах приходят в следующем JSON формате:
```
{
"event": "mission_complete",
"id": 123,
"points": 150
}
```
Вам необходимо сделать подстановку баллов из параметра "points" по следующей логике:
- если баллов равно/больше 100, то показываем текст: У вас Х баллов
- если баллов меньше 100, то текст не отображаем
Добавить строку с подстановкой данных можно в любую часть письма, ограничений нет
______
## Блок 3 (дополнительное).
### Работа с SQL.
Есть две таблицы:
1. orders (order_id, promocode_id) - заказы
2. promocodes (promocode_id, name, discount) – промокоды
Задачи:
1. Вывести все промокоды с скидкой более 30%
2. Собрать селект, показывающий долю заказов с промокодами
3. Вывести список промокодов (название) и число его использований, отсотированный по популярности.
_____
## Запуск проекта 
1. Клонировать проект репозитория командой 
```
git@github.com:Meatdam/Yandex_work.git
```
2. Необходимо установить виртуальное окружение себе на ПК
```
python3 -m venv venv для MacOs и linux систем
python -m venv venv для windows
```
3. Активировать виртуальное окружение
```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```
4. Установить пакеты с виртуального окрежения
```
pip install -r requirements.txt для всех систем
```
5. Выполнить команду для записи готового файла через jinja2 в файл yandex_result.html который будет находится в корне проекта.
```
 python score_message.py   
```
Команды SQL запросов лежат в корне проекта commands_SQL<br>
Сегментация лежит в корне проекта block_diagram.pdf<br>
файл score_message.py - скрипт для вывода баллов в шаблон.

