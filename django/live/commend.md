# Django 프로젝트 생성 & 실행 흐름

## 1. 가상환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 실행 (Windows PowerShell)
.\venv\Scripts\activate
# (Mac/Linux)
source venv/bin/activate
```

* 실행 확인: `which python`
* 설치된 라이브러리 확인: `pip list`

## 2. 라이브러리 설치

```bash
# requirements.txt 기준 설치
pip install -r requirements.txt

# Django 설치
pip install django
```

## 3. 프로젝트 및 앱 생성

```bash
# 프로젝트 생성
django-admin startproject {project_name} .

# 앱 생성 (예: articles)
python manage.py startapp articles
```

* **앱 등록**: `settings.py` → `INSTALLED_APPS`에 앱 이름 추가

```python
INSTALLED_APPS = [
    ...
    'articles',
]
```

## 4. Template 설정

1. **프로젝트 루트**에 `templates/` 폴더 생성 → `base.html` 추가
2. `settings.py > TEMPLATES > DIRS` 경로 수정 → `templates` 추가
3. 각 앱 안에도 `templates/{app_name}` 폴더 생성

   * 예: `articles/templates/articles/`
   * 이후 `base.html`을 상속받아 개별 페이지 작성

## 5. URL 설정

* **프로젝트 urls.py**

```python
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
]
```

* **앱 urls.py**

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
]
```

* 이후 템플릿에서 `articles:index` 형태로 URL을 참조 가능

## 6. 서버 실행

```bash
python manage.py runserver
```

개발용 서버가 실행되고, 브라우저에서 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 접속 가능
