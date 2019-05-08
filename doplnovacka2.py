"""
doplnovacka.py 
Moje kamarádka učí soukromě němčinu.
Potřebuje pro klienty připravit texty, které se časem naučí nazpaměň (jedná se o právní předpisy).
Proto jim připravuje stále stejný text, ve kterém vynechá nejprve každé 5. slovo,
později každé 4. slovo atd., až se text naučí zpaměti.
Výstupem bude nový soubor. Pracujte se souborem lorem.py.

Vytvořte pro ni program, jehož vstupem bude textový soubor a informace, kolikátý znak se má zaměnit.

Rozbor 
1) načíst soubor
2) splitnout slova podle mezery do seznamu
3) procházet jednotlivá slova seznamu
	když se jedná o x-té slovo:
	procházet písmenka a:
		písmenko nahradit pomlčkou
		vynechat interpunkci
	upravené slovo přidat do seznamu
	jinak:
		původní slovo přidat do seznamu
4) seznam spojit pomocí mezery do řetězce, řetězec uložit do nového souboru
"""
print("Vitej v programu, ktery ti pomuze naucit se jakykoliv text diky nahrazovani danych slov! :)")

input_file = input("Vloz soubor (i s priponou): ")
erase =  int(input("Kolikate slovo chces zamenit za '*': "))

def nahrazovani():
	lst = []
	lst = text.split(" ")

	result = []
	punctuation = ".,?!-;\""

	for i in range(0, len(lst)):
		word = lst[i]
		modified_word = ""
		if ((i + 1) % erase == 0):
			for letter in word:
				if letter not in punctuation:
					modified_word += "*"
				else:
					modified_word += letter
			result.append(modified_word)
		else:
			result.append(word)

	s = " ".join(result)
	print(s)


with open(input_file) as f:
	text = f.read()
f.closed
nahrazovani()