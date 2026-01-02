from apscheduler.schedulers.blocking import BlockingScheduler
import yagmail
from datetime import datetime

# Email function
def send_email():
    sender = sender_mail
    password = pass  # Gmail App Password
    receiver = recevier_mail

    yag = yagmail.SMTP(sender, password)
    yag.send(
        to=receiver,
        subject="Scheduled Mail",
        contents="This is a scheduled email sent using APScheduler."
    )

    print("Email sent at:", datetime.now())

# Scheduler
scheduler = BlockingScheduler()

# Run every day at 10:00 AM
scheduler.add_job(send_email, 'cron', hour=8, minute=15)

print("Scheduler started...")
scheduler.start()
