class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print(f"Saving {self.name} to database...")

    def send_welcome_email(self):
        print(f"Sending welcome email to {self.email}...")


"""
Responsibilities are separated into distinct classes: User for user data, 
UserRepository for database operations, and EmailService for email functionality.
"""


class UserImproved:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database...")


class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}...")
