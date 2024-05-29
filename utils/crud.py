def read_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twój znajomy {user['name']}: {user['surname']}, opublikował{user['posts']} postów")

def add_user(users: list)-> None:
    new_name: str = input("Podaj imie:")
    new_surname: str = input("Podaj imie:")
    new_posts: int = int(input("Podaj liczbe punktów"))
    new_user: dict = {"name": new_name, "surname": new_surname, "posts": new_posts}
    print(new_user)
    users.append(new_user)
