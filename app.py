        
# # save this as app.py

# from flask import Flask, request,render_template
# from markupsafe import escape
# import pickle
# import numpy as np

# app = Flask(__name__)
# model = pickle.load(open('randomForest_Model.pkl', 'rb'))

# @app.route('/predict', methods= ['GET','POST'])
# def predict():
#     name = request.args.get("name", "World")
#     return render_template("index.html")       
        
# if __name__ == "__main__"  :
#     app.run(debug=True)     
#         save this as app.py-
from flask import Flask, escape, request, render_template
import pickle
import numpy as np
import bz2file as bz2
from sklearn.metrics import precision_score,recall_score,accuracy_score

app = Flask(__name__)

def decompress_pickle(file):

   data = bz2.BZ2File(file, 'rb')
   data = pickle.load(data)
   return data
model = decompress_pickle('randomForestModelNewly.pbz2')
# model = pickle.load(open('randomForestModel', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST','GET' ])
def predict():
    if request.method ==  'POST':
        YearsofEmployment = float(request.form['emp_length_int'])
        AnnualIncome = float(request.form['annual_inc'])
        LoanAmount = float(request.form['loan_amount'])
        InterestRate = float(request.form['interest_rate'])
        Age = float(request.form['age'])
        Dit = float(request.form['dti'])
        TotalPayment = float(request.form['total_pymnt'])
        Installment = float(request.form['installment'])
        HomeOwnership = request.form['home_ownership']
        IncomeCategory = request.form['income_category']
        Term = request.form['term']
        ApplicationType = request.form['application_type']
        Purpose = request.form['purpose']
        InterestPayments = request.form['interest_payments']
        Grade = request.form['grade']
                
            



           

        # term
        if ( Term == "36"):
            Months_36=1
            Months_60=0
        elif( Term == "60"):
            Months_36=0
            Months_60=1

        # income_category
        if(IncomeCategory =='High'):
            income_category_1 = 1
            income_category_2 = 0
            income_category_3 = 0
        elif(IncomeCategory == 'Medium'):
            income_category_1 = 0
            income_category_2 = 1
            income_category_3 = 0
        elif(IncomeCategory =="Low"):
            income_category_1 = 0
            income_category_2 = 0
            income_category_3 = 1
        else:
            income_category_1 = 0
            income_category_2 = 0
            income_category_3 = 0  
            
           
        #HomeOwnership
        if(HomeOwnership =='Other'):
            Mortgage=0
            Other = 1
            Rent=0
            Own=0
            none=0
            
        elif(HomeOwnership =='Mortgage'):
            Mortgage=1
            Other = 0
            Rent=0
            Own=0
            none=0
           
        elif(HomeOwnership =='Rent'):
            Mortgage=0
            Other = 0
            Rent=1
            Own=0
            none=0
            
        elif(HomeOwnership =='Own'):
            Mortgage=0
            Other = 0
            Rent=0
            Own=1
            none=0
           
        elif(HomeOwnership =='None'):
            Mortgage=0
            Other = 0
            Rent=0
            Own=0
            none=1
           
            
        # Purpose
        if(Purpose  == "Car"):
            Car = 1
            Credit_card = 0  
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Credit card"):
            Car = 0
            Credit_card = 1
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose  == "Debt consolidation"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 1
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Educational"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 1
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Home improvement"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 1
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "House"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 1
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Major purchase"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 1
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Medical"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 1
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Moving"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 1
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0
        elif(Purpose == "Other"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 1
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0
        elif(Purpose == "Renewable energy"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 1
            Small_business = 0
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Small business"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 1
            Vacation = 0
            Wedding = 0

        elif(Purpose == "Vacation"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 1
            Wedding = 0

        elif(Purpose == "Wedding"):
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 1

        else:
            Car = 0
            Credit_card = 0
            Debt_consolidation = 0
            Educational = 0
            Home_improvement = 0
            House = 0
            Major_purchase = 0
            Medical = 0
            Moving = 0
            Other = 0
            Renewable_energy = 0
            Small_business = 0
            Vacation = 0
            Wedding = 0



        # interest payments
        if(InterestPayments=="High"):
            High=1
            Low=0
        elif(InterestPayments=="Low"):
            High=0
            Low=1
        else:
            High=0
            Low=0
            
        #applicationtype
        if(ApplicationType=="Individual"):
            Individual=1
            Joint=0
        elif(ApplicationType=="Joint"):
            Individual=0
            Joint=1
        else:
            Individual=0
            Joint=0

            #grade
        if(Grade == "A"):
            grade_A = 1
            grade_B = 0
            grade_C = 0 
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 0

        elif(Grade == "B"):
            grade_A = 0
            grade_B = 1
            grade_C = 0 
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 0

        elif(Grade == "C"):
            grade_A = 0
            grade_B = 0
            grade_C = 1
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 0

        elif(Grade == "D"):
            grade_A = 0
            grade_B = 0
            grade_C = 0 
            grade_D = 1
            grade_E = 0
            grade_F = 0
            grade_G = 0

        elif(Grade == "E"):
            grade_A = 0
            grade_B = 0
            grade_C = 0 
            grade_D = 0
            grade_E = 1
            grade_F = 0
            grade_G = 0

        elif(Grade == "F"):
            grade_A = 0
            grade_B = 0
            grade_C = 0 
            grade_D = 0
            grade_E = 0
            grade_F = 1
            grade_G = 0

        elif(Grade == "G"):
            grade_A = 0
            grade_B = 0
            grade_C = 0 
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 1

        else:
            grade_A = 0
            grade_B = 0
            grade_C = 0 
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 0


        # YearsofEmploymentlog = float(YearsofEmployment)
        # AnnualIncomelog = float(AnnualIncome)
        # LoanAmountlog = LoanAmount
        # YInterestRatelog = InterestRate
        # Agelog = Age
        # DTIlog = Dit
        # TotalPaymentlog = TotalPayment
        # Installmentlog = Installment

        prediction = model.predict([[YearsofEmployment ,AnnualIncome,LoanAmount,
                                     InterestRate, Age, Dit,TotalPayment,Installment, Mortgage,none ,Other,  
                                     Own, Rent,income_category_1,income_category_2,income_category_3,Months_36,Months_60,Individual,Joint, Car, Credit_card,Debt_consolidation,Educational,House,Major_purchase, Medical, Moving,Other ,Renewable_energy,Small_business, Vacation, Wedding,Home_improvement,High,Low, grade_A, grade_B,grade_C,grade_D,grade_E,grade_F, grade_G]])
              
                
        Accuracy= 94.15607344632768
        # print(prediction)

        if(prediction==0):
            prediction="The customer is suitable for a loan. Hence it will be a Good Loan"
            
            # probabilty= "There is a high chance to return the payments from the customer.The probabilty of the risk"
            return render_template("prediction.html",prediction_text=prediction,accuracy=Accuracy)
            
        elif(prediction==1):
            prediction="Oops!.......The customer is not suitable for a loan. Hence it will be a bad loan"
            
            # probabilty= "There is a low chance to return the payments from the customer.The probabilty of the risk"
            return render_template("prediction.html",prediction_text=prediction,accuracy=Accuracy)

        




    else:
         return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)


