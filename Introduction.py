import streamlit as st
import pandas as pd
import numpy as np


st.title('Impact of Respiratory and Cardiac Features on Effort-Based Decision Making')

st.subheader('Introduction')
st.write("""Breathing features such as average breathing rate, average tidal volume, or minutes ventilation were found many times to be relevant when trying to understand human behavior on decision making, which made us investigate if past respiratory features may help us predict future actions.
The study consists of extracting respiratory data using breathing-belt on subjects on mental and physical tasks. Each task has various levels of difficulty, and each type of task was repeated two times. Furthermore, we used Zeno lab breath metrics toolbox to extract respiratory features.""")
