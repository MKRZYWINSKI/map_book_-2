from models.data import users
from utils.crud import read_users,add_user


if __name__ == "__main__":
     print("Witaj użytkowniku")
     while True:
         print("Menu:")
         print("0.Zakończ program")
         print("1.Wyswietl co u znajomych")
         print("2. Dodaj użytkownika")
         manu_option: str = input("Dokonaj wyboru")
         if  manu_option == "0":
             print("Program kończy pracę")
             break
         if  manu_option == "1":
                read_users(users)
         if manu_option == "2":
             add_user(users)