#Using the scripting language of your choice, write a script that adds “Hello World” to a new line at the end of a text file, and then saves that file.
# A path to the text file should be provided to the script by an argument given at runtime (e.g. hello.sh path/to/file.txt).

#Open the file with access mode 'a' to append
edit_file = open('sample.txt', 'a')

#Add a new line that says "Hello World"
edit_file.write("\nHello World")

#Save and close the file
edit_file.close()

print("New line added to sample.txt")
