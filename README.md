# BS4 Parser PEP
Содержит четыре парсера:
1. **whats_new** собирает ссылки на статьи о нововведениях в Python    
2. **latest_versions** cобирает информацию о статусах версий Python    
3. **download** скачивает архив с актуальной документацией в папку **downloads/**    
4. **pep** собирает информацию о количестве статусов PEP 

## Техно-стек
* python 3.7.9
* beautiful soup 4.9.3

## Запуск проекта
1. Клонировать репозиторий
```
git clone git@github.com:avnosov3/Bs4_parser_pep.git
```
2. Перейти в папку с проектом и создать виртуальное окружение
```
cd Bs4_parser_pep
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Активировать виртуальное окружение
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Установить зависимости из файла requirements.txt
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Запустить парсер
```
cd src
python main.py <НАЗВАНИЕ ПАРСЕРА>(whats_new, latest_versions, download, pep)
```
6. Вывести информации в терминал
```
python main.py <НАЗВАНИЕ ПАРСЕРА> --output pretty
```
7. Cохранить информацию в папке result
```
python main.py <НАЗВАНИЕ ПАРСЕРА> --output file
```

## Автор
[Артём Носов](https://github.com/avnosov3)
