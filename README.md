## Report_Generation - Hydraulic photo appendix
Python tool for generating photo appendix for hydraulic modeling reports

Workflow is based on submittal from surveyors, which can depend upon the company and
is not necessarily standardized.  A general folder structure that works looks like
the following (each submission may require small changes to the scripts to run 
correctly)

## Underlying Data Folder Structure

'''bash
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
│   │   │   ├───MAD_030
│   │   │   ├───MAD_040&MAD_050
│   │   │   ├───MAD_060
│   │   │   ├───MAD_070
│   │   │   ├───MAD_080
│   │   │   ├───MAD_090
│   │   │   ├───MAD_100
│   │   │   ├───MAD_110
│   │   │   ├───MAD_120
│   │   │   ├───MAD_130
│   │   │   ├───MAD_140
│   │   │   ├───MAD_150
│   │   │   ├───MAD_160
│   │   │   ├───MAD_1_010
│   │   │   ├───MAD_1_020
│   │   │   ├───MAD_2_010
│   │   │   ├───MAD_2_020
│   │   │   ├───MAD_2_030
│   │   │   ├───MAD_2_040
│   │   │   ├───MAD_3_010
│   │   │   ├───MAD_3_020
│   │   │   ├───MAD_3_030
│   │   │   ├───MAD_3_040
│   │   │   ├───MAD_4_010
│   │   │   ├───MAD_5_010
│   │   │   └───MAD_6_010
│   │   └───XS_Photos
│   │       ├───MAD_1000
│   │       ├───MAD_10000
│   │       ├───MAD_11000
│   │       ├───MAD_113000
│   │       ├───MAD_12000
│   │       ├───MAD_13000
│   │       ├───MAD_1_1000
│   │       ├───MAD_1_2000
│   │       ├───MAD_1_3000
│   │       ├───MAD_1_4000
│   │       ├───MAD_1_5000
│   │       ├───MAD_1_6000
│   │       ├───MAD_1_7000
│   │       ├───MAD_1_8000
│   │       ├───MAD_1_9000
│   │       ├───MAD_2000
│   │       ├───MAD_26000
│   │       ├───MAD_27000
│   │       ├───MAD_28000
│   │       ├───MAD_29000
│   │       ├───MAD_3000
│   │       ├───MAD_30000
│   │       ├───MAD_31000
│   │       ├───MAD_32000
│   │       ├───MAD_33000
│   │       ├───MAD_34000
│   │       ├───MAD_35000
│   │       ├───MAD_36000
│   │       ├───MAD_37000
│   │       ├───MAD_38000
│   │       ├───MAD_39000
│   │       ├───MAD_4000
│   │       ├───MAD_40000
│   │       ├───MAD_41000
│   │       ├───MAD_42000
│   │       ├───MAD_43000
│   │       ├───MAD_44000
│   │       ├───MAD_45000
│   │       ├───MAD_46000
│   │       ├───MAD_47000
│   │       ├───MAD_48000
│   │       ├───MAD_49000
│   │       ├───MAD_5000
│   │       ├───MAD_50000
│   │       ├───MAD_51000
│   │       ├───MAD_52000
│   │       ├───MAD_53000
│   │       ├───MAD_54000
│   │       ├───MAD_55000
│   │       ├───MAD_6000
│   │       ├───MAD_60000
│   │       ├───MAD_61000
│   │       ├───MAD_62000
│   │       ├───MAD_67000
│   │       ├───MAD_68000
│   │       ├───MAD_69000
│   │       ├───MAD_7000
│   │       ├───MAD_70000
│   │       ├───MAD_71000
│   │       ├───MAD_72000
│   │       ├───MAD_77000
│   │       ├───MAD_78000
│   │       ├───MAD_79000
│   │       ├───MAD_8000
│   │       ├───MAD_80000
│   │       ├───MAD_81000
│   │       ├───MAD_82000
│   │       ├───MAD_83000
│   │       ├───MAD_84000
│   │       ├───MAD_85000
│   │       ├───MAD_86000
│   │       ├───MAD_9000
│   │       ├───MAD_91000
│   │       └───MAD_96000
│   ├───MDO
│   ├───ODE
│   │   └───Structure_Photos
│   └───REY
├───Sketches
│   ├───BLA
│   ├───CLE
│   ├───DAR
│   ├───DDL
│   ├───JEF
│   ├───JFO
│   ├───JFS
│   ├───LOW
│   ├───MAD
│   ├───MDO
│   ├───ODE
│   └───REY
├───Spatial_Files
├───Supplemental_Data
│   ├───Field_Notes
│   └───Spatial_Data
│       └───Supplemental_S_Str
├───Survey_Data
└───Task_Documentation
    ├───FieldSurveyReport
    │   └───MSWord
    └───StructureInventoryReport
        └───MSWord
'''

Photos
    FloodingSourceName
        Structure_Photos
            FloodingSourceName_RiverStation
                photo1.jpg
                photo2.jpg
        XS_Photos
            FloodingSourceName_RiverStation
                photo1.jpg
                photo2.jpg

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


