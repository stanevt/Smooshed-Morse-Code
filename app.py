from collections import defaultdict
import pprint as pp
import time 


def smorse(seq):
	cipher = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", 
	".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
	encoded = ""
	for ch in seq:
		index = ord(ch)-97
		encoded += cipher[index]
	
	return encoded

def buildLexicon(vocab):
	lexicon = defaultdict(list)
	for word in vocab:
		word = word.lower().strip()
		encoded = smorse(word)
		lexicon[encoded].append(word)
	return lexicon

def mostAmbiguous(lexicon):
	length = 13
	result = [x for x in lexicon.items() if  len(x[1]) == length]
	print("===Most ambiguous===")
	pp.pprint(result)

def mostConsecutiveDashes(lexicon):
	length = 15
	dashes = [x for x in lexicon.items() if len(list(filter(lambda y: len(y) == length, x[0].split('.')))) > 0]
	print("===Most consecutive dashes===")
	pp.pprint(dashes)


def perfectBalance(lexicon):
	length = 21
	balance = [x for x in lexicon.items() if (x[0].count('-') == x[0].count('.')) and len(list(filter(lambda y: len(y) == length, x[1]))) > 0]
	print("===Max Balanced===")
	pp.pprint(balance)
		
def isPalindrome(seq):
	if len(seq) % 2 != 0:
		mid = int(len(seq)/2)
		seq = seq[:mid] + seq[mid+1:]
	mid = int(len(seq)/2)
	return seq[:mid] == seq[mid:][::-1]
	

def checkPalindrome(lexicon):
	length = 13
	palindromes = sorted([ x for x in lexicon.items() if isPalindrome(x[0]) and len(list(filter(lambda y: len(y) == length, x[1]))) > 0], key = lambda x: max(x[1], key = len))
	print("===Palindrome===")
	pp.pprint(palindromes)


def bothPalindrome(lexicon):
	palindromes = [ (x, [p for p in y if isPalindrome(p)]) for x, y in lexicon.items() if isPalindrome(x) and len(list(filter(lambda word: isPalindrome(word), y))) > 0]
	print("===Both Palindrome===")
	pp.pprint(palindromes)
	
	
	
vocab = []
with open("vocab.txt", "r") as r:
	for word in r:
		vocab.append(word)
lexicon = buildLexicon(vocab)

s = time.time()
mostAmbiguous(lexicon)
mostConsecutiveDashes(lexicon)
perfectBalance(lexicon)
checkPalindrome(lexicon)
bothPalindrome(lexicon)
e = time.time()
print("Running time {}".format(e - s))