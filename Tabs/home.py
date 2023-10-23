"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Concrete Strength Detection System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Vertebral column anomaly detection using machine learning is a cutting-edge application of artificial intelligence in the field of healthcare. The vertebral column, also known as the spine, is a crucial component of the human skeletal system, and anomalies within it can have significant implications for a person's overall health and well-being. Machine learning models are being employed to analyze medical imaging data, such as X-rays, CT scans, or MRIs, to automatically detect and classify various vertebral column anomalies, including scoliosis, herniated discs, and fractures.<br><br>These machine learning algorithms are trained on vast datasets of labeled medical images, allowing them to learn complex patterns and features associated with normal and abnormal spinal structures. Through deep learning techniques, such as convolutional neural networks (CNNs) and recurrent neural networks (RNNs), these models can accurately identify anomalies, providing physicians with invaluable assistance in diagnosing and planning treatment for patients. Furthermore, machine learning can help in early detection, enabling timely interventions that can prevent the progression of spinal conditions and improve patient outcomes.<br><br>The integration of machine learning in vertebral column anomaly detection not only enhances diagnostic accuracy but also reduces the burden on healthcare professionals by automating the initial screening process, saving time and resources. As technology continues to advance, this approach holds great promise in revolutionizing the field of spinal healthcare, making early intervention and treatment more accessible and efficient.
        </p>
    """, unsafe_allow_html=True)
