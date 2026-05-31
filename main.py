import streamlit as st
import time
import random

from student_registration import student_registration
from course_enrollment import course_enrollment
from student_records import student_records
from search_sort_students import search_sort_students
from fee_calculation import fee_calculation
from file_manager import file_manager
from directory_scanner import directory_scanner
from performance_analytics import performance_analytics
from reports import reports

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Smart Campus Management System",
    page_icon="🎓",
    layout="wide"
)

# =====================================
# CUSTOM STYLING
# =====================================

st.markdown("""
<style>

.stApp{
    background-color:#F5F9FF;
}

.main-title{
    text-align:center;
    color:#0A4D8C;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#5A5A5A;
}

.card{
    padding:15px;
    border-radius:12px;
    background-color:white;
    border:1px solid #D8E6F3;
}

.quote-box{
    background-color:#EAF4FF;
    padding:15px;
    border-radius:10px;
    color:#0A4D8C;
}

</style>
""",
unsafe_allow_html=True)

# =====================================
# MOTIVATIONAL QUOTES
# =====================================

quotes = [

"Success is the sum of small efforts repeated every day.",

"Dream big. Start small. Act now.",

"Every expert was once a beginner.",

"Learning never exhausts the mind.",

"Your future is created by what you do today."

]

# =====================================
# SESSION VARIABLES
# =====================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "show_splash" not in st.session_state:
    st.session_state.show_splash = True

if "username" not in st.session_state:
    st.session_state.username = "admin"

if "full_name" not in st.session_state:
    st.session_state.full_name = "Student User"

if "department" not in st.session_state:
    st.session_state.department = "Computer Science"

if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)

# =====================================
# SPLASH SCREEN
# =====================================

if st.session_state.show_splash:

    st.image(
        "assets/dsce_logo.png",
        width=220
    )

    st.markdown(
        """
        <div class='main-title'>
        Smart Campus Management System
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='sub-title'>
        Building A Smart Campus Tomorrow
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.info(
        "Initializing Smart Campus..."
    )

    progress = st.progress(0)

    for i in range(100):

        progress.progress(i + 1)

        time.sleep(0.03)

    time.sleep(2)

    st.session_state.show_splash = False

    st.rerun()

# =====================================
# LOGIN PAGE
# =====================================

if not st.session_state.logged_in:

    st.image(
        "assets/dsce_logo.png",
        width=150
    )

    st.title(
        "Welcome Back"
    )

    st.write(
        "Please login to continue."
    )

    username = st.text_input(
        "User ID"
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

            st.session_state.username = username

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )

# =====================================
# DASHBOARD
# =====================================

else:

    top1, top2 = st.columns([8,2])

    with top1:

        st.title(
            "🎓 Smart Campus Management System"
        )

    with top2:

        st.write(
            f"👤 {st.session_state.full_name}"
        )

    st.success(
        "Welcome Back!"
    )

    st.markdown(
        f"""
        <div class='quote-box'>
        "{st.session_state.quote}"
        </div>
        """,
        unsafe_allow_html=True
    )
        # =====================================
    # PROFILE SECTION
    # =====================================

    with st.expander(
        "👤 Profile Settings"
    ):

        full_name = st.text_input(
            "Full Name",
            st.session_state.full_name
        )

        department = st.text_input(
            "Department",
            st.session_state.department
        )

        if st.button(
            "Update Profile"
        ):

            st.session_state.full_name = full_name

            st.session_state.department = department

            st.success(
                "Profile Updated Successfully"
            )
    # =====================================
    # =====================================
# LIVE DASHBOARD COUNTS
# =====================================

    student_count = 0
    course_count = 0
    record_count = 0
    fee_total = 0

    try:
        with open("students.txt", "r") as file:
            student_count = len(file.readlines())
    except:
        pass

    try:
        with open("courses.txt", "r") as file:
            course_count = len(file.readlines())
    except:
       pass
 
    try:
        with open("student_records.txt", "r") as file:
            record_count = len(file.readlines())
    except:
        pass

    try:
        with open("fees.txt", "r") as file:
            records = file.readlines()

            for record in records:
                parts = record.strip().split(",")

                if len(parts) >= 5:
                    fee_total += int(parts[4])

    except:
        pass

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Students", student_count)

    with c2:
        st.metric("Courses", course_count)

    with c3:
        st.metric("Records", record_count)

    with c4:
        st.metric("Fees", f"₹{fee_total}")
    

   

    # =====================================
    # WORKFLOW MENU
    # =====================================

    menu = st.sidebar.radio(

        "Select Module",

        [

            "① Student Registration",

            "② Course Enrollment",

            "③ Student Records",

            "④ Search & Sort",

            "⑤ Fee Calculation",

            "⑥ File Manager",

            "⑦ Directory Scanner & File Viewer",

            "⑧ Performance Analytics",

            "⑨ Final Dashboard",

            "⑩ Reports"

        ]

    )

    # =====================================
    # MODULE NAVIGATION
    # =====================================

    if menu == "① Student Registration":

        student_registration()

    elif menu == "② Course Enrollment":

        course_enrollment()

    elif menu == "③ Student Records":

        student_records()

    elif menu == "④ Search & Sort":

        search_sort_students()

    elif menu == "⑤ Fee Calculation":

        fee_calculation()

    elif menu == "⑥ File Manager":

        file_manager()

    elif menu == "⑦ Directory Scanner & File Viewer":

        directory_scanner()

    elif menu == "⑧ Performance Analytics":

        performance_analytics()

    elif menu == "⑨ Final Dashboard":

        st.header(
            "📈 Final Dashboard"
        )

        d1, d2, d3, d4 = st.columns(4)

        with d1:

            st.metric(
                "Students",
                "0"
            )

        with d2:

            st.metric(
                "Courses",
                "0"
            )

        with d3:

            st.metric(
                "Records",
                "0"
            )

        with d4:

            st.metric(
                "Fees",
                "₹0"
            )

        st.write("")

        st.subheader(
            "Campus Overview"
        )

        st.info(
            """
            This dashboard combines data from:

            • Student Registration

            • Course Enrollment

            • Student Records

            • Fee Calculator

            • Academic Records

            • Performance Analytics
            """
        )

        st.write("")

        st.subheader(
            "Recent Activity"
        )

        st.write(
            "Recent student registrations will appear here."
        )

        st.write(
            "Recent fee payments will appear here."
        )

        st.write(
            "Recent academic records will appear here."
        )

    elif menu == "⑩ Reports":

        reports()

    # =====================================
    # SIDEBAR INFO
    # =====================================

    st.sidebar.write("---")

    st.sidebar.write(
        f"👤 {st.session_state.full_name}"
    )

    st.sidebar.write(
        f"🏫 {st.session_state.department}"
    )

    st.sidebar.write("---")

    st.sidebar.info(
        "Smart Campus Management System"
    )

    # =====================================
    # LOGOUT
    # =====================================

    if st.sidebar.button(
        "Logout"
    ):

        st.success(
            "Thank you for using Smart Campus Management System."
        )

        st.session_state.logged_in = False

        st.rerun()