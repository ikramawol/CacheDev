# Sentiment Analysis Dashboard powered by AI

## Project Overview

This project involves creating a sentiment analysis dashboard powered by AI. The main features and functionalities include:
- **Sentiment Analysis:** Analyze text data to determine sentiment (positive, negative, neutral) using pre-existing AI models.
- **Data Visualization:** Display sentiment analysis results in a user-friendly dashboard.
- **Real-Time Analysis:** Provide real-time sentiment analysis of incoming text data.
- **Integration with Social Media:** Connect to social media platforms to analyze public sentiment on various topics.

## Team Members

- **Team Captain:** Ikram Awol
- Adane Moges
- Mikiyas Endalew
- Kenean Biru
- Agumas Desalew

## Technical Stack

- **Programming Languages:**
  - Python (for backend development and AI model integration)
  - JavaScript (for frontend development)

- **Frameworks/Libraries:**
  - Flask (for backend framework)
  - React (for frontend framework)
  - Plotly (for data visualization)

- **External AI Models:**
  - Hugging Face's BERT or similar pre-existing AI models for natural language processing and sentiment analysis

- **Tools:**
  - Git (for version control)
  - Flask
  - React
  - SQLite (for database management)
  - Jupyter Notebook (for experimentation)

## Project Setup

### Prerequisites

- Python 3.x
- Node.js
- SQLite

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ikramawol/CacheDev.git
    cd CacheDev
    ```

2. **Backend Setup:**

    - Create a virtual environment and activate it:

        ```bash
        python3 -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`
        ```

    - Install the required packages:

        ```bash
        pip install -r backend/requirements.txt
        ```

    - Set up the database:

        ```bash
        # Ensure PostgreSQL is running
        # Create a database and update `backend/settings.py` with your database credentials
        python manage.py migrate
        ```

    - Run the backend server:

        ```bash
        python manage.py runserver
        ```

3. **Frontend Setup:**

    - Navigate to the frontend directory and install the required packages:

        ```bash
        cd frontend
        npm install
        ```

    - Run the frontend server:

        ```bash
        npm start
        ```

4. **Docker Setup (Optional):**

    - Build and run the Docker containers:

        ```bash
        docker-compose up --build
        ```
### If you want to understand more about the project's folder structure, please refer to the [Folder Structure](./folder_structure.md) documentation.

## Usage

1. Access the backend API at `http://localhost:8000`.
2. Access the frontend dashboard at `http://localhost:3000`.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or inquiries, please contact the team captain, Ikram Awol, at [ikram.awol@a2sv.org].

---

**CacheDev Team**
