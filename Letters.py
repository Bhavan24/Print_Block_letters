letters = {
'A' : ["  A  "," A A ","A   A","AAAAA","A   A","A   A","A   A"],
'B' : ["BBBB ","B   B","B   B","BBBB ","B   B","B   B","BBBB "],
'C' : [" CCC ","C   C","C    ","C    ","C    ","C   C"," CCC "],
'D' : ["DDDD ","D   D","D   D","D   D","D   D","D   D","DDDD "],
'E' : ["EEEEE","E    ","E    ","EEEEE","E    ","E    ","EEEEE"],
'F' : ["FFFFF","F    ","F    ","FFFFF","F    ","F    ","F    "],
'G' : [" GGG ","G    ","G    ","G GGG","G   G","G   G"," GGG "],
'H' : ["H   H","H   H","H   H","HHHHH","H   H","H   H","H   H"],
'I' : ["IIIII","  I  ","  I  ","  I  ","  I  ","  I  ","IIIII"],
'J' : [" JJJJ","    J","    J","    J","    J","J   J"," JJJ "],
'K' : ["K   K","K  K ","K K  ","KK   ","K K  ","K  K ","K   K"],
'L' : ["L    ","L    ","L    ","L    ","L    ","L    ","LLLLL"],
'M' : ["M   M","MM MM","M M M","M   M","M   M","M   M","M   M"],
'N' : ["N   N","N   N","NN  N","N N N","N  NN","N   N","N   N"],
'O' : [" OOO ","O   O","O   O","O   O","O   O","O   O"," OOO "],
'P' : ["PPPP ","P   P","P   P","PPPP ","P    ","P    ","P    "],
'Q' : [" QQQ ","Q   Q","Q   Q","Q   Q","Q   Q"," QQQ ","    Q"],
'R' : ["RRRR ","R   R","R   R","RRRR ","R R  ","R  R ","R   R"],
'S' : [" SSSS","S    ","S    "," SSS ","    S","    S","SSSS "],
'T' : ["TTTTT","  T  ","  T  ","  T  ","  T  ","  T  ","  T  "],
'U' : ["U   U","U   U","U   U","U   U","U   U","U   U"," UUU "],
'V' : ["V   V","V   V","V   V","V   V","V   V"," V V ","  V  "],
'W' : ["W   W","W   W","W   W","W   W","W W W","WW WW","W   W"],
'X' : ["X   X","X   X"," X X ","  X  "," X X ","X   X","X   X"],
'Y' : ["Y   Y"," Y Y ","  Y  ","  Y  ","  Y  ","  Y  ","  Y  "],
'Z' : ["ZZZZZ","    Z","   Z ","  Z  "," Z   ","Z    ","ZZZZZ"],
'SP' : ["    ","    ","    ","    ","    ","    ","    "],
"1" : ['  1  ', '1 1  ', '  1  ', '  1  ', '  1  ', '  1  ', '11111'],
"2" : ['22222', '    2', '    2', '22222', '2    ', '2    ', '22222'],
"3" : ['33333', '    3', '    3', '33333', '    3', '    3', '33333'],
"4" : ['4   4', '4   4', '4   4', '44444', '    4', '    4', '    4'],
"5" : ['55555', '5    ', '5    ', '55555', '    5', '    5', '55555'],
"6" : ['66666', '6    ', '6    ', '66666', '6   6', '6   6', '66666'],
"7" : ['77777', '    7', '    7', '    7', '    7', '    7', '    7'],
"8" : ['88888', '8   8', '8   8', '88888', '8   8', '8   8', '88888'],
"9" : ['99999', '9   9', '9   9', '99999', '    9', '    9', '99999'],
"0" : ['00000', '0   0', '0   0', '0   0', '0   0', '0   0', '00000'],
}

while True:
	user_text = input("Enter your text: ")
	string = user_text.upper()
	print()	
	for j in range(0,7,1):
		for i in string:
			if i == " ":
				print(letters['SP'][j], end=" ")
			else:
				print(letters[i][j], end=" ")
		print()
	if input("\nDo you want to continue? (y/n): ") == "n":
		break