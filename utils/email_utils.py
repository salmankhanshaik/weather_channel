# import re

# from pydantic     import EmailStr

# from we_love_branding.settings.config     import settings, conf
# from fastapi_mail import MessageSchema, FastMail





# async def send_email_for_verification(email: EmailStr, name: str,company_name: str,  otp_number: int):
#     message             =     MessageSchema(
#         subject         =    "Account Verification Mail",
#         recipients      =    [email],  # List of recipients, as many as you can pass '
#         template_body   =    {
#             "user_name"   : name,
#             "company_name": company_name,
#             "otp_number"  : otp_number 
#         }
#     )

#     fm = FastMail(conf)
#     await fm.send_message(message, template_name="otp_verification.html")
