# Ovary-oracle:A PCOS predicting model
![pexels-rfstudio-3825586](https://github.com/Wachira-2030/Ovary-oracle/assets/42667708/f3b80c87-f704-4546-a223-0ec77b4b0ef7)


## Introduction
![pexels-larissa-farber-16190930](https://user-images.githubusercontent.com/58382818/182008486-01c0a56b-f055-4d94-b38f-7d838d5f8b0f.png)


## Business Understanding
> PCOS a significant public health problem and is one of the commonest hormonal disturbances affecting women of reproductive age. The condition affects an estimated 8–13% of women of reproductive age, and up to 70% of cases are undiagnosed.

The prevalence of PCOS is higher among some ethnicities and these groups often experience more complications, in particular related to metabolic problems.

Polycystic ovary syndrome (PCOS) is a common hormonal condition that affects women of reproductive age. It usually starts during adolescence, but symptoms may fluctuate over time.

PCOS can cause hormonal imbalances, irregular periods, excess androgen levels and cysts in the ovaries. Irregular periods, usually with a lack of ovulation, can make it difficult to become pregnant. PCOS is a leading cause of infertility.


## Main Objective
To create a deployable PCOS predicting model. 

## Data Understanding

> The dataset was collected from 10 different hospitals in Kerala,India.
- The variables: 
The columns in the main data set include:
       'Sl. No', 'Patient File No.', 'PCOS (Y/N)', ' Age (yrs)', 'Weight (Kg)',
       'Height(Cm) ', 'BMI', 'Blood Group', 'Pulse rate(bpm) ',
       'RR (breaths/min)', 'Hb(g/dl)', 'Cycle(R/I)', 'Cycle length(days)',
       'Marraige Status (Yrs)', 'Pregnant(Y/N)', 'No. of aborptions',
       '  I   beta-HCG(mIU/mL)', 'II    beta-HCG(mIU/mL)', 'FSH(mIU/mL)',
       'LH(mIU/mL)', 'FSH/LH', 'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio',
       'TSH (mIU/L)', 'AMH(ng/mL)', 'PRL(ng/mL)', 'Vit D3 (ng/mL)',
       'PRG(ng/mL)', 'RBS(mg/dl)', 'Weight gain(Y/N)', 'hair growth(Y/N)',
       'Skin darkening (Y/N)', 'Hair loss(Y/N)', 'Pimples(Y/N)',
       'Fast food (Y/N)', 'Reg.Exercise(Y/N)', 'BP _Systolic (mmHg)',
       'BP _Diastolic (mmHg)', 'Follicle No. (L)', 'Follicle No. (R)',
       'Avg. F size (L) (mm)', 'Avg. F size (R) (mm)', 'Endometrium (mm)',
       'Unnamed: 44'




  ## Data Preprocessing.
*Assessing the Data:* The dataset contains  a list of 541 rows of recipes and 45 columns.
## Modeling
The project started off with a baseline model which was a untuned logistic regression model .

<br><br>
## *Data Cleaning:* 
A new dataframes were created to contain relevant features.  Data in the dataset were stripped of irrelevant characters, converted to float type and columns renamed to contain units of measurements.   The dataframe was then checked to identify the presence of duplicates and missing values. 
<br><br>
## *Exploring the Data/Selecting Features:* 
To build an effective prediction system, a comprehensive exploratory data analysis (EDA) was conducted. This involved examining the key features of the dataset.
<br><br>
To get a better understanding of the dataset, visualizations were created. Correlation heatmap and stacked plots were used to explore the relationship between the target variable and various features.
<br><br>
Histograms were used to examine the distribution of key features. These plots provided insights into the distribution of these values and helped to identify any potential outliers or anomalies.

<br><br>
Overall, the EDA analysis provided valuable insights into the key features of the dataset and helped to identify any potential issues or challenges that needed to be addressed before building the prediction model.


<br><br>
## Making predictions 

The model that was used was a logistic regression model.It went through hyperparameter tuning and its accuracy score increased.


## Deployment 
The model was deployed and tested on streamlit.

## *How to run the model*
After downloading the file on your environment,ensure you have a data science environment and have streamlit installed in the environment you are working on

After you are done run on your bash:
$ streamlit run app.py

## Conclusion 

This was a small passion project that does have room for more training. One can use it to learn more and try new things.
*Happy Learning Guys!<br> And Cheers*
