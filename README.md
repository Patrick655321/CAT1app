# Welcome to the Roster-Right App, created in 2022 by Patrick Hamer of the Coder Academy.

## HELP
This documeent is aimed at explaining to educators how I met requirements for the rubric. For help file type
```
open_rr.sh help
```
or if using windows access the **windows_help.md** file.

## R4 Provide a link to your source control repository
My source control repository can be found at the following URL:
[Patrick on Github](https://github.com/Patrick655321/CAT1app)

## R5 Identify any style guide or styling conventions that the application will adhere to:  
## Reference the chosen style guide appropriately.
For this app I have used the **PEP 8 – Style Guide for Python Code** by Guido van Rossum, Barry Warsaw and Nick Coghlan. See reference section for further information.

## R6 Develop a list of features that will be included in the application:  
### Navigate a main menu
Using functions and variables the program allows users to select from a list at the beginning, returning them to it whenever they have completed their task until they type exit. This is done using a combination of variables (for the menu items themselves) and loops (once in the secondary functions)
Once an item has been selected the a variable is created and while that value is not equal to "N" the loop will repeat the task, from input to return. At the end of each loop or if an error is encountered the user is given the option to continue, or to change stop, which changes the initial variable which in turn clears the screen and starts at the main menu again.

### Edit a roster template:
Staff can be added or removed from shift. Using a series of questions the correct nested dictionarty is located and the staff are either added to a list within or removed depending on the request. Using if statements the program will check to see if the staff exist and if the staff are where they are expected to be in the database. This prevents errors from trying to remove a staff member from a shift they are not working, Add a staff member that doesn't exist, etc.

### Save roster to an external file:
To be able to print this information the progrom will save the roster to a .csv file so it can be stored either locally or on google drive. This is done by importing 'csv' to the code and then using the csv.writer command to create a file that will be readable by both wexcel and Google Drive.

### Create staff profiles
Given that staff cannot be added without profiles the user has the ability to create new staff profiles within the program, allowing new people to be introduced into the system. This creates a new staff member as the key in a dictionary with their details being the value

### Error handling
The extensive use of dictionaries led to a lot of KeyError issues while testing, so this has been compensated for with try/except code, ensuring the app doesn't crash if invalid data is entered.
Also the use of proper nouns was a large issue. All data is now stored in lower case with all necessary inputs directed to be lowercase as well to avoid throwing up errors as the user navigates the program.

R5	
Identify any code style guide or styling conventions that the application will adhere to.

### R7	Implementation Plan:
https://trello.com/b/03VIOMyB/rosterright



## References

G. Rossum, B. Warsaw & M. Coghlan, 2001, PEP 8 – Style Guide for Python Code, 21/07/2022, https://peps.python.org/pep-0008/#imports
