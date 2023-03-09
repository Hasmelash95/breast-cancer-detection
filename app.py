import streamlit as st 
from app_pages.multipage import MultiPage
from app_pages.page_summary import summary_body
from app_pages.page_ultrasound_visualizer import ultrasound_visual_body
from app_pages.page_breast_cancer_detector import cancer_detector_body
from app_pages.page_hypothesis import hypothesis_body
from app_pages.page_ml_performance import ml_performance_body

# Creates an instance of the MultiPage class
app_instance = MultiPage(app_name="Breast Cancer Detection")

# Calls the app_page() method in the MultiPage class
app_instance.app_page("Summary", summary_body)
app_instance.app_page("Ultrasound Visualizer", ultrasound_visual_body)
app_instance.app_page("Breast Cancer Detector", cancer_detector_body)
app_instance.app_page("Hypothesis", hypothesis_body)
app_instance.app_page("ML Performance", ml_performance_body)

# Runs the app
app_instance.run() 

