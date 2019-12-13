#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This algorithm is O(n) the complexity will increase linearly for the value of n, if n= 1, [a= 0 , 1*1*1 = 1] so loop continues until next pass where a is set as 1, taking one complete pass, if n =2 then [a=0, 0< 2*2*2 =8] a is then set to 4 and the cycle repeats n=2 [a=4, 4 < 2^3 = 8]
so a is set to 4+2*2 or 8, thus ending the loop after 2 rounds. So as the value of n increases it will take a linearly increasing amount of time to run AKA O(n) 


b) O(n^2) loops when nested are always O(n^l) where l is the number of loops. in this case the l = 2 so O(n^2)


c) O(n) Linear time because with each recursive pass the n decreases by 1 until n = 0

## Exercise II

1. list floors ascending 
2. boolean for broken egg after droppend
3. start at middle list
5. while broken is false move floor index up
    5.1 Save non breaking floors in below f index 
4. if broken is true move floor index down
    4.1 save floor in index -1 as floor f

I believe this solution would be O(n)


