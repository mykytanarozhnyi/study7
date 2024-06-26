from post import Post, Userlogin
import sqlite3

def main():
    while True:
        print("Welcome to the new social")
        message = ("""
            Choose the option:
            1. Sign up
            2. Sign in
            0. Exit 

            Your Choice: """)
        choice = input(message)
        match choice:
            case "1":
                Userlogin.register_user()
            case "2":
                user_id = Userlogin.login_user()
                if user_id:
                    print("Login successful. You can now add posts and interact with the app")
                    user_menu(user_id)
            case "0":
                break
            case _:
                print("Wrong choice")

def user_menu(user_id):
    while True:
        message = ("""
            Choose the option:
            1. Add post
            2. See all posts
            3. Like a post
            4. Dislike a post
            5. Ratings posts
            0. Logout

            Your Choice: """)
        choice = input(message)
        match choice:
            case "1":
                new_post = Post(user_id)
            case "2":
                Post.show_posts()
            case "3":
                post_id = int(input("Enter the ID of the post to like: "))
                Post.like(post_id)
            case "4":
                post_id = int(input("Enter the ID of the post to dislike: "))
                Post.dislike(post_id)
            case "5":
                post_id = int(input("Enter the ID post to see rating:"))
                post = Post.find_by_id(post_id)
                if post:
                    print(f"Rating: {post[4] - post[5]}")  # likes at index 4, dislikes at index 5
            case "0":
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()