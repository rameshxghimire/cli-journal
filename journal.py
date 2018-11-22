"""
journal.py - This module will contain the Journal object with a list of journals and individual entries (or daily journals)
as another object.
"""

version = "1.0.0"
main_author = "Ramesh Ghimire"
contributors = []

import datetime        # Importing datetime system module for recording the entry dates. 

last_id = 0        # Initializing a variable to store journal ids.

class Entries:
    """ Represents daily journal entries in the Journal (A Journal is a collection of such entries). 
    The entries in the journal have the content and tags to identify them.
    """

    def __init__(self, content, tags=""):
        """Initializes the entries with content and tag field, assigns date and id automatically."""
        self.content = content
        self.tags = tags
        self.written_date = datetime.date.today()
        global last_id
        last_id += 1        # Autoincrementing id number as entries happen.
        self.id = last_id        # Assigning the value of last_id to id variable.

    def match(self, searchtext):
        """ Finding out if the note is retrived using a search text, this is important for the search functionality.
        Seach can also be performed on tags.
        """
        return searchtext in self.content and self.tags

class Journal:
    """ Journal represents a collection of Entries, it is like a folder where files are like Entries which are kept here.
    """
    def __init__(self):
        """ This initializes an empty list to be used to store Entries."""
        self.entries = []

    def new_entry(self, content, tags=""):
        """ Create a new Entry and append it in the list."""
        self.entries.append(Entries(content, tags))

    def edit_entry(self, entry_id, content):
        """ Change the content of an entry by finding it with id."""
        for content in self.entries:
            if entries.id == entry_id:
                entries.content = content
                break
    
    def edit_tags(self, entry_id, tags):
        """ Changing tags. """
        for content in self.content:
            if entry.id == entry_id:
                entries.tags = tags
                break

    def search(self, searchtext):
        """ Find entries by searching with a string."""
        return [entry for entry in self.entries if entry.match(searchtext) ]

# Work in progress.
# Basic structure of this file is complete. Retest all the functions before proceeding. 
# edit_entry and edit_tags have some problems as they are failing tests. Reviewing the code now before proceeding further.
# Remove these comments before proceeding.


