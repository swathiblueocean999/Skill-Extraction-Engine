# AI Data Entity Design Document


## 1.Objective

The objective of this design is to convert unstructured resumes and job descriptions into a structured JSON format. This enables an AI system to precisely match candidates with job roles.



## 2.Entities

The following entities have been defined to organize the data:

​Candidate Profile: Stores basic information such as Name, Email, and Phone.

​Education History: Captures degrees, institutions, and graduation years.

​Professional Experience: Tracks job titles, companies, and the duration of employment.

​Skills Set: Organizes technical and soft skills into searchable lists.

​3. Mapping Logic (How it Connects)
The AI system connects the Resume Schema and the Job Description(JD) Schema using these mapping rules:

​Skill Mapping: The system compares the skills_set from the resume with the mandatory_skills in the Job Description to calculate a match score.

​Experience Mapping: The candidate's total_experience is validated against the required experience range specified in the job posting.

​Role Alignment: NLP (Natural Language Processing) is used to verify if the candidate's previous roles align with the requirements of the new position.



## Conclusion

By using this structured data, the AI can automatically select the best candidates, saving time and reducing errors.

