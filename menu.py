"""
This is an interface for the user to use the journal. It provides users options to use the journal.
"""
import sys

from journal import Entry, Journal


class Menu:
    """ Show menu options for the user."""

    def __init__(self):
        self.journal = Journal()
        self.options = {
            "1": self.show_entries,
            "2": self.search_entries,
            "3": self.add_entries,
            "4": self.edit_entries,
            "5": self.quit
        }

    def show_menu(self):
        print("1. Show all entries.\n2. Search entries.\3. Add a new entry.\n4. Edit an entry.\n5. Close the journal.\n")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.show_menu()
            choice = input("Enter an option: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice. Try again!")

    def show_entries(self, entries=None):
        if not entries:
            entries = self.journal.entries
        for entry in entries:
            print(f"{entry.id}: {entry.tags}\n{entry.content}")

    def search_entries(self):
        filter = input("Search for: ")
        content = self.journal.search(filter)
        self.show_entries(content)

    def add_entries(self):
        content = input("Enter an entry: ")
        self.journal.new_entry(content)
        print("Your journal entry has been added.")

    def edit_entries(self):
        id = input("Enter an id: ")
        content = input("Enter the journal entry: ")
        tags = input("Enter tags: ")
        if content:
            self.journal.edit_entry(id, content)
        if tags:
            self.journal.edit_tags(id, tags)

    def quit(self):
        print("Thank you for using your journal today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
