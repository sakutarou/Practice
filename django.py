# -*- coding: utf-8 -*-
# 安裝 django / 建立虛擬環境 / 在虛擬環境下工作
mkdir djangogirls
cd djangogirls
python3 -m venv myvenv
source myvenv/bin/activate
pip install django==1.6.6 # 安裝django
deactivate # 結束虛擬環境

# 建立 django 專案
django-admin.py startproject mysite . # 創建資料夾與檔案腳本
python manage.py migrate # 創建資料庫
python manage.py runserver # 執行 web server
python manage.py -h # 查看 manage.py 裡的指令
python manage.py runserver -h # 解釋 runserver

# 創建 blog app
python manage.py startapp blog 
open mysite/settings.py  INSTALLED_APPS plus 'blog' # 新增使用的 app
open blog/models.py # 建立內容
python manage.py makemigrations# 建立資料庫
python manage.py migrate

django-admin.py startproject mysite
python manage.py runserver
python manage.py startapp trips
# 去 mysite/settings.py 的 INSTALLED_APPS 新增“trips"


# 在 python 的終端機裡試做
python manage.py shell
from blog.models import Post # 載入 post 操作套件
from django.contrib.auth.models import User # 載入 User 操作套件
author = models.ForeignKey(User,on_delete=models.CASCADE) # 在 models.py 中加入預設User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword') # 新增 User
user.last_name = 'Lennon'
user.save()
User.objects.all() # 有哪些 User
Post.objects.create(author = user, title = 'Sample title', text = 'Test') # 創建 Post
Post.objects.all() # 有哪些Post
Post.objects.filter(author=user) # 篩選 post
Post.objects.filter(title__contains='title') 
post = Post.objects.get(id=1) # 指定 post
post.publish() # 發布 post
Post.objects.filter(published_date__isnull=False) # 已發布的網誌
Post.objects.order_by('created_date') # 依創造日期排列
Post.objects.order_by('-created_date') # 依創造日期反排列
exit()

# Django admin 
python manage.py createsuperuser --username=joe --email=joe@example.com # 創造超級 user
python manage.py runserver
127.0.0.1:8000/admin

# Deploy
pip install dj-database-url gunicorn whitenoise 
pip freeze > requirements.txt
psycopg2==2.5.3 in requirements.txt 
web: gunicorn mysite.wsgi # create Procfile
python-3.4.1 # create runtime.txt

