## Report_Generation - Hydraulic photo appendix
Python tool for generating photo appendix for hydraulic modeling reports

Workflow is based on submittal from surveyors, which can depend upon the company and
is not necessarily standardized.  Folder structure must match the example below.  It's
recommended to copy photos to local  drive, recreating the folder structure below.

## Underlying Data Folder Structure
```bash
├───Photos
│   ├───BLA
│   │   └───Structure_Photos
│   │       └───BLA_010
│   ├───DAR
│   ├───DDL
│   ├───JEF
│   ├───JFO
│   ├───LOW
│   ├───MAD
│   │   ├───Structure_Photos
│   │   │   ├───MAD_010
│   │   │   ├───MAD_020
│   │   └───XS_Photos
│   │       ├───MAD_1000
│   │       ├───MAD_10000
```


## Running Scripts
With folder structure in place, script "1_working_generate_structurelist.py" can be 
run to generate the "Cross_reference.csv" file.  Two fields will need to be updated 
manually before running "2_Working_generate_pdfsV4.py" - (hec-ras xs and flooding_source_name).
"hec-ras xs is the associated modeling cross section closest to the surveyor_pt.shp data.
"flooding_source_name" is used for printing the river name on each pdf page.

Script 2 will generate individual pdfs for individual folders found in the photos folder
provided (user will need to update paths before running script).  A merged pdf is 
also created.

An environment.yml file provides the necessary python packages to successfully run
this process.
        
## License
[MIT](https://choosealicense.com/licenses/mit/)


