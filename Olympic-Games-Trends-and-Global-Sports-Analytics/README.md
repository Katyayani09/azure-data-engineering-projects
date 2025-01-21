# Leveraging Data Engineering and Science for Olympic Game Trends and Global Sports Analytics

## Project Description
This project is a comprehensive data pipeline designed to ingest, transform, store, and visualize data related to the Olympic Games trends over the past years. This project leverages cutting-edge cloud technologies and tools to enable real-time analytics, advanced data transformation, and interactive dashboards for impactful decision-making.

---

## Architecture Diagram
![Architecture Diagram](https://github.com/user-attachments/assets/8f33d201-65a1-4ffa-88a7-e7259830228b)

---

## Workflow Steps
### **1. Sources**
- 📡 **Apache Kafka**: Streams real-time event data related to the Olympic games.
- 📂 **GitHub Repository**: Stores raw datasets and Python scripts for initial ETL processes.

### **2. Ingestion**
- 🌐 **Azure Event Hubs**: Captures real-time event data from Apache Kafka for processing.

### **3. CI/CD**
- 🔄 **Azure DevOps**: Manages continuous integration and deployment pipelines for code and infrastructure.

### **4. Data Transformation**
- 🧠 **Azure Databricks**:
  - Performs initial ETL operations using PySpark.
  - Conducts advanced data transformation to prepare analytics-ready datasets.

### **5. Data Storage**
- 🗄️ **Azure Data Lake Storage**:
  - **Raw Layer**: Stores ingested raw data for archival.
  - **Transformed Layer**: Stores processed and analytics-ready data.

### **6. Analytics**
- 📊 **Azure Synapse Analytics**:
  - Enables ad-hoc analysis and complex queries on transformed datasets.

### **7. Visualization**
- 📈 **Power BI**:
  - Interactive dashboards for key stakeholders to explore insights related to the Game Trends and Sports popularity

---

## Technologies Used
- 🌐 **Azure Event Hubs**: Real-time data ingestion.
- 🧠 **Azure Databricks**: Data transformation and analytics using PySpark.
- 🗄️ **Azure Data Lake Storage**: Centralized data storage.
- 📊 **Azure Synapse Analytics**: On-demand SQL queries and analytics.
- 📈 **Power BI**: Interactive dashboards.
- 📡 **Apache Kafka**: Real-time data streaming.
- 🔄 **Azure DevOps**: CI/CD pipelines.

---

## Setup Instructions

### **1. Prerequisites**
- ✅ Azure subscription.
- ✅ Access to a GitHub repository with relevant scripts and raw data.
- ✅ Installed tools: Git, Python, and Azure CLI.

### **2. Steps to Set Up**
1. **Event Hubs Configuration**:
   - 🌐 Create an Azure Event Hubs namespace and event hub.
   - 🔗 Configure Apache Kafka to stream data into Event Hubs.

2. **Azure Data Lake Storage**:
   - 🗄️ Set up containers for `raw_data` and `transformed_data`.

3. **Databricks Cluster**:
   - 🧠 Create a Databricks workspace.
   - 🔧 Configure a Spark cluster with appropriate specifications.

4. **Azure DevOps CI/CD**:
   - 🔄 Set up pipelines to deploy Python scripts and Databricks notebooks.

5. **Synapse Analytics**:
   - 📊 Create a Synapse workspace and configure linked services to Azure Data Lake Storage.

6. **Power BI Dashboard**:
   - 📈 Connect Power BI to Synapse Analytics and build visualizations.

---

## Usage
- 🔍 **Real-time Data Analysis**: Analyze live event data streams of Sport Events Data
- 📊 **Data Visualization**: Explore key metrics such as medal tallies, athlete performance, and event scheduling through Power BI dashboards.
- 📂 **Ad-hoc Queries**: Run complex analytics queries using Synapse Analytics.

---

## Contact Information
For questions or feedback, please contact:
- 📛 **Name**: Katyayani Jandhyala
