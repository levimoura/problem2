How to run the software

To run the software you should start the server e go to your browser and localhost:8080/result
I was unable to set a form to make the file upload without the use of an external server so you
have to put the file with the name 'arquivo.txt' under the problem2 folder.


I have assumed that the text file conatains only one array of data and that there are no spaces.

The design was focused on simplicity, the softwares breaks the string imported from the file and
breaks it on the ',' than the new array is passed to a function that will iterate trough it in 
order to solve the problem itself, wich will than return a webpage with the result.
