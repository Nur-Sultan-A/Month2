import email


class User:
    total_users = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return cls.total_users

    @classmethod
    def create_user(cls, name, email):
        if not cls.validate_email(email):
            raise ValueError("jopa blyat")
        user = cls(name, email)
        return user


    @staticmethod
    def validate_email(email):
        return '@' in email


# user1 = User("Albert", "Albertgmail.com")
# user2 = User("Igor", "igor@gmail.com")
#
# user1.total_users = 4
# print(User.total_users)
# print(user1.total_users)
# print(User.get_total_users())
# print(User.validate_email("@"))
# print(User.validate_email("Albert"))
# print(User.create_user("Albert", "rere"))
User_1 = User("jopa", "jopa@")
is_valid = User.validate_email(User_1.email)
print(f"Email '{User_1.email}' валиден? {is_valid}")
