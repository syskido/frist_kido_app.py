# import streamlit as st
# import time
# # from dotenv import load_dotenv
# # load_dotenv()
# import os
# os.environ['OPENAI_API_KEY'] = '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'

# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()
# # from langchain.llms import OpenAI
# # llm = OpenAI()

# # content = "연인"

# # result = llm.predict(content + "에 대한 시를 써줘")
# # print(result)
# st.link_button("나령 윤기도", "https://syskido.tistory.com")
# st.text('인공지능 Kido 단편소설')
# content = st.text_input('단편소설의 주제를 제시해주세요.')
# if st.button('단편소설 2000자 내외 작성 요청하기'):
#     with st.spinner('단편소설 작성 중...'):
#        time.sleep(100)
#     result = chat_model.predict(content + "에 대한 단편소설을 써줘")
#     st.write(result)
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)
