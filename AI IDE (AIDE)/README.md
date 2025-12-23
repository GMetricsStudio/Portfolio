# AI Dev IDE

## Description
The AI Dev IDE is a comprehensive development environment designed for artificial intelligence (AI) developers. It integrates cutting-edge AI models, advanced code editors, and powerful debugging tools to streamline the development process. The IDE features include but are not limited to:

- **Settings Integration**: Users can configure their development settings seamlessly within the application.
- **Full Functionality**: The tool is fully operational with all necessary components for a complete development experience.
- **Modular Design**: Easily extendable and customizable, allowing users to add new features or integrate additional tools as needed.

## Features
- **AI Model Integration**: Utilizes state-of-the-art AI models from Hugging Face's repository.
- **Advanced Code Editor**: Integrates a sophisticated code editor powered by Pygments for syntax highlighting and other enhancements.
- **Multi-Language Support**: Supports Python, C++, Java, and more out of the box with plans to expand support for additional languages.
- **Debugging Tools**: Includes advanced debugging features such as breakpoints, variable inspection, and step execution.
- **User Settings Management**: Allows users to customize their IDE settings including editor themes, font sizes, and other preferences.

## Setup Instructions
### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or later
- Docker (for running the containerized version of the IDE)

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-dev-ide.git
   cd ai-dev-ide
   ```
2. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Build the Docker Image** (if you plan to run it in a container):
   ```bash
   docker build -t ai-dev-ide .
   ```
4. **Run the Docker Container**:
   ```bash
   docker run -p 5900:5900 -e VNC_PASSWORD=YourSecurePassword --rm --name ai-dev-ide ai-dev-ide
   ```

### Running the IDE
1. **Local Execution**:
   ```bash
   python app.py
   ```
2. **Container Execution** (if you built the Docker image):
   Open a web browser and navigate to `http://localhost:5900` using your VNC viewer, providing the password set in the previous step.

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](https://github.com/yourusername/ai-dev-ide/blob/main/CONTRIBUTING.md) for guidelines on how to contribute to this project.

## Support
For additional support, please refer to the documentation or reach out through the issue tracker on GitHub.

---

This README provides a comprehensive guide for users and contributors to understand and engage with the AI Dev IDE project effectively.