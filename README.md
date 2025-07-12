# S.U.N.D.A *(Smart Utility Navigational Directional Assistance)*


## Deskripsi Proyek

Proyek **Smart Helmet AI** adalah sistem helm pintar yang mengintegrasikan berbagai teknologi canggih seperti AR HUD, deteksi blind spot berbasis LiDAR, asisten suara AI, navigasi GPS, rekaman dashcam, dan konektivitas smartphone (Android Auto, Apple CarPlay). Sistem ini bertujuan meningkatkan keselamatan dan kenyamanan pengendara dengan informasi real-time dan kontrol suara.

## Struktur Direktori Proyek

```
S.U.N.D.A/
├── core/
│   ├── config.py             # Konfigurasi sistem dan variabel global
│   ├── logger.py             # Modul logging standar proyek
│   └── main.py               # Entrypoint utama menjalankan semua modul
│
├── hud/
│   └── hud_renderer.py       # Modul untuk menampilkan HUD AR (OpenGL/Pygame)
│
├── sensors/
│   ├── lidar_parser.py       # Parsing data LiDAR dan deteksi obstacle
│   ├── imu_handler.py        # Pembacaan IMU dan deteksi impact
│   ├── gps_handler.py        # Pembacaan data GPS
│   └── battery_monitor.py    # Monitor status baterai ESP32
│
├── voice_assistant/
│   ├── assistant_engine.py   # Engine asisten suara utama (STT, TTS, Wake word)
│   ├── stt.py                # Speech to text (offline/online)
│   ├── tts.py                # Text to speech
│   └── wake_word.py          # Engine wake word (Snowboy, Porcupine)
│
├── camera/
│   ├── dashcam_recorder.py   # Pengelolaan perekaman video continuous loop
│   ├── imu_trigger.py        # Trigger rekaman saat impact terdeteksi
│   └── overlay_timestamp.py  # Overlay timestamp pada video hasil rekaman
│
├── connectivity/
│   └── wifi_manager.py       # Pengelolaan koneksi Wi-Fi dan LTE
│
├── mobile_interface/
│   ├── server.py             # REST API (FastAPI) untuk kontrol dari smartphone
│   ├── websocket_handler.py  # WebSocket untuk live telemetry & update
│   └── layout_config.py      # Penyimpanan konfigurasi layout HUD dari HP
│
├── esp32_firmware/
│   ├── battery_display.ino   # Firmware ESP32 untuk baca status baterai
│   ├── button_handler.ino    # Firmware tombol voice command
│   └── serial_comm.ino       # Firmware komunikasi serial ESP32-Pi
│
├── test/
│   ├── test_lidar.py         # Simulasi data LiDAR
│   ├── test_gps.py           # Simulasi GPS
│   ├── test_imu.py           # Simulasi IMU
│   ├── test_battery.py       # Simulasi baterai
│   └── test_voice_assistant.py # Simulasi voice assistant (CLI)
│
├── boot.sh                   # Script startup otomatis saat boot
├── helmet.service            # Systemd service file untuk manajemen proses
└── README.md                 # Dokumentasi proyek (file ini)
```


## Cara Kerja Sistem

1. **`core/main.py`** sebagai entrypoint utama yang menjalankan semua modul secara paralel (multithreading).
2. Modul **sensors/** membaca dan memproses data sensor seperti LiDAR, IMU, GPS, dan baterai.
3. Modul **hud/** menampilkan informasi penting seperti waktu, battery, navigasi, dan indikator blind spot pada HUD AR helm.
4. Modul **voice_assistant/** mengelola interaksi suara, mulai dari mendengar wake word, mengenali perintah, hingga merespon dengan suara.
5. Modul **camera/** merekam video perjalanan secara terus-menerus, dengan trigger khusus saat terjadi kecelakaan.
6. Modul **connectivity/** memastikan helm selalu terhubung ke internet atau smartphone untuk update dan sinkronisasi.
7. Modul **mobile_interface/** menyediakan API dan WebSocket untuk mengatur HUD dan menerima perintah dari aplikasi smartphone.
8. Firmware **esp32_firmware/** bertugas mengirim data baterai dan input tombol ke sistem utama melalui komunikasi serial.
9. Folder **test/** berisi simulasi berbagai sensor untuk pengujian tanpa hardware.

## Modul dan Dependensi Utama

- **Python 3.7+**
- FastAPI — REST API server
- uvicorn — ASGI server untuk FastAPI
- websockets — WebSocket server
- PyOpenGL atau Pygame — untuk rendering HUD
- ffmpeg — perekaman dan overlay video
- **ESP32 SDK** untuk firmware (Arduino IDE)
- Library pendukung AI: Mycroft, Snowboy (offline wake word), Vosk (offline STT), Google TTS (online)
- Library sensor (contoh: `pyserial` untuk serial ESP32, `pygps` untuk GPS parsing)
- Virtual environment (disarankan)


## Variabel dan Konfigurasi Penting

- `core/config.py`
    - `VIDEO_DIR` — Folder penyimpanan video rekaman
    - `API_PORT` — Port FastAPI berjalan (default 5000)
    - `HUD_LAYOUT_FILE` — File konfigurasi HUD
    - `SERIAL_PORT` — Port komunikasi serial ESP32 (misal: `/dev/ttyUSB0`)
    - `BATTERY_THRESHOLD` — Persen minimum baterai sebelum peringatan
    - `WIFI_SSID` dan `WIFI_PASSWORD` — Untuk koneksi Wi-Fi otomatis (jika dipakai)
- `esp32_firmware/` sesuaikan pin ADC baterai, tombol, dan kecepatan serial di firmware


## Cara Instalasi dan Menjalankan

1. Clone repo ke Raspberry Pi atau Jetson Nano:

```bash
git clone https://github.com/muhammadIdhamMaarif/S.U.N.D.A.git
cd S.U.N.D.A
```

2. Setup environment Python:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Pastikan dependencies sistem terinstall:
    - `ffmpeg`
    - `libusb-dev` (untuk LiDAR)
    - Driver kamera CSI / USB
4. Sesuaikan `core/config.py` sesuai kebutuhan hardware dan jaringan.
5. Upload dan compile firmware ESP32 melalui Arduino IDE.
6. Jalankan sistem dengan:

```bash
./boot.sh
```

atau aktifkan systemd:

```bash
sudo systemctl start helmet.service
```

7. Untuk development, jalankan test sensor di folder `test/` untuk simulasi.

## Cara Pengembangan

- Modular: Setiap fitur terpisah di folder masing-masing, mudah untuk maintenance dan testing.
- Gunakan logger `core/logger.py` untuk debugging dan audit log.
- Tambahkan unit test dan integrasi test pada folder `test/`.
- Gunakan virtual environment agar dependensi konsisten.
- Dokumentasi API FastAPI ada di `http://localhost:5000/docs`.


## Penjelasan Variabel Penting di Kode

| Variabel | Fungsi/Deskripsi | Lokasi |
| :-- | :-- | :-- |
| `VIDEO_DIR` | Tempat penyimpanan file rekaman video | `core/config.py` |
| `API_PORT` | Port untuk FastAPI API | `core/config.py` |
| `HUD_LAYOUT_FILE` | File JSON konfigurasi layout HUD | `core/config.py` |
| `SERIAL_PORT` | Port komunikasi serial dengan ESP32 | `core/config.py` |
| `BATTERY_THRESHOLD` | Batas minimal baterai untuk peringatan | `core/config.py` |
| `WIFI_SSID`, `WIFI_PASSWORD` | Data login Wi-Fi | `core/config.py` |
| `start_hud()`, `start_lidar()` ... | Fungsi entrypoint modul masing-masing | Di folder masing-masing |

## Referensi Modul Internal

- `core/logger.py` — Logger standar dengan timestamp dan tag modul.
- `hud/hud_renderer.py` — Renderer HUD, menampilkan overlay info AR.
- `sensors/` — Membaca dan mengolah data sensor LiDAR, IMU, GPS, baterai.
- `voice_assistant/` — Wake word detection, speech recognition, voice response.
- `camera/` — Pengelolaan rekaman video, trigger kecelakaan.
- `connectivity/wifi_manager.py` — Manajemen koneksi Wi-Fi dan LTE.
- `mobile_interface/` — API dan websocket untuk smartphone control.
- `esp32_firmware/` — Firmware ESP32 pengirim data baterai dan tombol.


## Pengembangan Selanjutnya \& Enhancement

- Integrasi AI wake word dan voice command yang lebih canggih.
- Otomatis update OTA firmware dan software helm.
- Implementasi UI mobile app lengkap (Flutter/Android/iOS).
- Penambahan sensor fall detection dan emergency alert.
- Live streaming video ke smartphone via LTE.
- Pengamanan komunikasi (enkripsi, token auth API).


## Kontak \& Kontribusi

Silakan fork, buat issue, atau pull request di repo GitHub untuk kolaborasi.

Terima kasih sudah menggunakan dan berkontribusi di proyek S.U.N.D.A !



