Let's start by looking at the recurrence relation of the non-random pivot quicksort in order to estimate its average runtime complexity.
Let's start by looking at the recurrence relation of the non-random pivot quicksort in order to estimate its average runtime complexity.
In this version, the array's final element is frequently chosen as the pivot due to deterministic pivot selection. Let's write n as the length of the array.
For this quicksort variation, the recurrence relation is written as follows:
T(n)=T(k)+T(n-k-1)+O(n)
In this case, the time required to sort an array of size n is denoted by T(n).
The index at which the pivot settles following partitioning is denoted by k. The partitioning step, in which we divide the array around the selected pivot by traversing it once, is where the O(n) phrasoriginates.
T(n)=T(n/2)+T(n/2)+O(n)
Let's now investigate the typical case complexity. In this case, we suppose that the array is divided into roughly equal pieces by the pivot. 






