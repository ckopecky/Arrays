# Arrays

Arrays are the most common and perhaps the simplest of the data structures. Is it really so simple, though? 

High-level languages like Python and Javascript all have built-in "magic" that hides the complexity of the many array methods. Although the complexity is hidden, you still have to pay the performance costs of that complexity. 

You will be implementing a high-level array functionality from the ground up. You will construct methods from memory and pointers to create, destroy, read and write arrays. Then, you will write code to add and remove elements from your array. 

By the end of this assignment, you will gain much appreciation for the magic of high-level coding languages as well as a deeper understanding of the costs associated with their functionality. 

#### Part 1: Create, Read, Destroy and Append

You are given the skeleton of an array implementation in Python for which you will be responsible for filling out. Start by reviewing the Array class, then fill out the following functions: 

1. `create_array()`
2. `destroy_array()`
3. `arr_append()`
4. `arr_read()`

Create and destory should be self-explanatory: Initialize your array values and allocate memory on creation, then free that memory on destruction. 

Reading from the array is simple as well: Check if the given index is in range and then return the value at that index. 

`arr_append()` should work like Python's `append` method: Insert an element to the end of the array. Note that you will only be able to add as many elements as you allocated space for when you created the array. 


#### Part 2: Insert, Delete and Resize

Insertion and deletion should work like the Python `insert() `and `remove()` list methods. 

Insert should let you add an element to an arbitrary index in the array and delete should look for the first instance of the provided element and remove it.

 Remember that arrays require each element to be side-by-side like a bookshelf so you will need to move each element after the given index to the right or left for insert/delete respectively.

Resizing involves allocating a block of memory with double the storage, copying elements from the old block to the new, and freeing the old block. 

You should automatically resize when an insert or append takes your array past the allocated capacity.

`arr_insert()`

`arr_remove()`

`resize_array()`

#### Stretch Goals
Reimplement your Dynamic Array using a linked list instead of a contiguous array (or if you used a linked list in the first place, use a contiguous array).

 How does the time complexity of each operation change as a result of swapping out the underlying data structure?

How would we go about making our dynamic array be able to handle multiple types in a single instance? Hint: we'll probably want to make use of C unions for this. Think about how you might do this and then implement it!

If you finish these goals, try implementing some of the other Python functions:

`clear()`

`copy()`

`extend()`

`index()`

`pop()`

`reverse()`

`sort()`

Check the official documentation or use Python's `help()` method for implementation details.



