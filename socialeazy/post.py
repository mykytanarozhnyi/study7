from datetime import datetime

class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
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
        + f"Likes: {self.likes}" | "Dislikes: {self.dislikes}")

def __eq__(self,other):
    return self.rating == other.rating

class Post(Content):
    entries = list()

    def __init__(self):
        super().__init__()  # Content.__init__()
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

if __name__ == "__main__":

    post1 = Post() #rating 1
    post2 = Post() #rating -1
    Post.like(1)
    Post.dislike(2)
    print(post1 == post2)