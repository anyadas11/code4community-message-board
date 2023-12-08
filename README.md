# code4community message board
 Simple message board where user can post timestamped messages. Developed using Python, Flask, SQLAlchemy, HTML, CSS, and JavaScript

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

## Features

- Each message features message content and timestamp (UTC-5)
- Messages are displayed from most to least recent.
- Each message is limited to 128 characters.
- Delete button performs a soft delete and causes message to be removed from the message board, however, data is preserved on SQLite database and will survive an application restart
- When hosted on a nonlocal server, users have the capability to post/view messages from multiple computers

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Flask

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/anyadas11/code4community-message-board.git
    cd code4community-message-board
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application

    ```bash
    flask run
    ```

2. Open web browser and go to http://127.0.0.1:5000

3. Type message into input form and push the "Post Message" button



