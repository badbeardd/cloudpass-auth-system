import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv  # ✅ fix here

load_dotenv()  # ✅ this loads variables from .env

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
print(SENDGRID_API_KEY, FROM_EMAIL)  # ✅ for debugging

def send_magic_link_email(to_email: str, magic_link: str) -> bool:
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject="Your Magic Login Link",
        html_content=f"<p>Click to login:</p><a href='{magic_link}'>{magic_link}</a>"
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"✅ Email sent: status {response.status_code}")
        print(response.body)
        print(response.headers)
        return True
    except Exception as e:
        print(f"❌ SendGrid error: {e}")
        print(e.__dict__)  # inspect this to debug deeply
        return False
