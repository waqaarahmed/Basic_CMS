
# Basic Flask CMS

This project is a simple Content Management System (CMS) built with Python and Flask. It allows users to create, read, update, and delete content. The CMS is styled with a modern theme using white, blue, and black colors.

## Features

- **CRUD Operations**: Create, read, update, and delete content entries.
- **User Authentication**: Basic user authentication to manage content securely.
- **Responsive Design**: Modern, responsive UI designed with Bootstrap and custom CSS.
- **Template Inheritance**: Use of template inheritance for easy customization and maintenance.
- **Database Integration**: SQLite database integration for storing content.

## Screenshots

![CMS Screenshot](path/to/your/screenshot.png)

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask-cms.git
   cd flask-cms
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the application:**
   ```bash
   flask run
   ```

7. **Access the CMS:**
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

- **Creating Content:**
  - Log in to the CMS.
  - Navigate to the "Create Content" section.
  - Fill out the form and submit to create new content.

- **Updating Content:**
  - Go to the "Content List" page.
  - Click on the "Edit" button next to the content you wish to update.
  - Modify the fields and submit.

- **Deleting Content:**
  - Go to the "Content List" page.
  - Click on the "Delete" button next to the content you wish to remove.

## File Structure

```
flask-cms/
├── app.py             # Main application file
├── models.py          # Database models
├── forms.py           # Flask-WTF forms
├── static/
│   └── css/
│       └── style.css  # Custom CSS styles
├── templates/
│   ├── base.html      # Base template
│   ├── index.html     # Home page template
│   ├── login.html     # Login page template
│   ├── create.html    # Create content template
│   ├── update.html    # Update content template
│   └── content_list.html # Content list template
└── requirements.txt   # Python dependencies
```

## Customization

- **Colors and Theme:**
  Modify the `style.css` file located in the `static/css/` directory to change the color scheme and layout of the CMS.

- **Database:**
  By default, the CMS uses SQLite. You can configure a different database by modifying the `SQLALCHEMY_DATABASE_URI` in `app.py`.

## Contributing

Feel free to fork this repository, submit pull requests, or open issues for suggestions and improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
