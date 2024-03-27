import random

# Definisikan parameter
jumlah_individu = 10
jumlah_generasi = 100
prob_mutasi = 0.1
jumlah_dosen_max = 2

# Definisikan struktur ruang kelas
gedung_kuliah = {
    'Gedung A': {'ruang1': 50, 'ruang2': 40, 'ruang3': 30},
    'Gedung B': {'ruang1': 60, 'ruang2': 45, 'ruang3': 35},
    'Gedung C': {'ruang1': 70, 'ruang2': 55, 'ruang3': 40},
    'Gedung D': {'ruang1': 80, 'ruang2': 60, 'ruang3': 50}
}

# Data mata kuliah, jumlah mahasiswa, jadwal pertemuan, dosen, dan preferensi dosen
mata_kuliah = {
    'Matematika': {'students': 50, 'meetings': 2, 'lecturers': ['Dr. John', 'Prof. Smith'], 'duration': (2, 3)},
    'Fisika': {'students': 40, 'meetings': 1, 'lecturers': ['Dr. Johnson'], 'duration': (2, 3)},
    'Kimia': {'students': 30, 'meetings': 1, 'lecturers': ['Prof. Brown'], 'duration': (2, 3)},
    'Biologi': {'students': 35, 'meetings': 2, 'lecturers': ['Dr. Lee', 'Prof. Davis'], 'duration': (2, 3)},
    'Bahasa Inggris': {'students': 45, 'meetings': 1, 'lecturers': ['Prof. Wilson'], 'duration': (2, 3)}
}

# Definisikan hari perkuliahan
hari_perkuliahan = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat']

# Data preferensi dosen
preferensi_dosen = {
    'Dr. John': {'days_off': ['Jumat'], 'hours_off': [(14, 17)]},
    'Prof. Smith': {'days_off': ['Selasa'], 'hours_off': [(9, 12)]},
    'Dr. Johnson': {'days_off': ['Rabu'], 'hours_off': [(8, 11)]},
    'Prof. Brown': {'days_off': ['Kamis'], 'hours_off': [(13, 16)]},
    'Dr. Lee': {'days_off': ['Senin'], 'hours_off': [(10, 13)]},
    'Prof. Davis': {'days_off': ['Jumat'], 'hours_off': [(15, 17)]},
    'Prof. Wilson': {'days_off': ['Rabu'], 'hours_off': [(14, 17)]}
}

# Fungsi untuk menghasilkan populasi awal secara acak
def generate_population(jumlah_individu, mata_kuliah):
    population = []
    for _ in range(jumlah_individu):
        schedule = {}
        for course, info in mata_kuliah.items():
            schedule[course] = []
            for _ in range(info['meetings']):
                building = random.choice(list(gedung_kuliah.keys()))
                room = random.choice(list(gedung_kuliah[building].keys()))
                day = random.choice(hari_perkuliahan)
                start_time = random.randint(8, 17 - info['duration'][1])  # Jam mulai antara 8 pagi hingga 5 sore
                end_time = start_time + info['duration'][1]
                lecturers = random.sample(info['lecturers'], random.randint(1, min(jumlah_dosen_max, len(info['lecturers']))))

                # Memperhitungkan preferensi dosen
                for lecturer in lecturers:
                    if lecturer in preferensi_dosen:
                        pref = preferensi_dosen[lecturer]
                        while day in pref['days_off'] or any(start_time <= end and end <= start_time + 3 for start, end in pref['hours_off']):
                            day = random.choice(hari_perkuliahan)
                            start_time = random.randint(8, 17 - info['duration'][1])
                            end_time = start_time + info['duration'][1]

                schedule[course].append({'building': building, 'room': room, 'day': day, 'start_time': start_time, 'end_time': end_time, 'lecturers': lecturers})
        population.append(schedule)
    return population

# Fungsi untuk menghitung fitness
def calculate_fitness(schedule):
    fitness = 0
    for course, meetings in schedule.items():
        for meeting in meetings:
            capacity = gedung_kuliah[meeting['building']][meeting['room']]
            if mata_kuliah[course]['students'] <= capacity:
                fitness += 1
    return fitness

# Fungsi seleksi orang tua menggunakan metode turnamen
def select_parents(population):
    parents = []
    for _ in range(2):
        tournament_size = int(len(population) * 0.1)
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=calculate_fitness)
        parents.append(winner)
    return parents

# Fungsi crossover menggunakan satu titik potong
def crossover(parents):
    child = {}
    for course in mata_kuliah.keys():
        parent_index = random.randint(0, 1)
        child[course] = parents[parent_index][course]
    return child

# Fungsi mutasi dengan mengubah hari perkuliahan, ruang kelas, atau jadwal
def mutate(schedule, mata_kuliah):
    mutated_schedule = schedule.copy()
    course = random.choice(list(schedule.keys()))
    meeting_index = random.randint(0, len(schedule[course]) - 1)
    meeting = mutated_schedule[course][meeting_index]
    meeting['day'] = random.choice(hari_perkuliahan)
    building = random.choice(list(gedung_kuliah.keys()))
    room = random.choice(list(gedung_kuliah[building].keys()))
    meeting['building'] = building
    meeting['room'] = room
    start_time = random.randint(8, 17 - mata_kuliah[course]['duration'][1])
    meeting['start_time'] = start_time
    meeting['end_time'] = start_time + mata_kuliah[course]['duration'][1]
    return mutated_schedule

# Fungsi utama untuk algoritma genetika
def genetic_algorithm(mata_kuliah, jumlah_individu, jumlah_generasi, prob_mutasi):
    population = generate_population(jumlah_individu, mata_kuliah)
    for _ in range(jumlah_generasi):
        new_population = []
        for _ in range(jumlah_individu // 2):
            parents = select_parents(population)
            child = crossover(parents)
            if random.random() < prob_mutasi:
                child = mutate(child, mata_kuliah)
            new_population.append(child)
            new_population.append(mutate(child, mata_kuliah))
        population = new_population
    best_schedule = max(population, key=calculate_fitness)
    return best_schedule, calculate_fitness(best_schedule)

# Menjalankan algoritma genetika
best_schedule, best_fitness = genetic_algorithm(mata_kuliah, jumlah_individu, jumlah_generasi, prob_mutasi)


print("Penjadwalan Terbaik:")
for course, meetings in best_schedule.items():
    print(course + ":")
    for meeting in meetings:
        print(f"- Hari: {meeting['day']}, Jam Mulai: {meeting['start_time']}:00, Jam Selesai: {meeting['end_time']}:00, Gedung: {meeting['building']}, Ruang: {meeting['room']}, Dosen: {', '.join(meeting['lecturers'])}")
print("Fitness:", best_fitness)
