# **📈 Data Ingestion and Visualization**

## **📝 Overview**  
This project focuses on **ingesting IBM stock price data** using **Mage.ai** and **visualizing** it through a **Streamlit dashboard** with data stored in **PostgreSQL**.

---

## **📌 Table of Contents**
- [Overview](#-overview)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
  - [1 Clone the Repository](#1-clone-the-repository)
  - [2 Set Up Data Ingestion](#2-set-up-data-ingestion)
  - [3 Set Up Data Visualization](#3-set-up-data-visualization)

---

## **🛠️ Technologies Used**
- **[Mage.ai](https://www.mage.ai/)** - Data ingestion & ETL pipeline  
- **PostgreSQL** - Database for storing stock prices  
- **[Streamlit](https://streamlit.io/)** - Interactive dashboard for data visualization  
- **Docker & Docker Compose** - Containerized setup  
- **Pandas & Plotly** - Data processing and visualization  

---

## **📂 Project Structure**
```
├── ingestion/             # Data ingestion pipeline using Mage.ai
│   ├── ....
│   ├── README.md
├── visualizations/        # Streamlit dashboard for data visualization
│   ├── ....
│   ├──
│   ├── README.md
├── README.md              # Project documentation
```

---

## **🚀 Setup Instructions**

### **1 Clone the Repository**
```bash
git clone https://github.com/ganeshtiwari/workshop-dashboard.git
cd workshop-dashboard
```

### **2 Set Up Data Ingestion**
- Navigate to the `ingestion/` folder and follow instructions in [`ingestion/README.md`](ingestion/README.md)  
- Run the **Mage.ai** pipeline to fetch and store stock data  

### **3 Set Up Data Visualization**
- Navigate to the `visualizations/` folder and follow instructions in [`visualizations/README.md`](visualizations/README.md)  
- Run the Streamlit app to visualize data  

---

