class Array():
    
    def __init__(self, capacity=1):
        self.capacity = capacity # how many elements can this array hold? 
        self.storage = [None] * self.capacity #preallocated array
        self.count = 0 #this changes when we replace the preallocated 'None' with a different state.

    def __repr__(self):
        return f'{self.storage}'

    def destroy_list(self):
        self.storage = self.storage.clear()

    
    def resize_array(self):
        old_capacity = self.capacity
        new_capacity = self.capacity * 2
        self.capacity = new_capacity
        new_storage = self.storage #make copy of old storage
        
        # create a new array with double capacity
        for i in range(old_capacity):
            new_storage.append(None)
        self.storage = new_storage


        
    '''
    Return the element in the array at the given index. Throw an error if the index is out of range. 
    '''
    def read_index(self, index):
        #check if index is greater than count
        if index >= self.count:
            print(f'IndexError: Index {index} out of range\n')
            return None
        
        return self.storage[index]
    
    '''
    Insert value at given index. If index is greater than the count, throw an error. If the count is greater than or equal to capacity, resize the array. Don't forget to increase the count!

    '''

    def arr_insert(self, value, index):
        if index > self.count:
            print(f'IndexError: Index {index} out of range\n')
            return
        if self.capacity <= self.count:
            resize_array()
        
        for i in range(self.count, index, -1):
            self.storage[index] = self.storage[index - 1]

        # copy the value and add it to the array
        new_element = value
        self.storage[index] = new_element
        self.count += 1

    '''
    append item to end of array. remember that self.count keeps track of the last used index + 1
    '''
        
    def arr_append(self, value):
        self.arr_insert(value, self.count)

    def arr_remove(self, value): #searches for and removes given value
        removed = 0
        for i in range(self.count):
            if removed:
                self.storage[i - 1] = self.storage[i]
            elif self.storage[i] == value:
                del self.storage[i]
                removed = 1
        
        if(removed):
            self.count -= 1
            self.storage[self.count] = None
        else:
            print(f'ValueError: {value} not in array')
            return

    # pops the given index and returns it
    
    def arr_pop(self, index):
        if index >= self.count:
            print(f'IndexError: popped index {index} is out of range')
            return None
        
        return_value = self.storage[index]

        for i in range(index + 1, self.count):
            self.storage[i - 1] = self.storage[i]
        
        self.count -= 1
        self.storage[self.count] = None

        return return_value

    
# tests

array = Array(9)
array.resize_array()
print("arr", array)
array.arr_insert(23, 0)
print("after insert", array)
array.arr_insert(46, 1)
array.arr_insert(298, 2)
array.arr_insert(13, 3)
array.arr_insert(2, 4)
array.arr_insert(34, 5)
array.arr_insert(56, 6)
array.arr_insert(92, 7)
array.arr_insert(2111, 8)
array.arr_insert(21987, 9)
array.arr_insert(222, 10)
array.arr_insert(21, 11)
array.arr_insert(44, 12)
array.arr_append(67)
print(array)
array.arr_remove(21)
print(array)
array.arr_remove(21)
print(array)
returned_pop = array.arr_pop(4)
print(returned_pop)
print(array)




