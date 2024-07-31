# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth.models import User
# from .models import PvdmUsers1


# # backends.py
# import logging



# logger = logging.getLogger(__name__)

# class PlainTextAuthBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user_record = PvdmUsers1.objects.get(username=username)
#             logger.debug(f"User record found: {user_record}")

#             logger.debug(f"Provided password: '{password}'")
#             logger.debug(f"Stored password: '{user_record.password}'")

#             if user_record.password == password:
#                 logger.debug("Password matches")
#                 user, created = User.objects.get_or_create(username=username)
#                 if created:
#                     user.set_password(password)
#                     user.save()
#                 return user
#             else:
#                 logger.debug("Password does not match")
#         except PvdmUsers1.DoesNotExist:
#             logger.debug("User record not found")
#             return None
#         except Exception as e:
#             logger.error(f"Error during authentication: {e}")
#             return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None