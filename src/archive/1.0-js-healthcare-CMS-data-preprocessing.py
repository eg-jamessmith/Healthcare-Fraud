# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:26:50 2020

@author: James Smith

1.0-js-data-preprocessing


"""

# Working with directories
import os
# Finds pathnames matching a specified pattern
import glob
import pandas as pd
#import dask

###############################################################################
###############################################################################
#----- 1 Get Supporting Data -----#
###############################################################################
###############################################################################

###############################################################################
#----- 1.1 List of drugs to exclude, as mentioned below -----#
###############################################################################

"""
"Big Data fraud detection using multiple medicare data sources"

Procedures are labeled by their Healthcare Common Procedure Coding System (HCPCS) code
- CMS: HCPCS—General Information. https://www.cms.gov/Medicare/Coding/MedHCPCSGenInfo/index.html.

For Part B, we fltered out all instances with HCPCS codes referring to prescriptions. Tese
prescription-related codes are not actual medical procedures, but instead are for specifc
services listed on the Medicare Part B Drug Average Sales Price file 

- https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Information-on-Prescription-Drugs/index

JS - I got them here
    - https://www.cms.gov/medicare/medicare-part-b-drug-average-sales-price/2020-asp-drug-pricing-files
    - January 2020 ASP Pricing File (accessed 03/03/2020)
"""
## Setup ##

# Define working directory
path = os.getcwd()
# Define parent directory
source_code_directory = os.path.abspath(os.path.join(path, os.pardir))
# Define project directory
project_directory = os.path.abspath(os.path.join(source_code_directory, os.pardir))
# Raw data location
data_folder = os.path.join(project_directory, "data", "raw", 
                           "Healthcare Provider Fraud Detection",
                           "Original Data")

## Get Drug Data ##

# Read CSV of drugs to exclude
medicare_drugs = pd.read_csv(os.path.join(data_folder, "Drugs", "medicare_drugs.csv"))

###############################################################################
#----- 1.2 Fraud Labelling -----#
###############################################################################

"""
"Big Data fraud detection using multiple medicare data sources"

- Real-world Medicare provider fraud labels are identifed using the publicly available
    LEIE data
- The LEIE exclusion type attribute is a categorical value that describes the ofense
    and its severity.
- Following the work by Bauder and Khoshgoftaar  [35], a subset of exclusion rules 
    that are most indicative of fraud is selected for labeling Medicare providers.
- We use the NPI numbers of excluded individuals that have
    been convicted under one of these rules to identify fraudulent providers within the
    Medicare Part B data set.
- For these providers in the Medicare Part B data set, whose
    NPI number matches those of the LEIE data set, **claims that are dated prior to the
    provider’s exclusion date are labeled as fraudulent.**



JS - I got it here
    - https://oig.hhs.gov/exclusions/exclusions_list.asp
    - Accessed 03/03/2020
"""

# Defining Fraudulent Exclusion Types based on Bauder and Khoshgoftaar [35]
fraudulent_exclusion_types = {'1128a1' : 'Conviction of program-related crimes',
                              '1128a2' : 'Conviction relating to patient abuse or neglect',
                              '1128a3' : 'Felony conviction relating to health care fraud',
                              '1128a4' : 'License revocation, suspension, or surrender',
                              '1128a7' : 'Fraud, kickbacks, and other prohibited activities'}
# Read CSV of LEIE data
LEIE_data = pd.read_csv(os.path.join(data_folder, "Fraud Mapping", "LEIE_data.csv"))
# Keep important columns
LEIE_data = LEIE_data[['NPI', 'EXCLTYPE', 'EXCLDATE']]
# Keep rows with valid NPI numbers
LEIE_data = LEIE_data.query("NPI != 0")
# Create Fraud flag - NOT COMPLETE
LEIE_data = LEIE_data.query("EXCLTYPE in {}".format(list(fraudulent_exclusion_types.keys())))


###############################################################################
###############################################################################
#----- 2 Combining Data Sources -----#
###############################################################################
###############################################################################

"""
"Medicare fraud detection using neural networks"

- a: Remove records with missing NPI numbers and missing HCPCS codes
- b: Remove records where HCPCS codes correspond to prescription drugs 
- c: Remove provider-level attributes 
- Create year attribute
- Fraud Labelling - Since Medicare PUF and LEIE data have different release schedules, Herland et al.
decided to round exclusion end dates to the nearest year.
- Group records on year, NPI, provider type, and gender creating summary attributes
    - mean
    - sum
    - median
    - standard deviation 
    - minimum
    - maximum 
    
"Big Data fraud detection using multiple medicare data sources"
    
we replace the original numeric variables with
the aggregated mean, sum, median, standard deviation, minimum and maximum values,
creating six new features for each original numeric feature. The resulting features are all
complete except for standard deviation which contains NA values. These NA values are
generated when a physician has performed/prescribed a HCPCS/drug once in a given
year. Therefore, the population standard deviation for one unique instance is 0, and thus
we replace all NA values with 0 representing that this single instance has no variability
in that particular year.
"""

# Find all zip files in data folder
all_zip_folders = glob.glob(data_folder + "/*.zip")

###############################################################################
#----- 2.1 Transforming Data Sources -----#
###############################################################################

#----- Example -----#
zip_folder_example = all_zip_folders[1]
# read_table since it's tab delimited
tbl_1 = pd.read_table(zip_folder_example, nrows = 10000)

# a: Remove records with missing NPI numbers and missing HCPCS codes
tbl_1 = tbl_1.query("NPI not in [0,1] & HCPCS_CODE not in ['0','1']")
tbl_1 = tbl_1.dropna(subset=['NPI', 'HCPCS_CODE'])

# b: Remove records where HCPCS codes correspond to prescription drugs
tbl_1 = tbl_1.query("HCPCS_CODE not in {}".format(medicare_drugs["HCPCS Code"].tolist()))


tbl_1[['NPI', 'NPPES_PROVIDER_ZIP']].head()



# c: Remove provider-level attributes 
cms_medicare_features = ['NPI', 'PROVIDER_TYPE', 'NPPES_PROVIDER_GENDER',
                         'LINE_SRVC_CNT', 'BENE_UNIQUE_CNT', 'BENE_DAY_SRVC_CNT',
                         'AVERAGE_SUBMITTED_CHRG_AMT', 'AVERAGE_MEDICARE_PAYMENT_AMT']

tbl_1 = tbl_1[cms_medicare_features]


"""
The above is provider-level attributes
- Maybe work could be done on simply linking providers together in some way
- Name 
- Address
- HCPCS code

Not sure how one would create a network - what are the nodes?


"""

