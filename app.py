import pandas as pd
import streamlit as st
from src.sentiment import analyze_sentiment
from src.word_count import count_words
from src.sentence_count import count_sentences

st.title('Our simple NLP APP to practice GIT')
user_txt = st.text_area('text to analyze', value='Enter your text here')

# Map options to their handler functions
TOOLS = {
    "Number of words": count_words,
    "Number of sentences": count_sentences,
    "Sentiment Analysis": analyze_sentiment,
}

selection = st.pills("Tools", list(TOOLS.keys()), selection_mode="single")

if selection:
    st.markdown(f"**Selected tool:** {selection}")

    # Call the selected function
    result = TOOLS[selection](user_txt)

    # Handle different result types
    if selection == "Sentiment Analysis":
        df = pd.DataFrame({
            'Negative': [result['neg']],
            'Neutral': [result['neu']],
            'Positive': [result['pos']]
        })
        st.bar_chart(df, horizontal=True, stack=True,
                     color=['#ff4444', '#888888', '#44ff44'])
    else:
        st.write(result)
