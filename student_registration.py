import streamlit as st

def student_registration():

    st.header(
        "🎓 Student Registration & Grade Evaluation"
    )

    student_name = st.text_input(
        "Enter Student Name"
    )

    score_text = st.text_input(
        "Enter Exam Score (0-100)"
    )

    if st.button(
        "Generate Report"
    ):

        if student_name == "":

            st.error(
                "Please enter student name"
            )

        elif score_text == "":

            st.error(
                "Please enter score"
            )

        else:

            score = float(
                score_text
            )

            # ==========================
            # ORIGINAL GRADE LOGIC
            # ==========================

            if score >= 90 and score <= 100:

                grade = "A"

                remark = "Excellent"

            elif score >= 75:

                grade = "B"

                remark = "Very Good"

            elif score >= 60:

                grade = "C"

                remark = "Good"

            elif score >= 40:

                grade = "D"

                remark = "Average"

            else:

                grade = "F"

                remark = "Needs Improvement"

            # ==========================
            # SAVE TO FILE
            # ==========================

            with open(
                "students.txt",
                "a"
            ) as file:

                file.write(

                    student_name
                    + ","
                    + str(score)
                    + ","
                    + grade
                    + ","
                    + remark
                    + "\n"

                )

            st.success(
                "Student Record Saved Successfully"
            )

            # ==========================
            # REPORT
            # ==========================

            st.subheader(
                "Student Report"
            )

            st.write(
                "Name:",
                student_name
            )

            st.write(
                "Score:",
                score
            )

            st.write(
                "Grade:",
                grade
            )

            st.write(
                "Performance Remark:",
                remark
            )

    st.write("---")

    st.subheader(
        "Registered Students"
    )

    try:

        with open(
            "students.txt",
            "r"
        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No student records available."
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "students.txt not found."
        )