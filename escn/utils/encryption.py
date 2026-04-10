from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.ENCRYPTION_KEY)

def encrypt_pin(pin):
    return fernet.encrypt(pin.encode()).decode()

def decrypt_pin(encrypted_pin):
    return fernet.decrypt(encrypted_pin.encode()).decode()