from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ImgConverter(App):
    def build(self):
        self.root_widget = BoxLayout(orientation='horizontal')

        # two sides of the root layout
        self.files_to_convert = self.create_file_list_widget()
        self.convert_button = self.create_convert_button()

        self.root_widget.add_widget(self.files_to_convert)
        self.root_widget.add_widget(self.convert_button)
        Window.bind(on_dropfile=self._on_file_drop)
        return self.root_widget

    ### Creates the file list widget (the left hand pane).
    def create_file_list_widget(self):
        files_to_convert = BoxLayout(orientation='vertical')

        file_list_label = Label(text='Drop HEIC files/folders here to be converted.')
        file_list_label.size_hint_y = 1

        file_list = BoxLayout(orientation='vertical')
        file_list.size_hint_y = 6

        files_to_convert.add_widget(file_list_label)
        files_to_convert.add_widget(file_list)

        return files_to_convert

    ### Creates the right hand pane, the button to convert files listed on the left.
    def create_convert_button(self):
        return Button(text='Convert!', font_size=45)

    def _on_file_drop(self, instance, file_path):
        print(file_path)
        new_file = Button(text=file_path.decode('UTF-8'))
        new_file.size_hint_y = None
        new_file.height = 21

        self.files_to_convert.children[0].add_widget(new_file)

if __name__ == '__main__':
    app = ImgConverter()
    app.run()
