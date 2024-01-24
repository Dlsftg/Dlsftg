from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import yagmail

class EmailSenderApp(App):
    def build(self):
        # Thiết lập giao diện
        layout = BoxLayout(orientation='vertical')

        self.label_to = Label(text='Email mục tiêu:')
        self.input_to = TextInput()

        self.label_subject = Label(text='Chủ đề:')
        self.input_subject = TextInput()

        self.label_content = Label(text='Nội dung:')
        self.input_content = TextInput()

        self.btn_send = Button(text='Gửi Email')
        self.btn_send.bind(on_press=self.send_email)

        layout.add_widget(self.label_to)
        layout.add_widget(self.input_to)
        layout.add_widget(self.label_subject)
        layout.add_widget(self.input_subject)
        layout.add_widget(self.label_content)
        layout.add_widget(self.input_content)
        layout.add_widget(self.btn_send)

        return layout

    def send_email(self, instance):
        # Lấy thông tin từ người dùng
        to_email = self.input_to.text
        subject = self.input_subject.text
        content = self.input_content.text

        # Thông tin đăng nhập Gmail
        sender_email = 'supershark.indo@gmail.com'  # Thay bằng địa chỉ email của bạn
        sender_password = 'cskrpwkdbfjzalyv'  # Thay bằng mật khẩu của bạn

        # Gửi email
        try:
            yag = yagmail.SMTP(sender_email, sender_password)
            yag.send(to=to_email, subject=subject, contents=content)
            yag.close()
            print('Email đã được gửi thành công!')
        except Exception as e:
            print(f'Có lỗi xảy ra: {str(e)}')

if __name__ == '__main__':
    EmailSenderApp().run()
