from dash import callback_context as ctx
from dash_mantine_components import TextInput


class InputField:
    def __init__(self, label, placeholder, icon, input_type="text"):
        self.label = label
        self.placeholder = placeholder
        self.icon = icon
        self.input_type = input_type

    def get_input(self, id):
        return TextInput(
            label=self.label,
            placeholder=self.placeholder,
            icon=self.icon,
            id=id,
            type=self.input_type,
            error=""
        )
