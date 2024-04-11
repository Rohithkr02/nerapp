import streamlit as st
import spacy
from spacy import displacy
#from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from newspaper import Article
st.header("NER Demo")
status =st.radio("select pargarph or url",('url','text'))
if (status=='text'):
   text=st.text_area("enter paragraph")
   if (st.button("Analyse")):
      doc = nlp(text)
      ent_html = displacy.render(doc, style="ent", jupyter=False)
    # Display the entity visualization in the browser:
      st.markdown(ent_html, unsafe_allow_html=True)     
else:
   url=st.text_area("enter url") 
   if (st.button("Analyse")):
      article=Article(url)
      article.download()
      article.parse()
      doc = nlp(article.text)
      ent_html = displacy.render(doc, style="ent", jupyter=False)
    # Display the entity visualization in the browser:
      st.markdown(ent_html, unsafe_allow_html=True)    
