"""
This is an interface for the user to use the journal. It provides users options to use the journal.
"""
import sys

from journal import Entries, Journal


class menu:
    """ Show menu options for the user."""

    def __init__(self):
        self.journal = Journal()
        self.options = {
            "1": self.show_entries,
            "2": self.search_entries,
            "3": self.add_entries,
            "4": self.edit_entries,
            "5": self.close
        }

    def show_menu(self):
        print("""
        1. Show all entries.
        2. Search entries.
        3. Add a new entry.
        4. Edit an entry.
        5. Close the journal.
        """)
