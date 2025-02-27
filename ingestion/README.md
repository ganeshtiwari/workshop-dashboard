# **📥 Data Ingestion**

## **📝 Overview**
This folder contains the **Mage.ai pipeline** for ingesting **IBM stock price data from lcoal json file** and storing it in **PostgreSQL**.

---

## **🚀 Setup Instructions**

### **1 Start the Services Using Docker**
Ensure Docker is installed, then run:
```bash
docker-compose up -d
```
This will:
✅ Start a **PostgreSQL** container  
✅ Create the **`stock_prices`** table in PostgreSQL  
✅ Start a **Mage.ai** container  

### **2 Access Mage.ai UI**
Once the services are running, access Mage.ai at:
```
http://localhost:6789
```

---

## **🛠️ Pipeline Details**
- **Source:** Fetches stock price data from Alpha Vantage API
- **Transformation:** Cleans and formats data
- **Destination:** Stores data in PostgreSQL (`stock_prices` table)

---

