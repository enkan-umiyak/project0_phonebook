# Array List implementation of Contacts
from Contact import Contact

class ContactList:
    """Contact List class that creates an array list of the phonebook.
    """

    def __init__(self, size: int = 50):
        """
            Create an array list of contacts with default storage size of 50.
        """
        self.phonebook = [None] * size
        self.size = 0

    def getSize(self):
        """
            Get the size of this contact list.
        """
        return self.size
    
    def first(self) -> Contact:
        """
            Get the first contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        return 
    
    def getLast(self) -> Contact:
        """
            Get the last contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        return 

    def getContactAtIndex(self, index: int) -> Contact:
        """Gets the contact at given index in the contact linked list.
        Returns None if index is not found in the list.

        Args:
            index (int): Index to get in the contact linked list.

        Returns:
            Contact: Contact at index.
        """
        # Complete this Method
        return 
    
    def getContact(self, student_num: str) -> Contact:
        """Gets the contact based on given student number. Will return None
        if contact is not found.

        Args:
            student_num (str): Student number to base search from.

        Returns:
            Contact: Contact information.
        """
        # Complete this Method
        return 
    
    def getContactBySurname(self, surname: str) -> Contact:
        """Gets the contact based on surname. Will return None if contact is not found.
        """
        # Complete this Method
        return 
    
    def isEmpty(self) -> bool:
        """
            Checks if contact list has no contacts.
        """
        return self.getSize() == 0
    
    def incrSize(self) -> None:
        """
            Increase the size of this contact list.
        """
        # Complete this Method
        self.size += 1

    def decrSize(self) -> None:
        """
            Decrease the size of this contact list
        """
        self.size -= 1

    def __increasePhonebookSize(self) -> None:
        """
            Increases the size of this phonebook by two times.
        """
        # Complete this Method
        return 
    
    def insert(self, c : Contact):
        """Inserts new contact at index point.

        Args:
            c (Contact): Contact to be inserted.
        """
        # Complete this Method
        return 

    def __findIndexInsertion(self, c: Contact) -> int:
        """Finds the index to insert from based on contact's
        last name, and first name if both have the same first names.

        Args:
            c (Contact): Contact to compare and to be inserted.

        Returns:
            int: Node insertion point for new contact.
        """
        # Complete this Method
        return 
    
    def __adjustPhonebook(self, start: int, end = int, dir: str = "f") -> None:
        """
        Adjusts the arrangement of this phonebook from start to end.

        Args:
            index (int): Index for adjustment.
            dir (str): Direction of adjustment:
                "f" -> Forward indexing adjustment. For example, element at index 0 takes the value of the element at index 1.
                "b" -> Backward indexing adjustment. For example, elemet at index 1 takes the value of the element at index 0.
        """
        # Complete this Method
        return 
    
    def deleteContact(self, stdn: str) -> Contact:
        """Finds the contact based on their student number.
        Returns the deleted contact. Otherwise, returns -1 if not found.

        Args:
            stdn (str): Student number of contact to be deleted.

        Returns:
            Contact: Deleted contact, if found.
        """
        # Complete this Method
        return 
        
    def __str__(self, f = None) -> str:
        """Prints every contact in this contact list.

        Args:
            f (list, optional): A list that filters which contact should
                be outputted. Defaults to None.

        Returns:
            str: Every contact in this contact list.
        """
        # Complete this method
        s = "<----Phonebook---->"
        if not self.isEmpty():
            # Complete this method.
            print("Not Empty")
        else:
            s += "\nThis phonebook is currently empty..."
        s += "\n<----End---->"
        return s