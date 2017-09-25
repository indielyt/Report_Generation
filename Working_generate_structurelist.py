# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:29:45 2017

@author: Daniel.Aragon
"""

### Script for generating a csv to cross reference surveyor cross sections to
### hec-ras cross sections.  csv can be passed to pdf generation script to fill 
### in the hec ras station automatically (once field is populated)

import pandas as pd
import os


# define directory, output path, and global variable 'structures'
path = r'C:\Users\Daniel.Aragon\Desktop\TEMP\beaverhead_appendixF_data\Photos'
outpath = r'C:\Users\Daniel.Aragon\Desktop\TEMP\beaverhead_testing\ReportGeneration\Photos\Cross_reference.csv'
structures = pd.DataFrame(columns = ['flooding_source','surveyor_xs'])

# Function for recursively finding images in the directory
def get_directories(current_directory, directory_exclusion=['XS_Photos']):
   
    # Global
    global structures

    # Get path of current_directory
    current_directory = os.path.abspath(current_directory)
    
    # Get list of files in the current_directory
    current_directory_files = os.listdir(current_directory)
    
    # Traverse through files, walking down through folder directories
    # and populating images list when image files are encountered. Image list
    # is reset after all image files in folder are appended.
    
    for filename in current_directory_files:
        filepath = os.path.join(current_directory, filename)
            
        # Check if filename is a file, if so, get info on the directory for titling
        if os.path.isfile(filepath):
            filepath= os.path.dirname(filepath)
           
            # Generate information for titling from last filepath of iteration            
            path_list = filepath.split('\\')
            surveyor_xs = path_list[-1]
            flooding_source = path_list[-3] 
            
            # Handle on exception in folder structure with Beaverhead River
            if flooding_source == 'Structure_Photos':
                flooding_source = path_list[-4]

            # Write to temporary data frame
            temp_df = pd.DataFrame([[flooding_source, surveyor_xs]], columns = ['flooding_source','surveyor_xs'])

            # Merge structures dataframe with temp_df, outer prevents multiple identical entries
            structures = pd.merge(structures, temp_df, how='outer')
        
        # Check if filename is a directory, if so and if not in directory exclusion, recursively call get_directories
        else:
            # if filepath ends with directory exclusion, skip
            if filepath.endswith(directory_exclusion[0]):
                continue
            else:
               get_directories(filepath)
               
    # Return the appended structures dataframe
    return (structures)


# Call Cross Reference List function
CrossReference_List = get_directories(path)
# Add field for 'hec-ras xs' 
CrossReference_List['hec-ras_xs']="_"
print (CrossReference_List.head())

# Generate csv from dataframe
CrossReference_List.to_csv(outpath, sep=',')






















#            else:
#                filepath = os.path.dirname(filepath)
#                # Generate information for titling from last filepath of iteration            
#                path_list = filepath.split('\\')
#                surveyor_xs = path_list[-1]
#                flooding_source = path_list[-3] 
#            elif flooding_source == 'Structure_Photos':
                 
#            # otherwise, call get_directories recursively 
#            elif:
#                filepath = os.path.dirname(filepath)
#                # Generate information for titling from last filepath of iteration            
#                path_list = filepath.split('\\')
#                surveyor_xs = path_list[-1]
#                flooding_source = path_list[-3]  
#                
#            
#            # Handle the one exception - irregular file structure in Beaverhead River file
#            elif flooding_source == 'Structure_Photos':
#                flooding_source = path_list[-4]
#            
#            else:               
#                get_directories(filepath)








#    # This is the end of the for loop, which exits with a list of 
#    # images from a single directory (folder)
#    
#
#    # Test images list for content, if empty, move on, other wise call 'generate_pdf' function
#    if len(images) > 0:
#        
#        # Function to create a pdf from list of images.  Inputs are current filepath and list of images
#        def generate_pdf(filepath, images):
#            
#            # Import necessary reportlab modules
#            from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image, Frame, PageTemplate, KeepTogether, BaseDocTemplate 
#            from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
#            from reportlab.lib.enums import TA_CENTER, TA_LEFT
#            from reportlab.lib.pagesizes import letter
#            from reportlab.lib.units import inch, cm
# 
#            # Generate information for titling from last filepath of iteration            
#            path_list = filepath.split('\\')
#            surveyor_xs = path_list[-2]
#            flooding_source = path_list[-4]  
#            # Handle the one exception - irregular file structure in Beaverhead River file
#            if  flooding_source == 'Structure_Photos':
#                flooding_source = path_list[-5]
#
#            # Generate information for title
#            pdf_title = str(flooding_source) + str(surveyor_xs) + '.pdf'            
#            pdf_header = flooding_source + "; " + "Surveyor's Station: " + surveyor_xs
#            river_station = 'HecRAS River Station:' # we'll have to fill this in later
#
#
#            
#            # Add the river station for the page
#            text = str(river_station)
#
#            for image in images:
#                
#                # split residual filepath from above 
#                split_path = os.path.split(filepath)
#                
#                # Rejoin the image name with its absolute path
#                img_path = os.path.join(split_path[0],image)
#    
#                # Append photo after calling re-sizing function
##                img = size_image(img_path,width=1*cm)
#                story.append(size_image(img_path,width=4.5*cm))
#                
#                # Append image title below image
#                text = str(image)
#                para = Paragraph(text,style['Justify'])
#                story.append(para) 
#                story.append(Spacer(inch*0.2, inch*0.2))
##                story.append(KeepTogether(para,img))
#           
#            # Apply template
#            pdf.addPageTemplates([PageTemplate(id='TwoCol', frames=[frame1, frame2]), ])
#            
#            # Construct the pdf
#            pdf.build(story)
#        
#        # Call the generate_pdf function from within the get_images function
#        output = generate_pdf(filepath, images)
#
#
## Call get_images function (and nested generate_pdf function)    
#get_images(path) 
#
## Call 'merge_pdfs_in_directory
#merge_pdfs_in_directory(os.getcwd())
#    
#    
#    
#
#
#
#















