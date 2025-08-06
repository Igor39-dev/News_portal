# News_portal
# список всех команд, запускаемых в Django shell:
python manage.py shell
from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

# 1.Создать двух пользователей
user1 = User.objects.create_user('Igor', password='123')
user2 = User.objects.create_user('Petya', password='1234')

# 2.Создать два объекта модели Author, связанные с пользователями.
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# 3.Добавить 4 категории в модель Category.
cat1 = Category.objects.create(name='Спорт')
cat2 = Category.objects.create(name='Политика')
cat3 = Category.objects.create(name='Наука')
cat4 = Category.objects.create(name='IT')

# 4.Добавить 2 статьи и 1 новость.
post1 = Post.objects.create(author=author1, post_type='AR', title='Статья об Олимпийских играх', text='Такой-то текст про игры...')
post2 = Post.objects.create(author=author1, post_type='AR', title='Статья про выборы', text='Такой-то текст про политику...')
post3 = Post.objects.create(author=author2, post_type='NW', title='новость про Python', text='Такой-то текст про Python...')

# 5.Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
post1.categories.add(cat1)
post2.categories.add(cat2, cat3)
post3.categories.add(cat4)

# 6.Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comment1 = Comment.objects.create(post=post1, user=user2, text='Хорошая статья.')
comment2 = Comment.objects.create(post=post2, user=user1, text='Интересненько...')
comment3 = Comment.objects.create(post=post3, user=user1, text='Спасибо за полезную информацию!')
comment4 = Comment.objects.create(post=post3, user=user2, text='Очень интересно!')

# 7.Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post1.like()
post1.like()
post2.like()
post2.dislike()
post3.like()
post3.like()
post3.like()
comment1.like()
comment2.dislike()
comment3.like()
comment3.like()
comment4.like()

# 8.Обновить рейтинги пользователей.
author1.update_rating()
author2.update_rating()

# 9.Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
best_author = Author.objects.order_by('-rating').first()
best_author.user.user.name
bets_author.rating

# 10.Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
best_post = Post.objects.order_by('-rating').first()
print(f'Дата: {best_post.time_create}\nАвтор: {best_post.author.user.username}\nРейтинг: {best_post.rating}\nЗаголовок: {best_post.title}\nПревью: {best_post.preview()}')

# 11.Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
comments = Comment.objects.filter(post=best_post)
comments.values('created', 'user__username', 'rating', 'text')
