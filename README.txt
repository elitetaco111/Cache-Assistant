   _____          _____ _    _ ______             _____ _____ _____  _____ _______       _   _ _______ 
  / ____|   /\   / ____| |  | |  ____|     /\    / ____/ ____|_   _|/ ____|__   __|/\   | \ | |__   __|
 | |       /  \ | |    | |__| | |__       /  \  | (___| (___   | | | (___    | |  /  \  |  \| |  | |   
 | |      / /\ \| |    |  __  |  __|     / /\ \  \___ \\___ \  | |  \___ \   | | / /\ \ | . ` |  | |   
 | |____ / ____ \ |____| |  | | |____   / ____ \ ____) |___) |_| |_ ____) |  | |/ ____ \| |\  |  | |   
  \_____/_/    \_\_____|_|  |_|______| /_/    \_\_____/_____/|_____|_____/   |_/_/    \_\_| \_|  |_|   
                                                                                                                                                                                                      
Cache Clearing Assistant 1.1
By Dave Nissly
Created - 1/28/2025
Last Update - 1/30/2025

How to use:
1. Drag csv file with the formatted data renamed to data.csv in this folder
2. Run cacheclearing.py
3. Open output.csv for your cache clearing needs
4. ???
5. Profit

Input Data Format: 
No headers, no totals row at the bottom
Column 0 = name/sku
Column 1 = #images to clear cache (aka tickled for AIR)
**Data in columns beyond this will be ignored**

Output Information:
Columns have headers describing whats in that Column
Items with more than one image will go further to the right, ****EACH ROW CONTAINS ALL OF THE LINKS FOR A SINGLE ITEM****

BugFixes:
v1.1 - fixed missing first item per # of images (single image clearing works now)
     - general style fixing
     - README clarifications
     - fixed large image cloudinary link
