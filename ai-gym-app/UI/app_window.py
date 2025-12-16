import os
from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from UI.Pages.welcome_page import WelcomePage
from UI.Pages.onboarding_page import OnboardingPage
from UI.Pages.login_page import LoginPage
from UI.Pages.register_page import RegisterPage1, RegisterPage2
from UI.Pages.home_page import HomePage

WINDOW_W = 375
WINDOW_H = 812

def project_path(*parts):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, *parts)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fitness App')
        self.setFixedSize(WINDOW_W, WINDOW_H)

        self.stack = QStackedWidget()
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.addWidget(self.stack)

        # Create all pages
        self.welcome = WelcomePage(project_path('UI', 'assets', 'Welcome Screen - 1 (1).svg'))
        self.onboard1 = OnboardingPage(project_path('UI', 'assets', 'Onboarding - 1.svg'), 1, 2)
        self.onboard2 = OnboardingPage(project_path('UI', 'assets', 'Onboarding - 2.svg'), 2, 2)
        self.login_page = LoginPage(project_path('UI', 'assets', 'Login Page.svg'))
        self.register1 = RegisterPage1(project_path('UI', 'assets', 'Register Page - 1.svg'))
        self.register2 = RegisterPage2(project_path('UI', 'assets', 'Register Page - 2.svg'))
        self.home_page = HomePage(project_path('UI', 'assets', 'Home Page.svg'))

        # Add all pages to stack
        for p in [self.welcome, self.onboard1, self.onboard2, self.login_page, 
                 self.register1, self.register2, self.home_page]:
            self.stack.addWidget(p)

        # Connect signals
        self.welcome.loginRequested.connect(lambda: self.goto(self.login_page))
        self.welcome.registerRequested.connect(lambda: self.goto(self.register1))
        
        self.onboard1.nextRequested.connect(lambda: self.goto(self.onboard2))
        self.onboard1.skipRequested.connect(lambda: self.goto(self.login_page))
        
        self.onboard2.backRequested.connect(lambda: self.goto(self.onboard1))
        self.onboard2.nextRequested.connect(lambda: self.goto(self.login_page))
        self.onboard2.skipRequested.connect(lambda: self.goto(self.login_page))
        
        self.login_page.backRequested.connect(lambda: self.goto(self.welcome))
        self.login_page.loginSuccess.connect(lambda data: self.on_login_success(data))
        self.login_page.goToRegister.connect(lambda: self.goto(self.register1))
        
        self.register1.backRequested.connect(lambda: self.goto(self.login_page))
        self.register1.nextRequested.connect(lambda: self.goto(self.register2))
        
        self.register2.backRequested.connect(lambda: self.goto(self.register1))
        self.register2.registerSuccess.connect(lambda data: self.on_register_success(data))
        
        self.home_page.logoutRequested.connect(lambda: self.goto(self.login_page))

        self.stack.setCurrentWidget(self.welcome)

    def goto(self, target: QWidget):
        self.stack.setCurrentWidget(target)

    def on_login_success(self, user_data: dict):
        print(f"Login successful: {user_data['email']}")
        self.home_page.set_user_data(user_data)
        self.goto(self.home_page)

    def on_register_success(self, user_data: dict):
        print(f"Registration successful: {user_data['email']}")
        self.home_page.set_user_data(user_data)
        self.goto(self.home_page)