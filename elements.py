'''
 Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''

n = int(input("Enter the number of values: "))  
values = []
for _ in range(n):
    values.append(int(input()))
unique_values = set(values)
duplicate_count = len(values) - len(unique_values)
print(f"Duplicate Values: {duplicate_count}")
print(" ".join(map(str, unique_values)))
