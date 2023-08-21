import streamlit as st
import pandas as pd
import altair as alt

st.header("Was sich gehört: Jung und Alt sind sich weitgehend einig")
st.subheader("Zustimmung zu Aussagen zum Thema Höflichkeit (in Prozent) (Gesamtbevölkerung)")

source = pd.DataFrame({
        'Anteil(%)': [94, 91, 78],
        'Meinung': ['Wenn in der Bahn eine ältere oder schwangere Person einsteigt, sollte ihr jemand einen Sitzplatz freimachen', 'Ich finde es unhöflich, wenn Menschen während eines Gespräches ständig auf ihr Handy schauen', 'Männer sollten Frauen die Tür aufhalten und den Vortritt lassen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: YouGov")