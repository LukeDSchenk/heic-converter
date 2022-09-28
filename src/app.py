import logging

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from convert import heics_to_jpg

logger = logging.getLogger(__name__)


class ImgConverter(App):
    """
    Class representing the image converter application.
    """

    def build(self):
        """
        Build the Kivy app from its components.
        """

        self.root = BoxLayout(orientation="horizontal")

        # two sides of the root layout
        self.files_to_convert = self.create_file_list_widget()
        self.convert_button = self.create_convert_button()

        self.root.add_widget(self.files_to_convert)
        self.root.add_widget(self.convert_button)
        Window.bind(on_dropfile=self._on_file_drop)
        Window.size = (700, 350)
        return self.root

    def create_file_list_widget(self):
        """
        Creates the file list widget (the left hand pane).
        """

        files_to_convert = BoxLayout(orientation="vertical", size_hint_x=3)

        file_list_label = Label(
            text="Drop HEIC files/folders here to convert them to JPEGs.\nClick files to remove them from the list."
        )
        file_list_label.size_hint_y = 1

        file_list = BoxLayout(orientation="vertical")
        file_list.size_hint_y = 5

        files_to_convert.add_widget(file_list_label)
        files_to_convert.add_widget(file_list)
        files_to_convert.path_set = set()

        return files_to_convert

    def create_convert_button(self):
        """
        Creates the right hand pane, the button to convert files listed on the left.
        """

        convert_button = Button(text="Convert!", font_size=35, size_hint_x=1)
        convert_button.bind(on_release=self._convert_release)
        return convert_button

    def _convert_release(self, instance):
        heics_to_jpg(list(self.files_to_convert.path_set))

    def _on_file_drop(self, instance, file_path):
        """
        Adds a file path to a list on the left when a file is dropped.

        :param _ instance: # TODO
        :param str file_path:
        """

        p = file_path.decode("UTF-8")

        if p not in self.files_to_convert.path_set:
            new_file = Button(text=p)
            new_file.size_hint_y = None
            new_file.height = 21
            new_file.bind(on_release=self._remove_file_from_list)

            self.files_to_convert.children[0].add_widget(new_file)
            self.files_to_convert.path_set.add(p)
            logger.debug(f"{p} added")
        else:
            logger.debug(f"{p} already in path list")

    def _remove_file_from_list(self, instance):
        """
        Removes a file path from the left hand list when it is clicked.
        """

        self.files_to_convert.children[0].remove_widget(instance)
        self.files_to_convert.path_set.remove(instance.text)
        logger.debug(f"{instance.text} removed")
