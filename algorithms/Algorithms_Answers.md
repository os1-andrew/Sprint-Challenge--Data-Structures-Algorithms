Add your answers to the Algorithms exercises here.

Exercise I:

	a) O(n^3)

	b) O(n^3)

	work:
	    sum = 0 
	    for (i = 0; i < n; i++)                 O(n)
	      for (j = i + 1; j < n; j++)           O(n-1) = O(n)
	        for (k = j + 1; k < n; k++)         O(n-2) = O(n)
	          for (l = k + 1; l < 10 + k; l++)  O(8)
	            sum++

	c) O(n) or O(bunnies)

Exercise II:

This question is trying to basically minimize the number of dropEgg() calls we have to make in order to find floor _f_. We can achieve this with log(n) efficiency.

let n = max floor of buidling
let f = current floor
let l = lowest floor where egg broke (set initially as the topmost floor of the building)

First we start at the middle floor(f = n//2) of the building and we drop an egg. If it breaks we note that down (l = f). Then, we go down to the halfway point between the current floor and the lobby (f = f/2). We drop an egg. If the egg doesn't break we go to the halfway point between the current floor and the last floor where the egg broke (f = f + (l-f)//2). If this is the first egg we dropped then the last floor would by default be the topmost floor. We drop an egg and continue this process following the same steps in response to the fate of the egg. 

We do this until, eventually, the egg doesn't break and the next floor that we need to go to is the current floor that we are on. This means that the egg has already broken on the floor above. This floor is the floor that the eggs are safe.

Finally, we retrieve the bucket in which we drop all the eggs. Filter the shell versus egg yolk/white and make breakfast for everyone minus vegans in the building.

PSEUDO CODE: I did this iteratively as opposed to recursively although both methods would work.

function droppEgg(n) -> Boolean:
	drop egg at floor n

	if egg breaks:
		return true:
	else:
		return false:

function findFloor(n) -> floor:
	current_floor = n//2
	last_break = n #arbitrary assignment. Initializes to top floor so it 			  doesn't start off as none
	while true:
		if dropEgg(current_floor): #if it breaks
			last_break = current_floor
			current_floor = current_floor//2
		else:
			next_floor = current_floor + (last_break - current_floor)//2
			if current_floor == next_floor:
				return current_floor
			current_floor = next_floor

	