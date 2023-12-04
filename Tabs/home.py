import streamlit as st

def app():
  
    st.title(" SleepEmoStress Analyzer: Stress Level Detector")

    st.image("./images/jen.jpg") 

    st.markdown(
    """<p style="font-size:20px;">
            Considering today’s lifestyle, people just sleep forgetting the benefits sleep provides to the human body. SleepEmoStress Analyzer is proposed to help in understanding the relationship between stress and sleep and to fully materialize the idea of “Smart-Sleeping” by proposing an edge device. An edge processor with a model analyzing the physiological changes that occur during sleep along with the sleeping habits is proposed. Based on these changes during sleep, stress prediction for the following day is proposed. The secure transfer of the analyzed stress data along with the average physiological changes to the IoT cloud for storage is implemented. A secure transfer of any data from the cloud to any third-party applications is also proposed. A user interface is provided allowing the user to control the data accessibility and visibility. SleepEmoStress Analyzer is novel, with security features as well as consideration of sleeping habits for stress reduction, with an accuracy of up to 96%.
        </p>
    """, unsafe_allow_html=True)