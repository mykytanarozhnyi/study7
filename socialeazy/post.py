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

class Post(Content):
    def __init__(self, author_id):
        self.author_id = author_id
        super().__init__()
        self.likes = 0
        self.dislikes = 0
        self.save_post()

    def save_post(self):
        Userlogin.cursor.execute("""
            INSERT INTO posts (author_id, content, created_at, likes, dislikes)
            VALUES (?, ?, ?, ?, ?)
        """, (self.author_id, self.text, self.created_at, self.likes, self.dislikes))
        Userlogin.conn.commit()
        self.id = Userlogin.cursor.lastrowid

    @classmethod
    def show_posts(cls):
        Userlogin.cursor.execute("""
            SELECT p.id, u.first_name, u.last_name, p.content, p.created_at, p.likes, p.dislikes 
            FROM posts p JOIN userseazy u ON p.author_id = u.id
        """)
        posts = Userlogin.cursor.fetchall()
        for post in posts:
            print(f"#{post[0]} {post[1]} {post[2]} said at {post[4]}: {post[3]} Likes: {post[5]} | Dislikes: {post[6]}")

    @classmethod
    def find_by_id(cls, post_id):
        Userlogin.cursor.execute("""
            SELECT * FROM posts WHERE id=?
        """, (post_id,))
        post = Userlogin.cursor.fetchone()
        if post:
            return post
        else:
            print("Post not found")
            return None

    @classmethod
    def like(cls, post_id):
        post = cls.find_by_id(post_id)
        if post:
            likes = post[4] + 1  # likes are at index 4
            Userlogin.cursor.execute("""
                UPDATE posts SET likes=? WHERE id=?
            """, (likes, post_id))
            Userlogin.conn.commit()

    @classmethod
    def dislike(cls, post_id):
        post = cls.find_by_id(post_id)
        if post:
            dislikes = post[5] + 1  # dislikes are at index 5
            Userlogin.cursor.execute("""
                UPDATE posts SET dislikes=? WHERE id=?
            """, (dislikes, post_id))
            Userlogin.conn.commit()

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
    conn = sqlite3.connect('newsocial.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS userseazy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            password TEXT
            )
    """)
    conn.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_id INTEGER,
            content TEXT,
            created_at TIMESTAMP,
            likes INTEGER DEFAULT 0,
            dislikes INTEGER DEFAULT 0,
            FOREIGN KEY(author_id) REFERENCES userseazy(id)
            )
    """)
    conn.commit()

    @staticmethod
    def register_user():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")

        while True:
            password1 = input("Enter your password: ")
            password2 = input("Confirm your password: ")

            if password1 == password2:
                password_hash = hashlib.sha256(password1.encode()).hexdigest()
                try:
                    Userlogin.cursor.execute("""
                        INSERT INTO userseazy (first_name, last_name, email, password)
                        VALUES (?,?,?,?)
                    """, (first_name, last_name, email, password_hash))
                    Userlogin.conn.commit()
                    print("You have successfully created an account.")
                    break
                except sqlite3.IntegrityError:
                    print("Error: This email is already registered")
                    break
            else:
                print("Your passwords must match")

    @staticmethod
    def login_user():
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        Userlogin.cursor.execute("""
            SELECT * FROM userseazy WHERE email=? AND password=?
        """, (email, password_hash))
        user = Userlogin.cursor.fetchone()

        if user:
            print("You have successfully logged in.")
            return user[0]  # Return user ID
        else:
            print("Error: Invalid email or password")
            return None

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
