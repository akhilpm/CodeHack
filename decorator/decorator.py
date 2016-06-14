def paragraphize(inputFunction):
	def newFunction():
		return "<p>" + inputFunction() + "</p>"
	return newFunction

@paragraphize
def getText():
	return "Here is some text!"

@paragraphize
def getAnotherText():
	return "Here is another text!"

def main():
	print getText()
	print getAnotherText()

if __name__ == '__main__':
	main()
