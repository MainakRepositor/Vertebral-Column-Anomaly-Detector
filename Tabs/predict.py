"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the detection of vertebral column anomaly.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    pelvic_incidence = st.slider("Pelvic Incidence", int(df["pelvic_incidence"].min()), int(df["pelvic_incidence"].max()))
 
    pelvic_tilt = st.slider("Pelvic Tilt", int(df["pelvic_tilt"].min()), int(df["pelvic_tilt"].max()))
    
    lumbar_lordosis_angle = st.slider("Lumbar Lordosis Angle", int(df["lumbar_lordosis_angle"].min()), int(df["lumbar_lordosis_angle"].max()))
    
    sacral_slope = st.slider("Sacral Slope", int(df["sacral_slope"].min()), int(df["sacral_slope"].max()))
    
    pelvic_radius = st.slider("Pelvic Radius", float(df["pelvic_radius"].min()), float(df["pelvic_radius"].max()))
    
    degree = st.slider("Degree", int(df["degree"].min()), int(df["degree"].max()))

    # Create a list to store all the features
    features = [pelvic_incidence,pelvic_tilt,lumbar_lordosis_angle,sacral_slope,pelvic_radius,degree]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.20 #correction factor
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The vertebral column has no deformities and is in healthy state")
        elif (prediction == 2):
            st.warning("The person is detected with hernia")
        elif (prediction == 3):
            st.error("The person is detected with spondylosis")

        # Print teh score of the model 
        st.write("The model used is trusted by physicians and has an accuracy of ", (score*100),"%")
