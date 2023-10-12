import modules.scripts as scripts
import gradio as gr
import os

from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            javbus = gr.HTML(
                """<p>跑图无聊去看看最近有什么新片      <a href="https://www.javbus.com/" target="_blank">去JAVBUS看看吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>想找磁力下载片子      <a href="https://btsow.motorcycles/tags" target="_blank">去BTSOW找找吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>中文字幕在线观看      <a href="https://www.jav777.xyz/page/1" target="_blank">去JAV777瞅瞅吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>素人片资料汇总      <a href="http://sougouwiki.com/" target="_blank">去素人wiki瞅瞅吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>想看羞羞的漫画      <a href="https://jmcomic1.me/" target="_blank">去禁漫天堂瞅瞅吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>真人看腻了想看点二次元的      <a href="https://www.hacg.lv/wp/" target="_blank">去琉璃神社看里番吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>想知道一部片子值不值得看      <a href="http://javbest.net/" target="_blank">去看看预览图吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>中国首档的成人影片解说节目      <a href="https://sgptv.vip/" target="_blank">去水果派看点中文影评吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>不认识小姐姐只认识小哥哥      <a href="https://avdanyuwiki.com/" target="_blank">去根据小哥哥找片吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p>想看日本小姐姐不可描述的直播      <a href="https://live.fc2.com/adult/" target="_blank">去FC2瞅瞅吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p><a href="https://sleazyfork.org/zh-CN" target="_blank">去找点成人用户脚本让自己看片更方便吧</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p><a href="https://www.xvideos.com/" target="_blank">xvideos</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p><a href="https://cn.pornhub.com/" target="_blank">pornhub</a></p>"""
            )
        with gr.Row():
            btsow = gr.HTML(
                """<p><a href="https://aabook.xyz/m/index.php" target="_blank">想看小黄书，看看有没有喜欢的吧</a></p>"""
            )
            
        return [(ui_component, "找点乐子", "extension_template_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)
