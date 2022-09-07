import os

import openpyxl

import streamlit as st

import webbrowser

import pandas as pd
import numpy as np
from st_aggrid import AgGrid

import streamlit.components.v1 as components




def main_page():

    col1, mid, col2 = st.columns([1,2,20])
    with col1:
        st.image(os.path.abspath("images/LI logo.png"),
            width=100)
    with col2:
        st.write("# LinkedIn Content Creator Tracker")

    # sidebar

    st.sidebar.markdown("# LinkedIn Content Creators")

    st.sidebar.markdown("**Created by Christian Wanser**")

    st.sidebar.markdown("##")

    st.sidebar.markdown("**Start** by uploading your data on the next page.")

    st.sidebar.markdown("The process for obtaining your data can be found on the **Data Directions page**.")

    # header

    st.subheader("Do you have favorites when it comes to LinkedIn content creators?")

    # welcome photo

    welcome_photo = "people excited.png"

    st.image(os.path.abspath("images/" + welcome_photo))

    st.markdown("**Track LinkedIn content creators** in one place!")
    st.markdown("**Click** on any content creator's name and **you're brought to that creator's LinkedIn page!**")
    st.markdown("**Even open all profile's at once!**")


def page2():

    col1, mid, col2 = st.columns([1,2,20])
    with col1:
        st.image(os.path.abspath("images/LI logo.png"),
            width=100)
    with col2:
        st.write("# LinkedIn Content Creators")


    # sidebar

    # load data

    # code for upload online

    file1 = st.sidebar.file_uploader("Upload LinkedIn Creators file",
        type=["xlsx"],
        help = "This is the file that has all of your favorite LinkedIn content creators' profile urls. Follow the directions on the Data Directions page."
    )


    if file1 is not None:

	    # To See details

        file1_details = {"filename":file1.name, "filetype":file1.type,
                        "filesize":file1.size}

    try:

        df = pd.read_excel(file1)


        st.subheader("Here are the top profiles you follow:")


        #m = st.markdown("""
        #<style>
        #div.stButton > button:first-child {
        #    background-color: rgb(134, 136, 138);
        #}
        #</style>""", unsafe_allow_html=True)



        col0, col1, col2, col3 = st.columns([1,1,1,1])

        with col0:

            st.subheader("Creator")

        with col1:

            st.subheader("Profile")

        with col2:

            st.subheader("Activity")

        with col3:

            st.subheader("Posts")


        col0, col1, col2, col3 = st.columns([1,1,1,1])

        with col0:

            st.markdown("All Creators")

        with col1:

            if st.button("Open everyone's profiles"):
                for i in range(0,df.shape[0]):
                    creator_url = df.iloc[i,1]

                    #webbrowser.open_new_tab(creator_url)

                    webbrowser.open(creator_url)

        with col2:

            if st.button("Open everyone's activity"):
                for i in range(0,df.shape[0]):
                    creator_url = df.iloc[i,1]
                    creator_all_activity = creator_url + "recent-activity/"
                    webbrowser.open_new_tab(creator_all_activity)

        with col3:

            if st.button("Open everyone's posts"):
                for i in range(0,df.shape[0]):
                    creator_url = df.iloc[i,1]
                    creator_posts = creator_url + "recent-activity/shares/"
                    webbrowser.open_new_tab(creator_posts)



        for i in range(0,df.shape[0]):

            creator_name = df.iloc[i,0]

            creator_url = df.iloc[i,1]

            creator_all_activity = creator_url + "recent-activity/"

            creator_posts = creator_url + "recent-activity/shares/"

            col0, col1, col2, col3 = st.columns([1,1,1,1])

            with col0:

                st.markdown(creator_name)

            with col1:

                if st.button(creator_name + "'s Profile"):
                    webbrowser.open_new_tab(creator_url)

            with col2:

                if st.button(creator_name + "'s Activity"):
                    webbrowser.open_new_tab(creator_all_activity)

            with col3:

                if st.button(creator_name + "'s Posts"):
                    webbrowser.open_new_tab(creator_posts)

            


    except:

        st.markdown("##")
        st.markdown("##")
        st.markdown("**Please upload your data :)**")




def page3():

    col1, mid, col2 = st.columns([1,2,20])
    with col1:
        st.image(os.path.abspath("images/LI logo.png"),
            width=100)
    with col2:
        st.write("# LinkedIn Content Creators")



    # directions

    st.subheader("Create your Favorite Content Creators Excel file")

    st.markdown("This file provides the data necessary for the dashboard.")

    st.markdown("Create an Excel file like the sample below.")

    st.markdown("Be sure to name your columns as I have here.")

    st.markdown("Obtain the profile URLs by going to a profile and copying/pasting the URL.")


    sample_df = pd.read_excel(os.path.abspath("LI Creators.xlsx"))

    AgGrid(
        sample_df,
        theme = 'fresh',
        fit_columns_on_grid_load = True
    )


# create site


page_names_to_funcs = {
    "LinkedIn Content Creators": main_page,
    "URL Launch Window": page2,
    "Data Directions": page3
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()






# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 






