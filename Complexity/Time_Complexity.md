## Time Complexity

`square function`

> square01

This function uses the smiplest loop to realize square function.

> square02

This function uses the recursion to realize the square function. But it recurse one by one, just like the revised loop, low efficiency. This method will exceed the deepest recursion.

> square03

This function uses the tree like recursion by separating each stage and recurse back.

However, the tree's nodes increase exponentially as the stages go down. The complexity of the algorithm is *the summary of the tree's nodes*. That is $2^m+2^{m-1}+\cdots+2^{2}+2^1+2^0=2^{m+1}-1$. Therefore, the **complexity** is still O(n).

> square04

This function separates the square index by decomposing the index into the multiplies of numbers. The recursion can done this task very efficiently. 

Write the recursion outside the calculation so that it will not be called for several times and forms a tree like calculation. Still implement the square03's idea here. Thus, the times is divided into half accordingly.

> ***Result***

For the times 10000, raw numbers range from 1 to 10, the time consumed is shown below:

![image-20201212004530262](/Users/organicsoul/Library/Application Support/typora-user-images/image-20201212004530262.png)