"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/

    https://cloud.google.com/text-to-speech
"""
import os
from datetime import datetime

from google.cloud import texttospeech


class VoiceGenerator:
    def __init__(self, google_application_credentials="C:\\workspace\\bbbig-TTS-keys.json",
                 save_home="C:\\Users\\herme\\Desktop\\recode\\",
                 audio_encoding=texttospeech.AudioEncoding.MP3,
                 pitch=0,
                 speaking_rate=1.0,
                 language_code="ko-KR",
                 name="ko-KR-Wavenet-D",
                 ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_application_credentials
        self.save_home = save_home

        # Instantiates a client
        self.client = texttospeech.TextToSpeechClient()

        # Voice parameters and audio file type
        # Select the type of audio file you want returned
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=audio_encoding,
            pitch=pitch,
            speaking_rate=speaking_rate
        )

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        self.voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            name=name,
            ssml_gender=ssml_gender
        )

    def generate(self, text="", filename=None):
        # Perform the text-to-speech request on the text input with the selected
        # The response's audio_content is binary.
        if filename is None:
            now = datetime.now()  # current date and time
            filename = now.strftime("[VOICE] %Y-%m-%d %H%M%S")

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )

        path = self.save_home + "{name}.mp3".format(name=filename)
        with open(path, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "{path}"'.format(path=path))


if __name__ == '__main__':
    filename = "[BBBig] Greetings"
    text = intro_message = """
        안녕하세요. 비비빅TV에 비기입니다.
    """
    voice_generator = VoiceGenerator()
    voice_generator.generate(text=text, filename=filename)
