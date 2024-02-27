class Notes:
    def __init__(self):
        self.notes = []

    def create_note(self, note):
        self.notes.append(note)
        print("Note created successfully!")

    def save_notes(self):
        with open("notes.txt", "w") as file:
            for note in self.notes:
                file.write(note + "\n")
        print("Notes saved successfully!")

    def read_notes(self):
        with open("notes.txt", "r") as file:
            for line in file:
                print(line.strip())

    def edit_note(self, index, new_note):
        if index < len(self.notes):
            self.notes[index] = new_note
            print("Note edited successfully!")
        else:
            print("Note does not exist.")

    def delete_note(self, index):
        if index < len(self.notes):
            del self.notes[index]
            print("Note deleted successfully!")
        else:
            print("Note does not exist.")

notes = Notes()

while True:
    print("1. Create a new note")
    print("2. Save notes")
    print("3. Read notes")
    print("4. Edit a note")
    print("5. Delete a note")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        note = input("Enter your note: ")
        notes.create_note(note)
    elif choice == 2:
        notes.save_notes()
    elif choice == 3:
        print("Your notes:")
        notes.read_notes()
    elif choice == 4:
        index = int(input("Enter the index of the note to edit: "))
        new_note = input("Enter the new note: ")
        notes.edit_note(index - 1, new_note)
    elif choice == 5:
        index = int(input("Enter the index of the note to delete: "))
        notes.delete_note(index)
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")