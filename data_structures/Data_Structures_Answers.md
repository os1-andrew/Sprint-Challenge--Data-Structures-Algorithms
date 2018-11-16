Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
N/A

2. What is the space complexity of your `depth_first_for_each` function?
N/A

3. What is the runtime complexity of your `breadth_first_for_each` method?
O(n) because we are applying the anonymous function to each element in the data structure

4. What is the space complexity of your `breadth_first_for_each` method?
O(n) because we are making a recursive call once for each element in the data structure.

5. What is the runtime complexity of your `heapsort` function?
O(nlog(n))

Work:
O(n) to create the heap 
O(log n) to delete each item from the heap O(n) -> O(n log(n))
O(N) to reverse the results

O(2n + nlog(n)) or O(nlog(n))

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?

Part 1: O(n)
Work: O(2n) <-the output array and the heap itself
The original array is not included because it is not working memory of the algorithm.

Part2: O(n)
Work: O(2n) <- the althered array just the heap itself 
Even if you alter the array itself, you will need to account for the working storage needed to append to the new array.