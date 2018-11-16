Add your answers to the Algorithms exercises here.

Exercise I:

	a) O(N^3)

	b) O(N^3)

	work:
	    sum = 0 
	    for (i = 0; i < n; i++)                 O(N)
	      for (j = i + 1; j < n; j++)           O(N-1) = O(N)
	        for (k = j + 1; k < n; k++)         O(N-2) = O(N)
	          for (l = k + 1; l < 10 + k; l++)  O(8)
	            sum++

	c) O(N) or O(bunnies)

Exercise II:

