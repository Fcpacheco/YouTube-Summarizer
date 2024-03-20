import os
from PIL import Image
from utils import utils
import streamlit as st
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv; load_dotenv()
from lyzr import QABot

# Setup your config
st.set_page_config(
    page_title="YouTube Summarizer",
    layout="centered",  # or "wide" 
    initial_sidebar_state="auto",
    page_icon="./logo/lyzr-logo-cut.png"
)

# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("YouTube Summarizer by Lyzr")
st.markdown("### Welcome to the YouTube Summarizer!")
st.markdown("YouTube Summarizer by Lyzr will providing users with quick access to key information without the need to watch the entire video.")

# Custom function to style the app
def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# Youtube Summarizer Application
    
# replace this with your openai api key or create an environment variable for storing the key.
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY') 


def youtube_video_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get('v')
    if video_id:
        return video_id[0]  # Returns the youtube video id, such as yfHHvmaMkcA
    else:
        return None  

def vector_store_configuration(id):
    vector_store_params = {
    "vector_store_type": "WeaviateVectorStore",
    "url": os.getenv('VECTOR_STORE_URL'), # replce the url with your weaviate cluster url
    "api_key": os.getenv('VECTOR_STORE_API'), # replace the api with your weaviate cluster api
    "index_name": f"Video{id}IndexName" 
  }
    
    return vector_store_params


def lyzr_yt_summarizer(youtube_id, vector_params):
    "This function will implement the Lyzr's QA agent to summarize the Youtube Video"
    yt_summarizer = QABot.youtube_qa(
            urls=[youtube_id],
            vector_store_params=vector_params
        )
    
    return yt_summarizer


if __name__ == "__main__":
    style_app()
    yturl = st.text_input("Paste Youtube video url here")
    if st.button("Summarize"):
        if len(yturl)>0:
            youtube_id = youtube_video_id(url=yturl)
            if youtube_id is not None:
                video_id = youtube_id
                vector_config = vector_store_configuration(id=video_id)
                summarizer_agent = lyzr_yt_summarizer(youtube_id=video_id, vector_params=vector_config)
                utils.summarizer(agent=summarizer_agent)
            else:
                st.error('Provide the correct url, click the address bar to select the entire URL')
        else:
            st.error('Please paste the video url')
    



    with st.expander("ℹ️ - About this App"):
        st.markdown("""
        This app uses Lyzr QABot agent to generate summary of a youtube video. The QABot agent is built on the powerful Retrieval-Augmented Generation (RAG) model, enhancing your ability to extract valuable insights. For any inquiries or issues, please contact Lyzr.
        
        """)
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)