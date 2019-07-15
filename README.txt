This is readme file that contains all information about CRUD - Create, Read, Update, Delete utility
***************************************************************************************************
WHAT IS IT ABOUT?
This utility would work with football team and it's players
For each player there are three points to work with:
string - Surname, Last name
integer - age
list - skills of player(strength, savvy, dribbling)
dict -  position: GK, salary: 5000$, contract: 3 years
---------------------------------------------------------------------------------------------------
HOW TO AUTHORISE?
This utility have three permission types
Admin - have all permissions to all functions
User - have permissions to create new players and read them
Guest - could only read info about players
---------------------------------------------------------------------------------------------------
WHICH Functions does the program have? Kind of traceability matrix
Create players - Admin, User
Read players - Admin, User, Guest
Delete Players - Admin
Change Players - Admin
-------Working with permissions-------
Add, Remove users - Admin only
***************************************************************************************************
Manipulations with data:
- it is possible to export data to json
- is is possible to sirealize and desirealize
---------------------------------------------------------------------------------------------------