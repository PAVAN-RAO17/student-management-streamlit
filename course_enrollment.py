import streamlit as st

def course_enrollment():

    st.header(
        "📚 Course Enrollment Management"
    )

    if "courses" not in st.session_state:

        st.session_state.courses = []

    max_courses = 5

    st.write(
        "Maximum Courses Allowed :",
        max_courses
    )

    course_name = st.text_input(
        "Enter Course Name"
    )

    credits_text = st.text_input(
        "Enter Credit Value"
    )

    if st.button(
        "Add Course"
    ):

        if len(
            st.session_state.courses
        ) >= max_courses:

            st.warning(
                "Maximum Course Limit Reached!"
            )

        else:

            if course_name == "":

                st.error(
                    "Please Enter Course Name"
                )

            elif credits_text == "":

                st.error(
                    "Please Enter Credit Value"
                )

            else:

                # ==========================
                # ORIGINAL VALIDATION LOGIC
                # ==========================

                if not credits_text.isdigit():

                    st.error(
                        "Invalid Credit Value!"
                    )

                else:

                    credits = int(
                        credits_text
                    )

                    if credits <= 0:

                        st.error(
                            "Credit Must Be Positive!"
                        )

                    else:

                        st.session_state.courses.append(

                            (
                                course_name,
                                credits
                            )

                        )

                        # ==========================
                        # SAVE TO FILE
                        # ==========================

                        with open(
                            "courses.txt",
                            "a"
                        ) as file:

                            file.write(

                                course_name
                                + ","
                                + str(credits)
                                + "\n"

                            )

                        st.success(

                            f"Course '{course_name}' Added Successfully"

                        )

    # ==========================
    # ENROLLMENT REPORT
    # ==========================

    st.write("---")

    st.subheader(
        "Enrollment Report"
    )

    if len(
        st.session_state.courses
    ) == 0:

        st.info(
            "No Courses Added Yet."
        )

    else:

        for course, credit in st.session_state.courses:

            st.write(

                "Course :",
                course,

                "| Credits :",
                credit

            )

        st.write("")

        st.write(

            "Total Courses Enrolled :",

            len(
                st.session_state.courses
            )

        )

    # ==========================
    # FILE RECORDS
    # ==========================

    st.write("---")

    st.subheader(
        "Saved Course Records"
    )

    try:

        with open(
            "courses.txt",
            "r"
        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No Course Records Found"
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "courses.txt not found."
        )