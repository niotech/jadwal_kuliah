# Jadwal Kuliah

### Solving problem with new College Semester, this will help generate schedule for:


- Lecturer with their availability day & time
- Student
- Subject/Course
- Building and Room (and it's capacity)


Running the code:

`python jadwal.py`

---

### Data Structure

Building data structure:
`
gedung_kuliah = {
    'Gedung A': {'ruang1': 50, 'ruang2': 40, 'ruang3': 30},
    'Gedung B': {'ruang1': 60, 'ruang2': 45, 'ruang3': 35},
    'Gedung C': {'ruang1': 70, 'ruang2': 55, 'ruang3': 40},
    'Gedung D': {'ruang1': 80, 'ruang2': 60, 'ruang3': 50}
}
`

Course data structure
`
mata_kuliah = {
    'Matematika': {'students': 50, 'meetings': 2, 'lecturers': ['Dr. John', 'Prof. Smith'], 'duration': (2, 3)},
    'Fisika': {'students': 40, 'meetings': 1, 'lecturers': ['Dr. Johnson'], 'duration': (2, 3)},
    'Kimia': {'students': 30, 'meetings': 1, 'lecturers': ['Prof. Brown'], 'duration': (2, 3)},
    'Biologi': {'students': 35, 'meetings': 2, 'lecturers': ['Dr. Lee', 'Prof. Davis'], 'duration': (2, 3)},
    'Bahasa Inggris': {'students': 45, 'meetings': 1, 'lecturers': ['Prof. Wilson'], 'duration': (2, 3)}
}
`

Lecturer availability data structure:

`
preferensi_dosen = {
    'Dr. John': {'days_off': ['Jumat'], 'hours_off': [(14, 17)]},
    'Prof. Smith': {'days_off': ['Selasa'], 'hours_off': [(9, 12)]},
    'Dr. Johnson': {'days_off': ['Rabu'], 'hours_off': [(8, 11)]},
    'Prof. Brown': {'days_off': ['Kamis'], 'hours_off': [(13, 16)]},
    'Dr. Lee': {'days_off': ['Senin'], 'hours_off': [(10, 13)]},
    'Prof. Davis': {'days_off': ['Jumat'], 'hours_off': [(15, 17)]},
    'Prof. Wilson': {'days_off': ['Rabu'], 'hours_off': [(14, 17)]}
}
`

---

### Example output


`Penjadwalan Terbaik:

Matematika:
- Hari: Senin, Jam Mulai: 11:00, Jam Selesai: 14:00, Gedung: Gedung C, Ruang: ruang3, Dosen: Prof. Smith
- Hari: Rabu, Jam Mulai: 12:00, Jam Selesai: 15:00, Gedung: Gedung D, Ruang: ruang2, Dosen: Dr. John

Fisika:
- Hari: Senin, Jam Mulai: 8:00, Jam Selesai: 11:00, Gedung: Gedung D, Ruang: ruang2, Dosen: Dr. Johnson

Kimia:
- Hari: Rabu, Jam Mulai: 9:00, Jam Selesai: 12:00, Gedung: Gedung B, Ruang: ruang3, Dosen: Prof. Brown

Biologi:
- Hari: Jumat, Jam Mulai: 9:00, Jam Selesai: 12:00, Gedung: Gedung B, Ruang: ruang1, Dosen: Prof. Davis
- Hari: Selasa, Jam Mulai: 13:00, Jam Selesai: 16:00, Gedung: Gedung B, Ruang: ruang2, Dosen: Prof. Davis, Dr. Lee

Bahasa Inggris:
- Hari: Senin, Jam Mulai: 10:00, Jam Selesai: 13:00, Gedung: Gedung B, Ruang: ruang2, Dosen: Prof. Wilson

Fitness: 6
`