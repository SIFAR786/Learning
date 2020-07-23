# name = input('what is your name? ')
# print('my name is ' + name)
# num = '01234567'
# print(num[::])
# print(type(num))
# print(num[0:len(num)])
# quote = 'to be or not to be'
# print(quote.upper())
# print(quote.lower())
# print(quote.capitalize())
# print(quote.title())
# print(quote.find('or'))
# print(quote.replace('be','me'))
# print(quote)
# var1={'a':'abc','b':'def'}	# dict
# var2=(1,2,3,4,5,6,7)	# tuple
# var3=[1,2,3,4,5,6,7]	# list
# var4={1,2,3,4,5,6,7}	# set

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
# print(1)
# print(0)
# print(True)
# print(False)
# print('True')
# print('False')

# _username = input('what is your username? : ')
# _password = input('what is your password? : ')
# _pass_len = len(_password)
# _hide_pass = '*' * _pass_len
# print(f'{_username}, your password {_hide_pass} is {_pass_len} letters long')

# ls = ['abc','def','ghi','jkl']
# ls_new = ls
# ls_new[0] = 'cat'
# ls_new1 = ls[:]
# ls_new1[2] = 'miki'
# print(ls_new)
# print(ls_new1)

''' Matrix 
		2D or multi-dimensional lists
'''
# matrix = [
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# 	]
# print(matrix[1][1])

# basket = [1,2,3,4,5]
# new_basket = basket.append(6)
# print(basket)
# print(new_basket)
# new_basket=basket
# print(new_basket)
# basket.insert(1,100)
# print(new_basket)
# print(basket)
# new_basket=basket.copy()
# new_basket.insert(2,200)
# print(new_basket)
# print(basket)
# basket.extend([11,22,33])
# print(basket)
# basket.remove(100) # removes element in-place if present
# print(basket)
# new_lst = basket.pop(4)	# removes element in-place at index but returns element name that was removed
# print(new_lst)
# print(basket)
# new_lst = basket.clear() # removes everything in basket in-place
# print(new_lst)
# print(basket)

basket = ['a','b','c','d','e']
print(basket.index('d'))