# ==========================================
# AI-POWERED CSV ANALYTICS ASSISTANT
# ==========================================

# Import libraries
import pandas as pd
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer


# ==========================================
# CHATBOT CLASS
# ==========================================

class CSVChatbot:

    # Constructor
    def __init__(self, csv_path):

        # ----------------------------------
        # STEP 1: LOAD CSV FILE
        # ----------------------------------

        self.df = pd.read_csv(csv_path)

        # ----------------------------------
        # STEP 2: CONVERT ROWS TO TEXT
        # ----------------------------------

        self.documents = self.df.astype(str).apply(
            lambda row: " | ".join(row),
            axis=1
        ).tolist()

        # ----------------------------------
        # STEP 3: LOAD EMBEDDING MODEL
        # ----------------------------------

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        # ----------------------------------
        # STEP 4: CREATE EMBEDDINGS
        # ----------------------------------

        self.embeddings = self.embedding_model.encode(
            self.documents
        )

        # ----------------------------------
        # STEP 5: CREATE FAISS INDEX
        # ----------------------------------

        dimension = self.embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.array(self.embeddings).astype("float32")
        )

    # ======================================
    # ASK FUNCTION
    # ======================================

    def ask(self, query):

        query = query.lower()

        # ----------------------------------
        # HIGHEST SALARY
        # ----------------------------------

        if "highest salary" in query:

            max_salary_row = self.df.loc[
                self.df["Salary"].idxmax()
            ]

            return (
                f"{max_salary_row['Name']} has the highest salary "
                f"of {max_salary_row['Salary']}."
            )

        # ----------------------------------
        # LOWEST SALARY
        # ----------------------------------

        elif "lowest salary" in query:

            min_salary_row = self.df.loc[
                self.df["Salary"].idxmin()
            ]

            return (
                f"{min_salary_row['Name']} has the lowest salary "
                f"of {min_salary_row['Salary']}."
            )

        # ----------------------------------
        # AVERAGE SALARY
        # ----------------------------------

        elif "average salary" in query:

            avg_salary = self.df["Salary"].mean()

            return (
                f"The average salary is "
                f"{avg_salary:.2f}."
            )

        # ----------------------------------
        # EMPLOYEE COUNT
        # ----------------------------------

        elif (
            "employee count" in query
            or "how many employees" in query
        ):

            count = len(self.df)

            return f"There are {count} employees."

        # ----------------------------------
        # LIST DEPARTMENTS
        # ----------------------------------

        elif "department" in query:

            departments = self.df["Department"].unique()

            return (
                "Departments are: "
                + ", ".join(departments)
            )

        # ----------------------------------
        # FILTER BY DEPARTMENT
        # ----------------------------------

        elif "data science" in query:

            filtered = self.df[
                self.df["Department"]
                == "Data Science"
            ]

            return filtered.to_string(index=False)

        elif "frontend" in query:

            filtered = self.df[
                self.df["Department"]
                == "Frontend"
            ]

            return filtered.to_string(index=False)

        elif "backend" in query:

            filtered = self.df[
                self.df["Department"]
                == "Backend"
            ]

            return filtered.to_string(index=False)

        elif "ai research" in query:

            filtered = self.df[
                self.df["Department"]
                == "AI Research"
            ]

            return filtered.to_string(index=False)

        # ----------------------------------
        # EMPLOYEE LOOKUP
        # ----------------------------------

        else:

            for _, row in self.df.iterrows():

                if row["Name"].lower() in query:

                    return (
                        f"{row['Name']} works in "
                        f"{row['Department']} with salary "
                        f"{row['Salary']} and "
                        f"{row['Experience']} years experience."
                    )

        # ----------------------------------
        # DEFAULT RESPONSE
        # ----------------------------------

        return "Sorry, I could not understand the question."