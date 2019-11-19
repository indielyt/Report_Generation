# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:29:16 2017

@author: Daniel.Aragon
"""
#  NOTE: currently script outputs to the folder location of the script, not the 'path' directory
import pandas as pd
import os

# Test directory, for development
#path = r'C:\Users\Daniel.Aragon\Desktop\TEMP\beaverhead_testing\ReportGeneration\Photos'

print ('started')
# Production directory, source data copied to local drive 
path = r'\\lakefs1\Projects\169207_MT_ThreeForks_Madison_Jefferson\18-08-0001S_Madison\Working\Survey\SurveySubmittal_MMI_20190118\Photos\MAD\Structure_Photos'

# Cross reference csv.  NOTE: need to amend this to include the actual hec-ras stations
# once modeling is complete (probably manually) then re-run this script
csv_path = r"C:\Users\Daniel.Aragon\Downloads\Report_Generation\Cross_reference.csv"
crossref = pd.read_csv(csv_path)
print(crossref.head())

# Function for recursively finding images in the directory
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
        
        # Function to create a pdf from list of images.  Inputs are current filepath and list of images
        def generate_pdf(filepath, images):
            
            # Import necessary reportlab modules
            from reportlab.platypus import Paragraph, Spacer, Image, Frame, PageTemplate, BaseDocTemplate 
            from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
            from reportlab.lib.enums import TA_CENTER, TA_LEFT
            from reportlab.lib.pagesizes import letter
            from reportlab.lib.units import inch, cm
 
            # Generate information for titling from last filepath of iteration            
            path_list = filepath.split('\\')
            surveyor_xs = path_list[-2]
            flooding_source = path_list[-4]  
            

            # Inspect values in terminal output
            # print('path list: ', path_list)
            # print('surveyor_xs: ', surveyor_xs)
            # print('flooding_source: ', flooding_source)

            # Handle the one exception - irregular file structure in Beaverhead River file
            if  flooding_source == 'Structure_Photos':
                flooding_source = path_list[-5]

            # Generate information for title
            # pdf_title = "str(flooding_source)" + str(surveyor_xs) + '.pdf'            
            # pdf_header = flooding_source + "; " + "Surveyor's Station: " + surveyor_xs
            pdf_title = "Madison River" + str(surveyor_xs) + '.pdf'            
            pdf_header = "Madison River" + "; " + "Surveyor's Station: " + surveyor_xs
            
            # Retrieve hec-ras station from crossref csv (converted to dataframe)
            # Generate a single entry dataframe that matches current flooding source and surveyor xs
            # print('p1: ', crossref[crossref['flooding_source']==flooding_source])
            # print('p2: ', crossref[crossref['surveyor_xs']==surveyor_xs])
            temp_df = crossref[crossref['flooding_source']==flooding_source][crossref['surveyor_xs']==surveyor_xs]

            print(temp_df)
            # Retrieve hec-ras station from temp_df
            river_station = ('Hec-RAS Station: ') + str(temp_df.iloc[0]['hec-ras_xs'])
            
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
          
            # Add the title information for the page            
            text = str(pdf_header)
            para = Paragraph(text, style['Title2'])
            story.append(para)
            
            # Add the river station for the page
            text = str(river_station)
            para = Paragraph(text, style['Title2'])
            story.append(para)
            
            # Add spacer between title information and photos
            story.append(Spacer(inch*0.2, inch*0.2))
            
            for image in images:
                
                # split residual filepath from above 
                split_path = os.path.split(filepath)
                
                # Rejoin the image name with its absolute path
                img_path = os.path.join(split_path[0],image)
    
                # Append re-sized image to the pdf 
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
        
        # Call the generate_pdf function from within the get_images function
        output = generate_pdf(filepath, images)
        





# Function for resizing the image (input width for scaling):
# def size_image(path, width=1*cm):
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





# Function to merge pdfs in directory and then delete originals
def merge_pdfs_in_directory(folder):
    import os
    # Need to have PyPDf2 installed
    from PyPDF2 import PdfFileReader, PdfFileMerger

    # Change this to 'n' if don't want to delete originals
    delete = 'n'
    
    # identify current directory
    current_directory = os.getcwd()
    print (current_directory)
    
    all_files = list()
    
    main_text = [f for f in os.listdir(current_directory) if '.pdf' in f]
    all_files.extend(main_text)
    
    merger = PdfFileMerger()
    for f in all_files:
        merger.append(PdfFileReader(f), 'rb')
    
    merger.write('merger_test.pdf')
    
#    print (all_files)
    
    if False:
        for f in all_files:
            parent = os.path.abspath(current_directory)
            os.remove(os.path.join(parent,f))





# Call get_images function (and nested generate_pdf function)    
get_images(path) 

# Call 'merge_pdfs_in_directory
merge_pdfs_in_directory(os.getcwd())
    
print ('complete') 















#def size_images(path, width=1*inch):
#    img = utils.ImageReader(path)
#    iw, ih = img.getSize()
#    aspect = ih/iw
#    return Image(path, width=width, height=(width*aspect))    
    
#    # As long as images list is not empty, we'll create a new pdf page
#    img_counter = 0
##    img_list_counter = 0
#    if len(images) > 0:
#        
##        img_list_counter += 1
#        
#        print (str(images))
#        
#        path_list = filepath.split('\\')
#        surveyor_xs = path_list[-2]
#        title = path_list[-3]
#        flooding_source = path_list[-4]
#        print (surveyor_xs)
#        print (title) 
#        print (flooding_source)
#        
#        
#        
#        pdf_title = flooding_source + "_" + surveyor_xs + ".pdf"
#        pdf = SimpleDocTemplate(pdf_title, pagesize = letter)
#        story=[]
#        
#        for image in images:
#            image_name = path_list[-1]
#            text = str(image_name)
#            para = Paragraph(text, style['Normal'])
#            story.append(para)
#            img_counter +=1
#        
#        pdf.build(story)
#        print ("img_counter= ", img_counter)
##        print ("img_list_counter= ", img_list_counter)
        
        
        
        
        
        
        
        
        
        
        
        
#        print ('break')
        
#        path_list = filepath.split('\\')
#        image_name = path_list[-1]
#        surveyor_xs = path_list[-2]
#        title = path_list[-3]
#        flooding_source = path_list[-4]
#        print (image_name)
#        
#        pdf_title = flooding_source + ".pdf"
#        pdf = SimpleDocTemplate(pdf_title, pagesize = letter)
##        style = getSampleStyleSheet()
#        
#        text = str(image_name)
#        para = Paragraph(text, style['Normal'])
#        
#        story=[]
#        story.append(para)
#        story.append(image_name)
        
        
        
        
#        for image in images:
#            img_path = os.path.abspath(image)
#            print (img_path)
#            sized_img = size_images(img_path, width=2*inch)
#            story.append(sized_img)
#            story.append(image_name)
#            story.append(Spacer(inch*0.5, inch*0.5))
        
        
#        pdf.build(story)
            
        
#        print (images) # this is the place for adding list of images to pdf page
#        print ('stop') # this is the place for making a new pdf page
        
        
            
            

            
            

    
#root = r'C:\Users\Daniel.Aragon\Desktop\TEMP\beaverhead\ReportGeneration\Photos'



















#print (os.getcwd())

#print (os.listdir(path))

#for path, subdir, file in os.walk(path, topdown=False):
#    print ('Found Directory: %s' % path)
#    for fname in file:
#        print ('\t%s' % fname)
#    if len(subdir) > 0:
#        del subdir[0]

#for path, subdir, file in os.walk(path, topdown=False):
#    print ('Found Directory: %s' % path)
#    for fname in file:
#        print ('\t%s' % fname)
#    
  


#for path,subdir,files in os.walk(path):
##  for name in subdir:
##    print (os.path.join(path,name)) # will print path of directories
#  for name in files:    
#    print (os.path.join(path,name)) # will print path of files
 
#for path, subdir, files in os.walk(rootDir, topdown=False):
#  for file in subdir:
#    print (os.path.join(path,name)) # will print path of directories
#    for name in files:    
#      print (os.path.join(path,name)) # will print path of files  
   
#for path, subdir, files in os.walk(path):
#  for subdir in path:    
#    for name in files:
#      if '.JPG' in name:
#        images.append(file)
#  print (images)
#  images=[]    
#  print ('next dir')

  
#  for file in subdir:
#    if '.jpg' in file:
#      print (file)
#    
  
