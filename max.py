'''
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''

input_values = input().strip()
values_set = set(map(int, input_values.split()))
max_value = max(values_set)
min_value = min(values_set)
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
