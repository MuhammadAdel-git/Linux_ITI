while True:
	#Which calculator mode is wanted
	calc_type=str(input('plz choose calculator type: s for (standard mode) or p for (programmer mode) !\n'))
	
	#if standard
	if calc_type == 's':
		op=str(input('plz choose: +, -, *, /, %, power  \n'))
		a= int(input('plz enter the first number \n'))
		b=int(input('plz enter the second number \n'))
		mydict= {'+': a+b,
				 '-': a-b,
				 '*': a*b,
				 '/': a/b,
				 '%': a%b,
				 'power': a**b,
				}
		if op=='+':
			print('{} + {} = {}'.format(a,b,mydict.get('+')))

		elif op=='-':
			print('{} - {} = {}'.format(a,b,mydict.get('-')))
		
		elif op=='*':
			print('{} * {} = {}'.format(a,b,mydict.get('*')))
		
		elif op=='/':
				print('{} / {} = {}'.format(a,b,mydict['/']))
				
		elif op=='%':
				print('{} % {} = {}'.format(a,b,mydict.get('%')))
				
		elif op=='power':
				print('{} ^ {} = {} '.format(a,b,mydict.get('power')))

	#if programmer
	elif calc_type=='p':

			print("1: for bin")
			print("2: for oct")
			print("3: for hex")
			print("4: for OR")
			print("5: for NOT")
			print("6: for AND")
			print("7: for XOR")
			op=str(input('plz choose a number from above\n'))
			a=int(input('plz enter a number !\n'))
			mydict1= {'1': bin(a),
					  '2': oct(a),
					  '3': hex(a),
					 }
			if op== '1':
				print('dec : {} >> bin : {}'.format(a,mydict1.get('1')))
			elif op== '2':
				print('dec : {} >> oct : {}'.format(a,mydict1.get('2')))
			elif op== '3':
				print('dec : {} >> hex : {}'.format(a,mydict1.get('3')))
			elif op== '4':
				print('{} OR {} = {}'.format(a,b,a|b))
				b=int(input('plz enter a second number\n'))
			elif op== '5':
				print('NOT {} = {}'.format(a,~a))
			elif op== '6':
				b=int(input('plz enter a second number\n'))
				print('{} AND {} = {}'.format(a,b,a&b))
			elif op== '7':
				b=int(input('plz enter a second number\n'))
				print('{} XOR {} = {}'.format(a,b,a|b))
				
	# if anymore calculation is wanted
	anymore = input("Do you want another calculation? (y/n): \n")
	if anymore == "n":
		break