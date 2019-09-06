# Report_Generation - Hydraulic photo appendix
Python tool for generating photo appendix for hydraulic modeling reports

Workflow is based on submittal from surveyors, which can depend upon the company and
is not necessarily standardized.  A general folder structure that works looks like
the following (each submission may require small changes to the scripts to run 
correctly)

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

With folder structure in place, script "1_working_generate_structurelist.py" can be 
run to generate the "Cross_reference.csv" file.  The hec-ras station will need to 
be manually updated (currently) before running "2_Working_generate_pdfsV4.py".
Script 2 will generate individual pdfs for individual folders found in the photos folder
provided (user will need to update paths before running script).  A merged pdf is 
also created.

An environment.yml file provides the necessary python packages to successfully run
this process.
        



