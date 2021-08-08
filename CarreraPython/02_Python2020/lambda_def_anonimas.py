def main():

	palindrome = lambda string: string == string[::-1]
	print(palindrome('lateletal'))
	print(palindrome('qwertytrewq'))
	print(palindrome('pocololocop'))
	print(palindrome('google'))








if __name__ == '__main__':
	main()