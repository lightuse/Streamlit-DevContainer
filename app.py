import streamlit as st
import streamlit.components.v1 as components

html_string = '''
<html>
    <head>
        <script>
            alert("JavaScript is running!");
        </script>
    </head>
    <body>
        <h1>Hello from Streamlit!</h1>
    </body>
</html>
'''
components.html(html_string)


st.title("My Streamlit App")
st.write("Hello, World!")
