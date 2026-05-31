import streamlit as st

def reports():

    st.header(
        "📑 Reports & Final Output"
    )

    # ==================================
    # STUDENT REPORT
    # ==================================

    st.subheader(
        "🎓 Student Registration Report"
    )

    try:

        with open(
            "students.txt",
            "r"
        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No Student Records Available"
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "students.txt not found."
        )

    st.write("---")

    # ==================================
    # COURSE REPORT
    # ==================================

    st.subheader(
        "📚 Course Enrollment Report"
    )

    try:

        with open(
            "courses.txt",
            "r"
        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No Course Records Available"
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "courses.txt not found."
        )

    st.write("---")

    # ==================================
    # STUDENT RECORDS REPORT
    # ==================================

    st.subheader(
        "📋 Student Records Report"
    )

    try:

        with open(
            "student_records.txt",
            "r"
        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No Student Records Found"
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "student_records.txt not found."
        )

    st.write("---")

    # ==================================
    # FEES REPORT
    # ==================================

    st.subheader(
        "💰 Fee Report"
    )

    try:

        with open(
            "fees.txt",
            "r"
        ) as file:

            data = file.read()

        if data.strip() == "":

            st.info(
                "No Fee Records Available"
            )

        else:

            st.text(
                data
            )

    except:

        st.info(
            "fees.txt not found."
        )

    st.write("---")

    # ==================================
    # CAMPUS SUMMARY
    # ==================================

    st.header(
        "📈 Campus Summary"
    )

    total_students = 0

    total_courses = 0

    total_records = 0

    total_fee_collection = 0

    # ==============================
    # STUDENTS
    # ==============================

    try:

        with open(
            "students.txt",
            "r"
        ) as file:

            records = file.readlines()

            total_students = len(
                records
            )

    except:

        pass

    # ==============================
    # COURSES
    # ==============================

    try:

        with open(
            "courses.txt",
            "r"
        ) as file:

            records = file.readlines()

            total_courses = len(
                records
            )

    except:

        pass

    # ==============================
    # STUDENT RECORDS
    # ==============================

    try:

        with open(
            "student_records.txt",
            "r"
        ) as file:

            records = file.readlines()

            total_records = len(
                records
            )

    except:

        pass

    # ==============================
    # FEES
    # ==============================

    try:

        with open(
            "fees.txt",
            "r"
        ) as file:

            records = file.readlines()

            for record in records:

                parts = record.strip().split(",")

                if len(parts) >= 5:

                    total_fee_collection += int(
                        parts[4]
                    )

    except:

        pass

    # ==============================
    # DASHBOARD CARDS
    # ==============================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Students",
            total_students
        )

    with c2:

        st.metric(
            "Courses",
            total_courses
        )

    with c3:

        st.metric(
            "Records",
            total_records
        )

    with c4:

        st.metric(
            "Fee Collection",
            "₹" + str(
                total_fee_collection
            )
        )

    st.write("---")

    st.success(
        "Smart Campus Report Generated Successfully"
    )

    st.info(
        """
        Final Output Generated From:

        • Student Registration

        • Course Enrollment

        • Student Records

        • Search & Sort

        • Fee Calculation

        • Academic Records

        • Directory Scanner

        • Performance Analytics
        """
    )