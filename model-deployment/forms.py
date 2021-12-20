from wtforms import Form, RadioField, StringField, PasswordField, validators , SubmitField

class InputForm(Form):
     DISBURSED_AMOUNT = StringField('DISBURSED_AMOUNT')
     ASSET_COST = StringField('ASSET_COST')
     PRI_NO_OF_ACCTS = StringField('PRI_NO_OF_ACCTS')
     PRI_ACTIVE_ACCTS = StringField('PRI_ACTIVE_ACCTS')
     PRI_OVERDUE_ACCTS = StringField('PRI_OVERDUE_ACCTS')
     PRI_CURRENT_BALANCE = StringField('PRI_CURRENT_BALANCE')
     PRIMARY_INSTAL_AMT = StringField('PRIMARY_INSTAL_AMT')
     NEW_ACCTS_IN_LAST_SIX_MONTHS = StringField('NEW_ACCTS_IN_LAST_SIX_MONTHS')
     DELINQUENT_ACCTS_IN_LAST_SIX_MONTHS = StringField('DELINQUENT_ACCTS_IN_LAST_SIX_MONTHS')
     NO_OF_INQUIRIES = StringField('NO_OF_INQUIRIES')
     LOANEE_DOB_DAYS_DAY = StringField('LOANEE_DOB_DAYS DAY')
     LOANEE_DOB_DAYS_Month = StringField('Month')
     LOANEE_DOB_DAYS_Year = StringField('Year')
     DISBURSAL_DATE_DAYS_Day = StringField('DISBURSAL_DATE_DAYS_Day')
     DISBURSAL_DATE_DAYS_Month = StringField('Month')
     DISBURSAL_DATE_DAYS_Year = StringField('Year')
     EMPLOYMENT_TYPE = StringField('EMPLOYMENT_TYPE')
     Risk = RadioField(choices = [('Low',  1 ), ('Medium', 1), ('High', 1), ('Very High', 1)])
     submitButton = SubmitField('Submit')


