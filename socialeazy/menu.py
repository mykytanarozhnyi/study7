from post import Post

if __name__ == "__main__":
    while True:
        print("Welcome to the new social")
        message = ("""
            Choose the option:
            1. Add post
            2. See all posts
            3. Like a post
            4. Dislike a post
            5. Ratings posts
            0. Exit 

            Your Choice: """)
        choice = input(message)
        match choice:
            case "1":
                new_post = Post()
            case "2":
                for entry in Post.entries:
                    print(entry)
            case "3":
                Post.like()
            case "4":
                Post.dislike()
            case "5":
                post_id = input("Enter the ID post to see rating:")
                for entry in Post.entries:
                    if entry.id == int(post_id):
                        print(entry.rating())
                        break
            case "0":
                break
            case _:
                print("Wrong choice")