import streamlit as st

def student_records():

    st.header(
        "📋 Student Records Management"
    )

    # ==========================
    # STUDENT RECORDS
    # ==========================

    if "students" not in st.session_state:

        st.session_state.students = []

    st.subheader(
        "Add Student Record"
    )

    student_name = st.text_input(
        "Student Name"
    )

    age_text = st.text_input(
        "Age"
    )

    grade1_text = st.text_input(
        "Grade 1"
    )

    grade2_text = st.text_input(
        "Grade 2"
    )

    grade3_text = st.text_input(
        "Grade 3"
    )

    if st.button(
        "Add Student Record"
    ):

        if (
            student_name == ""
            or age_text == ""
            or grade1_text == ""
            or grade2_text == ""
            or grade3_text == ""
        ):

            st.error(
                "Please Fill All Fields"
            )

        else:

            grades = [

                int(grade1_text),

                int(grade2_text),

                int(grade3_text)

            ]

            student = {

                "name": student_name,

                "age": int(age_text),

                "grades": grades

            }

            st.session_state.students.append(
                student
            )

            with open(
                "student_records.txt",
                "a"
            ) as file:

                file.write(

                    student_name
                    + ","
                    + age_text
                    + ","
                    + grade1_text
                    + ","
                    + grade2_text
                    + ","
                    + grade3_text
                    + "\n"

                )

            st.success(
                "Student Record Added Successfully"
            )

    # ==========================
    # DISPLAY RECORDS
    # ==========================

    st.write("---")

    st.subheader(
        "Student Records"
    )

    if len(
        st.session_state.students
    ) == 0:

        st.info(
            "No Student Records Available"
        )

    else:

        for student in st.session_state.students:

            st.write(
                "Name:",
                student["name"]
            )

            st.write(
                "Age:",
                student["age"]
            )

            st.write(
                "Grades:",
                student["grades"]
            )

            st.write("---")

    # ==========================
    # EVENT PARTICIPATION
    # ==========================

    st.header(
        "🎉 Event Participation Analysis"
    )

    eventA_text = st.text_input(
        "Event A Participants (comma separated)"
    )

    eventB_text = st.text_input(
        "Event B Participants (comma separated)"
    )

    if st.button(
        "Analyse Events"
    ):

        event_A = set()

        event_B = set()

        for item in eventA_text.split(","):

            if item.strip() != "":

                event_A.add(
                    item.strip()
                )

        for item in eventB_text.split(","):

            if item.strip() != "":

                event_B.add(
                    item.strip()
                )

        # ==========================
        # ORIGINAL SET OPERATIONS
        # ==========================

        common_participants = (

            event_A & event_B

        )

        all_participants = (

            event_A | event_B

        )

        only_event_A = (

            event_A - event_B

        )

        st.subheader(
            "Event Participation Analysis"
        )

        st.write(
            "Common Participants:"
        )

        st.write(
            common_participants
        )

        st.write(
            "All Participants:"
        )

        st.write(
            all_participants
        )

        st.write(
            "Only Event A Participants:"
        )

        st.write(
            only_event_A
        )

    # ==========================
    # FILE RECORDS
    # ==========================

    st.write("---")

    st.subheader(
        "Saved Student Records"
    )

    try:

        with open(
            "student_records.txt",
            "r"
        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No Saved Records Found"
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "student_records.txt not found."
        )