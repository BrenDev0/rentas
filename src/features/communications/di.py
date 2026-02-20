from src.di import Injector
from .application import VerifyEmail, EmailService

def register_dependencies(injector: Injector):
    injector.register(EmailService)
    injector.register(VerifyEmail)
