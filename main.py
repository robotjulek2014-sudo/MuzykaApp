from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class MusicApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.sounds = {
            "Minecraft": SoundLoader.load("MINECRAFT.mp3"),
            "Lem": SoundLoader.load("lem.mp3"),
            "E": SoundLoader.load("e.mp3"),
            "Duck Tales": SoundLoader.load("Duck_Tales.mp3"),
            "Dram": SoundLoader.load("dram.mp3"),
        }

        for name in self.sounds:
            btn = Button(text=name)
            btn.bind(on_press=self.play_sound)
            layout.add_widget(btn)

        stop_btn = Button(text="STOP")
        stop_btn.bind(on_press=self.stop_all)
        layout.add_widget(stop_btn)

        return layout

    def play_sound(self, instance):
        sound = self.sounds.get(instance.text)
        if sound:
            sound.stop()
            sound.play()

    def stop_all(self, instance):
        for sound in self.sounds.values():
            if sound:
                sound.stop()


if __name__ == "__main__":
    MusicApp().run()