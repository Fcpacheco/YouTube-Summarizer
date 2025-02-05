# Welcome to the YouTube Processor!

![YouTube Processor App Logo](./logo/youtube-processor-logo.webp)


The YouTube Summarizer Application is a powerful tool designed to condense lengthy YouTube videos into concise summaries, providing users with quick access to key information without the need to watch the entire video. This innovative application utilizes Lyzr's QABot Agent to analyze video content and generate accurate summaries.

*Note: For this application to function properly in your local system, ensure that the required dependencies are installed and configured correctly, and make sure that you have your OpenAI API Key.*

## Features

- **Video Summarization:** Get concise summaries of lengthy videos.
- **Transcript Analysis:** Leverage Lyzr's QABot Agent to perform Q&A on video transcripts.
- **Metadata Extraction:** Use PyTube to fetch additional video metadata (such as description, links, and timestamps).

## Dependencies

In addition to the existing dependencies, this application also uses **PyTube** to extract YouTube video metadata.

### Create Virtual Environment 
- `python3 -m venv venv` - Ubuntu/MacOS
- `python -m venv venv` - Windows

### Activate the Environment
- `source venv/bin/activate`  - Ubuntu/MacOS
- `venv\Scripts\activate` - Windows

### Installing Dependencies
- Install all required packages:
  - Ubuntu/MacOS: `pip3 install -r requirements.txt`
  - Windows: `pip install -r requirements.txt`
