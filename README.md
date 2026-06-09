# Python Crowd Funding Console App

A command-line crowd funding platform built with Python. This application allows users to create projects, browse existing campaigns, and support projects they believe in through a simple console interface.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
  - [User Authentication](#user-authentication)
  - [Managing Projects](#managing-projects)
  - [Supporting Projects](#supporting-projects)
- [File Structure](#file-structure)
- [Data Storage](#data-storage)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **User Authentication**: Secure login and registration system for users
- **Project Management**: Create, view, update, and manage crowdfunding projects
- **Project Discovery**: Browse and search through active projects
- **Funding Support**: Contribute to projects you want to support
- **User Dashboard**: View your projects and contributions at a glance
- **Data Persistence**: All user and project data stored in JSON format
- **Styled Interface**: Console-based UI with custom styling options

## 📁 Project Structure

```
Python-Crowd-Funding-console-app/
├── main.py                 # Entry point of the application
├── auth.py                 # User authentication and login logic
├── projects.py             # Project management functionality
├── helpers.py              # Utility functions and helpers
├── data.json               # Application data storage
├── users.json              # User profiles and credentials
├── projects.json           # Project details and information
├── style/                  # Styling and formatting modules
├── views/                  # User interface components
└── .gitignore              # Git ignore file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Arezk22/Python-Crowd-Funding-console-app-.git
cd Python-Crowd-Funding-console-app-
```

2. Navigate to the project directory:
```bash
cd Python-Crowd-Funding-console-app-
```

3. No external dependencies are required as this project uses only Python standard library.

### Running the Application

Execute the main script to start the application:

```bash
python main.py
```

The console application will launch with an interactive menu for you to navigate.

## 📖 Usage

### User Authentication

Upon launching the application, you'll be prompted to:
- **Register** as a new user (create account with username and password)
- **Login** with existing credentials

Your credentials are securely stored in `users.json`.

### Managing Projects

Once logged in, you can:
- **Create Projects**: Start your own crowdfunding campaign
  - Provide project title, description, and funding goal
  - Set project timeline and category
- **View Projects**: Browse all active projects
- **Edit Projects**: Modify your own project details (before funding closes)
- **Track Progress**: Monitor funding status and supporter information

### Supporting Projects

- **Browse Projects**: Explore all active campaigns
- **View Details**: Get comprehensive information about any project
- **Contribute**: Back a project with your funds
- **View History**: Track your contributions and supported projects

## 💾 Data Storage

The application uses JSON files for data persistence:

- **users.json**: Stores user accounts, credentials, and profile information
- **projects.json**: Contains all project details, goals, and current funding amounts
- **data.json**: General application data and metadata

All data is stored locally and updated in real-time as users interact with the application.

## 🤝 Contributing

Contributions are welcome! To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Arezk22**
- GitHub: [@Arezk22](https://github.com/Arezk22)

## 🔗 Links

- **Repository**: [Python-Crowd-Funding-console-app-](https://github.com/Arezk22/Python-Crowd-Funding-console-app-)
- **Issues**: [Report Issues](https://github.com/Arezk22/Python-Crowd-Funding-console-app-/issues)

## 📧 Support

If you encounter any issues or have questions about the application, please open an issue on GitHub.

---

**Happy Crowdfunding!** 🎉
