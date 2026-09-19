from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput

from main.models import Achievements, Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi pengalaman",
            "category": "kategori pengalaman yang diperoleh",
            "thumbnail": "URL gambar pengalaman",
            "started_at": "Waktu mulai pengalaman",
            "ended_at": "Waktu akhir pengalaman",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Judul pengalaman",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "certification, competition, award, scholarship, publication, other",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
            "ended_at": DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
        }

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