class AnimalGame:
    def __init__(self):
        self.filename = "animal_game.txt"
        self.data = {}
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    key, value = line.strip().split(':')
                    self.data[key] = value
        except FileNotFoundError:
            print(f"{self.filename} not found. Creating a new file.")
            open(self.filename, 'w').close() 
    def save_data(self):
        with open(self.filename, 'w') as file:
            for key, value in self.data.items():
                file.write(f"{key}: {value.strip()}\n")
    def display_data(self):
        print("\nAll Data:\n")
        for key, value in self.data.items():
            print(f"{key}: {value}")
    def add_update(self):
        key = input("Enter question: ")
        value = input("Enter answer: ")
        self.data[key] = value
    def delete_data(self):
        key = input("Enter the question to delete: ")
        if key in self.data:
            del self.data[key]
            print(f"Deleted entry for question: {key}")
        else:
            print(f"No entry found for question: {key}")
    def delete_all_data(self):
        self.data.clear()
        print("All data has been deleted.")
    def start_game(self):
        guessed = False
        for key, value in self.data.items():
            print(key)
            if input("yes/no: ") == "yes":
                print(f"Is it a {value}?")
                if input("yes/no: ") == "yes":
                    guessed = True
                    print("\nI WIN!")
                    break
        if not guessed:
            print("You win!")
            print("Add Q/A into the add/update data section to the main menu!")
    def intstructions(self):
        print("\nThe player builds the game by adding questions about animals.")
        print("If I run out of questions the user wins.")
        print("If I can guess your animal I win!")
        print("If you win please add a question to guess the animal")
        print("Be sure to save when exiting, any unsaved changes will not apply.\n")
    def play_game(self):
        self.load_data()
        while True:
            print("\nMain Menu:")
            print("1. Start Game")
            print("2. Add Data")
            print("3. Instructions")
            print("4. Display All Data")
            print("5. Delete Certain Data")
            print("6. Delete All Data")
            print("7. Save and Exit")
            choice = input("\nEnter your choice: ")
            print()
            if choice == '1':
                self.start_game()
            elif choice == '2':
                self.add_update()
            elif choice == '3':
                self.intstructions()
            elif choice == '4':
                self.display_data()
            elif choice == '5':
                self.delete_data()
            elif choice == '6':
                self.delete_all_data()
            elif choice == '7':
                self.save_data()
                print("Data saved. Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7.")
def main():
    game = AnimalGame()
    game.play_game()
main()