# Example 1
print('L {:<20} R'.format('x'))
# Example 2
print('L {:^20} R'.format('x'))
# Example 3
print('L {:>20} R'.format('x'))

print()
# Example 1
print('{:<10}:{}'.format('Iofi','Over'))
# Example 2
print('{:<10}:{}'.format('bignameone','bigtime1'))
# Example 3
print('{:<10}:{}'.format('a','0'))

from prettytable import PrettyTable

l = [["Hassan", 21, "LUMS"], ["Ali", 22, "FAST"], ["Ahmed", 23, "UET"]]

table = PrettyTable(['Name', 'Age', 'University'])

for rec in l:
    table.add_row(rec)

print(table)