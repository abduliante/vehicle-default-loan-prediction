# Vehicle Default Loan Prediction
Financial institues are suffering from significant loses due to car loan defaults. This has resulted in tighter car loans and higher car loan denial rates. Institutions have addressed the need for better credit risk scoring model. Therefore, in our project we seek to predict vehicle loan defaults on customers to determine whether a subject of given criteria is receptive to defaulting their loan or not. 

## Research Hypothesis:
In our project, we try to hypothesize if we can accurately predict the possibility that the loanee/borrower will default on the car loan. 

## Data Description
Our data is fetched from Kaggle website that contains information about loanee (Demographics such as age, income, etc.), loan itself (amount, loan to value ratio, Equated Monthly Installments, etc.) and information from the bureau (Bureau score, number of active accounts, status of other loans, credit history, etc.). There is no disclosure about the origin of the data (i.e country) but from our column investigation, it turns out to be from India. Based on that assumption which is not fully verified, we will treat it as undisclosed.

There are approximately 230k+ rows and 41 columns in the dataset. Data description goes as follows:

| Variable Name                       | Description                                                                        |
|-------------------------------------|------------------------------------------------------------------------------------|
| UniqueID                            | Identifier for customers                                                           |
| <mark>loan_default</mark>                        | <mark>"Payment default in the first EMI on due date, 1 for default"</mark>                      |
| disbursed_amount                    | Amount of Loan disbursed                                                           |
| asset_cost                          | Cost of the Asset                                                                  |
| ltv                                 | Loan to Value of the asset                                                         |
| branch_id                           | Branch where the loan was disbursed                                                |
| supplier_id                         | Vehicle Dealer where the loan was disbursed                                        |
| manufacturer_id                     | "Vehicle manufacturer(Hero, Honda, TVS etc.)"                                      |
| Current_pincode                     | Current pincode of the customer                                                    |
| Date.of.Birth                       | Date of birth of the customer                                                      |
| Employment.Type                     | Employment Type of the customer (Salaried/Self Employed)                           |
| DisbursalDate                       | Date of disbursement                                                               |
| State_ID                            | State of disbursement                                                              |
| Employee_code_ID                    | Employee of the organization who logged the disbursement                           |
| MobileNo_Avl_Flag                   | if Mobile no. was shared by the customer then flagged as 1                         |
| Aadhar_flag                         | if aadhar was shared by the customer then flagged as 1                             |
| PAN_flag                            | if pan was shared by the customer then flagged as 1                                |
| VoterID_flag                        | if voter  was shared by the customer then flagged as 1                             |
| Driving_flag                        | if DL was shared by the customer then flagged as 1                                 |
| Passport_flag                       | if passport was shared by the customer then flagged as 1                           |
| PERFORM_CNS.SCORE                   | Bureau Score                                                                       |
| PERFORM_CNS.SCORE.DESCRIPTION       | Bureau score description                                                           |
| PRI.NO.OF.ACCTS                     | count of total loans taken by the customer at the time of disbursement             |
| PRI.ACTIVE.ACCTS                    | count of active loans taken by the customer at the time of disbursement            |
| PRI.OVERDUE.ACCTS                   | count of default accounts at the time of disbursement                              |
| PRI.CURRENT.BALANCE                 | total Principal outstanding amount of the active loans at the time of disbursement |
| PRI.SANCTIONED.AMOUNT               | total amount that was sanctioned for all the loans at the time of disbursement     |
| PRI.DISBURSED.AMOUNT                | total amount that was disbursed for all the loans at the time of disbursement      |
| SEC.NO.OF.ACCTS                     | count of total loans taken by the customer at the time of disbursement             |
| SEC.ACTIVE.ACCTS                    | count of active loans taken by the customer at the time of disbursement            |
| SEC.OVERDUE.ACCTS                   | count of default accounts at the time of disbursement                              |
| SEC.CURRENT.BALANCE                 | total Principal outstanding amount of the active loans at the time of disbursement |
| SEC.SANCTIONED.AMOUNT               | total amount that was sanctioned for all the loans at the time of disbursement     |
| SEC.DISBURSED.AMOUNT                | total amount that was disbursed for all the loans at the time of disbursement      |
| PRIMARY.INSTAL.AMT                  | EMI Amount of the primary loan                                                     |
| SEC.INSTAL.AMT                      | EMI Amount of the secondary loan                                                   |
| NEW.ACCTS.IN.LAST.SIX.MONTHS        | New loans taken by the customer in last 6 months before the disbursment            |
| DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS | Loans defaulted in the last 6 months                                               |
| AVERAGE.ACCT.AGE                    | Average loan tenure                                                                |
| CREDIT.HISTORY.LENGTH               | Time since first loan                                                              |
| NO.OF_INQUIRIES                     | Enquries done by the customer for loans                                            |


## Tools:
The prediction is going to be delivered on an IPython Notebook using Cookiecutter structure. Tools to be used are:
* Python 3.7
* Pandas
* Numpy
* Scikit-learn
* Matplotlib
* Seaborn
* Tableau
* Flask - Deploying model through Heroku

