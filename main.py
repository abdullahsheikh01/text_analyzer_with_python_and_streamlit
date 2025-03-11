# Importing Streamlit
import streamlit as st
# Setting Up a Page
st.set_page_config(
    page_title="Text Analyzer By Abdullah Shaikh",
    page_icon="icon.png"
)
# Heading Of Page
st.markdown(
    """# Text Analyzer By [Abdullah Shaikh](https://www.linkedin.com/in/abdullah-shaikh-29699b302/)
"""
)
# Adding Text Area of Paragraph
text : str = st.text_area("Write Your Paragraph Here:")
# Displaying chrachters and words length of text
st.subheader("Count")
st.write("To know chrachters and words click on count button")
if st.button("Count: "):
    st.write(f"Chrachters: {len(text)}")
    st.write(f"Words: {len(text.split())}")
# Feature for user to get about word's occurence in paragraph
st.subheader("Word Occurence")
word : str = st.text_input(
    "To know about any word's occurence write in this box and click on get info:")
if st.button("Get Info:"):
    if not word:
        st.write("Write something to get know")
    elif text.lower().count(word.lower())==1:
        st.write(f"This Word Occur {text.lower().count(word.lower())} time in paragraph")
    elif text.lower().count(word.lower())>1:
        st.write(f"This Word Occur {text.lower().count(word.lower())} times in paragraph")
    else:
        st.write("This word is not occured in this paragraph")
# Feature to enable users to replace words
st.subheader("Replace Word")
replace_word1 : str = st.text_input("You want to replace word: ").lower()
replace_word2 : str = st.text_input("with ")
updatedText: str = text.lower().replace(replace_word1,replace_word2)
st.markdown("#### Updated Text: ")
if st.button("Replace:"):
    st.text(updatedText)