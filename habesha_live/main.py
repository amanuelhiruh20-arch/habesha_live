from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import os

# ==================== LOGIN SCREEN (KIVY) ====================
class LoginScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        layout.add_widget(Label(text="🔴 HABESHA LIVE", font_size=24, bold=True, color=(1, 1, 1, 1)))
        
        layout.add_widget(Label(text="ስልክ ቁጥር ወይም ኢሜይል", font_size=14, color=(0.8, 0.8, 0.8, 1)))
        self.user_input = TextInput(hint_text="ስልክ/ኢሜይል ያስገቡ", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.user_input)
        
        layout.add_widget(Label(text="የይለፍ ቃል (Password)", font_size=14, color=(0.8, 0.8, 0.8, 1)))
        self.pass_input = TextInput(hint_text="የይለፍ ቃል", password=True, multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.pass_input)
        
        login_btn = Button(text="ግባ (Login)", background_color=(1, 0.16, 0.33, 1), size_hint_y=None, height=45)
        login_btn.bind(on_press=self.do_login)
        layout.add_widget(login_btn)
        
        reg_btn = Button(text="አካውንት ፍጠር (Create Account)", background_color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=40)
        reg_btn.bind(on_press=self.goto_register)
        layout.add_widget(reg_btn)
        
        self.add_widget(layout)

    def do_login(self, instance):
        if self.user_input.text.strip() and self.pass_input.text.strip():
            self.manager.current = 'main'

    def goto_register(self, instance):
        self.manager.current = 'register'


# ==================== REGISTER SCREEN (KIVY) ====================
class RegisterScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        layout.add_widget(Label(text="🔴 HABESHA LIVE - ምዝገባ", font_size=22, bold=True, color=(1, 1, 1, 1)))
        
        layout.add_widget(Label(text="ስም (Full Name)", font_size=14))
        self.name_input = TextInput(hint_text="ስምዎን ያስገቡ", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.name_input)
        
        layout.add_widget(Label(text="ስልክ ቁጥር ወይም ኢሜይል", font_size=14))
        self.user_input = TextInput(hint_text="ስልክ/ኢሜይል", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.user_input)
        
        layout.add_widget(Label(text="አዲስ የይለፍ ቃል", font_size=14))
        self.pass_input = TextInput(hint_text="የይለፍ ቃል", password=True, multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.pass_input)
        
        signup_btn = Button(text="ተመዝገብ (Sign Up)", background_color=(0.2, 0.78, 0.35, 1), size_hint_y=None, height=45)
        signup_btn.bind(on_press=self.do_signup)
        layout.add_widget(signup_btn)
        
        back_btn = Button(text="ወደ መግቢያ ተመለስ", background_color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=40)
        back_btn.bind(on_press=self.goto_login)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def do_signup(self, instance):
        self.manager.current = 'login'

    def goto_login(self, instance):
        self.manager.current = 'login'


# ==================== ACCOUNT SAFETY & SUPPORT SCREEN (KIVY) ====================
class AccountSafetyScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        layout.add_widget(Label(text="🛡️ Account Safety & Help Centre", font_size=18, bold=True, size_hint_y=None, height=40, color=(1, 0.16, 0.33, 1)))
        
        # Scrollable help items
        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', size_hint_y=None, spacing=8)
        content.bind(minimum_height=content.setter('height'))
        
        topics = [
            ("👤 Account safety", "የአካውንት ደህንነት ጥበቃ እና አጠባበቅ"),
            ("👥 Suggested accounts", "የተጠቆሙ አካውንቶች ዝርዝር አሰራር"),
            ("⚠️ Inactive Account Policy", "እንቅስቃሴ የሌላቸው አካውንቶች መመሪያ"),
            ("🆕 Creating an account", "አዲስ አካውንት አፈጣጠር ሂደት"),
            ("📉 My posts aren't getting views", "የለቀቁዋቸው ፖስቶች እይታ ባለማግኘታቸው ዙሪያ"),
            ("⭐ Account types on TikTok", "የአካውንት አይነቶች እና መዋቅር"),
            ("🛡️ Privacy and user safety", "የግላዊነት እና የተጠቃሚ ደህንነት መመሪያዎች"),
            ("📊 TikTok post view history", "የፖስት እይታ ታሪክ መረጃ")
        ]
        
        for title, desc in topics:
            btn = Button(text=f"{title}\n{desc}", size_hint_y=None, height=50, background_color=(0.18, 0.18, 0.18, 1))
            content.add_widget(btn)
            
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        # Contact with us and AI chat box section inside Account Safety
        chat_box = BoxLayout(orientation='vertical', size_hint_y=None, height=100, spacing=5)
        chat_box.add_widget(Label(text="💬 Contact with us (AI Support)", font_size=12, color=(0, 0.8, 1, 1), size_hint_y=None, height=20))
        
        self.msg_input = TextInput(hint_text="ሰላም! ጥያቄዎን ወይም ቅሬታዎን እዚህ ይጻፉ...", multiline=False, size_hint_y=None, height=35)
        chat_box.add_widget(self.msg_input)
        
        send_btn = Button(text="Send", background_color=(1, 0.16, 0.33, 1), size_hint_y=None, height=35)
        send_btn.bind(on_press=self.send_message)
        chat_box.add_widget(send_btn)
        
        layout.add_widget(chat_box)
        
        back_home = Button(text="⬅️ ወደ ዋናው ገጽ ተመለስ", background_color=(0.2, 0.2, 0.2, 1), size_hint_y=None, height=40)
        back_home.bind(on_press=self.goto_main)
        layout.add_widget(back_home)
        
        self.add_widget(layout)

    def send_message(self, instance):
        query = self.msg_input.text.strip()
        if query:
            print(f"User Query: {query}")
            self.msg_input.text = ""
            print("AI Support Bot: ጥያቄዎ/ቅሬታዎ ደርሶናል። ትክክለኛው ማስተካከያ በራስ-ሰር ተደርጓል!")

    def goto_main(self, instance):
        self.manager.current = 'main'


# ==================== MAIN DASHBOARD SCREEN (KIVY) ====================
class MainScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="🔴 HABESHA LIVE - ዋና ዳሽቦርድ", font_size=20, bold=True, size_hint_y=None, height=40))
        
        safety_btn = Button(text="🛡️ Account Safety & Help Centre", background_color=(0.1, 0.5, 0.8, 1), size_hint_y=None, height=50)
        safety_btn.bind(on_press=self.goto_safety)
        layout.add_widget(safety_btn)
        
        logout_btn = Button(text="ውጣ (Logout)", background_color=(0.9, 0.2, 0.2, 1), size_hint_y=None, height=45)
        logout_btn.bind(on_press=self.do_logout)
        layout.add_widget(logout_btn)
        
        self.add_widget(layout)

    def goto_safety(self, instance):
        self.manager.current = 'safety'

    def do_logout(self, instance):
        self.manager.current = 'login'


# ==================== KIVY APP RUNNER ====================
class HabeshaLiveApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AccountSafetyScreen(name='safety'))
        return sm

if __name__ == '__main__':
    HabeshaLiveApp().run()
