Consecutive birthdays probability
=================================

Let n be a number of people. At least two of them may be born on the same day of the year with probability:
1 − ∏_{i=0}^{n−1} (365−i)/365

But what is the probability that at least two of them are born on two consecutive days of the year (considering December 31st and January 1st also consecutive)? Simulating pseudo-random integers with Python, we get a 99%-confidence interval for any number of people. It seems a good approximation is:
(1 − (n−1)(2×365+n−1)) × (1 − ∏_{i=0}^{n−1} (365−2*i)/365)

Here is the correct formula:
1 − ∑_{k=1}^{n} 1/((365^(n−k))*k) × (∏_{i=1}^{k−1} (365−(k+i))/(365×i)) × (∑_{j=0}^{k−1}(−1)^j C_j^k (k−j)^n)

An explanation can be found here:
http://math.stackexchange.com/questions/18268/consecutive-birthdays-probability/18363#18363
