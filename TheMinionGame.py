"""
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.
"""

from itertools import combinations


def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    cons_words = {}
    vow_words = {}

    combs = [combinations(string, i) for i in range(1, len(string)+1)]
    combs = [[''.join(i) for i in comb] for comb in combs]
    temp = list()
    for i in combs:
        temp.extend(i)
    # combs = set(temp)
    combs = temp
    # for i in string:
    #     combs.extend(i)

    for i in combs:
        if i[0] in 'AEIOUaeiou':
            vow_words[i] = vow_words.get(i, 0) + 1
        else:
            cons_words[i] = cons_words.get(i, 0) + 1

    for i in cons_words.values():
        stuart_score += i
    for i in vow_words.values():
        kevin_score += i
    print('Kevin ', kevin_score) if kevin_score > stuart_score else \
        print('Stuart ', stuart_score) if kevin_score != stuart_score else \
            print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
