"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .
"""


def method_a():
    happiness = 0
    for i in arr:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
    return happiness


def method_b():
    happiness = 0
    for i in a:
        if i in arr:
            happiness += 1
    for i in b:
        if i in arr:
            happiness -= 1
    return happiness


def method_c():
    """

    True-False
    Out[61]: 1

    False-True
    Out[62]: -1

    """
    return sum([(i in a) - (i in b) for i in arr])


if __name__ == '__main__':
    n, m = input().split()
    arr = input().split()
    a, b = input().split(), input().split()
    a, b, arr = set(a), set(b), tuple(arr)
    # Above line makes the code fast

    print(method_a())
    # print(method_b())
    # print(method_c())
    '''
    %timeit method_a()
    451 ns ± 15.8 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
    %timeit method_b()
    592 ns ± 18.5 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each
    %timeit method_c()
    938 ns ± 75.9 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
    '''