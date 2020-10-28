from django.urls import path

from apps.accounts.api.views import (
    # registration_view,
    LoginView, UsersListView, TeachersListView, StudentsListView,
    # account_properties_view,
    # update_account_view,
    # does_account_exist_view,
    # ChangePasswordView,
)

app_name = 'account'

urlpatterns = [
    # path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
    # path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    # path('properties', account_properties_view, name="properties"),
    # path('properties/update', update_account_view, name="update"),
    # path('register', registration_view, name="register"),

    path('login', LoginView.as_view(), name="login"),
    path('users', UsersListView.as_view(), name="users"),
    path('teachers', TeachersListView.as_view(), name="teachers"),
    path('students', StudentsListView.as_view(), name="students"),

]
