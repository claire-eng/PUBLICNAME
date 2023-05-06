# Solar Panels CAB Project

## What is it?
Our database is meant to be used by submitting queries for different questions one may have about solar panels in New Jersey. 
Questions such as: In Bergen County, what type of customer has the highest use of solar panels? can be answered by choosing Bergen County in Municipality and selecting the Customer Type you want to look at.

## Our Schema

**Customer**\
`app_id (PK) | zip_code | complete_date | contractor | cust_type | municipality | acceptance_date`

**Program**\
`app_id (FK) | zip_code | complete_date | contractor | cust_type | municipality | acceptance_date`

**Cost**\
`app_id (FK) | third_ownership | Interconnection`

**Power**\
`app_id (FK) | third_ownership | Interconnection`


## Install
1. Clone the GitHub Repo into the Terminal.  
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/000.png)
2. Go to path `cd cab-project-2/src/SQL` using the terminal.  
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/001.png)
3. Use the command `unzip EXTRACT_ME.zip` in terminal to extract the zip file containing the files `setup.sh`, `flask_install.sh`,`webapp.sh`, and `drop.sh`.  
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/002.png)
4. Run command `sh setup.sh` in terminal. This will create the tables and insert the data.
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/003.png)
>The inserts will take a few minutes. Be patient, there are close to 1 million inserts! :smirk_cat:
5. If you already don't have flask installed, while remaining in the same directory `([lion@roscoe SQL]$)`, run command `sh flask_install.sh` to install flask.

## Using the Database
### Starting the Web App
Run command `sh webapp.sh` to open the web app (Yes, you must stay in the same directory for this one as well).

![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/004.png)


You will be greeted wtih our home page. Hit "**Get Started**" to move on the query selection.

![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/005.png)
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/006.png)
### Dropdown Selectors
When selecting from dropdowns, you are only able to use one at a time.
#### Municipality Selector
The Municipality Selector allows the user to select up to 579 Municipalities recorded from SNJ! After making your desired selection, click submit, and tables will be produced.

There are four tables produced for this selector.
1. Average KW used for each Municipality Selected.
2. The most prominent Electric Utility in the selected Municipalities.
3. The most prominent customer type in the selected Municipalities.
4. Every row with that has the selected municipalities present.

##### Example
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/007.png)
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/008.png)

#### Electric Utility Selector
The Electric Utility Selector allows the user to select any recorded Electric Utility Company from SNJ. After making your desired selection, click submit, and tables will be produced.

There are four tables produced for this selector.
1. Average KW used for each Eletric Utility Company Selected.
2. The most prominent customer type that hired the selected Eletric Utility Company.
3. The Municipality that contains the most projects from the selected Electric Utility Company.
4. Every row with that has the selected Electric Utility Company present.

##### Example
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/009.png)
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/010.png)

#### Customer Type Selector
The Customer Type Selector allows the user to select any of the Categorized Customer Types Recorded from SNJ. After making your desired selection, click submit, and tables will be produced.

1. Average KW used for each Customer Type Selected.
2. The Municipality that contains the highest amount of the selected customer types.
3. The most popular Eletric Utility with the selected customer type.
4. Every row with that has the selected Customer Type Present Company present.

##### Example
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/011.png)
![image](https://github.com/TCNJ-degoodj/cab-project-2/blob/fe97700a06f4287ff5484c0554c2d1f0619c8f33/docs/Images/012.png)

**Have Fun Filtering!**

## Deleting the Databse
- In your terminal, run the code `sh drop.sh`

