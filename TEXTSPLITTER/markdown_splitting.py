from langchain_text_splitters import MarkdownTextSplitter

text = """
# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.


## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies


## Getting Started

1. Clone the repo  h
   git clone https://github.com/your-username/student-tracker.git

"""

# Initialize the splitter
splitter = MarkdownTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])
 