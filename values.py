'''
 Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.
'''

set1_input = input().strip()
set1 = set(map(int, set1_input.split()))
set2_input = input().strip()
set2 = set(map(int, set2_input.split()))
common_values = set1 & set2
sorted_common_values = sorted(common_values)
print(" ".join(map(str, sorted_common_values)) + " ")
