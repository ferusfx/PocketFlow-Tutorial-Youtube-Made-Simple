# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a YouTube video processing application that extracts transcripts from YouTube videos, identifies key topics, generates questions and ELI5 (Explain Like I'm 5) answers, then creates an HTML report. Built using the PocketFlow framework for LLM agent workflows.

## Key Commands

### Setup and Dependencies
```bash
pip install -r requirements.txt
```

### LLM Configuration Test (Interactive Mode)
```bash
python utils/call_llm.py
# Will prompt for interactive responses - no API setup needed
```

### Run Application
```bash
python main.py --url "https://www.youtube.com/watch?v=example"
```

### Individual Component Testing
```bash
python utils/youtube_processor.py  # Test YouTube processing
python utils/html_generator.py     # Test HTML generation
```

## Architecture

### Core Flow (flow.py)
The application uses PocketFlow's Node/Flow architecture with these key stages:
1. **ProcessYouTubeURL** - Extracts video metadata and transcript
2. **ExtractTopicsAndQuestions** - LLM identifies up to 5 topics with 3 questions each
3. **ProcessContent** (BatchNode) - Processes each topic in parallel to rephrase and generate ELI5 answers
4. **GenerateHTML** - Creates final HTML output

### Shared Memory Structure
```python
shared = {
    "url": str,
    "video_info": {"title", "transcript", "thumbnail_url", "video_id"},
    "topics": [{"title", "rephrased_title", "questions": [{"original", "rephrased", "answer"}]}],
    "html_output": str
}
```

### LLM Integration
- Uses Claude Code interactive mode for LLM processing
- `utils/call_llm.py` presents prompts to the user for interactive responses
- No external API keys or configuration required

### Key Utilities
- `utils/youtube_processor.py`: YouTube transcript extraction using youtube-transcript-api
- `utils/html_generator.py`: HTML generation with Tailwind CSS styling
- `utils/call_llm.py`: LLM wrapper for Anthropic Claude

## Development Notes

- Output is saved as `output.html` in project root
- Logging is configured to both console and `youtube_processor.log`
- HTML uses handwriting-style font (Patrick Hand) and Tailwind CSS
- BatchNode processes topics in parallel for efficiency
- YAML parsing is used for structured LLM responses
- Maximum 5 topics with 3 questions each to control processing time