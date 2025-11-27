import pandas as pd
import streamlit as st
from src.sentiment import analyze_sentiment
from src.word_count import count_words
from src.sentence_count import count_sentences
from src.make_text_uppercase import text_uppercase
from src.sudification import sudification

# The title
st.title('Our simple NLP APP to practice GIT')
# The text area for the user
user_txt = st.text_area('text to analyze', placeholder='Enter your text here')

# Map options to their handler functions
# Keys = Name on the button
# Values = Functions that is executed when button is clicked
TOOLS = {
    "Uppercase": text_uppercase,
    "Number of words": count_words,
    "Number of sentences": count_sentences,
    "Sentiment Analysis": analyze_sentiment,
    "Sudification": sudification,
}

selection: str|None = st.pills("Tools: ", list(TOOLS.keys()), selection_mode="single")

if selection:
    st.markdown(f"**Selected tool:** {selection}")

    # Call the selected function
    result = TOOLS[selection](user_txt)

    # Handle different result types // If you need to output something else than pure text, do it here
    if selection == "Sentiment Analysis":
        df = pd.DataFrame({
            'Negative': [result['neg']],
            'Neutral': [result['neu']],
            'Positive': [result['pos']]
        })
        st.bar_chart(df, horizontal=True, stack=True,
                     color=['#ff4444', '#888888', '#44ff44'])
    else:
        # It just print the result of your function here.
        st.write(result)
