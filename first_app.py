import streamlit as st #Importing a module

#Title
st.write("My first web app")

#Header
st.header("This is a header")

#Subheader
st.subheader("This is a subheader")

#checkbox
#check if the checkbox is checked
#title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
    #disply the text if the checkbox returns True value
    st.text("Showing the widget")

#radio button
#first argument is the title of the radio button
#second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

#conditional statement to print
#Male if male is selected else print female
#show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

#Create a button, that when clicked, shows a text
if (st.button("click me")):
    st.text("button clicked")


def sqr(num):
    return num*num

num=st.number_input("Insert a Number")

if st.button("Calculate Square"):
    result=sqr(num)
    st.text(result)
