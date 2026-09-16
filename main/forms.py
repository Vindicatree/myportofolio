from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Achievements

class AchievementsForm(ModelForm):
    class Meta:
        model = Achievements
        fields = [
            "title",
            "description",
            "category",
            "issuer",
            "thumbnail",
        ]

        labels = {
            "title": "Nama penghargaan",
            "description": "Deskripsi penghargaan",
            "category": "kategori penghargaan yang diperoleh",
            "issuer": "Pemberi penghargaan",
            "thumbnail": "URL Gambar penghargaan",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Judul Penghargaan",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan penghargaanmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "certification, competition, award, scholarship, publication, other",
                }
            ),
            "issuer": TextInput(
                attrs={
                    "placeholder": "Pemberi penghargaan",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }