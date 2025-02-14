# Password Strength Checker

A modern web application that checks password strength based on multiple criteria. The application provides real-time feedback on password strength with a user-friendly interface. It can be used as an API.

## Features

- Real-time password strength analysis
- Visual strength indicators
- Detailed password criteria feedback
- Modern, responsive UI
- RESTful API backend
- Cross-platform compatibility

## Screenshots

![Password Checker](https://github.com/Ejaaz-Ahmed/password-strength-checker/blob/main/images/1.jpg)
![Password Checker](https://github.com/Ejaaz-Ahmed/password-strength-checker/blob/main/images/2.jpg)
![Password Checker](https://github.com/Ejaaz-Ahmed/password-strength-checker/blob/main/images/3.jpg)
![Password Checker](https://github.com/Ejaaz-Ahmed/password-strength-checker/blob/main/images/4.jpg)


## Technical Stack

### Backend
- FastAPI (Python 3.7+)
- Pydantic for data validation
- CORS middleware for cross-origin requests
- Logging for monitoring

### Frontend
- HTML5
- Tailwind CSS for styling
- Font Awesome icons
- Vanilla JavaScript for interactions

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser

### Backend Setup

1. Clone the repository
```bash
git clone https://github.com/Ejaaz-Ahmed/password-strength-checker.git
cd password-checker
```

2. Install required packages
```bash
pip install fastapi uvicorn
```

3. Run the server
```bash
python main.py
```

The backend server will start on `http://localhost:8000`

### Frontend Setup

1. Simply open the `index.html` file in a web browser
   - Or use a local development server like Live Server in VS Code

## API Documentation

### Check Password Strength

```
GET /api/v1/check-password/
```

Parameters:
- `password` (string): The password to check

Response:
```json
{
    "strength": "Strong|Moderate|Weak",
    "details": {
        "length": true|false,
        "digits": true|false,
        "uppercase": true|false,
        "lowercase": true|false,
        "special_chars": true|false
    }
}
```

### Health Check

```
GET /health
```

Response:
```json
{
    "status": "healthy"
}
```

## Password Criteria

A password is evaluated based on the following criteria:
- Minimum length of 8 characters
- Contains at least one digit
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one special character

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Ejaz**
- GitHub: https://github.com/Ejaaz-Ahmed
- LinkedIn: https://www.linkedin.com/in/ejaz-ahmed-150369177/

## Acknowledgments

- FastAPI for the excellent Python web framework
- Tailwind CSS for the modern UI components
- Font Awesome for the icons

---
Created by Ejaz Ahmed
