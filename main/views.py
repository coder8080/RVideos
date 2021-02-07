# Импортируем необходимые библиотеки
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Video, Channel, Comment, Category
from django.contrib.auth.models import User
from fuzzywuzzy import fuzz

# Главная страница


class IndexView(View):
    def get(self, request):
        videos = Video.objects.all()[::-1]
        return render(request, 'main/index.html', {"videos": videos})


# Страница видео
class VideoView(View):
    def get(self, request, name):
        video = Video.objects.get(name=name)
        return render(request, 'main/video.html', {"video": video})


# Страница канала
class ChannelView(View):
    def get(self, request, name):
        # Получаем объект канала
        channel = Channel.objects.get(name=name)
        # Получаем общее кол-во видео
        count = len(channel.video_set.all())
        # Получаем все доступные категории (необходимо для работы формы загрузки видео внизу страницы канала)
        categories = Category.objects.all()
        return render(request, 'main/channel.html', {"channel": channel, "count": count, "categories": categories})


# Добавление комментария под видео
class AddCommentView(View):
    def post(self, request):
        # Начинаем готовить ответ
        response = HttpResponse()
        # Небольшая защита (долго писать от чего)
        try:
            # Получаем объект пользователя из базы данных
            user = User.objects.get(username=request.user.username)
            # Получаем объект видео
            video_name = request.POST.get("video")
            video = Video.objects.get(name=video_name)
            # Получаем текст будущего комментария
            text = request.POST.get("text")
            # Создаём запись о существовании комментария в базе данных
            comment = Comment.objects.create(
                user=user,
                video=video,
                text=text
            )
            comment.save()
            # Записываем информацию об успешном выполнении запроса
            response.status_code = 200
        except:
            response.status_code = 404
        # Возвращаем статус
        return response


# Страничка профиля пользователя
class ProfileView(View):
    def get(self, request):
        # Смотрим, вошёл ли пользователь и пропускаем только вошедших, иначе отправляем на страницу входа
        if request.user.is_authenticated:
            # Получаем список каналов, владельцем которых является пользователь
            try:
                channel_list = Channel.objects.get(
                    owner__username=request.user.username)
                try:
                    channel_list[0]
                except:
                    channel_list = [channel_list]
                are_channels = True
            except:
                channel_list = []
                are_channels = False
            # Возвращаем результат
            return render(request, 'main/profile.html', {"channel_list": channel_list, "are_channels": are_channels})
        else:
            return redirect('/accounts/login')


# Загрузка видео
class UploadVideoView(View):
    def post(self, request):
        response = HttpResponse()
        # Получаем информацию о будущем видео и необходимые объекты базы данных
        name = request.POST.get('name')
        description = request.POST.get('description')
        video = request.FILES.get('video')
        poster = request.FILES.get('poster')
        category_name = request.POST.get('category')
        category = Category.objects.get(name=category_name)
        channel_name = request.POST.get('channel')
        channel = Channel.objects.get(name=channel_name)
        # Создаём запись о видео в базе данных
        new_video = Video.objects.create(
            name=name,
            description=description,
            video=video,
            poster=poster,
            category=category,
            channel=channel
        )
        response.status_code = 200
        # Возвращаем информацию о выполнении запроса
        return response


class Search(View):
    def get(self, request):
        print("started")
        request_text = request.GET.get('request_text')
        print("request text is " + request_text)
        videos = Video.objects.all()
        correct_videos = []
        for video in videos:
            # if (fuzz.ratio(video.name.lower(), request_text.lower()) > 45) or (fuzz.ratio(request_text.lower(), video.description.lower()) > 45):
            if fuzz.ratio(video.name.lower(), request_text.lower()) > 45:
                print("joined")
                correct_videos += [video]
        print('дошёл до конца')
        print(correct_videos)
        return render(request, 'main/search.html', {"correct_videos": correct_videos})
