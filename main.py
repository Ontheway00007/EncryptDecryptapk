from kivy.lang import Builder
from cryptography.fernet import Fernet
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
KV = '''
#:import Clipboard kivy.core.clipboard.Clipboard
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Safetext"

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)



<Tab>

    
    MDLabel:
        text: 'Generate Your Key'
        pos_hint:{'center_x':0.70, 'center_y' : 0.850}
        font_size: (self.height/15)*0.6
    MDIcon:
        badge_icon: "key"
        pos_hint:{'center_x':0.83, 'center_y' : 0.845}
    MDFillRoundFlatButton
        text: "Generate Key"
        theme_text_color: "Custom"
        text_color: "black"
        on_press: root.generate()
        size_hint: .25, .04
        pos_hint:{'center_x':0.5, 'center_y' : 0.430}
    MDIconButton:
        icon: 'content-copy'
        theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.94, 'center_y':0.630}

        on_release:
            Clipboard.copy(genkey.text)
        
        
    MDTextField:
        id: genkey
        pos_hint: {'center_x':0.48, 'center_y':0.630}
        size_hint: 0.8, None
        height: "30dp"
        background_color: app.theme_cls.bg_normal
        multiline: True
<Tab2>
    
    MDFillRoundFlatButton
        text: "Encrypt text"
        theme_text_color: "Custom"
        text_color: "black"
        on_press: root.encrypt()
        size_hint: .25, .04
        pos_hint:{'center_x':0.5, 'center_y' : 0.230}
    

    
    MDTextField:
        id: inputkey
        hint_text: "Enter your key"
        pos_hint: {'center_x':0.50, 'center_y':0.830}
        size_hint: 0.7, None
        height: "30dp"
        background_color: app.theme_cls.bg_normal
        multiline: True
    MDIconButton:
        icon: 'content-paste'
        theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.88, 'center_y':0.830}

        on_release:
            inputkey.text=Clipboard.paste()
     
	MDIconButton:
	    icon: 'content-copy'
		theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.95, 'center_y':0.830}

        on_release:
            Clipboard.copy(inputkey.text)
    
    MDIcon:
        icon: "key"
        pos_hint: {'center_x':0.09, 'center_y':0.830}
        color: "orange"
    




    MDTextField:
        id: inputmessage
        hint_text: "Enter your message"
        pos_hint: {'center_x':0.50, 'center_y':0.630}
        size_hint: 0.7, None
        height: "30dp"
        background_color: app.theme_cls.bg_normal
        multiline: True
    MDIconButton:
        icon: 'content-paste'
        theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.88, 'center_y':0.630}

        on_release:
            inputmessage.text=Clipboard.paste()
    MDIcon:
        icon: "message"
        pos_hint: {'center_x':0.09, 'center_y':0.630}
        color: "orange"





    MDTextField:
        id: encryptedmessage
        pos_hint: {'center_x':0.50, 'center_y':0.430}
        size_hint: 0.7, None
        height: "30dp"
        background_color: app.theme_cls.bg_normal
        multiline: True
    MDIconButton:
        icon: 'content-copy'
        theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.88, 'center_y':0.430}

        on_release:
            Clipboard.copy(encryptedmessage.text)
    MDIcon:
        icon: "code-braces"
        pos_hint: {'center_x':0.09, 'center_y':0.430}
        color: "orange"
    
    
<Tab3>
    
    MDFillRoundFlatButton
        text: "Decrypt Text"
        theme_text_color: "Custom"
        text_color: "black"
        on_press: root.decrypt()
        size_hint: .25, .04
        pos_hint:{'center_x':0.5, 'center_y' : 0.230}

    
    MDTextField:
        id: Dinputkey
        hint_text: "Enter your key"
        pos_hint: {'center_x':0.50, 'center_y':0.830}
        size_hint: 0.7, None
        height: "30dp"
        background_color: app.theme_cls.bg_normal
        multiline: True
    MDIconButton:
        icon: 'content-paste'
        theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.90, 'center_y':0.830}

        on_release:
            Dinputkey.text=Clipboard.paste()
    MDIcon:
        icon: "key"
        pos_hint: {'center_x':0.09, 'center_y':0.830}
        color: "orange"
    




    MDTextField:
        id: Dinputmessage
        hint_text: "Enter your Decrpted  message"
        pos_hint: {'center_x':0.50, 'center_y':0.630}
        size_hint: 0.7, None
        height: "30dp"
        background_color: app.theme_cls.bg_normal
        multiline: True
    MDIconButton:
        icon: 'content-paste'
        theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.90, 'center_y':0.630}

        on_release:
            Dinputmessage.text=Clipboard.paste()
    MDIcon:
        icon: "code-braces"
        pos_hint: {'center_x':0.09, 'center_y':0.630}
        color: "orange"





    MDTextField:
        id: orginalmessage
        pos_hint: {'center_x':0.50, 'center_y':0.430}
        size_hint: 0.7, None
        height: "30dp"
        background_color: app.theme_cls.bg_normal
        multiline: True
    MDIconButton:
        icon: 'content-copy'
        theme_icon_color: "Custom"
        icon_color: "grey"
        pos_hint: {'center_x':0.90, 'center_y':0.430}

        on_release:
            Clipboard.copy(orginalmessage.text)
    MDIcon:
        icon: "message"
        pos_hint: {'center_x':0.09, 'center_y':0.430}
        color: "orange"
'''


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    def generate(self):
                key=Fernet.generate_key()
                decodedkey=key.decode()
                result=self.ids.genkey.text=str(decodedkey)
                return result
    
class Tab2(MDFloatLayout, MDTabsBase):
    def encrypt(self):
        try:
            key=self.ids.inputkey.text
            encodedkey=key.encode()
            cipher=Fernet(encodedkey)
            message=self.ids.inputmessage.text
        except:
            pass
        try:
            encryptedmsg=cipher.encrypt(message.encode())
            return_msg=self.ids.encryptedmessage.text=encryptedmsg.decode()
            return return_msg
        except:
            return_msg=self.ids.encryptedmessage.text="Enter Key and Message"
            return return_msg

class Tab3(MDFloatLayout, MDTabsBase):
    def decrypt(self):
        try:
            key=self.ids.Dinputkey.text
            encoded_key=key.encode()
            cipher=Fernet(encoded_key)
            message=self.ids.Dinputmessage.text
        except:
             pass
        try:
            decrypted_message=cipher.decrypt(message.encode())
            return_msg=self.ids.orginalmessage.text=decrypted_message.decode()
            return return_msg
        except:
            return_msg=self.ids.orginalmessage.text='Invaild Key or Code'
            return return_msg
class Safetext(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_start(self):
            self.root.ids.tabs.add_widget(Tab(title="Generator    "))
            self.root.ids.tabs.add_widget(Tab2(title="Encrypt            "))
            self.root.ids.tabs.add_widget(Tab3(title="Decrypt      "))
            
            
    

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        instance_tab.ids.Tab = tab_text

        

Safetext().run()


'''MDLabel:
        text: "Your Key:"
        pos_hint:{'center_x':0.5, 'center_y' : 0.820}
        font_size: (self.height/12)*0.4'''