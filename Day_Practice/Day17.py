class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"Initialized with id {id} and name {username}")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, "Tomato")
user_2 = User(2, "Potato")
user_2.follow(user_1)