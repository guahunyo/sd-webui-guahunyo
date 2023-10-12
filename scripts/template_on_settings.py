import modules.scripts as scripts
import gradio as gr
import os

from modules import shared
from modules import script_callbacks

def on_ui_settings():
    section = ('guahunyo', "找点乐子")
    shared.opts.add_option(
        "option1",
        shared.OptionInfo(
            False,
            "还没想好要设置啥",
            gr.Checkbox,
            {"interactive": True},
            section=section)
    )

script_callbacks.on_ui_settings(on_ui_settings)
