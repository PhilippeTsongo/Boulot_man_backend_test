from .models import User
import bcrypt

class UserService:
    @staticmethod
    def register_user(email, fullname, password):

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user = User.objects.create(email=email ,fullname=fullname, password=hashed_password)
        return user

