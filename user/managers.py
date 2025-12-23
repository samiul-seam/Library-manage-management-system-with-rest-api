from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, uid, password=None, **extra_fields):
        if not uid:
            raise ValueError('This uid field must be set.')
    
        uid = uid.strip().lower()
        user = self.model(uid=uid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, uid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff = True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser = True')
        
        return self.create_user(uid, password, **extra_fields)