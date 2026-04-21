 **Education & Certification Parsing Project**

📌 **Overview**

This project extracts structured Education and Certification details from unstructured text data (converted from PDF profiles).

🎯 **Objective**

Parse multiple profiles from a single text file

Extract key academic details

Organize the data into a structured format

📂 **Input**

full\_extracted\_text.txt  
(Contains 89 profiles converted from PDF)

📊 **Output**

**final\_day11\_full\_output.csv**

Columns included:

* **Profile**  
    
* **Degree**  
    
* **Field of Study**  
    
* **Institution**  
    
* **Graduation Year**  
    
* **Certifications**  
    
* **Normalized Degree**  
    
* **Certification Tag**

⚙️ **How It Works**

Split the text into individual profiles

Use keyword-based parsing to extract: 

* **Degree**  
    
* **Field**  
    
* **Institution**  
    
* **Year**  
    
* **Certifications**  
    
* **Handle missing data using "Not Mentioned"**  
    
* **Normalize degree names**  
    
* **Tag certifications based on relevance**

▶️ **How to Run**

python your\_script\_name.py 

🧠 Notes

* Not all profiles contain complete education details  
    
* Missing values are marked as "Not Mentioned"  
    
* Data is extracted using pattern matching and keyword detection


✅ **Status**

✔ Task Completed  
✔ Output Generated  
✔ Data Structured Successfully

