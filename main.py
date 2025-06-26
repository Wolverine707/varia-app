from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import requests

KV = '''
<RootWidget>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    TextInput:
        id: query_input
        hint_text: 'Enter your query…'
        size_hint_y: None
        height: '50dp'
        multiline: False
        on_text_validate: root.on_search()

    Button:
        text: 'Search'
        size_hint_y: None
        height: '50dp'
        on_press: root.on_search()

    ScrollView:
        Label:
            id: results
            text: ''
            markup: True
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
'''

class RootWidget(BoxLayout):
    def on_search(self):
        q = self.ids.query_input.text.strip()
        if not q:
            return
        summary = self.get_summary(q)
        links   = self.get_links(q)

        parts = ["[b]🧠 Summary[/b]\\n" + summary,
                 "[b]🔗 Links[/b]"] + links
        self.ids.results.text = "\\n\\n".join(parts)

    @staticmethod
    def get_summary(q):
        try:
            r = requests.get("https://api.duckduckgo.com/",
                             params={"q": q, "format": "json",
                                     "no_html": 1, "skip_disambig": 1},
                             timeout=6)
            return r.json().get("Abstract") or "No summary found."
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def get_links(q):
        url = "https://lite.duckduckgo.com/lite/?q=" + q.replace(" ", "+")
        return [f"Search results → [ref={url}][color=44aaff]{url}[/color][/ref]"]

class VariaApp(App):
    def build(self):
        Builder.load_string(KV)   # load kv rule
        return RootWidget()       # return an *instance* so Kivy has a root

if __name__ == '__main__':
    VariaApp().run()