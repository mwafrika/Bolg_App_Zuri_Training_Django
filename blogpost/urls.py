from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeletePostView, Register
from blogpost import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='details'),
    path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeletePostView.as_view(), name='delete_post'),
    path('register/', v.Register, name='signup'),
    path('login/', v.Login, name='login'),
    path('logout/', v.Logout, name='logout'),
    # password reset process
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='passwordReset/password_reset.html'
    ),
        name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='passwordReset/password_reset_sent.html'
    ),
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="passwordReset/psw_reset_complete.html"
    ),
        name="password_reset_complete")

]
