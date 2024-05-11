----
Генератор ценников на flet
---

Чтобы установить
1. Создайте виртуальное окружение
```bash
python -m venv env
```

Так оно активируется через bash консольку
```bash
source ./env/bin/activate
```


Скорее всего тут куча мути понапихано, ну и ладно
```bash
pip install -r requirements.txts
```

Теперь запускаем
```bash
flet run ./main.py
```

Можно еще сделать себе exe`шник
```bash
flet build windows
```