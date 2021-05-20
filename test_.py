import pandas as pd
df=pd.read_csv('dataset_1.csv')
from tabulate import tabulate

def name_format(NAME):
    NAME=NAME.lower().lstrip().rstrip()
    temp_list=NAME.split(' ')
    temp=[]
    temp2=''
    nameZ=''
    for i in temp_list:
        temp=list(i)
        temp[0]=str(temp[0]).upper()
        nameZ="".join(temp)
        temp2=temp2+" "+nameZ
    temp2=temp2.lstrip()
    return temp2

def phone_format(PHONE):
    PHONE.lstrip().rstrip()
    PHONE=int(PHONE)
    return PHONE


#adding new data portion
def add_data():
    name1=input("Enter name:")
    name1=name_format(name1)
    
    age1=input("Enter age")
    
    sex1=input("Sex")
    sex1=name_format(sex1)

    maritial_status1=input("Maritial Status")
    maritial_status1=maritial_status1.upper().lstrip().rstrip()

    adhaar_card_no1=input("Enter Adhaar Card NO.")
    
    pan_card_no1=input("PAN")
    pan_card_no1=pan_card_no1.upper().lstrip().rstrip()

    address1=input("Address")
    
    phone_no1=input("Phone no.")
    phone_no1=phone_format(phone_no1)
    
    policy_code1=input("Policy code")
    policy_name1=input("Policy name")
    policy_expiry_year1=input("Expiry year of Policy")
    
    insurance_amount1=input("Insurance Amount")
    insurance_amount1=insurance_amount1.lstrip().rstrip()

    nominee_name1=input("Nominee Name")
    nominee_name1=name_format(nominee_name1)
    
    nominee_relation1=input("Nominee Relation")
    nominee_relation1=nominee_relation1.upper().lstrip().rstrip()

    nominee_no1=input("Nominee Phone No.")
    nominee_no1=phone_format(nominee_no1)

    
    from csv import writer
    List=[name1,age1,sex1,maritial_status1,adhaar_card_no1,pan_card_no1,address1,phone_no1,policy_code1,policy_name1,policy_expiry_year1,insurance_amount1,nominee_name1,nominee_relation1,nominee_no1] 
    with open('dataset_1.csv', 'a') as f_object: 
        writer_object = writer(f_object) 
        writer_object.writerow(List)
        f_object.close() 

    df.sort_values(by=['NAME','PHONE NO.'], inplace=True) 


def find_data():
    #taking input from the user
   
    import pandas as pd
    df=pd.read_csv('dataset_1.csv')
    name=input("Enter name:")
    name=name_format(name)

    ph=input("Enter phone no.:")
    ph=phone_format(ph)

    #converting phone no. and name into required format ...
    #Abhay Kumar Shukla example
    #9121569089  example
    
    filt=(df['NAME']==name) & (df['PHONE NO.']==ph)
    ans=filt.tolist()

    if True not in ans:
        print('-------------------------')
        print('Not found in our database')
        print('-------------------------')
        print('Enter data')
        print('If want to enter data... Press 1')
        check=input()
        if int(check)==1:
            add_data()



    else:
        nominee_no=df.loc[filt,'NOMINEE NO.'].tolist()  #extracting data we found 
        nominee_name=df.loc[filt,'NOMINEE NAME'].tolist()
        address=df.loc[filt,'ADDRESS'].tolist()
        nominee_relation=df.loc[filt,'NOMINEE RELATION'].tolist()
        age=df.loc[filt,'AGE'].tolist()
        aadhar_card_no=df.loc[filt,'ADHAAR CARD NO.'].tolist()
        policy_code=df.loc[filt,'POLICY CODE'].tolist()
        policy_name=df.loc[filt,'POLICY NAME'].tolist()
        policy_expiry_year=df.loc[filt,'POLICY EXPIRY YEAR'].tolist()
        insurance_amount=df.loc[filt,'INSURANCE AMOUNT'].tolist()
        
        print('----------------------')
        print('Found in our data base')
        print('----------------------')
        print(nominee_name[0])     #printing data  
        print(nominee_relation[0])
        print(address[0])
        print(nominee_no[0])
        print(age[0])
        print(aadhar_card_no[0])
        print(policy_code[0])
        print(policy_name[0])
        print(policy_expiry_year[0])
        print(insurance_amount[0])

        table=[["Nominee Name",nominee_name[0]],
        ["Age",age[0]]]

        print(tabulate(table))
    

#print('Add Data for comapnies ')
#make a switch case 
#add_data()
find_data()
# print('find data ')

