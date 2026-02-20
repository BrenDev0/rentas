from pathlib import Path
import os
from ...domain import Email
from ..email_service import EmailService

class VerifyEmail:
    def __init__(
        self,
        email_service: EmailService
    ):
        __from_addr = os.getenv("MAILER_USER")
        if not __from_addr:
            raise ValueError("Email variables not set")
        
        self.__from_addr = __from_addr
        self.__subject = "Verificar Correo Electrónico"
        self.__email_service = email_service

    def __build_email( 
        self,
        to: str,
        verification_code: int
    ):
        template_path = Path(__file__).parent.parent.parent / "templates" / "email_verification.html"

        with open(template_path, 'r', encoding="utf-8") as f:
            template = f.read()
        
        email_body = template.replace('{{verification_code}}', str(verification_code))
        
        return Email(
            sender=self.__from_addr,
            recipient=to,
            subject=self.__subject,
            html=str(email_body)
        )
    
    def execute(
        self,
        to: str,
        verification_code: int
    ): 
        email = self.__build_email(
            to=to,
            verification_code=verification_code
        )

        self.__email_service.send_email(
            email=email
        )

        
        

        