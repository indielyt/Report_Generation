## Report_Generation - Hydraulic photo appendix
Python tool for generating photo appendix for hydraulic modeling reports

Workflow is based on submittal from surveyors, which can depend upon the company and
is not necessarily standardized.  A general folder structure that works looks like
the following (each submission may require small changes to the scripts to run 
correctly)

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
run to generate the "Cross_reference.csv" file.  The hec-ras station will need to 
be manually updated (currently) before running "2_Working_generate_pdfsV4.py".
Script 2 will generate individual pdfs for individual folders found in the photos folder
provided (user will need to update paths before running script).  A merged pdf is 
also created.

An environment.yml file provides the necessary python packages to successfully run
this process.
        
## License
[MIT](https://choosealicense.com/licenses/mit/)


