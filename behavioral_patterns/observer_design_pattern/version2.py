from __future__ import annotations


class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email


class UserManagement:

    def __init__(self, notification_service: NotificationService) -> None:
        self.notification_service = notification_service

    def register(self, user: User):
        print("CREATE NEW USER")
        self.notification_service.notify("New User Registered", user)

    def delete(self, user: User):
        print("DELETE USER FROM DB")
        self.notification_service.notify("User Deleted", user)


class LogService:

    def __init__(self, notification_service: NotificationService) -> None:
        self.notification_service = notification_service

    def handle_user_registration_event(self, user):
        print(f"EVENT: New User with username {user.username} joined the APP.")

    def handle_user_deletion_event(self, user):
        print(f"EVENT: Existing User with username {user.username} left the App and got deleted.")

    def setup_log_event_handlers(self):
        self.notification_service.subscribe("New User Registered", self.handle_user_registration_event)
        self.notification_service.subscribe("User Deleted", self.handle_user_deletion_event)


class EmailService:

    def __init__(self, notification_service: NotificationService) -> None:
        self.notification_service = notification_service

    def send_welcome_mail_to_user(self, user):
        print(f"EVENT: Sending welcome email to {user.email}.")

    def send_good_bye_mail_to_user(self, user):
        print(f"EVENT: Sending good bye email to {user.email}")

    def setup_email_event_handler(self):
        self.notification_service.subscribe("New User Registered", self.send_welcome_mail_to_user)
        self.notification_service.subscribe("User Deleted", self.send_good_bye_mail_to_user)


class NotificationService:

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type: str, fn):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = [fn]
        else:
            self.subscribers[event_type].append(fn)

    def notify(self, event_type: str, data):
        if event_type not in self.subscribers:
            return
        else:
            for fn in self.subscribers[event_type]:
                fn(data)


if __name__ == '__main__':
    notification_service = NotificationService()
    LogService(notification_service).setup_log_event_handlers()
    EmailService(notification_service).setup_email_event_handler()

    new_user = User(username="Bob", password="*********", email="bob@ross.com")

    user_handler = UserManagement(notification_service)

    user_handler.register(new_user)
    user_handler.delete(new_user)
