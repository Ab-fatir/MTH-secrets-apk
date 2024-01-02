from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDRoundFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import Screen

kv_string = '''
ScreenManager:
    MDScreen:
        name: "login_screen"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Login"
                font_style: 'H5'
                halign: 'center'

            MDTextField:
                id: username
                hint_text: "Username"
                icon_right: "account"

            MDTextField:
                id: password
                hint_text: "Password"
                icon_right: "eye-off"
                password: True

            MDRectangleFlatButton:
                text: "LOGIN"
                pos_hint: {'center_x': 0.5}
                on_press: app.login()
    MDScreen:
        name: "home_screen"

        Image:
            source: 'login_bg.jpg' 
            allow_stretch: True
            keep_ratio: False
        
        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.8
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDGridLayout:
                cols: 1
                padding: 40
                spacing: 30
                
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDLabel:
                        text: "MTH Secrets"
                        font_style: 'H5'
                        halign: 'center'

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Places"
                        on_press: app.root.current = "places_screen"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Rooms"
                        on_press: app.root.current = "pre_rooms"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Objects"
                        on_press: app.root.current = "pre_objects"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Secrets"
                        on_press: app.root.current = "pre_secrets"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Heartfelt Storage Guide"
                        on_press: app.root.current = "help"
                        size_hint_x: 0.5
        
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'
                    
                    MDFlatButton:
                        text: "Back"
                        on_release: app.root.current = "login_screen"
    MDScreen:
        name: "places_screen"

        Image:
            source: 'login_bg.jpg' 
            allow_stretch: True
            keep_ratio: False
        
        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.55}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDGridLayout:
                cols: 1
                padding: 40
                spacing: 20
                
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDLabel:
                        text: "Manage Places"
                        font_style: 'H5'
                        halign: 'center'

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Create Places"
                        on_press: app.root.current = "add_places"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Update Places"
                        on_press: app.root.current = "update_places"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Show Places"
                        on_press: app.root.current = "show_places"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Delete Places"
                        on_press: app.root.current = "delete_places"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75
        
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'
                    
                    MDFlatButton:
                        text: "Back"
                        on_release: app.root.current = "home_screen"   
    MDScreen:
        name: "add_places"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.48
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Add Places Here"
                font_style: 'H5'
                halign: 'center'

            MDTextField:
                id: add_place
                hint_text: "Enter Place Name"

            MDRectangleFlatButton:
                text: "Add Place"
                pos_hint: {'center_x': 0.5}
                on_press: app.add_place()
            
            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "places_screen"
    
    MDScreen:
        name: "update_places"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Enter Name of Place you want to update"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: index
                hint_text: "Enter Index to update"

            MDTextField:
                id: update_place
                hint_text: "Enter Place New Name"

            MDRectangleFlatButton:
                text: "Update Place"
                pos_hint: {'center_x': 0.5}
                on_press: app.update_place()
            
            MDRectangleFlatButton:
                text: "Show Places"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_places"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "places_screen"

    MDScreen:
        name: "show_places"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Click on The Botton to see Places"
                font_style: 'H5'
                halign: 'center'

            MDList:
                id: place_list

            MDRectangleFlatButton:
                text: "Show Places"
                size_hint: 0.8, 0.5
                pos_hint: {'center_x': 0.5}
                on_press: app.show_place()

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1}
                on_press: app.root.current = "places_screen"
    MDScreen:
        name: "delete_places"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Enter Name of Place you want to delete"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: delete_index
                hint_text: "Enter Index to delete"

            MDRectangleFlatButton:
                text: "delete Place"
                pos_hint: {'center_x': 0.5}
                on_press: app.delete_place()
            
            MDRectangleFlatButton:
                text: "Show Places"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_places"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "places_screen"
    MDScreen:
        name: "rooms_screen"

        Image:
            source: 'login_bg.jpg' 
            allow_stretch: True
            keep_ratio: False
        
        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.55}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDGridLayout:
                cols: 1
                padding: 40
                spacing: 20
                
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDLabel:
                        text: "Manage Rooms"
                        font_style: 'H5'
                        halign: 'center'

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Create Rooms"
                        on_press: app.root.current = "add_rooms"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Update Rooms"
                        on_press: app.root.current = "update_rooms"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Show Rooms"
                        on_press: app.root.current = "show_rooms"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Delete Rooms"
                        on_press: app.root.current = "delete_rooms"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75
        
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'
                    
                    MDFlatButton:
                        text: "Back"
                        on_release: app.root.current = "home_screen"
    MDScreen:
        name: "pre_rooms"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.48
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Enter Place in which you want to create room"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: room_check
                hint_text: "Enter Place Name"

            MDRectangleFlatButton:
                text: "Check Place"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "rooms_screen" if app.find_place_by_name() else app.false_condition()
            
            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "home_screen"
    MDScreen:
        name: "add_rooms"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.48
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Add Rooms Here"
                font_style: 'H5'
                halign: 'center'

            MDTextField:
                id: add_room
                hint_text: "Enter Room Name"

            MDRectangleFlatButton:
                text: "Add Room"
                pos_hint: {'center_x': 0.5}
                on_press: app.add_room()
            
            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "rooms_screen"
    
    MDScreen:
        name: "update_rooms"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Enter Name of Rooms you want to update"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: index_room
                hint_text: "Enter Index to update"

            MDTextField:
                id: update_room
                hint_text: "Enter Room New Name"

            MDRectangleFlatButton:
                text: "Update Room"
                pos_hint: {'center_x': 0.5}
                on_press: app.update_room()
            
            MDRectangleFlatButton:
                text: "Show Rooms"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_rooms"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "rooms_screen"

    MDScreen:
        name: "show_rooms"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Click on The Botton to see Rooms"
                halign: 'center'

            MDList:
                id: place_list

            MDRectangleFlatButton:
                text: "Show Rooms"
                size_hint: 0.8, 0.5
                pos_hint: {'center_x': 0.5}
                on_press: app.show_room()

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1}
                on_press: app.root.current = "rooms_screen"
    MDScreen:
        name: "delete_rooms"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Enter Index of Room you want to delete"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: delete_index_room
                hint_text: "Enter Index to delete"

            MDRectangleFlatButton:
                text: "delete Room"
                pos_hint: {'center_x': 0.5}
                on_press: app.delete_room()
            
            MDRectangleFlatButton:
                text: "Show Rooms"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_rooms"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "rooms_screen"
    MDScreen:
        name: "pre_objects"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.6
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Enter Place and room in which you want to create object"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: object_check1
                hint_text: "Enter Place Name"
            
            MDTextField:
                id: object_check2
                hint_text: "Enter Room Name"

            MDRectangleFlatButton:
                text: "Check Place & Room"
                pos_hint: {'center_x': 0.5}
                on_press:
                    app.root.current = "objects_screen" if app.find_place_object() and app.find_room_object() else app.false_object_condition()


            
            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "home_screen"
    MDScreen:
        name: "objects_screen"

        Image:
            source: 'login_bg.jpg' 
            allow_stretch: True
            keep_ratio: False
        
        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.55}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDGridLayout:
                cols: 1
                padding: 40
                spacing: 20
                
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDLabel:
                        text: "Manage Objects"
                        font_style: 'H5'
                        halign: 'center'

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Create Objects"
                        on_press: app.root.current = "add_objects"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Update Objects"
                        on_press: app.root.current = "update_objects"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Show Objects"
                        on_press: app.root.current = "show_objects"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Delete Objects"
                        on_press: app.root.current = "delete_objects"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75
        
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'
                    
                    MDFlatButton:
                        text: "Back"
                        on_release: app.root.current = "home_screen"
    MDScreen:
        name: "add_objects"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.48
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Add Objects Here"
                font_style: 'H5'
                halign: 'center'

            MDTextField:
                id: add_object
                hint_text: "Enter Object Name"

            MDRectangleFlatButton:
                text: "Add Object"
                pos_hint: {'center_x': 0.5}
                on_press: app.add_object()
            
            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "objects_screen"
    
    MDScreen:
        name: "show_objects"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Click on The Botton to see Objects"
                halign: 'center'

            MDList:
                id: object_list

            MDRectangleFlatButton:
                text: "Show Objects"
                size_hint: 0.8, 0.5
                pos_hint: {'center_x': 0.5}
                on_press: app.show_object()

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1}
                on_press: app.root.current = "objects_screen"
    MDScreen:
        name: "update_objects"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Enter Name of Object you want to update"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: index_object
                hint_text: "Enter Index to update"

            MDTextField:
                id: update_object
                hint_text: "Enter Object New Name"

            MDRectangleFlatButton:
                text: "Update Object"
                pos_hint: {'center_x': 0.5}
                on_press: app.update_object()
            
            MDRectangleFlatButton:
                text: "Show Objects"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_objects"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "objects_screen"
    MDScreen:
        name: "help"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.9
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "MTH Secrets"
                font_style: 'H5'
                bold: True
                halign: 'center'

            MDLabel:
                text: "Heartfelt Storage Guide"
                font_style: 'H5'
                halign: 'center'
                
            MDLabel:
                text: "Introduction:"
                font_style: 'H6'
                halign: 'center'
                
            MDLabel:
                text: "Heartfelt Storage: Safely store and manage cherished secrets tied to places, rooms, and objects."
                font_style: 'Body1'

            MDLabel:
                text: "Sign-Up/Login:"
                font_style: 'H6'
                halign: 'center'

            MDLabel:
                text: "Upon opening the app, create an account or log in with your credentials to access the features."
                font_style: 'Body1'

            MDLabel:
                text: "Exploring the Interface:"
                font_style: 'H6'
                halign: 'center'

            MDLabel:
                text: "The app interface comprises:"
                font_style: 'Body1'
                halign: 'center'
                
            MDLabel:
                text: "Main Menu:"
                font_style: 'H6'
                halign: 'center'

            MDLabel:
                text: "Navigate through options to manage places, rooms, objects, and secrets." 
                font_style: 'Body1'      

            MDLabel:
                text: "Function & Features"
                font_style: 'H6'
                halign: 'center'

            MDLabel:
                text: "Create , Update , Read and Delete places, rooms, objects, and secrets." 
                font_style: 'Body1'      

            MDRectangleFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "home_screen"
    MDScreen:
        name: "delete_objects"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Enter Index of Objects you want to delete"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: delete_index_object
                hint_text: "Enter Index to delete"

            MDRectangleFlatButton:
                text: "delete Object"
                pos_hint: {'center_x': 0.5}
                on_press: app.delete_object()
            
            MDRectangleFlatButton:
                text: "Show Objects"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_objects"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "objects_screen"
    MDScreen:
        name: "pre_secrets"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.8
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Enter Place,room and object in which you want to store Secret"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: secret_check1
                hint_text: "Enter Place Name"
            
            MDTextField:
                id: secret_check2
                hint_text: "Enter Room Name"
            
            MDTextField:
                id: secret_check3
                hint_text: "Enter Object Name"

            MDRectangleFlatButton:
                text: "Check Place , Room & Object"
                pos_hint: {'center_x': 0.5}
                on_press:
                    app.root.current = "secrets_screen" if app.find_place_secret() and app.find_room_secret() and app.find_object_secret() else app.false_secret_condition()


            
            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "home_screen"
    MDScreen:
        name: "secrets_screen"

        Image:
            source: 'login_bg.jpg' 
            allow_stretch: True
            keep_ratio: False
        
        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.55}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDGridLayout:
                cols: 1
                padding: 40
                spacing: 20
                
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDLabel:
                        text: "Manage Secrets"
                        font_style: 'H5'
                        halign: 'center'

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Create Secrets"
                        on_press: app.root.current = "add_secrets"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Update Secrets"
                        on_press: app.root.current = "update_secrets"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Show Secrets"
                        on_press: app.root.current = "show_secrets"
                        theme_text_color: "Custom"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75

                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'

                    MDRoundFlatButton:
                        text: "Delete secrets"
                        on_press: app.root.current = "delete_secrets"
                        text_color: (1, 1, 1)
                        md_bg_color: (0, 0.27450980392156865, 0.6705882352941176)
                        size_hint_x: 0.75
        
                MDBoxLayout:
                    size_hint_y: None
                    height: '50dp'
                    
                    MDFlatButton:
                        text: "Back"
                        on_release: app.root.current = "home_screen"
    MDScreen:
        name: "add_secrets"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.48
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Add Secrets Here"
                font_style: 'H5'
                halign: 'center'

            MDTextField:
                id: add_secret
                hint_text: "Enter Secret"

            MDRectangleFlatButton:
                text: "Add Secret"
                pos_hint: {'center_x': 0.5}
                on_press: app.add_secret()
            
            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "secrets_screen"
    MDScreen:
        name: "update_secrets"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.7
            padding: 25
            spacing: 25
            orientation: 'vertical'

            MDLabel:
                text: "Enter Secret you want to update"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: index_secret
                hint_text: "Enter Index to update"

            MDTextField:
                id: update_secret
                hint_text: "Enter New Secret"

            MDRectangleFlatButton:
                text: "Update Secret"
                pos_hint: {'center_x': 0.5}
                on_press: app.update_secret()
            
            MDRectangleFlatButton:
                text: "Show Secrets"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_secrets"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "secrets_screen"
    MDScreen:
        name: "show_secrets"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Click on The Botton to see Secrets"
                halign: 'center'

            MDList:
                id: secret_list

            MDRectangleFlatButton:
                text: "Show Secrets"
                size_hint: 0.8, 0.5
                pos_hint: {'center_x': 0.5}
                on_press: app.show_secret()

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1}
                on_press: app.root.current = "secrets_screen"
    MDScreen:
        name: "delete_secrets"

        Image:
            source: 'login_bg.jpg'
            allow_stretch: True
            keep_ratio: False

        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.9, 0.5
            padding: 25
            spacing: 15
            orientation: 'vertical'

            MDLabel:
                text: "Enter Index of Secret you want to delete"
                font_style: 'H6'
                halign: 'center'

            MDTextField:
                id: delete_index_secret
                hint_text: "Enter Index to delete"

            MDRectangleFlatButton:
                text: "delete Secret"
                pos_hint: {'center_x': 0.5}
                on_press: app.delete_secret()
            
            MDRectangleFlatButton:
                text: "Show Secrets"
                pos_hint: {'center_x': 0.5}
                on_press: app.root.current = "show_secrets"

            MDFlatButton:
                text: "Back"
                pos_hint: {'center_x': 0.1, 'center_y': 0}
                on_press: app.root.current = "secrets_screen"
                               
'''

class MTH_Secrets(MDApp):
    
    def build(self):
        self.kv_string = Builder.load_string(kv_string)
        self.theme_cls.primary_palette = "BlueGray"
        
        return Builder.load_string(kv_string)  
    def find_place_secret(self):
        object_place_name = self.root.ids.secret_check1.text
        for place in places:
                if place["name"] == object_place_name:
                    return place
                return None
    def find_place_object(self):
        object_place_name = self.root.ids.object_check1.text
        for place in places:
                if place["name"] == object_place_name:
                    return place
                return None  
    def find_room_object(self):
        object_place_name = self.root.ids.object_check1.text
        for place in places:
                if place["name"] == object_place_name:
                     object_room_name = self.root.ids.object_check2.text   
        rooms = place["rooms"]
        for room in rooms:
                if room["name"] == object_room_name:
                    return room
                return None
    def find_room_secret(self):
        object_place_name = self.root.ids.secret_check1.text
        for place in places:
                if place["name"] == object_place_name:
                     object_room_name = self.root.ids.secret_check2.text   
        rooms = place["rooms"]
        for room in rooms:
                if room["name"] == object_room_name:
                    return room
                return None
    def find_object_secret(self):
        object_place_name = self.root.ids.secret_check1.text
        for place in places:
                if place["name"] == object_place_name:
                     object_room_name = self.root.ids.secret_check2.text   
        rooms = place["rooms"]
        for room in rooms:
                if room["name"] == object_room_name:
                    secret_object_name = self.root.ids.secret_check3.text
        secret_object_name = self.root.ids.secret_check3.text
        objects = room["objects"]
        for object in objects:
                if object["name"] == secret_object_name:
                    return object
                return None
    def find_place_by_name(self):           
            place_name = self.root.ids.room_check.text
            for place in places:
                if place["name"] == place_name:
                    return place
                return None      
    def false_secret_condition(self):
            self.dialog = MDDialog(
                title="Error",
                text= "Please enter a Valid place , room and object name",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def false_object_condition(self):
            self.dialog = MDDialog(
                title="Error",
                text= "Please enter a Valid place and room name",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def false_condition(self):
            self.dialog = MDDialog(
                title="Error",
                text= "Please enter a Valid place name",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def add_secret(self):
        def find_object_secret(self):
            object_place_name = self.root.ids.secret_check1.text
            for place in places:
                    if place["name"] == object_place_name:
                        object_room_name = self.root.ids.secret_check2.text   
            rooms = place["rooms"]
            for room in rooms:
                    if room["name"] == object_room_name:
                        secret_object_name = self.root.ids.secret_check3.text
            secret_object_name = self.root.ids.secret_check3.text
            objects = room["objects"]
            for object in objects:
                    if object["name"] == secret_object_name:
                        return object
                    return None
        secrets = find_object_secret(self)
        secret_name = self.root.ids.add_secret.text
        secrets["secrets"].append(secret_name)
        self.dialog = MDDialog(
            title="Congratulations",
            text= f"'{secret_name}' has been added to the Secrets.",
            buttons=[
                MDFlatButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def add_object(self):
        def find_room_object(self):
            object_place_name = self.root.ids.object_check1.text
            for place in places:
                    if place["name"] == object_place_name:
                        object_room_name = self.root.ids.object_check2.text   
            rooms = place["rooms"]
            for room in rooms:
                    if room["name"] == object_room_name:
                        return room
                    return None
        objects = find_room_object(self)
        object_name = self.root.ids.add_object.text
        objects["objects"].append({"name": object_name, "secrets": []})
        self.dialog = MDDialog(
            title="Congratulations",
            text= f"'{object_name}' has been added to the objects.",
            buttons=[
                MDFlatButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def add_room(self):
        def find_place_by_name():
                    place_name = self.root.ids.room_check.text
                    for place in places:
                        if place["name"] == place_name:
                            return place
                    return None
        place = find_place_by_name()
        rooms = place
        room_name = self.root.ids.add_room.text
        rooms["rooms"].append({"name": room_name, "objects": []})
        self.dialog = MDDialog(
            title="Congratulations",
            text= f"'{room_name}' has been added to the '{place}'",
            buttons=[
                MDFlatButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def add_place(self):
        place_name = self.root.ids.add_place.text
        places.append({"name": place_name, "rooms": []})
        self.dialog = MDDialog(
            title="Congratulations",
            text= place_name+" has been added to the places",
            buttons=[
                MDFlatButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def update_secret(self):
        def find_object_secret(self):
            object_place_name = self.root.ids.secret_check1.text
            for place in places:
                    if place["name"] == object_place_name:
                        object_room_name = self.root.ids.secret_check2.text   
            rooms = place["rooms"]
            for room in rooms:
                    if room["name"] == object_room_name:
                        secret_object_name = self.root.ids.secret_check3.text
            secret_object_name = self.root.ids.secret_check3.text
            objects = room["objects"]
            for object in objects:
                    if object["name"] == secret_object_name:
                        return object
                    return None
        objects = find_object_secret(self)
        secrets = objects["secrets"]
        new_secret_name = self.root.ids.update_secret.text
        index_secret = self.root.ids.index_secret.text   
        if not secrets:
                    self.dialog = MDDialog(
                    title="No Secrets Found",
                    text= "The list is empty. Add Secrets first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(index_secret)-1) < len(secrets):
            secrets[(int(index_secret)-1)] = new_secret_name
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= "Secret updated successfully.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def update_object(self):
        def find_room_object(self):
                object_place_name = self.root.ids.object_check1.text
                for place in places:
                            if place["name"] == object_place_name:
                                object_room_name = self.root.ids.object_check2.text   
                rooms = place["rooms"]
                for room in rooms:
                            if room["name"] == object_room_name:
                                return room
                            return None
        rooms = find_room_object(self)
        objects = rooms["objects"]
        new_object_name = self.root.ids.update_object.text
        index_object = self.root.ids.index_object.text   
        if not objects:
                    self.dialog = MDDialog(
                    title="No Objects Found",
                    text= "The list is empty. Add Objects first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(index_object)-1) < len(objects):
            objects[(int(index_object)-1)]["name"] = new_object_name
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= "Object updated successfully.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def update_room(self):
        def find_place_by_name():
                    place_name = self.root.ids.room_check.text
                    for place in places:
                        if place["name"] == place_name:
                            return place
                    return None
        place = find_place_by_name()
        rooms = place["rooms"]
        new_room_name = self.root.ids.update_room.text
        index_room = self.root.ids.index_room.text   
        if not rooms:
                    self.dialog = MDDialog(
                    title="No Rooms Found",
                    text= "The list is empty. Add Rooms first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(index_room)-1) < len(places):
            rooms[(int(index_room)-1)]["name"] = new_room_name
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= "Room updated successfully.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def update_place(self):
        new_name = self.root.ids.update_place.text
        index = self.root.ids.index.text   
        if not places:
                    self.dialog = MDDialog(
                    title="No Places Found",
                    text= "The list is empty. Add places first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(index)-1) < len(places):
            places[(int(index)-1)]["name"] = new_name
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= "place updated successfully.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def show_secret(self):
                def find_object_secret(self):
                    object_place_name = self.root.ids.secret_check1.text
                    for place in places:
                            if place["name"] == object_place_name:
                                object_room_name = self.root.ids.secret_check2.text   
                    rooms = place["rooms"]
                    for room in rooms:
                            if room["name"] == object_room_name:
                                secret_object_name = self.root.ids.secret_check3.text
                    secret_object_name = self.root.ids.secret_check3.text
                    objects = room["objects"]
                    for object in objects:
                            if object["name"] == secret_object_name:
                                return object
                            return None
                objects = find_object_secret(self)
                secrets = objects["secrets"]
                secret_names = ""
                for index, secret in enumerate(secrets):
                    secret_names += f"{index + 1}. {secret}\n"
                self.dialog = MDDialog(
                        title="Congratulations",
                        text=f"The following Secrets have been added:\n{secret_names}",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
                self.dialog.open()        
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def show_object(self):
                def find_room_object(self):
                    object_place_name = self.root.ids.object_check1.text
                    for place in places:
                            if place["name"] == object_place_name:
                                object_room_name = self.root.ids.object_check2.text   
                    rooms = place["rooms"]
                    for room in rooms:
                            if room["name"] == object_room_name:
                                return room
                            return None
                rooms = find_room_object(self)
                objects = rooms["objects"]
                object_names = ""
                for index, object in enumerate(objects):
                    object_names += f"{index + 1}. {object['name']}\n"
                self.dialog = MDDialog(
                        title="Congratulations",
                        text=f"The following Objects have been added:\n{object_names}",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
                self.dialog.open()        
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def show_room(self):
                def find_place_by_name():
                    place_name = self.root.ids.room_check.text
                    for place in places:
                        if place["name"] == place_name:
                            return place
                    return None
                place = find_place_by_name()
                rooms = place['rooms']
                room_names = ""
                for index, room in enumerate(rooms):
                    room_names += f"{index + 1}. {room['name']}\n"
                self.dialog = MDDialog(
                        title="Congratulations",
                        text=f"The following rooms have been added:\n{room_names}",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
                self.dialog.open()            
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def show_place(self):
        place_names = ""
        for index, place in enumerate(places):
            place_names += f"{index + 1}. {place['name']}\n"
        self.dialog = MDDialog(
                title="Congratulations",
                text=f"The following places have been added:\n{place_names}",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
        self.dialog.open()             
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def delete_secret(self):
        def find_object_secret(self):
            object_place_name = self.root.ids.secret_check1.text
            for place in places:
                    if place["name"] == object_place_name:
                        object_room_name = self.root.ids.secret_check2.text   
            rooms = place["rooms"]
            for room in rooms:
                    if room["name"] == object_room_name:
                        secret_object_name = self.root.ids.secret_check3.text
            secret_object_name = self.root.ids.secret_check3.text
            objects = room["objects"]
            for object in objects:
                    if object["name"] == secret_object_name:
                        return object
                    return None
        objects = find_object_secret(self)
        secrets = objects["secrets"]
        delete_index_secret = self.root.ids.delete_index_secret.text
        if not secrets:
                    self.dialog = MDDialog(
                    title="No Secrets Found",
                    text= "The list is empty. Add Secrets first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(delete_index_secret)-1) < len(objects):
            deleted_secret = secrets.pop((int(delete_index_secret)-1))
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= f"'{deleted_secret}' has been deleted.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Please enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def delete_object(self):
        def find_room_object(self):
                object_place_name = self.root.ids.object_check1.text
                for place in places:
                            if place["name"] == object_place_name:
                                object_room_name = self.root.ids.object_check2.text   
                rooms = place["rooms"]
                for room in rooms:
                            if room["name"] == object_room_name:
                                return room
                            return None
        rooms = find_room_object(self)
        objects = rooms["objects"]
        delete_index_object = self.root.ids.delete_index_object.text
           
        if not rooms:
                    self.dialog = MDDialog(
                    title="No Objects Found",
                    text= "The list is empty. Add Objects first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(delete_index_object)-1) < len(objects):
            deleted_object = objects.pop((int(delete_index_object)-1))
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= f"'{deleted_object['name']}' has been deleted.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Please enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def delete_room(self):
        def find_place_by_name():
                    place_name = self.root.ids.room_check.text
                    for place in places:
                        if place["name"] == place_name:
                            return place
                    return None
        place = find_place_by_name()
        rooms = place["rooms"]
        delete_index_room = self.root.ids.delete_index_room.text
           
        if not rooms:
                    self.dialog = MDDialog(
                    title="No Rooms Found",
                    text= "The list is empty. Add Rooms first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(delete_index_room)-1) < len(rooms):
            deleted_room = rooms.pop((int(delete_index_room)-1))
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= f"'{deleted_room['name']}' has been deleted.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Please enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def delete_place(self):
        delete_index = self.root.ids.delete_index.text
           
        if not places:
                    self.dialog = MDDialog(
                    title="No Places Found",
                    text= "The list is empty. Add places first.",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.close_dialog
                        )
                    ],
                )
                    self.dialog.open()
                    return

        if 0 <= (int(delete_index)-1) < len(places):
            deleted_item = places.pop((int(delete_index)-1))
            self.dialog = MDDialog(
                        title="Congratulations",
                        text= f"'{deleted_item['name']}' has been deleted.",
                        buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    )
                ],
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                        title="Please enter a valid Index",
                        text= "Invalid Index",
                        buttons=[
                            MDFlatButton(
                                text="OK",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.close_dialog
                            )
                        ],
                    )
            self.dialog.open()
    def close_dialog(self, instance):
        self.dialog.dismiss()
    def login(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text

        users = [
            {"username": "Muhammad_Tallat", "password": "Nothing0921@"},
            {"username": "Mehatb_Saeec", "password": "Mehtab123@"},
            {"username": "Syed_Zurriat_Hussain", "password": "Zurriat123@"},
        ]

        if any(user["username"] == username and user["password"] == password for user in users):
            self.root.current = "home_screen"
        else:
            self.show_error_dialog("Invalid username or password")
    def show_error_dialog(self, message):
        self.dialog = MDDialog(
            title="Login Error",
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                )
            ],
        )
        self.dialog.open()
def close_dialog(self, instance):
        self.dialog.dismiss()

def new_box(self):
    add_places_screen = self.root.get_screen("add_places")
    add_place_text_field = add_places_screen.ids.add_place
    place_name = add_place_text_field.text   
places = []
if __name__ == "__main__":
    MTH_Secrets().run()
