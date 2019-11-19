# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:29:16 2017

@author: Daniel.Aragon
"""
#  NOTE: currently script outputs to the folder location of the script, not the 'path' directory

####### User Input, packages, setup

# Cross reference csv.  NOTE: need to amend this to include the actual hec-ras stations
# once modeling is complete (probably manually). flooding_source_name also needs to be manually updated in csv
csv_path = r"C:\Users\Daniel.Aragon\Documents\_Aragon_Backup_Files\02_Water_Resources\ThreeForks\Cross_reference.csv"

# Test directory, for development
#path = r'C:\Users\Daniel.Aragon\Desktop\TEMP\beaverhead_testing\ReportGeneration\Photos'

# Photos Parent Directory
path = r"C:\Users\Daniel.Aragon\Documents\_Aragon_Backup_Files\02_Water_Resources\ThreeForks\photos"

print ('script started')

# Import packages
import pandas as pd
import os

from reportlab.platypus import Paragraph, Spacer, Image, Frame, PageTemplate, BaseDocTemplate 
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm

# Create dataframe from cross reference csv
df_crossref = pd.read_csv(csv_path)
print(df_crossref.head())




#####  FUNCTIONS




# DEFINE FUNCTION for resizing the image (input width for scaling):
def size_image(path, width=1):
    from reportlab.platypus import Image
    # Import utils from reportlab
    from reportlab.lib import utils
    
    # Read in image, get width and height, return aspect ratio
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih/iw
    
    # Return Image rescaled using aspect ratio and user defined width
    return Image(path, width=width, height=(width*aspect))




# DEFINE FUNCTION to create a pdf from list of images.  Inputs are current filepath and list of images
def generate_pdf(filepath, images, crossref_dataframe):

    # Generate information for titling from last filepath of iteration            
    path_list = filepath.split('\\')
    surveyor_xs = path_list[-2]
    flooding_source = path_list[-4]  

    # temp dataframe matching current flooding source and cross section
    temp_df = crossref_dataframe[crossref_dataframe['flooding_source']==flooding_source][crossref_dataframe['surveyor_xs']==surveyor_xs]
    # print(temp_df)

    # flooding_source_text = crossref_dataframe[crossref_dataframe['flooding_source_name'][[crossref_dataframe['surveyor_xs'] ==surveyor_xs]]
    # df_flooding_source = crossref_dataframe['flooding_source_name'][crossref_dataframe['surveyor_xs'] == surveyor_xs]
    try:
        flooding_source_text = temp_df['flooding_source_name'].iloc[0]  
        # print(f'success at {surveyor_xs}: crossref dataframe length={len(crossref_dataframe)}, length df_flooding_source={len(temp_df)}')  
    except:
        # print(f'error at {surveyor_xs}: crossref dataframe length={len(crossref_dataframe)}, length df_flooding_source={len(temp_df)}')
        flooding_source_text = 'error'

    # Generate information for title
    pdf_title = f"ThreeForks{surveyor_xs}.pdf"            
    pdf_header_1 = f"{flooding_source_text}"
    pdf_header_2 = f"Surveyor's Station: {surveyor_xs}"

    # Retrieve hec-ras station from temp_df
    if len(temp_df)==0:
        river_station = "NA"
    else:
        river_station = str(temp_df.iloc[0]['hec-ras_xs'])  

    # If no hec-ras station, skip and don't create pdf
    if river_station=="NA" or river_station=="_" or river_station=='nan':
        print('passing')
        pass

    else:
        river_station_text = ('Hec-RAS Station: ') + river_station
        # Initialize the reportlab pdf for current list of images
        # BaseDocTemplate is preferrable to SimpleDocTemplate as frames will flow across pages
        pdf = BaseDocTemplate(pdf_title, pagesize = letter)

        # Define styles
        style = getSampleStyleSheet()
        style.add(ParagraphStyle(name='Justify', alignment = TA_CENTER, fontSize=10))
        style.add(ParagraphStyle(name='Title2', alignment = TA_LEFT, fontName = 'Helvetica-Bold'))

        # Initialize the story
        story = []

        # Define two column template for pages
        frame1 = Frame(pdf.leftMargin/2, pdf.bottomMargin, pdf.width/2-6, pdf.height, id='col1')
        frame2 = Frame(pdf.leftMargin + pdf.width/2+6, pdf.bottomMargin, pdf.width/2-6, pdf.height/1.1, id='col2')

        # Add the title 1 information for the page            
        text = str(pdf_header_1)
        para = Paragraph(text, style['Title2'])
        story.append(para)

        # Add the title 2 information for the page            
        text = str(pdf_header_2)
        para = Paragraph(text, style['Title2'])
        story.append(para)

        # Add the river station for the page
        text = str(river_station_text)
        para = Paragraph(text, style['Title2'])
        story.append(para)

        # Add spacer between title information and photos
        story.append(Spacer(inch*0.2, inch*0.2))

        for image in images:
            
            # split residual filepath from above 
            split_path = os.path.split(filepath)
            
            # Rejoin the image name with its absolute path
            img_path = os.path.join(split_path[0],image)

            # re-size with 'size_image' function, then append to the pdf 
            story.append(size_image(img_path,width=4.5*cm))
            
            # Append image title below image
            text = str(image)
            para = Paragraph(text,style['Justify'])
            story.append(para) 
            story.append(Spacer(inch*0.2, inch*0.2))

        # Apply template
        pdf.addPageTemplates([PageTemplate(id='TwoCol', frames=[frame1, frame2]), ])

        # Construct the pdf
        pdf.build(story)




# DEFINE FUNCTION for recursively finding images in the directory
def get_images(current_directory, directory_exclusion=['XS_Photos'], image_extension=['.jpg', '.JPG'], image_exclusion=['.Thumbs']):
     
    # Import os
    import os
    
    # initiate images list and clear list between iterations
    images = []
    # Get path of current_directory
    current_directory = os.path.abspath(current_directory)
    
    # Get list of files in the current_directory
    current_directory_files = os.listdir(current_directory)
    
    # Traverse through files, walking down through folder directories
    # and populating images list when image files are encountered. Image list
    # is reset after all image files in folder are appended.
    
    for filename in current_directory_files:
        filepath = os.path.join(current_directory, filename)
            
        # Check if filename is a file, otherwise go to elif below
        if os.path.isfile(filepath):
            if filepath.endswith(image_exclusion[0]):
                continue
            if filepath.endswith(image_extension[0]) or filepath.endswith(image_extension[1]):
                images.append(filename)
        
        # Check if filepath is a directory (folder) we want to pull images from
        elif os.path.isdir(filepath):
            # if filepath ends with directory exclusion, skip
            if filepath.endswith(directory_exclusion[0]):
                continue
            # otherwise, call get_images recursively to walk down and find image files
            else:               
                get_images(filepath)
    
    # This is the end of the for loop, which exits with a list of images from a single directory (folder) 

    # Test images list for content, if empty, move on, other wise call 'generate_pdf' function
    if len(images) > 0:
        
        # Call the generate_pdf function from within the get_images function
        output = generate_pdf(filepath, images, df_crossref)
        



# DEFINE FUNCTION to merge pdfs in directory and then delete originals
def merge_pdfs_in_directory(folder):
    import os
    # Need to have PyPDf2 installed
    from PyPDF2 import PdfFileReader, PdfFileMerger

    # Change this to 'n' if don't want to delete originals
    # delete = 'n'
    
    # identify current directory
    current_directory = os.getcwd()
    print (current_directory)
    
    all_files = list()
    
    main_text = [f for f in os.listdir(current_directory) if '.pdf' in f]
    all_files.extend(main_text)
    
    merger = PdfFileMerger()
    for f in all_files:
        merger.append(PdfFileReader(f), 'rb')
    
    merger.write('ThreeForks_1_merged.pdf')
    
    if False:
        for f in all_files:
            parent = os.path.abspath(current_directory)
            os.remove(os.path.join(parent,f))




####### CALL FUNCTIONS, Create Report




# Call get_images function (and nested generate_pdf function)    
get_images(path) 

# Call 'merge_pdfs_in_directory
merge_pdfs_in_directory(os.getcwd())
    
print (' Script Complete') 










