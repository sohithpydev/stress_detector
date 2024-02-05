"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector - An App by Sohith")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Considering today's lifestyle, people just sleep forgetting the benefits it provides to the human body. The reasons for not having a productive sleep could be many. Smart-Yoga Pillow (SaYoPillow) is envisioned as a device that may help in recognizing the importance of a good quality sleep to alleviate stress while establishing a measurable relationship between stress and sleeping habits. A system that analyzes the sleeping habits by continuously monitoring the physiological changes that occur during rapid eye movement (REM) and non-rapid eye movement (NREM) stages of sleep is proposed in the current work. In addition to the physiological parameter changes, factors such as sleep duration, snoring range, eye movement, and limb movements are also monitored. The SaYoPillow system is processed at the edge level with the storage being at the cloud. Not having to compromise the user's privacy, SaYoPillow proposes secure data transmission for both uploading and retrieving, and secure storage and communications as an attempt to reduce malicious attacks on healthcare. A user interface is provided for the user to control data accessibility and visibility. SaYoPillow has 96% accuracy which is close to other existing research works. However, SaYoPillow is the only work with security features as well as only work that considers sleeping habits for stress.
        </p>
    """, unsafe_allow_html=True)
