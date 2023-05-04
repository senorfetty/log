# from .models import Customer, Mkubwa
# from django.contrib.auth.backends import BaseBackend

# class CustomerBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = Customer.objects.get(username=username)
#         except Customer.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user

#         return None
    
#     def get_user(self, user_id):
#         try:
#             # Check if the user_id belongs to a Customer object
#             return Customer.objects.get(pk=user_id)
#         except Customer.DoesNotExist:
#             return None
            

# class MkubwaBackend:
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = Mkubwa.objects.get(username=username)
#         except Mkubwa.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user

#         return None
    
#     def get_user(self, user_id):
#         try:
#             return Mkubwa.objects.get(pk=user_id)
#         except Mkubwa.DoesNotExist:
#             # If the user_id doesn't belong to any user, return None
#             return None

from django.contrib.auth.backends import BaseBackend
from .models import Customer, Mkubwa

class MyAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # First, try to authenticate using the Customer model
            user = Customer.objects.get(username=username)
            if user.check_password(password):
                return user
        except Customer.DoesNotExist:
            pass

        try:
            # If authentication failed, try the Mkubwa model
            user = Mkubwa.objects.get(username=username)
            if user.check_password(password):
                return user
        except Mkubwa.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            # Check if the user_id belongs to a Customer object
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            try:
                # Check if the user_id belongs to a Mkubwa object
                return Mkubwa.objects.get(pk=user_id)
            except Mkubwa.DoesNotExist:
                # If the user_id doesn't belong to any user, return None
                return None
