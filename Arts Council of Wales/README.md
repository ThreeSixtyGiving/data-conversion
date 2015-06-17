Arts Council of Wales
======================

Data Source
-------------
FoI request: https://www.whatdotheyknow.com/request/grants_made_as_open_data#incoming-494549

On 360 Giving
------------------
Registry Organisation: http://data.threesixtygiving.org/group/arts-council-wales

CSV File: http://data.threesixtygiving.org/dataset/arts-council-wales-grants

JSON: 


Data Modelling
------------------
Source data has been transformed to 360 using Open Refine.  The Open Refine project has been exported and added to this repository.


Identifiers
---------------
360 Giving namespace:

* 360G-ACW

Organisation Identifier:
ACW have a Royal Charter (http://www.artswales.org.uk/about-us), which is registered on Companies House as RC000759 (https://opencorporates.com/companies/gb/RC000759)

* GB-COH-RC000759


File Transformations
-------------------------
The source file has one sheet.  No edits were made to the structure or format.


Columns Renamed
-------------------------

| Source Data Column Name  | 360 Column Name            |
|--------------------------|----------------------------|
| Organization Name        | Recipient Org:Name         |
| Organization Postal Code | Recipient Org:Postal Code  |
| Project Description      | Description                |
| Grant Amount             | Amount Awarded             |
| Government Region        | Beneficiary Location: Name |

Columns Added
----------------

| New 360 Column Name    | Value(s)                                                        |
|------------------------|-----------------------------------------------------------------|
| Identifier             | Concat of Funding Org:Identifier + Ref No                       |
| Currency               | GBP                                                             |
| Funding Org:Identifier | GB-COH-RC000759                                                 |
| Funding Org:Name       | Arts Council of Wales                                           |
| Data source            | https://www.whatdotheyknow.com/request/grants_made_as_open_data |
| Last modified          | dateTime                                                        |

Columns Not Mapped
--------------------

| Source Data Column Name | Notes                        |
|-------------------------|------------------------------|
| Type                    | Grant type not yet supported |
| Financial Year          | 360 does not support periods |

Data Transformations
------------------------

| 360 Data Column | Transformation                                |
|-----------------|-----------------------------------------------|
| Identifier      | Concat of Funding Org:Identifier + ID         |
| Title           | Concat of Recipient Org:Name + Financial Year |

Required Fields Status
------------------------------

| Required Field           | Notes       |
|--------------------------|-------------|
| Identifier               | Created     |
| Title                    | Created     |
| Description              | Mapped      |
| Currency                 | Added       |
| Amount Awarded           | Mapped      |
| Award Date               | Created     |
| Recipient Org:Identifier | Not created |
| Recipient Org: Name      | Added       |
| Funding Org: Identifier  | Added       |
| Funding Org: Name        | Added       |

Additional Notes
-----------------------

No Recipient Org:Identifier
*********************************************
This has not yet been added to the data.
See Issue: https://github.com/ThreeSixtyGiving/data-conversion/issues/2

Government Region not mapped
*********************************************
Some work is needed to mint region and local authority references
See Issue: https://github.com/ThreeSixtyGiving/data-conversion/issues/3


