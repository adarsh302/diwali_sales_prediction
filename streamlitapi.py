import pickle
import streamlit as st

model = pickle.load(open('E:/Desktop/ML Project/rf.pkl','rb'))

def main():
    st.title("Diwali Sales Prediction")

    #input variable
    
    product_1_mysore_pak = st.number_input("product_1_mysore_pak in Kg") 
    product_2_soan_papdi = st.number_input("product_2_soan_padi in Kg ")
    product_3_motichoor = st.number_input("product_3_motichoor in Kg")
    product_4_kaju_barfi = st.number_input("product_4_kaju_barfi in Kg")
    amount_1_mysore_pak = st.number_input("amount_1_mysore_pak in Rs")
    amount_2_soan_papdi = st.number_input("amount_2_soan_papdi in Rs")
    amount_3_motichoor = st.number_input("amount_3_motichoor in Rs")
    amount_4_kaju_barfi = st.number_input("amount_4_kaju_barfi in Rs")
    

    #prediction
    if st.button("Predict"):
        if product_1_mysore_pak==0.0 and product_2_soan_papdi==0.0 and product_3_motichoor==0.0 and product_4_kaju_barfi==0.0:
            st.success('Total amount is Rs {}'.format(0.0))
        else:
            makeprediction = model.predict([[product_1_mysore_pak,product_2_soan_papdi,product_3_motichoor,product_4_kaju_barfi,
            amount_1_mysore_pak,amount_2_soan_papdi,amount_3_motichoor,amount_4_kaju_barfi]])
            output = round(makeprediction[0],2)
            st.success('Total amount is Rs {}'.format(output))

if __name__ == '__main__':
    main()


