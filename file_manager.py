import streamlit as st

def file_manager():

    st.header(
        "📄 Academic Records File Handling"
    )

    st.subheader(
        "Add Academic Record"
    )

    student_id = st.text_input(
        "Enter Student ID"
    )

    student_name = st.text_input(
        "Enter Student Name"
    )

    marks_text = st.text_input(
        "Enter Marks"
    )

    # ==========================
    # ADD RECORD
    # ==========================

    if st.button(
        "Add Record"
    ):

        if (

            student_id == ""

            or student_name == ""

            or marks_text == ""

        ):

            st.error(
                "Please Fill All Fields"
            )

        else:

            with open(

                "student_records.txt",

                "a"

            ) as file:

                file.write(

                    student_id

                    + ","

                    + student_name

                    + ","

                    + marks_text

                    + "\n"

                )

            st.success(
                "Record Added Successfully"
            )

    # ==========================
    # GENERATE REPORT
    # ==========================

    if st.button(
        "Generate Report"
    ):

        try:

            with open(

                "student_records.txt",

                "r"

            ) as file:

                records = file.readlines()

            total_students = 0

            total_marks = 0

            highest_marks = -1

            top_student = ""

            st.subheader(
                "Stored Records"
            )

            for record in records:

                st.write(
                    record.strip()
                )

            for record in records:

                parts = record.strip().split(",")

                if len(parts) >= 3:

                    marks = int(
                        parts[2]
                    )

                    name = parts[1]

                    total_students += 1

                    total_marks += marks

                    if marks > highest_marks:

                        highest_marks = marks

                        top_student = name

            if total_students > 0:

                average_marks = (

                    total_marks

                    / total_students

                )

                st.write("---")

                st.subheader(
                    "Academic Report"
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
                    "Top Student:",
                    top_student
                )

                st.write(
                    "Highest Marks:",
                    highest_marks
                )

        except:

            st.error(
                "No Records Found"
            )

    # ==========================
    # VIEW FILE
    # ==========================

    st.write("---")

    st.subheader(
        "Saved Academic Records"
    )

    try:

        with open(

            "student_records.txt",

            "r"

        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No Records Available"
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "student_records.txt not found."
        )

    # ==========================
    # SUMMARY
    # ==========================

    st.write("---")

    st.info(
        """
        Features Included:

        • File Writing

        • File Reading

        • Report Generation

        • Average Marks Calculation

        • Top Student Identification
        """
    )