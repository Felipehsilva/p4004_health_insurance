import pickle
import pandas as pd

class HealthInsurance:
    

      
    
    def data_cleaning(self, df1):
        #Rename columns
        cols_new = ['id', 'gender', 'age', 'driving_license', 'region_code',
       'previously_insured', 'vehicle_age', 'vehicle_damage', 'annual_premium',
       'policy_sales_channel', 'vintage', 'response']
        
        #rename
        df1.columns = cols_new
        
        return df1
    
    def feature_engineering(self, df2):
        #Vehicle Damage Number
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        #vehicle_age
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_year')
        return df2
                        
        
    def data_preparation (df5): 
        # -----------Standardization----------------------
        
        # annual_premium
        df5['annual_premium'] = self.annual_premium.transform (df5[['annual_premium']].values)
        
       
        # -----------Reescaling----------------------
        

        # age MinMax Scaler
        df5['age'] = self.mms_age.transform(df5[['age']].values) 
        
        # vintage MinMax Scaler
        df5['vintage'] = self.mms_vintage.transform(df5[['vintage']].values) 
      
        
        # -----------Encoding----------------------
        
        #gender - One Hot Encoding / Target Encoding
       
        df5.loc[:,'gender'] = df5['gender'].map(self.target_encode_gender)
       


        # region_code - Frequency encoding / Target encoding / Weighted Terget Enconding
        #Escolhido Target encoding

        #target_encode_region_code.head()
        df5.loc[:,'region_code'] = df5['region_code'].map(self.target_encode_region_code)
       


        # previously_insured - no need encode it is already in 0/1)

        # vehicle_age - One Hot Enconding / Order Enconding  / Frequency encoding -
        #Escolhido One Hot Enconding
        #Get dummies passa a columna que quero e devolve o DF inteiro para sustentar o one hot encode
        df5 = pd.get_dummies(df5,prefix = 'vehicle_age', columns =['vehicle_age'])

        # vehicle_damage - no need encode it is already in 0/1)

        # policy_sales_channel - Frequency encoding / Target encoding 
        #frequency encoding
   
        df5.loc[:,'policy_sales_channel'] = df5 ['policy_sales_channel'].map(self.fe_policy_sales_channel)
        

        # -----------Selected feature----------------------

        cols_selected = ['annual_premium','vintage','age','region_code','vehicle_damage','policy_sales_channel','previously_insured']
        
        return df5[cols_selected]
        
        
    def get_prediction (self,model, original_data, test_data):
        
        #model prediction
        pred = model.predict_proba(test_data)
        
        #join prediction into original data
        original_data['score'] = prod
        
        return original_data.to_json(orient='records', date_format='iso')
        
