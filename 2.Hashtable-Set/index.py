class HashsTable:
    def __init__(self,size):
        
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self,key):
        """Hash function: Converts a key into an index."""
        return hash(key)% self.size
    
    def insert(self,key,value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return 
        self.table[index].append([key,value])
    
    def search(self,key):
        """Retrieve the value associated with a key."""
        index = self._hash(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        
        index = self._hash(key)
        
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False
    
    def display(self):
        
        for i , bucket in enumerate(self.table):
            print(f"key:{i},value:{bucket}")


hashtable = HashsTable(4)
hashtable.insert('Name','Robin')
hashtable.insert('Age',23)
hashtable.insert('Place','Kochi')
hashtable.insert('Role','ML/AI Engineer')
hashtable.display()
"""
How to Handle Collisions?
A collision in a hash table occurs when two different keys produce the same hash index.

hash("apple") % 10  # Assume this gives index 3
hash("banana") % 10  # Assume this also gives index 3

To Solve this issue:
1.Separate Chaining 
    When a collision occurs, the new key-value pair is simply added to the list at that index
    Ex:self.table = [[] for _ in range(size)]
2. Open Addressing
    Instead of storing multiple values at one index, open addressing searches for 
    another empty index when a collision occurs.
    
     A. Linear Probing
        def linear_probe(self, key):
            index = self._hash(key)
            while self.table[index] is not None:  # Find an empty spot
                index = (index + 1) % self.size  # Move to the next index (circular)
            return index
            
     B. Quadratic Probing
        Instead of moving to the next slot, it moves farther away using squares (index + 1², index + 2², etc.).
            Example:
            index = (index + i^2) % self.size
    C.Double Hashing
        Uses a second hash function to determine the next position.
            Example:
            index = (hash1(key) + i * hash2(key)) % self.size
"""