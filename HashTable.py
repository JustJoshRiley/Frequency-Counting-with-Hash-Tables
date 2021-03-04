from LinkedList import LinkedList

class HashTable:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)


    # 1️⃣ TODO: Complete the create_arr method.

    # Each element of the hash table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

    def create_arr(self, size):
        
        array = []

        for i in range(size): 
            newLinkedList = LinkedList()
            array.append(newLinkedList)
    
        return array




    # 2️⃣ TODO: Create your own hash function.

    # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

    def hash_func(self, key):
        # lowercase the word 
        word = key.lower()
        # takes the number in the string and returns the index 
        # ord() gives us the ascii value of the first letter in the string
        integer_from_string = ord(word[0])
        #  pass in the variable to find the index 
        index = integer_from_string % self.size

        return index


    # 3️⃣ TODO: Complete the insert method.

    # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

    def insert(self, key, value):
        # step 1 : use the hash function to find which Linked List to access.
        hash_key = self.hash_func(key)
        # step 2 :  using the hash key, access the linked list from the array.
        newLinkedList = self.arr[hash_key]
        #  step 3 : check if the key is in the given linked list.
        found = newLinkedList.find(key)
        #if the key/ word is not found ... 
        if found == -1:
            # create a tuple
            item = (key, value)
            # append it 
            self.arr[hash_key].append(item)
        
        




    # 4️⃣ TODO: Complete the print_key_values method.

    # Traverse through the every Linked List in the table and print the key value pairs.

    # For example: 
    # a: 1
    # again: 1
    # and: 1
    # blooms: 1
    # erase: 2

    def print_key_values(self):
        for LinkedList in self.arr: 
            LinkedList.print_nodes()
    print('DONE')
    



