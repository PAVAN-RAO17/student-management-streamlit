import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def performance_analytics():

    st.header(
        "📊 Performance Analytics"
    )

    option = st.radio(

        "Choose Analysis Mode",

        [

            "Internal System Analytics",

            "CSV File Analytics"

        ]

    )

    # ==================================
    # INTERNAL SYSTEM ANALYTICS
    # ==================================

    if option == "Internal System Analytics":

        st.subheader(
            "System Analytics"
        )

        try:

            with open(
                "student_records.txt",
                "r"
            ) as file:

                records = file.readlines()

            total_students = 0

            total_marks = 0

            highest_marks = -1

            lowest_marks = 101

            top_student = ""

            names = []

            marks_list = []

            for record in records:

                parts = record.strip().split(",")

                if len(parts) >= 3:

                    name = parts[1]

                    marks = int(parts[2])

                    names.append(name)

                    marks_list.append(marks)

                    total_students += 1

                    total_marks += marks

                    if marks > highest_marks:

                        highest_marks = marks

                        top_student = name

                    if marks < lowest_marks:

                        lowest_marks = marks

            if total_students > 0:

                average_marks = (

                    total_marks

                    / total_students

                )

                st.write(
                    "Total Students:",
                    total_students
                )

                st.write(
                    "Average Marks:",
                    round(
                        average_marks,
                        2
                    )
                )

                st.write(
                    "Highest Marks:",
                    highest_marks
                )

                st.write(
                    "Lowest Marks:",
                    lowest_marks
                )

                st.write(
                    "Top Student:",
                    top_student
                )

                # ==================
                # BAR CHART
                # ==================

                st.subheader(
                    "Student Performance Chart"
                )

                fig, ax = plt.subplots()

                ax.bar(
                    names,
                    marks_list
                )

                ax.set_title(
                    "Student Marks"
                )

                ax.set_xlabel(
                    "Students"
                )

                ax.set_ylabel(
                    "Marks"
                )

                st.pyplot(
                    fig
                )

            else:

                st.warning(
                    "No Records Found"
                )

        except:

            st.error(
                "student_records.txt not found."
            )

        # ==========================
        # FEE ANALYTICS
        # ==========================

        st.write("---")

        st.subheader(
            "Fee Analytics"
        )

        try:

            with open(
                "fees.txt",
                "r"
            ) as file:

                records = file.readlines()

            total_collection = 0

            fee_count = 0

            highest_fee = 0

            for record in records:

                parts = record.strip().split(",")

                if len(parts) >= 5:

                    fee = int(
                        parts[4]
                    )

                    total_collection += fee

                    fee_count += 1

                    if fee > highest_fee:

                        highest_fee = fee

            if fee_count > 0:

                average_fee = (

                    total_collection

                    / fee_count

                )

                st.write(
                    "Total Fee Collection:",
                    total_collection
                )

                st.write(
                    "Average Fee:",
                    round(
                        average_fee,
                        2
                    )
                )

                st.write(
                    "Highest Fee:",
                    highest_fee
                )

        except:

            st.info(
                "No Fee Records Available"
            )

    # ==================================
    # CSV FILE ANALYTICS
    # ==================================

    elif option == "CSV File Analytics":

        st.subheader(
            "CSV Performance Analysis"
        )

        uploaded_file = st.file_uploader(

            "Upload CSV File",

            type=["csv"]

        )

        if uploaded_file is not None:

            try:

                df = pd.read_csv(
                    uploaded_file
                )

                st.subheader(
                    "Raw Data"
                )

                st.dataframe(
                    df
                )

                st.subheader(
                    "Statistical Summary"
                )

                st.write(
                    df.describe()
                )

                scores = df[
                    [

                        "Math",

                        "Science",

                        "English"

                    ]

                ].to_numpy()

                mean_scores = np.mean(

                    scores,

                    axis=0

                )

                median_scores = np.median(

                    scores,

                    axis=0

                )

                std_scores = np.std(

                    scores,

                    axis=0

                )

                st.subheader(
                    "NumPy Analysis"
                )

                st.write(
                    "Mean Scores:",
                    mean_scores
                )

                st.write(
                    "Median Scores:",
                    median_scores
                )

                st.write(
                    "Standard Deviation:",
                    std_scores
                )

                # ==================
                # TOP PERFORMERS
                # ==================

                top_math = df.loc[
                    df["Math"].idxmax(),
                    "Name"
                ]

                top_science = df.loc[
                    df["Science"].idxmax(),
                    "Name"
                ]

                top_english = df.loc[
                    df["English"].idxmax(),
                    "Name"
                ]

                st.subheader(
                    "Top Performers"
                )

                st.write(
                    "Math:",
                    top_math
                )

                st.write(
                    "Science:",
                    top_science
                )

                st.write(
                    "English:",
                    top_english
                )

                # ==================
                # CHART
                # ==================

                st.subheader(
                    "Average Subject Scores"
                )

                fig, ax = plt.subplots()

                subjects = [

                    "Math",

                    "Science",

                    "English"

                ]

                ax.bar(

                    subjects,

                    mean_scores

                )

                ax.set_title(
                    "Average Scores"
                )

                st.pyplot(
                    fig
                )
                # ==================
                # STUDENT COMPARISON CHART
                # ==================

                st.subheader(
                     "Student Performance Comparison"
             )

                fig2, ax2 = plt.subplots()

                df.plot(
                    x="Name",
                    y=[
                        "Math",
                        "Science",
                        "English"
                    ],
                kind="bar",
                ax=ax2
                )

                ax2.set_title(
                    "Student Performance Comparison"
                )

                ax2.set_ylabel(
                    "Marks"
                )

                st.pyplot(fig2)

            except Exception as e:

                st.error(
                    f"Error : {e}"
                )
        

    # ==================================
    # INFO
    # ==================================

    st.write("---")

    st.info(
        """
        Features Included

        • Internal Analytics

        • CSV Analytics

        • Pandas

        • NumPy

        • Matplotlib

        • Statistical Analysis

        • Top Performer Identification

        • Performance Visualization
        """
    )