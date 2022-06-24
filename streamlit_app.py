
   
import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Akshay Narvate, Data Scientist.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Data Scientist with almost 0.6 years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills worked closely with business partners.
- Developed customised models for various business problems and designed the prototypes from problem identification to model deployment to increase the
  financial gains and the efficiency.
- Experience in developing statistical/Machine Learning models
  using various techniques and technologies using R, Python.
- Provided EDA to uncover meaningful patterns out of data using R/Python.
- Ensuring that analysis are delivered on time with more focussed on client &
  business satisfaction.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Akshay Narvate</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Data Science Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
      
def txt5(a, b, c, d):
  col1, col2, col3, col4 = st.columns([1.5,2,1.5,1.5])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
  with col4:
    st.markdown(d)


#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Science** (Microbiology, Genetics, Chemistry),  *Bhavans Vivekananda College* , Hyderabad',
'2015-2018')
st.markdown('''
- Percentage: `66`
- Graduated with First Class.''')


#####################
st.markdown('''
## Work Experience
''')

txt('**Data Science Intern**,  Bepec Solutions , Bangalore , India',
'2022-Present')
txt('**Data Science Real life Projects:-**', '')
txt('**Next Best Action**, Churn Customer , Standard Bank , Mozambique' ,
'2022')
st.markdown('''
- Increased the **Revenue** of Standard Bank by **1.2%** by **decreasing** the **Customer churn** rate by **5%**.
- **Proactively finding** out about the **Churn Customer**.
- Done **EDA** to uncover **meaningful patterns** out of data using Python.
- Developed **customised model** for **business problem** to increase the
  **financial gains** & **efficiency**.
- **Timely** delivery of **Analysis** more focussed on **client** &
  **business satisfaction**.
- Transformed business by **creating value** out of data using **analytics**.''')

txt('**Recommendation Engine**, Bank Product Recommendation Engine , Standard Bank , Mozambique' ,
'2022')
st.markdown('''
- Developed **Collaborative Filtering Recommendation Engine** which is User centric by understanding **patterns in ratings**.
- Created **Proof of Concept** for business demonstration.
- Based on **pattern understanding** in ratings **similar products** are recommended which interests them.
''')

txt('**Fitness Prediction App**, Gym App , India' ,
'2022')
st.markdown('''
- **Developed** customised **Proof of Concept** that helps predict health status based on inputs.
- Extracted **meaningful** hidden **patterns** and flawlessly predict outcome.
- **Fully Deployed** fitness prediction **app** to predict outcome based on age, height, weight.
''')

txt('**Technical Writer**, [Akshay Narvate Blog](https://medium.com/@akshaynarvate786123) on Medium.com',
'2022-Present')
st.markdown('''
- `2+` subscribers on Medium
- Written `3` blogs on data science, machine learning, business and mindset.
''')

#####################
st.markdown('''
## Data Science Projects
''')
txt4('Next Best Action Standard Bank', 'This is an supervised Machine Learning project that uses Random forest method that proactively finds out the churn customer.', 'https://github.com/akshaynarvate/Next-Best-Action')    
txt5('Bank Product Recommendation Engine', 'This is an unsupervised Machine Learning project that uses Collaborative Filtering method that recommends products based on the similar customer interests.', 'https://akshaynarvate-product-recommendation-engine-main-2cy7u3.streamlitapp.com/', 'https://github.com/akshaynarvate/Bank-Product-Recommendation-engine')
txt5('Fitness Prediction Application', 'Gym-App is a fully deployed Machine Learning model that helps you predict your health status based on your inputs.', 'https://akshaynarvate-gymapp-main-82qgiy.streamlitapp.com/', 'https://github.com/akshaynarvate/Gymapp')
txt5('Stock Price Prediction with LSTM', 'Reliance Stock Prediction is Deep Learning LSTM model that predicts stock closing price using LSTM based on the Open, High, Low and Volume as inputs.','https://akshaynarvate-stock-price-prediction-lstm-main-f70w7d.streamlitapp.com/', 'https://github.com/akshaynarvate/Stock-Price-Prediction-LSTM')
txt5('Health Insurance Premium Prediction App', 'Health Insurance Premium Amount Prediction uses Machine learning predicts premium amount using Linear Regression taking age, sex, bmi, smoker as inputs.', 'https://akshaynarvate-health-insurance-premium-prediction-main-2iugd5.streamlitapp.com/', 'https://github.com/akshaynarvate/Health-Insurance-Premium-Prediction')
txt5('Future Sales Prediction', 'Application predicts future sales using Machine Learning taking TV and Radio advertising budget as input.','https://akshaynarvate-future-sales-prediction-main-qcfcjf.streamlitapp.com/', 'https://github.com/akshaynarvate/Future-Sales-Prediction')
    

#####################
st.markdown('''
## Skills
''')
txt3('Python', 'R')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
#txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/akshaynarvate')
txt2('GitHub', 'https://github.com/akshaynarvate')
txt2('Email', 'akshaynarvate@proton.me')
txt2('Medium', 'https://medium.com/@akshaynarvate786123')
