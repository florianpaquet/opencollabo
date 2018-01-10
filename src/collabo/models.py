import os
import uuid
import subprocess
import tempfile

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):

    name = models.CharField(
        _("name"),
        max_length=128)

    def __str__(self):
        return self.name


class Sentence(models.Model):

    text = models.TextField(
        _("text"))

    def __str__(self):
        return self.text

    def render(self, person):
        return self.text.format(person=person)

    def say(self, person):
        text = self.render(person)

        with tempfile.TemporaryDirectory(prefix='collabo-') as tmp_dir:
            wav_path = os.path.join(tmp_dir, 'collabo.wav')
            subprocess.call(
                'pico2wave -w {wav} -l {tts_lang} "{text}" && aplay {wav}'.format(
                    wav=wav_path, tts_lang='fr-FR', text=text),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
