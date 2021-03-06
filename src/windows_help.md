- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application

# How to use RosterRight

The purpose of RosterRight is to allow the user to create and manipulate a simple roster for a cafe/bar. Shifts are spereated into days and divided but day/night then within these divided further into the role which will be required (bar, restaurant, manager). Staff details can be stored and there is an ability to create an external roster file for the purposes of printing/emailing information to other users.

### System Requirements
To use RosterRight you will need to have [Python 3](https://www.python.org/downloads/) installed
If the link fails please copy and paste the URL below to be directed to the official download page.
https://www.python.org/downloads/

Other system requirements are a Command Line prompt and a keyboard with which to operate it. The libraries used in this app are all standard with Python 3 HOWEVER if required they are:
- csv
- time
- os
- group (included with app)
- schedule (indluded with app)

### Installation:

You will need to create a clone of the [github repository](https://github.com/Patrick655321/CAT1app).
To do this simply create an empty directory in which you would like the program stored, change in to that directory and then type:
```
git clone git@github.com:Patrick655321/CAT1app.git
```
After this it is a simple matter of changing into the
```
CAT1app
```
directory created by the clone and then typing
```
open_rr.sh
```

### Using the app

Once in the app the process is linear. You will be greeted with a menu which will allow you to select an option.
Follow the prompts on the screen to guide you through the process of adding/removing staff and viewing rosters.
User input is not case sensitive.
Please not when creating staff profiles the initial request for a name will be the name on the appearing on the roster. A first and last name can be added in the following section "Staff Details". Staff Details ARE Case sensitive when being entered as input.

### Features

#### View Shifts
This feature allows the user to narrow down to a shift by which day it is and whether it is day or night shift and then displays a list of all staff working and the capacity in which they will be working

#### Add Staff
Add Staff allows the user to add staff from the existing database into different shifts that need to be filled. Staff need to be in the database (Staff Profiles) before they can be added to a shift.

#### Remove Staff
As the name suggests this feature allows the user to remove staff from any shift they are working. If the staff are NOT working that shift the program will simplyu ask if any further staff would like to be removed, offering a chance to leave teh sub-menu.

#### Staff Contact Details
This feature presents the user with a list of staff using their roster names and allows them to type in the name of who they want to see and then view their details.

#### Create new profile
This feature allows the entry of new staff profiles into the database so that they can be added to shifts.

#### Export Roster
This feature creates **New Roster.csv** which will contain a hard copy of all the changes made which will be able to be printed or emailed to somebody else. The **New Roster.csv** file will be overwritten everytrime the user exports.

#### Exit
Exits the program.