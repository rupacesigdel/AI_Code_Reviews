# python/django-AI Code Reviewer

AI Code Reviewer is a web application that analyzes code submitted by users, provides feedback on potential issues, and offers corrected versions of the code. This project uses Django as the backend framework, integrated with a custom code analysis agent (`LangGraphAgent`), and leverages the `CopilotKit` SDK for additional functionalities.

---

## Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Demo Video](#demo-video)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Summary of Sections](#summary-of-sections)
  
## Features

- **Code Upload**: Users can upload or paste their code for analysis.
- **Code Analysis**: The code is analyzed for potential issues (syntax errors, best practices, etc.).
- **Code Correction**: A corrected version of the code is returned along with analysis feedback.
- **REST API**: A REST API endpoint allows users to send code and receive analysis and corrected code.

---
## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, JavaScript (with Fetch API)
- **Code Analysis**: `LangGraphAgent` for analyzing and correcting code
- **Dependencies**: `CopilotKitSDK`, `LangGraphAgent`

---
## Demo video
[Watch the demo video](https://github.com/userattachments/assets/0933bcfe-e3bb-43ab-8818-e5c3d0215c93)

## Installation

### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.12 or higher
- Django 4.x or higher
- Django REST Framework
- Other Python dependencies (listed below)

### Steps to Set Up

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rupace/AI_Code_Reviews.git
   cd AI_Code_Reviews
   
2. **Create a Virtual Environment:**
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: source myenv\Scripts\activate
    ```

3. **Upgrade pip (if needed):**

    ```bash
    pip install --upgrade pip
    ```

4. **Install Required Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Database Setup:**
    - Run migrations to set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the server:**

   ```bash
   python manage.py runserver
   ```
7. **Visit the web application**:
-   Open your browser and navigate to ```http://127.0.0.1:8000/``` to access the AI Code Reviewer.
---

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. When contributing, ensure that your code adheres to the existing code style and includes appropriate tests.

## License
This project is licensed under the MIT License. See the  [LICENSE](LICENSE) file for more details.

---
## Summary of Sections:
1. **Features**: Describes the functionality provided by the app.
2. **Tech Stack**: Lists the technologies and libraries used.
3. **Installation**: Step-by-step instructions to set up and run the project.
4. **API Endpoints**: Documentation of the available API endpoint (`/analyze-code/`) to interact with the backend.
5. **Frontend**: Information on the frontend functionality (input field, analyze button, results display).
6. **Development Notes**: Notes on the core components like `LangGraphAgent` and `CopilotKitSDK`.
7. **Contributing**: Instructions for contributing to the project.
8. **License**: Specifies the licensing information.

---
This `README.md` serves as a comprehensive guide for setting up, using, and contributing to your AI Code Reviewer project.
