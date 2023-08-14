class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)
        print("Entry added to the diary.")

    def view_entries(self):
        if self.entries:
            print("Diary Entries:")
            for index, entry in enumerate(self.entries, start=1):
                print(f"{index}. {entry}")
        else:
            print("No entries in the diary.")

def main():
    diary = Diary()

    while True:
        print("\n1. Add Diary Entry")
        print("2. View Diary Entries")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            entry = input("Enter your diary entry: ")
            diary.add_entry(entry)
        elif choice == "2":
            diary.view_entries()
        elif choice == "3":
            print("Exiting the diary application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

