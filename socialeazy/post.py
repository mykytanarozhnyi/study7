from datetime import datetime
import sqlite3
import hashlib

class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value > 150:
            raise ValueError()
        self._age = value
    @age.deleter
    def age(self):
        del self._age

class Content:
    def __init__(self):
        self.author = input("Enter nickname: ")
        self.text = input("Write your post: ")
        self.created_at = datetime.now()

    def __str__(self):
        return (f"{self.author} said at {self.created_at}: {self.text}"
                + f" Likes: {self.likes} | Dislikes: {self.dislikes}")

def __eq__(self, other):
    return self.rating == other.rating

class Post(Content):
    entries = list()

    def __init__(self):
        super().__init__()
        self.entries.append(self)
        self.id = len(self.entries)
        self.likes = 0
        self.dislikes = 0

    @classmethod
    def show_posts(cls):
        for entry in sorted(cls.entries, reverse=True):
            print(entry)

    @classmethod
    def find_by_id(cls):
        post_id = input("Enter post id: ")
        for post in cls.entries:
            if post.id == int(post_id):
                return post

    @classmethod
    def like(cls):
        post = cls.find_by_id()
        post.likes += 1

    @classmethod
    def dislike(cls):
        post = cls.find_by_id()
        post.dislikes += 1

    def get_rating(self):
        return self.likes - self.dislikes

    def __eq__(self, other):
        return self.get_rating() == other.get_rating()

    def __lt__(self, other):
        return self.get_rating() < other.get_rating()

    def __gt__(self, other):
        return self.get_rating() > other.get_rating()

    def __le__(self, other):
        return self.get_rating() <= other.get_rating()

    def __ge__(self, other):
        return self.get_rating() >= other.get_rating()

    def __ne__(self, other):
        return self.get_rating() != other.get_rating()

    def __str__(self):
        return f"#{self.id} {self.author} said: {self.text} Likes: {self.likes} | Dislikes: {self.dislikes}"

class Userlogin:
    conn = sqlite3.connect('loginsocialeazy.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS userseazy (
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    @staticmethod
    def register_user():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")

        while True:
            password1 = input("Enter your password: ")
            password2 = input("Confirm your password: ")


            if password1 == password2:
                hashed_password = Userlogin.hash_password(password2)
                print("You have successfully registered!")
                break
            else:
                print("Your passwords must match")

        try:
            Userlogin.cursor.execute("""
                INSERT INTO userseazy (first_name, last_name, email, password)
                VALUES (?, ?, ?, ?)
            """, (first_name, last_name, email, hashed_password))
            Userlogin.conn.commit()
            print("You have successfully created an account.")
        except sqlite3.IntegrityError:
            print("Error: This email is already registered")

    @staticmethod
    def login_user():
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        hashed_password = Userlogin.hash_password(password)

        Userlogin.cursor.execute("""
            SELECT * FROM userseazy WHERE email=? AND password=?
        """, (email, hashed_password))
        user = Userlogin.cursor.fetchone()

        if user:
            print("You have successfully logged in.")
            return True
        else:
            print("Error: Invalid email or password")
            return False

class Image:
    pass

class PostWithImage(Post, Image):
    pass

class Comment(Content):
    def __init__(self, post_id):
        super().__init__()
        self.post_id = post_id

    def __str__(self):
        return f"{self.author} commented on {self.post_id}: {self.text}"

if __name__ == "__main__":
    post1 = Post()  # rating 1
    post2 = Post()  # rating -1
    Post.like(1)
    Post.dislike(2)
    print(post1 == post2)