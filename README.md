# Real Estate Web App

This is a cozy, beige-themed Flask web application designed to assist users in buying, selling, or renting homes. The application features a user-friendly interface with a chatbot placeholder, hot properties, and top agents sections.

## Project Structure

```
real-estate-app
├── app.py                  # Main entry point of the Flask application
├── static
│   ├── css
│   │   └── style.css       # CSS styles for the application
│   └── images
│       ├── house1.jpg      # Featured house image 1
│       ├── house2.jpg      # Featured house image 2
│       ├── house3.jpg      # Featured house image 3
│       ├── agent1.jpg      # Real estate agent image 1
│       ├── agent2.jpg      # Real estate agent image 2
│       └── agent3.jpg      # Real estate agent image 3
├── templates
│   ├── base.html           # Base layout for the application
│   ├── index.html          # Landing page of the application
│   ├── hot-properties.html  # Page displaying featured houses
│   └── top-agents.html     # Page showcasing real estate agents
└── README.md               # Documentation for the project
```

## Features

- **Landing Page**: Includes a chatbot placeholder and buttons to navigate to hot properties and top agents.
- **Hot Properties**: Displays featured houses with images and descriptions.
- **Top Agents**: Showcases real estate agents with images and short bios.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd real-estate-app
   ```

3. Install the required packages:
   ```
   pip install Flask
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## Technologies Used

- Flask: A lightweight WSGI web application framework in Python.
- HTML/CSS: For structuring and styling the web pages.
- Images: Used for displaying properties and agents.

## License

This project is licensed under the MIT License.