from datetime import datetime


class Content:

    def __init__(self):
        self.author = input("Enter nickname: ")
        self.text = input("Write your post: ")
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.author} said at {self.created_at}: {self.text}"


class Post(Content):
    entries = list()

    def __init__(self):
        super().__init__()  # Content.__init__()
        self.entries.append(self)
        self.id = len(self.entries)
        self.likes = 0
        self.dislikes = 0

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1

    def rating(self):
        return self.likes - self.dislikes

    def __str__(self):
        return f"#{self.id} {self.author} said: {self.text}Likes: {self.likes} | Dislikes: {self.dislikes}"


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