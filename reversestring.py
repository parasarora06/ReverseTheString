from colorama import Fore, Back, Style 
Input_from_user=raw_input(Fore.RED + "Enter the string : "+ Fore.GREEN + ' ')
Store_input=(Fore.GREEN + Input_from_user[::-1])
z=(Fore.RED + 'ReversedString: ')
SolvedString= z +Store_input
print(SolvedString)
