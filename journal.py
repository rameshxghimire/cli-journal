# Importing datetime system module for recording the entry dates.
import datetime
"""
journal.py - This module will contain the Journal object with a list of journals and individual entries (or daily journals)
as another object.
"""

version = "1.0.0"

last_id = 0        # Initializing a variable to store journal ids.


class Entry:
    """ Represents daily journal entries in the Journal (A Journal is a collection of such entries). 
    The entries in the journal have the content and tags to identify them.
    """

    def __init__(self, content, tags=""):
        """Initializes the entries with content and tag field, assigns date and id automatically."""
        global last_id
        self.tags = tags
        self.written_date = datetime.date.today()
        self.content = content
        last_id += 1        # Autoincrementing id number as entries happen.
        # Assigning the value of last_id to id variable.
        self.id = last_id

    def match(self, searchtext):
        """ Finding out if the note is retrived using a search text, this is important for the search functionality.
        Seach can also be performed on tags.
        """
        return searchtext in self.content and self.tags

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content


class Journal:
    """ Journal represents a collection of Entries, it is like a folder where files are like Entries which are kept here.
    """

    def __init__(self):
        """ This initializes an empty list to be used to store Entries."""
        self.entries = []

    def new_entry(self, content, tags=""):
       # Create a new Entry and append it in the list.
        self.entries.append(Entry(content, tags))

    # edit entry of given id
    # @param entry_id [Integer] entry id
    # @param content [String] new content to update/edit
    # @return void sets entry
    def edit_entry(self, entry_id, content):
        """ Change the content of an entry by finding it with id."""
        for instance in self.entries:
            if instance.id == entry_id:
                instance.setContent(content)
                break

    def edit_tags(self, entry_id, tags):
        """ Changing tags. """
        for instance in self.entries:
            if instance.id == entry_id:
                instance.tags = tags
                break

    def search(self, searchtext):
        """ Find entries by searching with a string."""
        return [entry for entry in self.entries if entry.match(searchtext)]
