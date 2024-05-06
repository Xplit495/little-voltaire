# Little Voltaire

## About

A Python-based bot that automates interactions on https://www.projet-voltaire.fr/. It simulates user activity on the platform, 
allowing it to increase hours without direct user engagement. Note that while it increases time spent, it does not provide correct answers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Feature](#feature)
- [Dependencies](#dependencies)
- [Author](#author)
- [License](#license)

## Installation

Follow these instructions to install the project on your local machine. This is intended for developers wishing to test and use the project.

```bash
git clone https://github.com/Xplit495/little-voltaire.git
cd LittleVoltaire
pip install -r requirements.txt
```

Next, you need to download chromeDriver. <br>To download the good version of ChromeDriver for your Chrome version, 
you can click [here](https://googlechromelabs.github.io/chrome-for-testing/#stable) <br> 
(Download chromeDriver and not just chrome ! After replace the existing chromedriver in the project by the new one)


## Usage

After installation, here's how you can start using the project:<br><br>
Navigate to the project directory and run the following command:

```python
python .\main.py
```

## Feature

The project include the following feature:

- **Auto-login**: Enter mail/pass into login.txt.

## Dependencies

- Python 3.12.2 (or higher)
- Selenium 4.15.2 (or higher)
- ChromeDriver (depending on your Chrome version) <br>

## Author

**Carrola Quentin**

- GitHub: [Xplit495](https://github.com/Xplit495)
- LinkedIn: [Quentin Carrola](https://www.linkedin.com/in/quentin-carrola-24306b304/)
- Email: carrolaquentin.pro@gmail.com

## License

This project is licensed under the MIT License. For more details, 
see the [LICENSE](LICENSE) file included in this repository.



