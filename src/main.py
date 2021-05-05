from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from convert import heics_to_jpg

class ImgConverter(App):
    def build(self):
        self.root = BoxLayout(orientation='horizontal')

        # two sides of the root layout
        self.files_to_convert = self.create_file_list_widget()
        self.convert_button = self.create_convert_button()

        self.root.add_widget(self.files_to_convert)
        self.root.add_widget(self.convert_button)
        Window.bind(on_dropfile=self._on_file_drop)
        Window.size = (700, 350)
        return self.root

    ### Creates the file list widget (the left hand pane).
    def create_file_list_widget(self):
        files_to_convert = BoxLayout(orientation='vertical', size_hint_x=3)

        file_list_label = Label(text='Drop HEIC files/folders here to be converted.\nClick to remove files.')
        file_list_label.size_hint_y = 1

        file_list = BoxLayout(orientation='vertical')
        file_list.size_hint_y = 5

        files_to_convert.add_widget(file_list_label)
        files_to_convert.add_widget(file_list)
        files_to_convert.path_list = set()

        return files_to_convert

    ### Creates the right hand pane, the button to convert files listed on the left.
    def create_convert_button(self):
        convert_button = Button(text='Convert!', font_size=35, size_hint_x=1)
        convert_button.bind(on_release=convert_heics)
        return convert_button

    ### Adds a file path to a list on the left when a file is dropped.
    def _on_file_drop(self, instance, file_path):
        p = file_path.decode('UTF-8')

        if p not in self.files_to_convert.path_list:
            new_file = Button(text=p)
            new_file.size_hint_y = None
            new_file.height = 21
            new_file.bind(on_release=self._remove_file_from_list)

            self.files_to_convert.children[0].add_widget(new_file)
            self.files_to_convert.path_list.add(p)
            print(f"{p} added")
        else:
            print(f"{p} already in path list")

    ### Removes a file path from the left hand list when it is clicked.
    def _remove_file_from_list(self, instance):
        self.files_to_convert.children[0].remove_widget(instance)
        self.files_to_convert.path_list.remove(instance.text)
        print(f"{instance.text} removed")

if __name__ == '__main__':
    app = ImgConverter()
    app.run()
