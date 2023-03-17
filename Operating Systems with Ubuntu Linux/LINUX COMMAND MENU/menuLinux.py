import os
import time

option=0
activeMenu=1
ending="\n-------------- FINALIZANDO COMANDO --------------"
menu="""
-- STARTING LINUX COMMAND MENU --

1. Find the largest file in D2 and the smallest file in D1.
2. Compare the files in the two directories (D1 and D2) and show the most recent and oldest.
3. Copy the contents of file2.txt into file3.txt.
4. Count the number of occurrences of the letters "r" and "R" in a file in D1.
5. Change the permissions of a file to executable only.
6. Change the owner and group of a file in D2.
7. Create a script to rename file4.txt.
8. Encrypt and decrypt file1.txt.
9. Quit.
"""
while activeMenu==1:
	if os.path.isdir('/home/jorgesarricolea/PRAXIS/D1'):
		time.sleep(1)
		print(menu)
		option = int(input("Select an option by typing the number: "))
		print("\n-------------------------------------------------")
		if option == 1:
			print("\nShowing list of files in D1: \n")
			time.sleep(1)
			os.system('ls -l D1')
			print("\nThe smallest file in D1 is: ")
			time.sleep(1)
			os.system('ls -Sr D1 | head -1')
			time.sleep(1)
			print("\nShowing list of files in D2:\n")
			time.sleep(1)
			os.system('ls -l D2')
			time.sleep(1)
			print("\nThe largest file in D2 is: ")
			time.sleep(1)
			os.system('find D2 -type f | sort -n | tail -1')
			print(ending)
		elif option == 2:
			time.sleep(1)
			print("\n")
			os.system('./compareFiles.sh')
			time.sleep(1)
			print(ending)
		elif option == 3:
			print("\nContent of file2: ")
			time.sleep(1)
			os.system('cat D1/file2.txt')
			time.sleep(1)
			print("\nContent of file3 before copying: ")
			time.sleep(1)
			os.system('cat D1/file3.txt')
			time.sleep(1)
			print("\nContent of file3 after copying: ")
			time.sleep(1)
			os.system('cat D1/file2.txt >> D1/file3.txt')
			time.sleep(1)
			os.system('cat D1/file3.txt')
			time.sleep(1)
			print(ending)
		elif option == 4:
			print("\nShowing content of file3.txt")
			time.sleep(1)
			os.system('cat D1/file3.txt')
			time.sleep(1)
			os.system('cat D1/archivo3.txt | grep -o "r"')
			time.sleep(1)
			print(ending)
		elif option == 5:
			print("\nShowing permissions of files in D1. File to modify: file1.txt")
			time.sleep(1)
			os.system('ls -l D1')
			time.sleep(1)
			os.system('chmod +x D1/file1.txt')
			os.system('chmod -w D1/file1.txt')
			os.system('chmod -r D1/file1.txt')
			time.sleep(1)
			print("\nfile1.txt modified:")
			time.sleep(1)
			os.system('ls -l D1')
			time.sleep(1)
			print(ending)
		elif option == 6:
			print("\nShowing owners of files in D2. File to modify: file5.txt")
			os.system('ls -l D2')
			print("\file5.txt Owner modified:")
			os.system('chown jorge D2/archivo5.txt')
			os.system('chown jorge:students D2/file5.txt')
			os.system('ls -l D2')
			print(ending)
		elif option == 7:
			os.system('./changeName.sh')
			print(ending)
		elif option == 8:
			print("\nShowing files in D1:")
			time.sleep(1)
			os.system('ls -l D1')
			os.system('ccrypt -e D1/file1.txt')
			print("\nShowing encrypted file1.txt")
			time.sleep(1)
			os.system('ls -l D1')
			print("\nDecrypting file1.txt")
			time.sleep(1)
			os.system('ccrypt -d D1/file1.txt.cpt')
			os.system('ls -l D1')
			time.sleep(1)
			print(ending)
		elif option == 9:
			print("\n---------------  END  ---------------")
			activeMenu=0
	else:
		os.system('mkdir D1')
		os.system('mkdir D2')
		print("To start the menu, two directories (D1 and D2) have been created. D1 with 3 files and D2 with 2 files. Press enter and then ctrl + D when you finish inputting the content of each one.")
		print("Escribe el contenido del archivo1: ")
		print("Enter the content of file1: ")
		os.system('cat > D1/file1.txt')
		print("Enter the content of file2: ")
		os.system('cat > D1/file2.txt')
		print("Enter the content of file3: ")
		os.system('cat > D1/file3.txt')
		print("Enter the content of file4: ")
		os.system('cat > D2/file4.txt')
		print("Enter the content of file5: ")
		os.system('cat > D2/file5.txt')
		print("Two directories have been created: D1 with 3 txt files and D2 with 2 txt files.")