import streamlit as st
import random
import os

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# =====================================
# CREATE FILES IF NOT PRESENT
# =====================================

required_files = [

    "students.txt",

    "courses.txt",

    "fees.txt"

]

for file in required_files:

    if not os.path.exists(file):

        open(file, "w").close()

# =====================================
# CUSTOM STYLING
# =====================================

st.markdown(
"""
<style>

.stApp{
background-color:#FFF4D6;
}

.main-title{
font-size:48px;
font-weight:bold;
color:#333333;
}

.quote{
font-size:20px;
font-style:italic;
color:green;
}

.small-title{
font-size:30px;
font-weight:bold;
}

.card{
padding:20px;
border-radius:15px;
background-color:#FFF8E7;
margin-top:10px;
margin-bottom:10px;
}

</style>
""",
unsafe_allow_html=True
)

# =====================================
# MOTIVATIONAL QUOTES
# =====================================

quotes = [

"Success is the sum of small efforts repeated daily.",

"Dream big. Start small. Act now.",

"Every expert was once a beginner.",

"Learning never exhausts the mind.",

"Discipline beats motivation.",

"The future depends on what you do today.",

"Consistency creates excellence."

]

# =====================================
# SESSION STATE
# =====================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "quote" not in st.session_state:

    st.session_state.quote = random.choice(
        quotes
    )

# =====================================
# LOGIN PAGE
# =====================================

if not st.session_state.logged_in:

    st.markdown(
        """
        <div class="main-title">
        🌸 Student Management System 🌸
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.write(
        "### Please Login"
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login"
    ):

        if (
            username == "admin"
            and
            password == "admin123"
        ):

            st.session_state.logged_in = True

            st.session_state.quote = random.choice(
                quotes
            )

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )

# =====================================
# DASHBOARD
# =====================================

else:

    st.markdown(
        """
        <div class="main-title">
        🌸 Welcome to the Student Management System 🌸
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="quote">
        "{st.session_state.quote}"
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    menu = st.sidebar.radio(

        "Select Module",

        [

            "Student Registration",

            "Course Enrollment",

            "Student Records",

            "Sorting & Searching",

            "Fee Calculator",

            "Reports"

        ]

    )

    st.sidebar.write("---")

    st.sidebar.write(
        "🎓 Student Management System"
    )

    if st.sidebar.button(
        "Logout"
    ):

        st.session_state.logged_in = False

        st.rerun()
    # =====================================
    # PROGRAM 1
    # STUDENT REGISTRATION
    # =====================================

    if menu == "Student Registration":

        st.header(
            "👨‍🎓 Student Registration & Grade Evaluation"
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

                # Original Logic

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

                with open(
                    "students.txt",
                    "a"
                ) as file:

                    file.write(
                        f"{student_name},{score},{grade},{remark}\n"
                    )

                st.success(
                    "Student Record Saved"
                )

                st.write(
                    "### Student Report"
                )

                st.write(
                    f"Name : {student_name}"
                )

                st.write(
                    f"Score : {score}"
                )

                st.write(
                    f"Grade : {grade}"
                )

                st.write(
                    f"Performance Remark : {remark}"
                )

    # =====================================
    # PROGRAM 2
    # COURSE ENROLLMENT
    # =====================================

    elif menu == "Course Enrollment":

        st.header(
            "📚 Course Enrollment Management"
        )

        if "courses" not in st.session_state:

            st.session_state.courses = []

        max_courses = 5

        course_name = st.text_input(
            "Enter Course Name"
        )

        credits_text = st.text_input(
            "Enter Credits"
        )

        if st.button(
            "Add Course"
        ):

            if len(
                st.session_state.courses
            ) >= max_courses:

                st.warning(
                    "Maximum course limit reached!"
                )

            else:

                if not credits_text.isdigit():

                    st.error(
                        "Invalid credit value!"
                    )

                else:

                    credits = int(
                        credits_text
                    )

                    if credits <= 0:

                        st.error(
                            "Credit must be positive!"
                        )

                    else:

                        st.session_state.courses.append(
                            (
                                course_name,
                                credits
                            )
                        )

                        with open(
                            "courses.txt",
                            "a"
                        ) as file:

                            file.write(
                                f"{course_name},{credits}\n"
                            )

                        st.success(
                            "Course Added Successfully"
                        )

        st.write(
            "### Enrollment Report"
        )

        for course, credit in st.session_state.courses:

            st.write(
                f"Course : {course} | Credits : {credit}"
            )

        st.write(
            f"Total Courses Enrolled : {len(st.session_state.courses)}"
        )
    # =====================================
    # PROGRAM 3
    # STUDENT RECORDS
    # =====================================

    elif menu == "Student Records":

        st.header(
            "📋 Student Records"
        )

        if "students" not in st.session_state:

            st.session_state.students = []

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
            "Add Student"
        ):

            if (
                student_name == ""
                or
                age_text == ""
                or
                grade1_text == ""
                or
                grade2_text == ""
                or
                grade3_text == ""
            ):

                st.error(
                    "Please fill all fields"
                )

            else:

                grades = [

                    int(
                        grade1_text
                    ),

                    int(
                        grade2_text
                    ),

                    int(
                        grade3_text
                    )

                ]

                student = {

                    "name": student_name,

                    "age": int(
                        age_text
                    ),

                    "grades": grades

                }

                st.session_state.students.append(
                    student
                )

                st.success(
                    "Student Added Successfully"
                )

        st.write(
            "### Student Records"
        )

        for student in st.session_state.students:

            st.write(
                f"Name : {student['name']}"
            )

            st.write(
                f"Age : {student['age']}"
            )

            st.write(
                f"Grades : {student['grades']}"
            )

            st.write("---")

        # =====================================
        # EVENT PARTICIPATION ANALYSIS
        # =====================================

        st.write(
            "## 🎉 Event Participation Analysis"
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

            for item in eventA_text.split(","):

                event_A.add(
                    item.strip()
                )

            event_B = set()

            for item in eventB_text.split(","):

                event_B.add(
                    item.strip()
                )

            common_participants = (
                event_A & event_B
            )

            all_participants = (
                event_A | event_B
            )

            only_event_A = (
                event_A - event_B
            )

            st.write(
                "### Results"
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
    # =====================================
    # PROGRAM 4
    # SORTING & SEARCHING
    # =====================================

    elif menu == "Sorting & Searching":

        st.header(
            "🔍 Sorting & Searching Student IDs"
        )

        ids_text = st.text_input(
            "Enter Student IDs separated by commas"
        )

        target_text = st.text_input(
            "Enter Target ID"
        )

        if st.button(
            "Run Sorting & Searching"
        ):

            if ids_text == "" or target_text == "":

                st.error(
                    "Please fill all fields"
                )

            else:

                parts = ids_text.split(",")

                student_ids = []

                for item in parts:

                    student_ids.append(
                        int(item.strip())
                    )

                st.write(
                    "Original IDs:",
                    student_ids
                )

                # =========================
                # Bubble Sort
                # =========================

                bubble_ids = student_ids.copy()

                n = len(
                    bubble_ids
                )

                for i in range(n):

                    for j in range(
                        0,
                        n - i - 1
                    ):

                        if bubble_ids[j] > bubble_ids[j + 1]:

                            temp = bubble_ids[j]

                            bubble_ids[j] = bubble_ids[j + 1]

                            bubble_ids[j + 1] = temp

                st.write(
                    "Bubble Sort:",
                    bubble_ids
                )

                # =========================
                # Selection Sort
                # =========================

                selection_ids = student_ids.copy()

                n = len(
                    selection_ids
                )

                for i in range(n):

                    min_index = i

                    for j in range(
                        i + 1,
                        n
                    ):

                        if selection_ids[j] < selection_ids[min_index]:

                            min_index = j

                    temp = selection_ids[i]

                    selection_ids[i] = selection_ids[min_index]

                    selection_ids[min_index] = temp

                st.write(
                    "Selection Sort:",
                    selection_ids
                )

                target = int(
                    target_text
                )

                # =========================
                # Linear Search
                # =========================

                found_index = -1

                for i in range(
                    len(student_ids)
                ):

                    if student_ids[i] == target:

                        found_index = i

                        break

                if found_index != -1:

                    st.write(

                        "Linear Search: ID",

                        target,

                        "found at index",

                        found_index

                    )

                else:

                    st.write(
                        "Linear Search: ID not found"
                    )

                # =========================
                # Binary Search
                # =========================

                low = 0

                high = len(
                    bubble_ids
                ) - 1

                binary_index = -1

                while low <= high:

                    mid = (
                        low + high
                    ) // 2

                    if bubble_ids[mid] == target:

                        binary_index = mid

                        break

                    elif bubble_ids[mid] < target:

                        low = mid + 1

                    else:

                        high = mid - 1

                if binary_index != -1:

                    st.write(

                        "Binary Search: ID",

                        target,

                        "found at index",

                        binary_index

                    )

                else:

                    st.write(
                        "Binary Search: ID not found"
                    )
    # =====================================
    # PROGRAM 5
    # FEE CALCULATOR
    # =====================================

    elif menu == "Fee Calculator":

        st.header(
            "💰 Student Fee Calculator"
        )

        student_name = st.text_input(
            "Student Name"
        )

        tuition_text = st.text_input(
            "Tuition Fee"
        )

        hostel_text = st.text_input(
            "Hostel Fee"
        )

        transport_text = st.text_input(
            "Transportation Fee"
        )

        # Original Function

        def calculate_fee(
            tuition_fee,
            hostel_fee=0,
            transportation_fee=0
        ):

            total_fee = (
                tuition_fee +
                hostel_fee +
                transportation_fee
            )

            return total_fee

        if st.button(
            "Calculate Fee"
        ):

            if (
                student_name == ""
                or tuition_text == ""
                or hostel_text == ""
                or transport_text == ""
            ):

                st.error(
                    "Please fill all fields"
                )

            else:

                tuition = int(
                    tuition_text
                )

                hostel = int(
                    hostel_text
                )

                transport = int(
                    transport_text
                )

                total_fee = calculate_fee(
                    tuition,
                    hostel,
                    transport
                )

                with open(
                    "fees.txt",
                    "a"
                ) as file:

                    file.write(
                        f"{student_name},{tuition},{hostel},{transport},{total_fee}\n"
                    )

                st.success(
                    "Fee Calculated Successfully"
                )

                st.write(
                    "### Fee Details"
                )

                st.write(
                    f"Student Name : {student_name}"
                )

                st.write(
                    f"Tuition Fee : {tuition}"
                )

                st.write(
                    f"Hostel Fee : {hostel}"
                )

                st.write(
                    f"Transportation Fee : {transport}"
                )

                st.write(
                    f"Total Fee : {total_fee}"
                )

    # =====================================
    # REPORTS PAGE
    # =====================================

    elif menu == "Reports":

        st.header(
            "📊 Reports"
        )

        # -----------------------
        # Student Records
        # -----------------------

        st.subheader(
            "Student Registration Records"
        )

        try:

            with open(
                "students.txt",
                "r"
            ) as file:

                data = file.read()

            if data.strip() == "":

                st.info(
                    "No student records found"
                )

            else:

                st.code(
                    data
                )

        except:

            st.info(
                "No student records found"
            )

        # -----------------------
        # Course Records
        # -----------------------

        st.subheader(
            "Course Enrollment Records"
        )

        try:

            with open(
                "courses.txt",
                "r"
            ) as file:

                data = file.read()

            if data.strip() == "":

                st.info(
                    "No course records found"
                )

            else:

                st.code(
                    data
                )

        except:

            st.info(
                "No course records found"
            )

        # -----------------------
        # Fee Records
        # -----------------------

        st.subheader(
            "Fee Records"
        )

        try:

            with open(
                "fees.txt",
                "r"
            ) as file:

                data = file.read()

            if data.strip() == "":

                st.info(
                    "No fee records found"
                )

            else:

                st.code(
                    data
                )

        except:

            st.info(
                "No fee records found"
            )

        st.success(
            "Reports Loaded Successfully"
        )