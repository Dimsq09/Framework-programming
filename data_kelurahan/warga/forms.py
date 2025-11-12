# forms.py

from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        # ↓↓↓ UBAH DI SINI
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
        widgets = {
            'nik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NIK'}),
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama lengkap'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Masukkan alamat'}),
            # ↓↓↓ UBAH DI SINI JUGA
            'no_telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nomor telepon'}),
        }

# Class PengaduanForm Anda sudah terlihat benar, tidak perlu diubah.
class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['pelapor', 'judul', 'deskripsi']
        
        widgets = {
            'pelapor': forms.Select(attrs={'class': 'form-select'}),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pelapor'].queryset = Warga.objects.order_by('nama_lengkap')