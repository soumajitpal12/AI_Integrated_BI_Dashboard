import streamlit as st

st.set_page_config(page_title="Conversational BI", layout="wide")

# Hide sidebar
st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
button[kind="header"] {display: none;}
div[data-testid="stSidebarNav"] {display: none;}

body{
background-color:#020617;
color:white;
}

.navbar{
top: 10px;
display:flex;
justify-content:space-between;
align-items:center;
padding:20px 60px;
background:#020617;
}

.logo{
font-size:28px;
font-weight:bold;
color:#38bdf8;
}

.nav-links{
display:flex;
gap:30px;
}

.nav-links a{
text-decoration:none;
color:white;
font-size:18px;
}

.hero{
height:50vh;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
}

.hero-title{
font-size:65px;
font-weight:bold;
color:#38bdf8;
}

.hero-text{
font-size:22px;
max-width:650px;
}

.section{
height:90vh;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
}

.section h2{
font-size:50px;
color:#38bdf8;
}

.section p{
font-size:20px;
max-width:700px;
}
            
/* Try It Now button container */
.trybutton {
display:flex;
justify-content:center;
margin-top:40px;
}

/* Streamlit button styling */
.trybutton button {
background: linear-gradient(90deg,#00c6ff,#0072ff);
color:white;
font-size:24px;
font-weight:700;
padding:18px 60px;
border-radius:60px;
border:none;
cursor:pointer;
transition:all 0.35s ease;
box-shadow:0px 10px 30px rgba(0,114,255,0.5);
letter-spacing:1px;
}

/* Hover animation */
.trybutton button:hover {
transform:translateY(-3px) scale(1.08);
background:linear-gradient(90deg,#0072ff,#00c6ff);
box-shadow:0px 15px 40px rgba(0,114,255,0.8);
}
            
</style>
""", unsafe_allow_html=True)


# NAVBAR
st.markdown("""
<div class="navbar">

<div class="logo">
Conversational BI
</div>

<div class="nav-links">
<a href="#home">Home</a>
<a href="#features">Features</a>
<a href="#about">About</a>
<a href="#contact">Contact</a>
</div>

</div>
""", unsafe_allow_html=True)


# HERO
st.markdown("""
<div id="home" class="hero">

<div class="hero-title">
AI Powered Conversational BI Dashboard
</div>

<div class="hero-text">
Ask business questions in natural language and instantly generate SQL queries and visual insights powered by AI.
</div>

</div>
""", unsafe_allow_html=True)


center = st.columns([3,1,3])[1]

st.markdown('<div class="trybutton">', unsafe_allow_html=True)

left, center, right = st.columns([3,1,3])

with center:
    if st.button("Try It Now"):
        st.markdown(
            '<meta http-equiv="refresh" content="0; url=http://localhost:8501/streamlit_app">',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)


# FEATURES
st.markdown("""
<div id="features" class="section">

<h2>Features</h2>

<p>
The Conversational Business Intelligence Dashboard enables users to explore and analyze data using natural language instead of complex SQL queries. By leveraging Artificial Intelligence, the system converts user questions into SQL queries and automatically retrieves the relevant data from the database.
</p>

<p>
One of the key features of this project is intelligent chart generation. Based on the query result, the system automatically selects the most suitable visualization to represent the data. It supports multiple chart types including bar charts, pie charts, line charts, scatter plots, and histograms for effective data interpretation.
</p>


<p>
Additionally, the system includes secure user authentication to ensure controlled access to the dashboard. With a clean interface and AI-powered analytics, the platform simplifies business intelligence and makes data-driven decision making faster and more accessible for users.
</p>

</div>
""", unsafe_allow_html=True)


# ABOUT
st.markdown("""
<div id="about" class="section">

<h2>About</h2>

<p>
This project, <b>Conversational BI Dashboard</b>, is developed as an academic project to demonstrate how Artificial Intelligence can simplify data analysis and business intelligence. 
The system allows users to ask questions in natural language and instantly generate SQL queries, insights, and visualizations.
</p>

<p>
This project is developed by <b>Soumajit Pal</b>, with a keen interest in AI/ML, data analytics, and intelligent system design. 
The objective of this project is to create smart, user-friendly solutions that simplify data analysis and empower users to make faster, data-driven decisions.
</p>



</div>
""", unsafe_allow_html=True)


# CONTACT
st.markdown("""
<div id="contact" class="section">

<h2>Contact</h2>

<p>
Developed By: Soumajit Pal

</p>
<p>
Email: soumajitpal1@gmail.com
</p>

</div>
""", unsafe_allow_html=True)
