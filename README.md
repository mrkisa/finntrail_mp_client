#### Установка
1. Клонировать проект
```sh
git clone https://github.com/mrkisa/finntrail_mp_client.git
```
2. Перейти в папку проекта
```sh 
cd finntrail_mp_client
 ```
3. Установить зависимости
```sh
pip install -r requiremens.txt
```
4. Переименовать `config.rename.py` в `config.py`
```sh
mv config.rename.py config.py
```
5. В файле `config.py` прописать нужный `DATABASE`
```sh
DATABASE = '...'
```
6. Запустить скрипт 
```sh 
python -m wb.orders
```
