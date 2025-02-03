class Notification:
    def send(self):
        raise NotImplementedError("Subclass must implement the send method")

class Email_Notification(Notification):
    def send(self, message):
        return f"Sending email notification: {message}"

class SMS_Notification(Notification):
    def send(self, message):
        return f"Sending SMS notification: {message}"

email_notification = Email_Notification()
sms_notification = SMS_Notification()
print(email_notification.send("This is an email message"))
print(sms_notification.send("This is an SMS message"))
