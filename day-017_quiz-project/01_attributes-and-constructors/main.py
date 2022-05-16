class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


u0001 = User("0001", "john")
print(u0001.user_id)
print(u0001.username)
