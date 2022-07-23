# TESTING THE ROSTERING APP

Testing this app was essentially a matter of testing hte logic with mroe and more different variables to try and find holes in it. This program relies heavily on input from the user and so this was a major source of frustration throughout the testing process:

Test 1: The user input/spelling errors
Understanding that there are myriad ways in which a user could input information into this app I went through each form of user input and tested. First I would type in lower case, then upper, then a mixture of both.
After that I would attempt to enter words I knew were incompatible with the program or random strings of letters. Through doing this I quickly learned many, many differnet ways in which the user could shut the program down with the slip of a finge. One of hte more amusing tests was:
#### Remove staff test:
I had completed most of the app and was testing the different features. No matter what I did I could no longer remove staff, no matter how I typed their name into the remove feature. I had expected if anything that I had a glitch in my remove_staff code and that if I typed lower case the issue would be fixed but this was not the case. It turns out I had at some point taken out the str.lower() part of the add_staff function and thus staff I had entered with capital letters into the roster had stayed.
#### Funnel_info
This was a headache. I initially had 3 questions requiring user input. I tried to create a function for these to make my code DRYer, but was unable to yield any results.
What I had expected was that in creating a function where the 'return' was 3 variables and then using that function within a function further along I would be able to use the 3 returned variables. This did not work.
I then created global variables hoping that if I had the variables from the get-go then they would be found, changed and be able to be used (seeing as they were global). This was also not the case.
Eventually I spoke to the educators and witht their help and a bit of thinking on my end I was able to sort the issue out by creating a funnel_info() function and then returning a variable that was a list, later on referencing the different list indices to allow for the information to be transferred. This was a steep learning curve as it took over a day for me to get on top of!

Below is a picture of my test-log.