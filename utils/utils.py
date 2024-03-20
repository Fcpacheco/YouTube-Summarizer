import streamlit as st

def summarizer(agent):
    summary = agent.query("What is this video about? can you explain in a short paragrqaph")
    keypoints = agent.query('Provide 3-5 key points from this video?')
    content_alaysis = agent.query('Write any examples or case studies mentioned in the video? If so, what are they?')
    audience_engagement = agent.query("""
                                        "How does the speaker engage with the audience in the video?"
                                        "Are there any interactive elements or calls to action in the video?"
                                        """)
    
    additional_information = agent.query("""
                                        "Are there any references or citations provided in the video?"
                                        "Can you identify any trends or patterns in the content of the video?"
                                         """)
    if summary is not None:
        st.subheader('Video Summary')
        st.write(summary.response)
        st.write(keypoints.response)
        if len(content_alaysis.response)>150:
            st.subheader('Content Analysis')
            st.write(content_alaysis.response)
            if len(audience_engagement.response)>150:
                st.subheader('Audience Engagement')
                st.write(audience_engagement.response)
                if len(additional_information.response)>150:
                    st.header('Additional Information')
                    st.write(additional_information.response)
