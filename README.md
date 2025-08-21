# rankensemblesig
Calculates p-values assocaited with an enemble of ranks.

rankensemblesig is a python packages that takes a set of ranks and outputs the probability associated with observing those ranks due to chance. 

#Example:
Supoose there are four nearby lunch spots and you need to decide which to choose for a lunch date with your friends. You send out a poll and ask your friends to rank their preferences, yielding the following table:
Friend|	Sandwiches | Tacos | Noodles |	Pizza |
| ---- | ---- | ----- | ----- | ----- |
| A | 1 |	3 | 4 | 2 |
| B | 4	| 1 | 3 | 2 |
| C | 2 | 3 | 4 | 1 |
| D | 4 | 2 | 3 | 1 |
| E | 4 | 3 | 1 | 2 |


If you add up the ranks Pizza is the winner. But lets say you prefer tacos, and you want to know if the ranks given to Pizza might just be due to chance. This might seem like a pretty straightforward calculation: the chance of getting rank 1 at chance is 1/4, and chance at least rank 2 is 1/2, so you just multiply the probably of each rank together to get 1/2 * 1/2 * 1/4 * 1/4 * 1/2 =  1/128, which is pretty low. However, there are two reasons why this is wrong.
First, we're not really interested in Pizza specifically. If Sandwiches was the most highly ranked food we would be focusing on Sandwiches. So we're not interesting in the probability of observing the ranks of Pizza, but in the probability of observing any feature with the ranks seen in Pizza. 
Second, ranks of features are inherently depedent on each other. If someone assigns Tacos rank 3 they can't also assign Pizza rank 3.
In short, we have to adjust for multiple observations and the fact that observations are dependent on each other.
For feature i out of n total features (making the highest rank n), and samples j:

$p(r_j) =(n!)^{-s}\displaystyle\sum_{k=1}^{min(r_i)} (-1)^{(k+1)}{n \choose k} \displaystyle\prod_{j=1} {r_{ij} \choose k} k! (n - k)!$
