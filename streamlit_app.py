import streamlit as st

st.markdown("*JAWIR* is **brigez** ***tiriss***.")
st.markdown('''
    :red[JAWIR] :orange[is] :blue[persib] :blue[maung] :violet[bandung]
    :gray[kang] :red[dedi] and :red-background[mulyadi] text.''')
st.markdown("Aku jawa &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
