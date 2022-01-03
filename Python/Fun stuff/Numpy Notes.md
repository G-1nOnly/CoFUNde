## Numpy Notes

1. #### **Creating numpy array**
   
   ```python
   A = np.array([1,2,3])
   # 1-d array
   ```

2. #### **Shape of the numpy array**
   
   ```python
   print(A.shape)
   # Return the shape in the form of (r,c) row × column 
   print(A.shape[0])
   # Row number
   print(A.shape[1])
   # Column number
   print(A.size)
   # Row × Column size of the stored values
   ```

3. #### **Creating special arrays**
   
   Note that the shape (2,2) could be changed !
   
   ```python
   a = np.zeros((2,2))
   # 2 × 2 zero matrix
   b = np.ones((2,2))
   # 2 × 2 mat# 2 × 2 matrix contains all 1rix contains all 1
   c = np.full((2,2), 3)
   # 2 × 2 matrix contains all 3
   d = np.eye(2)
   # 2-d Identity matrix
   e = np.random.random((2,2))
   # 2 × 2 matrix contains all random values in range(0,1)
   ```

4. #### **Array indexing**
   
   Note that the index starts from **0**, and the slicing is **end-point exclusive**.
   
   ```python
   a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
   b = a[:2, 1:3]
   print(b)
   # :2 here means from the first two rows
   # 1:3 here means the column1 and column2
   # b would be  
   # [[2 3]
   #  [6 7]]
   
   print(a[[1,2],1)
   # Print the element1 and element2 of the second row
   print(a[1, :])
   # Print the second row of a
   print(a[:, 1])
   # Print the second column of a
   
   c = np.arange(5)
   # Creates an array [0,1,2,3,4]
   
   # Boolean Indexing
   np_arr = np.array([[1,2], [3, 4], [5, 6]])
   print(np_arr[np_arr > 2])
   # The result would be [3,4,5,6]
   ```

5. #### **Data type**
   
   ```python
   a = np.array([1, 2], dtype=np.int64)
   # Force the type to be int
   ```

6. #### **Numpy Math**
   
   Apart from 
   
   ```python
   # Elementwise computation
   np.add()
   np.substract()
   np.multiply()
   np.divide()
   
   # Matrix manipulation
   np.dot()
   np.outer()
   @ # The same as np.dot(), usage A@B
   # Note that A*B would be element-wise operation
   
   np.sum(a)
   # Sum all the element 
   np.sum(a, axis = 0)
   # Sum by each column
   np.sum(a, axis = 1)
   # Sum by each row
   np.sum(a, axis = 1, keepdims=True)
   # Sum by each row and keep the dimension
   ```

7. #### **Broadcasting**
   
   ```python
   a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
   np.empty_like(a)
   # Create an empty matrix with the same shape as a
   
   x = np.array([1,2,3])
   np.tile(x, (4, 1))
   # Stack 4 copies of x on top of each other
   # view x as an element, the shape would be (4,1)
   # Result would be 
    # [[1 2 3]
    #  [1 2 3]
    #  [1 2 3]
    #  [1 2 3]]"
   
   y = x + 1
   # The result would be [2,3,4]
   # Here, 1 first would be broadcasted to be [1,1,1] and then added
   z = np.array([[1,2,3],[1,2,3],[1,2,3]])
   z = z + x
   # The result woule be [[2,4,6],
   #                      [2,4,6],
   #                      [2,4,6]]
   # Here, [1,2,3] would be broadcasted to be 3 × 3 shape and then added.
   ```

The **rules** for broadcasting two arrays:

- If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
- The two arrays are said to be **compatible in a dimension** if they have the same size in the dimension, or if one of the arrays has size **1** in that dimension.
- The arrays can be broadcast together if they are compatible in **all dimensions.**
- After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
- In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension.

**e.g.**

    A:8×7×6×5  B: 1×6×1 A+B √  

    B could be broadcasted and then added



    A:3×2×4  B:2×3 A+B × 

    B could not be broadcasted due to incompatible dimension 

8. #### **Reshape**
   
   ```python
   x = np.array([[1,2,3], [4,5,6]])
   x = x.reshape((3,2))
   # The shape of x would be reshaped into (3,2)
   ```




























