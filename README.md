Этот репозиторий содержит простое веб-приложение, созданное с использованием Flask для практического изучения Github CI/CD и деплоя на VPS. Публикация происходит при каждом обновлении в ветке `main`.


## Следуйте этим инструкциям, чтобы запустить приложение на вашем локальном компьютере.

Предварительные требования
Прежде чем начать, убедитесь, что у вас установлен Python версии 3.x и pip.

### Шаг 1: Клонировать репозиторий
Сначала клонируйте репозиторий на свой локальный компьютер. Введите следующую команду в командной строке:

```bash
git clone https://github.com/e-Nicko/python-cicd-learn
```
### Шаг 2: Установить зависимости
Перейдите в каталог проекта и установите зависимости, введя следующие команды:

```bash
cd <название_каталога>
```
```bash
pip install -r requirements.txt
```
### Шаг 3: Настройка переменных окружения
Создайте файл .env в корневом каталоге проекта и установите переменную окружения DEBUG в true, если вы хотите включить режим отладки. Пример содержимого файла .env:

```
DEBUG=true
```
### Шаг 4: Запуск приложения
Теперь вы можете запустить приложение, введя следующую команду:

```bash
python app.py
```
После этого ваше приложение будет доступно по адресу http://127.0.0.1:5000/ в вашем веб-браузере.

### Шаг 5 (опционально): Изменение конфигурации
Вы можете изменить настройки приложения, отредактировав файл app.py в соответствии с вашими потребностями.

####Примечание
Не забудьте, что это только для локального развертывания. При развертывании на сервере или в облачной среде необходимо учитывать дополнительные шаги и меры безопасности.

