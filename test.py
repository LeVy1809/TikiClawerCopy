cal = '''
 _______________________
/_____________________/ |
|        CASIO        | |
|  _________________  | |
| | JO           0. | | |
| |_________________| | |
|  ___ ___ ___   ___| | | 
| |SHI|DEL|AC | |ON | | |
| |___|___|___| |___| | |
| | 7 | 8 | 9 | | + | | |
| |___|___|___| |___| | |
| | 4 | 5 | 6 | | - | | |
| |___|___|___| |___| | |
| | 1 | 2 | 3 | | x | | |
| |___|___|___| |___| | |
| | . | 0 | = | | / | | |
| |___|___|___| |___| | |
|                     | | 
|_____________________|/
'''
raw = cal[116:124]
user = input()
result = eval(user)
new_cal = cal.replace(raw, f' {result:.2f} ')
print(new_cal)