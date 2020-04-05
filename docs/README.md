# Healthcare Provider Fraud Detection

Possibly related to this paper - **Big Data fraud detection using multiple medicare data sources**

> The Part B dataset provides claims information for each procedure a physician performs
within a given year. Currently, this dataset is available on the CMS website for the 2012
through 2015 calendar years (with 2015 being released in 2017) [45].

> We discuss data processing for
all four datasets and the mapping of real-world provider fraud labels

> we employ the List of Excluded Individuals and Entities (LEIE)
[19], which contains the following information: reason for exclusion, date of exclusion
and reinstate/waiver date for all current physicians found unsuited to practice medicine and thus excluded from practicing in the United States for a given period of time.

> The LEIE is aggregated at the provider-level and does not have specifc information
regarding procedures, drugs or equipment related to fraudulent activities.

> For this study, we are only interested in particular attributes from each dataset in
order to provide a solid basis for our experiments and analyses.  

https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier2017

The dataset lives on [Kaggle](https://www.kaggle.com/rohitrox/healthcare-provider-fraud-detection-analysis). After asking the person who posted the data, "it is a hackathon data and provided by INSOFE INDIA." -  International School of Engineering

## Healthcare Provider Fraud Overview

Provider Fraud is one of the biggest problems facing Medicare. According to the government, the total Medicare spending increased exponentially due to frauds in Medicare claims. Healthcare fraud is an organized crime which involves peers of providers, physicians, beneficiaries acting together to make fraud claims.

Rigorous analysis of Medicare data has yielded many physicians who indulge in fraud. They adopt ways in which an ambiguous diagnosis code is used to adopt costliest procedures and drugs. Insurance companies are the most vulnerable institutions impacted due to these bad practices. Due to this reason, insurance companies increased their insurance premiums and as result healthcare is becoming costly matter day by day.

Healthcare fraud and abuse take many forms. Some of the most common types of frauds by providers are:

1. Billing for services that were not provided.

2. Duplicate submission of a claim for the same service.

3. Misrepresenting the service provided.

4. Charging for a more complex or expensive service than was actually provided.

5. Billing for a covered service when the service actually provided was not covered.

**Problem Statement**

The goal of this project is to "predict the potentially fraudulent providers" based on the claims filed by them. Along with this, we will also discover important variables helpful in detecting the behaviour of potentially fraud providers. further, we will study fraudulent patterns in the provider's claims to understand the future behaviour of providers.

## Introduction to the Dataset

For the purpose of this project, we are considering Inpatient claims, Outpatient claims and Beneficiary details of each provider. Lets's see their details :

 **Inpatient Data**

This data provides insights about the claims filed for those patients who are admitted in the hospitals. It also provides additional details like their admission and discharge dates and admit d diagnosis code.

**Outpatient Data**

This data provides details about the claims filed for those patients who visit hospitals and not admitted in it.

**Beneficiary Details Data**

This data contains beneficiary KYC details like health conditions or region they belong to etc.

## Definitions

- **Health care provider:** A health care provider is an individual or an institution that provides preventive, curative, promotional, or rehabilitative health care services in a systematic way to individuals, families or communities. An individual health care provider may be a health care professional within medicine, nursing, or allied health professions. Health care providers may also be a public/community health professional. Institutions include hospitals, clinics, primary care centres, and other service delivery points. The practice of health professionals and operation of health care institutions is typically regulated by national or state/provincial authorities through appropriate regulatory bodies for purposes of quality assurance. Together, they form part of an overall health care system.
- **Medicare:** Health insurance program in America
- **Inpatient:** means that the procedure requires the patient to be admitted to the hospital, primarily so that he or she can be closely monitored during the procedure and afterwards, during recovery.
- **Outpatient:** means that the procedure does not require hospital admission and may also be performed outside the premises of a hospital.
- **Beneficiary:** a person who receives benefits under health care insurance through the medicare or medicaid program
- **KYC:** KYC is an acronym for Know Your Customer, a legal requirement to perform identity checks and do customer due diligence. While KYC laws differ from country to country, the general principle involves collecting enough information to properly identify an individual and ensure that their activities are legitimate.

## Reading List

- https://rgare.com/knowledge-center/media/articles/provider-fraud-detection-and-management
- https://healthpayerintelligence.com/news/top-5-most-common-healthcare-provider-fraud-activities
