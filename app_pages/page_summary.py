import streamlit as st 

def summary_body():
    st.header("Summary of Project")

    st.info(f"Breast Cancer is the most common cancer in" 
             " the UK with nearly 56000 new cases every year."
             " The vast majority of patience are women with"
             " men comprising less than 400 of these cases."
             " It is caused by uncontrolled cell division in"
             " in the breast tissue that forms a tumour."
             " Early detection and diagnosis is key in the"
             " treatment of breast cancer."
             " One method of diagnosis is a breast ultrasound"
             " which uses sound waves to look around inside"
             " the breast to find any tumours.\n"
             " This project uses 780 ultrasound images from"
             " women between ages 25 and 75 collected in"
             " 2018.")

    st.subheader("Business Requirements")

    st.success(f"1. The client is interested in determining"
                " the visual differences between normal breast"
                " ultrasounds, those containing benign tumours"
                " and those containing malignant tumours.\n"
                " 2. The client is interested in predicting"
                " whether a given breast ultrasound is normal"
                " benign or malignant.")

    st.subheader("Additional Information")

    st.info(f"For more information, please read the README document:\n"
             " https://github.com/Hasmelash95/breast-cancer-detector/blob/main/README.md")