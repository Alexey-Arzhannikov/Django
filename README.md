
# Дипломная работа по курсу "Python-разработчик"  👋
Тема проекта: Разработка web-приложения с использованием фреймворка Django и библиотеки FER(Face Expression Recognition).
## My Skill Set  
<table><tr><td valign="top" width="33%">



### Frontend  
<div align="center">  
<a href="https://getbootstrap.com/docs/3.4/javascript/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/bootstrap-plain.svg" alt="Bootstrap" height="50" /></a>  
<a href="https://www.w3schools.com/css/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/css3-original-wordmark.svg" alt="CSS3" height="50" /></a>  
<a href="https://en.wikipedia.org/wiki/HTML5" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/html5-original-wordmark.svg" alt="HTML5" height="50" /></a>  
</div>

</td><td valign="top" width="33%">



### Backend  
<div align="center">  
<a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>  
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="50" /></a>  
<a href="https://www.postgresql.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/postgresql-original-wordmark.svg" alt="PostgreSQL" height="50" /></a>  
</div>

</td><td valign="top" width="33%">



### DevOps  
<div align="center">  
<a href="https://opencv.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/opencv-icon.svg" alt="OpenCV" height="50" /></a>  
<a href="https://pytorch.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/pytorch-icon.svg" alt="pytorch" height="50" /></a>  
<a href="https://www.tensorflow.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/tensorflow-icon.svg" alt="TensorFlow" height="50" /></a>  
</div>

</td></tr></table>  

<br/>  

<details><summary><b>Установка и настройка</b></summary>
Проект реализован на языке python с использованием фрэймворка Django и библиотеки FER.<br>
Для работы понадобится python (использовался python 3.12).<br>
Необходимо установить следующее:

Фреймворк Django
```
pip install Django==5.1.2
```
драйвер Python для PostgreSQL
```
pip install psycopg2==2.9.10
```
библиотеку <a href="https://github.com/JustinShenk/fer/blob/master/README.md">FER</a>
```
pip install fer==22.5.1
```
В файле .venv/Lib/site-packages/fer/classes.py нужно внести следующие изменения:
<ul>
<li>
Произвести импорт

```
import matplotlib.pyplot as plt
```
</li>
<li>
Изменить путь для обработанного видео

```
recognition/media/fer_video/videos
```
<img src="\readme\image3.png" width="550">
</li>
<li>
В методе to_pandas добавить код для сохранения графика

```python
plt.figure(figsize=(6, 4), dpi=400)
df.plot()
plt.savefig(f'recognition/media/graph/processed.png')
```
<img src="\readme\image4.png" width="550">
</li>
<li>
Произвесть изменения в методе analyze
<img src="\readme\image5.png" width="550">
</li>
<li>
Корректируем имя обработанного видео
<img src="\readme\image6.png" width="550">
</li>

</ul>


</details>
<details><summary><b>Возможности</b></summary>
Реализованы следующие возможности:
<ul>
<li>Реализовано распознование эмоций на фотографии, с выводом результата
<br>
<img src="\readme\image1.jpeg" width="550">
<br>
</li>
<li>Реализовано распознование эмоций на видео, с выводом графика результата
<br>
<img src="\readme\image2.jpeg" width="550">
<br>
</li>
</ul>
</details>

<details><summary><b>Структура</b></summary>

В django создано приложение recognition. Структура проекта выглядит следующим образом<br>

<ul>

<li>
EmotionRecognitionSite
    <ul>
        <li>__init__.py</li>
        <li>asgi.py</li>
        <li>settings.py</li>
        <li>urls.py</li>
        <li>wsgi.py</li>
    </ul>
</li>
<li>recognition
    <ul>
        <li>media
            <ul>
                <li>fer_video
                    <ul>
                        <li>videos</li>
                    </ul>
                </li>
                <li>graph</li>
                <li>images</li>
                <li>videos
                    <ul>
                        <li>processed_video</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li>migrations</li>
        <li>templates</li>
        <li>__init__.py</li>
        <li>admin.py</li>
        <li>apps.py</li>
        <li>forms.py</li>
        <li>models.py</li>
        <li>tests.py</li>
        <li>urls.py</li>
        <li>utils.py</li>
        <li>views.py</li>
    </ul>
</li>
<li>static</li>
    <ul>
        <li>style.css</li>
    </ul>
<li>manage.py</li>
<li>requirememts.txt</li>
</ul>

<details><summary><b>Модель</b></summary>
Определены 3 модели: ImageFeed, RecognizedEmotion, VideoFeed.
<ul>
<li>ImageFeed - модель для хранения загруженных изображений.<br>
Имеет следующую структуру:

```
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"
```
</li>
<li>RecognizedEmotion - модель для хранения информации о распознанных эмоциях на фото.<br>
Имеет следующую структуру:

```
    confidence = models.FloatField(null=True)
    emotion = models.CharField(max_length=30, null=True)
    info_feed = models.ForeignKey(ImageFeed, related_name='recognized_emotions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.emotion} ({self.confidence}) on {self.info_feed.image.name}"
```
</li>
<li>VideoFeed - модель для хранения видео и информации о распознанных эмоциях на видео<br>
Имеет следующую структуру:

```
   video = models.FileField(upload_to='videos/')
    processed_video = models.FileField(upload_to='videos/', null=True, blank=True)
    graph_emotion = models.ImageField(upload_to='graph/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.video.name} - {self.processed_video}"
```
</li>
</ul>
Создайте миграцию для приложения.

```
python manage.py makemigrations
```
Примените миграцию к БД.

```
python manage.py migrate.
```
</details>
<details><summary><b>Утилиты</b></summary>
Функции реализованы в файле utils.py

<ul>
<li>
Функция process_image использует сверточную нейронную сеть, веса которой представлены в файле HDF5.<br>
При необходимости, модель можно переобучить с помощью конструктора FER при вызове и инициализации модели.<br>
MTCNN (Multi-task Cascaded Neural Network) является параметром конструктора. Это техника для распознавания лиц.<br>
Когда установлено значение "True", модель MTCNN используется для обнаружения лиц,<br>
иначе функция использует классификатор OpenCV Haar Cascade по умолчанию.
</li>
<li>
Функция process_video реализует определение эмоций на видео.<br>
Создает файл .mp4(обработанное видео) и передает в модель VideoFeed.<br>
На основе полученных данных, строит график, также передает в модель VideoFeed.
</li>
</ul>
</details>
