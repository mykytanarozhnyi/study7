from post import Post, Userlogin
import sqlite3


if __name__ == "__main__":
    while True:
        print("Welcome to the new social")
        message = ("""
            Choose the option:
            1. Sign up
            2. Sign in
            3. Add post
            4. See all posts
            5. Like a post
            6. Dislike a post
            7. Ratings posts
            0. Exit 

            Your Choice: """)
        choice = input(message)
        match choice:
            case "1":
                Userlogin.register_user()
            case "2":
                if Userlogin.login_user():
                    print("Login successful. You can now add posts and interact with the app")
            case "3":
                new_post = Post()
            case "4":
                for entry in Post.entries:
                    print(entry)
            case "5":
                Post.like()
            case "6":
                Post.dislike()
            case "7":
                post_id = input("Enter the ID post to see rating:")
                for entry in Post.entries:
                    if entry.id == int(post_id):
                        print(entry.get_rating())
                        break
            case "8":
                pass
            case "0":
                break
            case _:
                print("Wrong choice")