from post import Post
if __name__ == "__main__":
    posts = list()
    while True:
        print("Welcome to the eazy")
        message = ("""Choose the option:
        1. Add post
        2. See all posts 
        0. exit")
        
        Your Choice: """)

        choice = input(message)
        match choice:
            case "1" | "155":
                new_post = Post()
                posts.append(new_post)
            case "2":
                for entry in Post.entries:
                    print(entry)
            case "0":
                break
            case _:
                print("try something else")

