import streamlit as st

def search_sort_students():

    st.header(
        "🔍 Sorting & Searching Student IDs"
    )

    ids_text = st.text_input(
        "Enter Student IDs (comma separated)"
    )

    target_text = st.text_input(
        "Enter Target ID"
    )

    if st.button(
        "Run Sorting & Searching"
    ):

        if ids_text == "" or target_text == "":

            st.error(
                "Please Fill All Fields"
            )

        else:

            # ==========================
            # CREATE LIST OF IDS
            # ==========================

            student_ids = []

            parts = ids_text.split(",")

            for item in parts:

                student_ids.append(

                    int(
                        item.strip()
                    )

                )

            st.subheader(
                "Original IDs"
            )

            st.write(
                student_ids
            )

            # ==========================
            # BUBBLE SORT
            # ==========================

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

            st.subheader(
                "Bubble Sort"
            )

            st.write(
                bubble_ids
            )

            # ==========================
            # SELECTION SORT
            # ==========================

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

                    if (

                        selection_ids[j]

                        <

                        selection_ids[min_index]

                    ):

                        min_index = j

                temp = selection_ids[i]

                selection_ids[i] = selection_ids[min_index]

                selection_ids[min_index] = temp

            st.subheader(
                "Selection Sort"
            )

            st.write(
                selection_ids
            )

            # ==========================
            # LINEAR SEARCH
            # ==========================

            target = int(
                target_text
            )

            found_index = -1

            for i in range(

                len(student_ids)

            ):

                if student_ids[i] == target:

                    found_index = i

                    break

            st.subheader(
                "Linear Search"
            )

            if found_index != -1:

                st.success(

                    "ID "

                    + str(target)

                    + " found at index "

                    + str(found_index)

                )

            else:

                st.error(
                    "ID Not Found"
                )

            # ==========================
            # BINARY SEARCH
            # ==========================

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

            st.subheader(
                "Binary Search"
            )

            if binary_index != -1:

                st.success(

                    "ID "

                    + str(target)

                    + " found at index "

                    + str(binary_index)

                )

            else:

                st.error(
                    "ID Not Found"
                )

    st.write("---")

    st.info(
        """
        Algorithms Included:

        • Bubble Sort

        • Selection Sort

        • Linear Search

        • Binary Search
        """
    )