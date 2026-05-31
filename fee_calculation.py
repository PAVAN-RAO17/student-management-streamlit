import streamlit as st

def fee_calculation():

    st.header(
        "💰 Student Fee Calculation"
    )

    st.subheader(
        "Enter Fee Details"
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

    # ==========================
    # FUNCTION
    # ==========================

    def calculate_fee(

        tuition_fee,

        hostel_fee=0,

        transportation_fee=0

    ):

        total_fee = (

            tuition_fee

            + hostel_fee

            + transportation_fee

        )

        return total_fee

    # ==========================
    # BUTTON
    # ==========================

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
                "Please Fill All Fields"
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

            # ==========================
            # SAVE TO FILE
            # ==========================

            with open(

                "fees.txt",

                "a"

            ) as file:

                file.write(

                    student_name

                    + ","

                    + str(tuition)

                    + ","

                    + str(hostel)

                    + ","

                    + str(transport)

                    + ","

                    + str(total_fee)

                    + "\n"

                )

            st.success(
                "Fee Calculated Successfully"
            )

            st.subheader(
                "Fee Report"
            )

            st.write(
                "Student Name:",
                student_name
            )

            st.write(
                "Tuition Fee:",
                tuition
            )

            st.write(
                "Hostel Fee:",
                hostel
            )

            st.write(
                "Transportation Fee:",
                transport
            )

            st.write(
                "Total Fee:",
                total_fee
            )

    # ==========================
    # DISPLAY SAVED RECORDS
    # ==========================

    st.write("---")

    st.subheader(
        "Saved Fee Records"
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

    # ==========================
    # EXAMPLES
    # ==========================

    st.write("---")

    st.info(
        """
        Example:

        Tuition Fee = 50000

        Hostel Fee = 30000

        Transportation Fee = 10000

        Total Fee = 90000
        """
    )