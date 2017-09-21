# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:29:16 2017

@author: Daniel.Aragon
"""

import os
#from PIL import Image


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib import utils
from reportlab.platypus import Frame, Image
from reportlab.platypus import PageBreak

path = r'C:\Users\Daniel.Aragon\Desktop\TEMP\beaverhead\ReportGeneration\Photos'



def size_image(path, width=1*cm):
  img = utils.ImageReader(path)
  iw, ih = img.getSize()
  aspect = ih/iw
  return Image(path, width=width, height=(width*aspect))

def get_images(current_directory, directory_exclusion=['XS_Photos'], image_extension=['.jpg', '.JPG'], image_exclusion=['.Thumbs']):
    
    # initiate pdf using reportlab
#    pdf = SimpleDocTemplate('multipage_test.pdf', pagesize = letter)
#    style = getSampleStyleSheet()
#    story = []
    
    
    # initiate images list and clear list between folder directories
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
    
    # This is the end of the for loop, which exists with a single list of 
    # images from a single directory (folder)
    
    
    # Test images list for content, if empty, move on, other wise... do stuff
    if len(images) > 0:
        
        path_list = filepath.split('\\')
        surveyor_xs = path_list[-2]
        flooding_source = path_list[-4]  
        
        pdf_title = str(flooding_source) + str(surveyor_xs) + '.pdf'
        pdf = SimpleDocTemplate(pdf_title, pagesize = letter)
        style = getSampleStyleSheet()
        
        pdf_header = flooding_source + "; " + "Surveyor's Station: " + surveyor_xs
        river_station = " " # we'll have to fill this in later
        
        story = []
        
        text = str(pdf_header)
        para = Paragraph(text, style['Normal'])
        story.append(para)
        story.append(river_station)
        story.append(Spacer(inch*0.5, inch*0.5))
        
        for image in images:
            
            # split residual filepath from above 
            split_path = os.path.split(filepath)
            
            # Rejoin the image name with its absolute path
            img_path = os.path.join(split_path[0],image)

            # Append photo after calling re-sizing function
            story.append(size_image(img_path,width=5*cm))
            
            # Append image title below image
            text = str(image)
            para = Paragraph(text,style['Normal'])
            story.append(para) 
            story.append(Spacer(inch*0.5, inch*0.5))
        
        pdf.build(story)

    
    
    
    
get_images(path) 
    
    
    















def size_images(path, width=1*inch):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih/iw
    return Image(path, width=width, height=(width*aspect))    
    
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
  
