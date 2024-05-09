# SecPassGen

SecPassGen is a secure password generator web application built with Flask, allowing users to generate strong and unique passwords based on their preferences. It utilizes the zxcvbn library to assess the strength of generated passwords and SQLite to store generated passwords securely.

## Features

- Password length customization.
- Option to include uppercase letters, numbers, and special characters in generated passwords.
- Real-time strength assessment of generated passwords.
- Secure storage of generated passwords using SQLite.

## Prerequisites

- Python 3.x
- Flask
- zxcvbn
- SQLite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/instax-dutta/Secure-Password-Generator-Webapp.git
```

2. Navigate to the project directory:

```bash
cd Secure-Password-Generator-Webapp
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and go to `http://localhost:5000`.

3. Customize the password settings as desired:
   - Set the password length.
   - Choose whether to include uppercase letters, numbers, and special characters.

4. Click the "Generate Password" button to generate a strong and unique password.

5. The generated password and its strength will be displayed on the screen.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Flask web framework: [Flask](https://flask.palletsprojects.com/)
- zxcvbn library: [zxcvbn](https://github.com/dwolfhub/zxcvbn-python)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
