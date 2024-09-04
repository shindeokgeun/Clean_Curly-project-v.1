from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 홈 페이지,  # index 뷰를 루트 URL에 매핑
    # 로그인 페이지를 users 앱의 URL로 연결합니다.
    path('login/', include('users.urls')),  # 수정된 부분
    path('logout/', include('users.urls')),  # 수정된 부분
    path('signup/', include('users.urls')),  # 수정된 부분

]