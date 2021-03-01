from LinkedList import LinkedList

class HashTable:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)


    # Each element of the hash table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

    def create_arr(self, size):
        
        array = []

        for i in range(size): 
            newLinkedList = LinkedList()
            array.append(newLinkedList)
    
        return array


    # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

    def hash_func(self, key):
        
        hash_key = hash(key)
        index = (hash_key * 21) % self.size

        return index


    # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

    def insert(self, key, value):
        
        hash_key = self.hash_func(key)
        newLinkedList = self.arr[hash_key].find_update(key)

        item = (key, value)
        
        if newLinkedList == -1:
            self.arr[hash_key].append(item)


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
    
    print('DONE TRAVERSING')