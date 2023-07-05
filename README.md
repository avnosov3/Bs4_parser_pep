# BS4 Parser PEP

<details><summary>Russian language</summary>  
  
Содержит четыре парсера:
1. **whats-new** собирает ссылки на статьи о нововведениях в Python    
2. **latest-versions** cобирает информацию о статусах версий Python    
3. **download** скачивает архив с актуальной документацией в папку **downloads/**    
4. **pep** собирает информацию о количестве статусов PEP 

## Техно-стек
* python 3.7.9
* beautiful soup 4.9.3

## Запуск проекта
1. Клонировать репозиторий
```
git clone git@github.com:avnosov3/Parser_bs4_pep.git
```
2. Перейти в папку с проектом и создать виртуальное окружение
```
cd Parser_bs4_pep
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
python main.py <НАЗВАНИЕ ПАРСЕРА>(whats-new, latest-versions, download, pep)
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
</details>

<details><summary>English language</summary>  
  
Contains 4 parsers:
1. **whats-new** collects links to articles about innovations in Python
2. **latest-versions** collects information about Python version statuses
3. **download** downloads the archive with the latest documentation to the **downloads/** folder    
4. **pep** collects information about the number of PEP statuses

## Stack
* python 3.7.9
* beautiful soup 4.9.3

## Launch of the project
1. Clone repository
```
git clone git@github.com:avnosov3/Parser_bs4_pep.git
```
2. Go to the project folder and create a virtual environment
```
cd Parser_bs4_pep
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Activate a virtual environment
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Install dependencies from requirements.txt
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Run parser
```
cd src
python main.py <PARSER NAME>(whats-new, latest-versions, download, pep)
```
6. Output information to the terminal
```
python main.py <PARSER NAME> --output pretty
```
7. Save information in result folder
```
python main.py <PARSER NAME> --output file
```

## Author
[Artem Nosov](https://github.com/avnosov3)
</details>
