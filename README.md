# 📊 Conversational BI Dashboard

An **AI-powered Business Intelligence Dashboard** that allows users to analyze data using **natural language queries**.  
Instead of writing complex SQL queries, users can simply type questions in plain English, and the system automatically generates SQL queries, retrieves data, and visualizes insights through interactive charts.

This project demonstrates how **Artificial Intelligence and Business Intelligence tools** can be combined to simplify data analysis for both technical and non-technical users.

---

# 🚀 Project Features

### 1. Natural Language Querying
Users can ask questions in simple English, and the system automatically converts the query into SQL using an AI model.

### 2. Automatic SQL Generation
The AI model interprets the user's question and dynamically generates SQL queries to retrieve the relevant data from the database.

### 3. Intelligent Data Visualization
The system automatically selects the most appropriate chart type based on the query result.

Supported visualizations include:
- Bar Charts
- Pie Charts
- Line Charts
- Scatter Plots
- Histograms

### 4. Interactive Dashboard
Users can continuously explore data by asking multiple queries and instantly viewing the generated charts.

### 5. Secure User Authentication
The system includes a **login and registration system** that ensures only authenticated users can access the dashboard.

### 6. User-Friendly Interface
The project includes an attractive **landing page**, a **login/signup page**, and an **interactive dashboard interface**.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Backend logic |
| Streamlit | Web application framework |
| SQLite | Database |
| Plotly | Interactive data visualization |
| Pandas | Data processing |
| Google Gemini API | Natural language to SQL generation |
| HTML/CSS | Landing page design |

---

# 📂 Project Structure

```
AI_Integrated_BI_Dashboard
│
├── landing.py
├── auth.py
├── database.py
├── llm_query.py
├── dataset.csv
│
├── pages
│   ├── login.py
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
gh repo clone soumajitpal12/AI_Integrated_BI_Dashboard```

```bash
cd AI_Integrated_BI_Dashboard
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Gemini API Key

Create a `.env` file and add:

```
GEMINI_API_KEY=your_api_key_here
```

You can obtain a free API key from:

https://ai.google.dev

---

### 5️⃣ Run the Application

```bash
streamlit run landing.py
```

The application will open in your browser.

---

# 📊 Example Queries

Users can ask questions such as:

- Show average online spend by gender  
- Compare monthly online orders across different city tiers  
- Analyze relationship between income and online spending  
- Show distribution of shopping preferences  
- Compare online and store spending by gender  

The system will automatically generate SQL queries and create the appropriate visualization.

---

# 👨‍💻 Developer

This project is developed by Soumajit Pal, with a keen interest in AI/ML, data analytics, and intelligent system design. 
The objective of this project is to create smart, user-friendly solutions that simplify data analysis and empower users to make faster, data-driven decisions.


# 🎯 Project Objective

The main objective of this project is to demonstrate how **AI-driven conversational interfaces** can simplify business intelligence systems by allowing users to analyze data without requiring technical expertise in SQL or data analytics tools.

---

# 🔮 Future Improvements

Potential enhancements include:

- Support for multiple datasets  
- Advanced dashboard filtering  
- Voice-based query input  
- Deployment on cloud platforms  
- Integration with real-time business data sources  

---

# 📜 License

This project is developed for **academic and educational purposes**.

---

⭐ If you found this project helpful, consider giving it a **star on GitHub**!
