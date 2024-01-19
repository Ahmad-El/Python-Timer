from PyQt6.QtWidgets import (
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QWidget, 
    QGridLayout, 
    )
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QFont
import datetime
from spinboxes import Spinbox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setWindowTitle("Timer")
        self.setStyleSheet("background-color: #24292E;") 
        self.total_in_seconds = datetime.datetime.now()
        self.app_time = datetime.datetime.now()
        self.total_on_minutes = 0
        
        self._init_labels()
        self._init_left_spin_boxs(layout)
        self._init_right_spin_boxs(layout)
        self._init_buttons()
        self._init_media()
    

        layout.addWidget(self.label_main_clock, 0, 0, 1, 3)
        layout.addWidget(self.label_timer, 4, 0, 1, 3)
        layout.addWidget(self.label_total_time, 5, 0, 1, 3)
        layout.addWidget(self.button_start, 1, 1, 3, 1)
        
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        
    def _init_buttons(self):
        self.button_start = QPushButton()
        self.button_start.setText("Start")
        self.button_start.setFixedSize(230, 80)
        self.button_start.setStyleSheet(
            """
            QPushButton {
                background-color: #35484C;
                font-size: 50px;
                }
            """
        )
        self.button_start.clicked.connect(self.start_timer)
        
    def _init_left_spin_boxs(self, layout):
        spinbox0 = Spinbox(True, 2)
        self.left_spin_box = Spinbox(False, 3)
        self.left_spin_box.set_font(25)
        
        spinbox2 = Spinbox(True, 4)
        self.left_spin_box.setMinimum(-1)
        
        layout.addWidget(spinbox0, 1, 0)
        layout.addWidget(self.left_spin_box, 2, 0)
        layout.addWidget(spinbox2, 3, 0)
        self.left_spin_box.update_all(spinbox0, spinbox2)
        
    def _init_right_spin_boxs(self, layout):
        spinbox0 = Spinbox(True, 59)
        self.right_spin_box = Spinbox(False, 0)
        self.right_spin_box.set_font(25)
        spinbox2 = Spinbox(True, 1)
        self.right_spin_box.setMinimum(-1)
        
        layout.addWidget(spinbox0, 1, 2)
        layout.addWidget(self.right_spin_box, 2, 2)
        layout.addWidget(spinbox2, 3, 2)
        self.right_spin_box.update_all(spinbox0, spinbox2)
    
    def _init_labels(self):
        self.label_main_clock = QLabel()
        self.label_main_clock.setFont(QFont("Helvetica [Cronyx]", 150))
        self.label_main_clock.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.label_timer = QLabel()
        self.label_timer.setFont(QFont("Helvetica [Cronyx]", 150))
        self.label_timer.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_timer.setText("00:00")
        self.set_time()
        
        self.label_total_time = QLabel()
        self.label_total_time.setFont(QFont("Helvetica [Cronyx]", 130))
        self.label_total_time.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_total_time.setText("00:00")
        
    def start_timer(self):
        m = self.left_spin_box.value()
        s = self.right_spin_box.value()
        self.total_in_seconds = datetime.datetime.now() + datetime.timedelta(seconds=m*60+s)
        
    def reset_timer(self):
        if self.total_in_seconds < datetime.datetime.now(): return
        time = self.total_in_seconds - datetime.datetime.now()
        time_now = f"{time.seconds // 60:02d}:{time.seconds%60:02d}"
        if time.seconds == 0:
            self.play_song()
        self.label_timer.setText(time_now)
        
    def set_time(self):
        time_now = datetime.datetime.now().strftime("%H:%M")
        self.label_main_clock.setText(time_now)
        self.reset_timer()
        self.count_total_sitting_time()
    
    def count_total_sitting_time(self):
        if self.app_time.minute == datetime.datetime.now().minute: return
        self.app_time = datetime.datetime.now()
        self.total_on_minutes += 1
        hour = self.total_on_minutes // 60
        minutes = self.total_on_minutes % 60
        time = f"{hour:02d}:{minutes:02d}"
        self.label_total_time.setText(time)
    
    def play_song(self):
        self.player.play()
        
    def _init_media(self):
        filename = "media/times_up.mp3"
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.audioOutput.setVolume(50)
        