import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Akshay Narvate.
##### *Resume* 
''')

image = Image.open('dp.png')
#st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
#st.info('''
- Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
- Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
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
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
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

#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Science** (Microbiology, Genetics, Chemistry), *Bhavans Vivekananda College*, Hyderabad',
'1998-2002')
st.markdown('''
- Percentage: `66`
- Graduated with First Class.
''')

#####################
st.markdown('''
## Work Experience
''')

#txt('**Head, Center of Data Mining and Biomedical Informatics**, Faculty of Medical Technology, Mahidol University, Thailand',
'2011-2021')
#st.markdown('''
- Managing a Center of `10` professors, researchers and students to ensure KPIs are strategically achieved namely to publish at least `20+` research publications annually. 
- Actively took part in the talent hiring process as well as help employees to plan and develop their career path.
- Set budget and handle procurement in order to facilitate education and research activities. Secured `> 10 million THB` budget.
- Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
''')

txt('**Technical Writer**, [Akshay Narvate Blog](https://medium.com/@akshaynarvate786123) on Medium.com',
'2022-Present')
st.markdown('''
#- `1` subscribers on Medium
- Written `3` technical blogs on data science, machine learning and on mindset.
''')

#####################
st.markdown('''
## Data Science Projects
''')
txt4('Fitness Prediction Application', 'Gym-App is a fully deployed Machine Learning model that helps you predict your health status based on your inputs.', 'https://share.streamlit.io/akshaynarvate/gymapp/main/main.py')
txt4('Bank Product Recommendation Engine', 'This is an unsupervised Machine Learning project that uses Collaborative Filtering method that recommends products based on the similar customer interests.', 'https://share.streamlit.io/akshaynarvate/product-recommendation-engine/main/main.py')
txt4('Stock Price Prediction with LSTM', 'Reliance Stock Prediction is Deep Learning LSTM model that predicts stock closing price using LSTM based on the Open, High, Low and Volume as inputs.','https://share.streamlit.io/akshaynarvate/stock-price-prediction-lstm/main/main.py')
txt4('Health Insurance Premium Prediction App', 'Health Insurance Premium Amount Prediction uses Machine learning predicts premium amount using Linear Regression taking age, sex, bmi, smoker as inputs.', 'https://share.streamlit.io/akshaynarvate/health-insurance-premium-prediction/main/main.py')
txt4('Future Sales Prediction', 'Application predicts future sales using Machine Learning taking TV and Radio advertising budget as input.','https://share.streamlit.io/akshaynarvate/future-sales-prediction/main/main.py')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
#txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/akshaynarvate')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/akshaynarvate')
txt2('Email', 'akshaynarvate786123@gmail.com')
txt2('Medium', 'https://medium.com/@akshaynarvate786123')
