Sport England
======================

Data Source
-------------
Sport England website: http://www.sportengland.org/funding/investments-weve-made/

There are two source files - both cover the period: April 2009 - March 2015

* Exchequer Awards
* Lottery Awards

Also see: http://www.sportengland.org/about-us/corporate-information/transparency/ - non grant data / transparency

FoI Request: https://www.whatdotheyknow.com/request/grants_for_last_five_financial_y

On 360 Giving
------------------
Registry Organisation: http://data.threesixtygiving.org/group/sport-england

CSV File: http://data.threesixtygiving.org/group/sport-england-grants

JSON: 


Data Modelling
------------------
Source data has been transformed to 360 using Open Refine.  The Open Refine project has been exported and added to this repository.


Identifiers
---------------
360 Giving namespace:

* 360G-SE

Organisation Identifier:
SE have a Royal Charter (info not available on SE site), which is registered on Companies House as RC000766 (https://opencorporates.com/companies/gb/RC000766)

* GB-COH-RC000766


File Transformations
-------------------------
Each source file has two sheets.  

* Explanatory Notes - this has been digarded in the conversion, but is used in the Registry
* Awards - the grants data.  No edits were made to the structure of this file

There are two files from source:

* Exchequer Awards
* Lottery Awards

Similar columns are not named consistently - eg: "Finance Year" vs "Fin Year" - which makes it difficult to automate processes.

Columns Renamed
-------------------------

| Source Data Column Name | 360 Column Name       |
|-------------------------|-----------------------|
| Recipient               | Recipient Org:Name    |
| Project_Title           | Title                 |
| Award_Amount            | Amount Awarded        |
| Award_Date              | Award Date            |
| Programme_Name          | Grant Programme:Title |


Columns Added
----------------

| New 360 Column Name    | Value(s)                                                              |
|------------------------|-----------------------------------------------------------------------|
| Identifier             | Concat of Funding Org:Identifier + MD5 hash of Title (no ID provided) |
| Currency               | GBP                                                                   |
| Funding Org:Identifier | GB-COH-RC000766                                                       |
| Funding Org:Name       | Sport England                                                         |
| Data source            | http://www.sportengland.org/funding/investments-weve-made/            |
| Last modified          | dateTime                                                              |

Columns Not Mapped
--------------------

| Source Data Column Name | Notes                        |
|-------------------------|------------------------------|
| Main_Sport              | To be investigated           |
| Financial Year          | 360 does not support periods |
| Region                  | To be investigated           |
| Local_Authority         | To be investigated           |
| Organisation_Type       | To be investigated           |

Additionally - in the lottery source file:

| Source Data Column Name  | Notes              |
|--------------------------|--------------------|
| Distributing Body Sector | To be investigated |

Data Transformations
------------------------

| 360 Data Column | Transformation                         |
|-----------------|----------------------------------------|
| Identifier      | Concat of Funding Org:Identifier + URN |


Required Fields Status
------------------------------

| Required Field           | Notes       |
|--------------------------|-------------|
| Identifier               | Created     |
| Title                    | Mapped      |
| Description              | Not created |
| Currency                 | Added       |
| Amount Awarded           | Mapped      |
| Award Date               | Mapped      |
| Recipient Org:Identifier | Not created |
| Recipient Org: Name      | Added       |
| Funding Org: Identifier  | Added       |
| Funding Org: Name        | Added       |

Additional Notes
-----------------------

No Recipient Org:Identifier
*********************************************
This has not yet been added to the data.
See Issue:

Region, Local Authority & Parliamentary Constuency not mapped
**************************************************************
Some work is needed to mint region and admin geo references
See Issue: 

Organisation Type not mapped
**************************************************************
See Issue: 

Lottery and Exchequer sources
*************************************
Investigate how best to attribute these sources in the data.



