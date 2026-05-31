import streamlit as st
import os
import zipfile

def directory_scanner():

    st.header(
        "📂 Directory Scanner & File Viewer"
    )

    option = st.radio(

        "Choose Mode",

        [

            "Local Directory Scanner",

            "Cloud File Viewer",

            "Cloud Directory Scanner"

        ]

    )

    # ==================================
    # CUSTOM EXCEPTION
    # ==================================

    class MissingFileOrFolderError(
        Exception
    ):

        pass

    # ==================================
    # LOCAL DIRECTORY SCANNER
    # ==================================

    if option == "Local Directory Scanner":

        st.subheader(
            "Scan Local Directory"
        )

        directory_path = st.text_input(
            "Enter Directory Path"
        )

        if st.button(
            "Scan Directory"
        ):

            try:

                if directory_path == "":

                    raise MissingFileOrFolderError(

                        "Please Enter Directory Path"

                    )

                if not os.path.exists(
                    directory_path
                ):

                    raise FileNotFoundError(

                        "Directory Not Found"

                    )

                st.success(
                    "Directory Found"
                )

                st.write("---")

                st.subheader(
                    "Folder Structure"
                )

                for root, dirs, files in os.walk(
                    directory_path
                ):

                    level = root.replace(

                        directory_path,

                        ""

                    ).count(os.sep)

                    indent = " " * 4 * level

                    st.text(

                        f"{indent}{os.path.basename(root)}/"

                    )

                    sub_indent = (

                        " " * 4 * (level + 1)

                    )

                    for file in files:

                        st.text(

                            f"{sub_indent}{file}"

                        )

            except FileNotFoundError as e:

                st.error(
                    str(e)
                )

            except MissingFileOrFolderError as e:

                st.warning(
                    str(e)
                )

            except Exception as e:

                st.error(

                    f"Unexpected Error : {e}"

                )

    # ==================================
    # CLOUD FILE VIEWER
    # ==================================

    elif option == "Cloud File Viewer":

        st.subheader(
            "Upload And View Files"
        )

        uploaded_file = st.file_uploader(

            "Choose File",

            type=[

                "txt",

                "csv",

                "py"

            ]

        )

        if uploaded_file is not None:

            try:

                st.success(
                    "File Uploaded Successfully"
                )

                st.write(
                    "File Name:",
                    uploaded_file.name
                )

                st.write(
                    "File Size:",
                    uploaded_file.size,
                    "bytes"
                )

                st.write("---")

                st.subheader(
                    "File Contents"
                )

                file_content = uploaded_file.read()

                try:

                    text = file_content.decode(
                        "utf-8"
                    )

                    st.text_area(

                        "Contents",

                        text,

                        height=300

                    )

                except:

                    st.warning(

                        "Unable To Display File"

                    )

            except Exception as e:

                st.error(

                    f"Error : {e}"

                )
    # ==================================
# CLOUD DIRECTORY SCANNER
# ==================================

    elif option == "Cloud Directory Scanner":

        st.subheader(
            "Scan Uploaded ZIP Folder"
        )

        uploaded_zip = st.file_uploader(

            "Upload ZIP File",

            type=["zip"]

        )

        if uploaded_zip is not None:

            try:

                st.success(
                    "ZIP Uploaded Successfully"
                )

                with zipfile.ZipFile(
                    uploaded_zip,
                    "r"
                ) as zip_ref:

                    file_list = zip_ref.namelist()

                st.subheader(
                    "Folder Structure"
                )

                for file in file_list:

                    st.text(
                        file
                    )

                st.write("---")

                st.write(
                    "Total Items:",
                    len(file_list)
                )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

    # ==================================
    # INFO
    # ==================================

    st.write("---")

    st.info(
        """
        Features Included

        • Local Directory Scanning

        • Cloud File Upload

        • File Viewer

        • Exception Handling

        • Custom Exceptions

        • os.walk()

        • File Metadata Display
        """
    )