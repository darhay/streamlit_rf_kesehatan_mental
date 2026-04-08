import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd

model = joblib.load(os.path.join(os.path.dirname(__file__), "random_forest_90_10.pkl"))

st.set_page_config(page_title="Prediksi Kesehatan Mental",layout="centered")

# load css
with open(os.path.join(os.path.dirname(__file__), "assets/style.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# session step
if "step" not in st.session_state:
    st.session_state.step = 1

def progress_bar(current):
    steps = []
    for i in range(1, 4):
        if i < current:
            steps.append('<div class="progress-step done"></div>')
        elif i == current:
            steps.append('<div class="progress-step active"></div>')
        else:
            steps.append('<div class="progress-step"></div>')
    st.markdown(f'<div class="progress-bar">{"".join(steps)}</div>', unsafe_allow_html=True)

# =========================
# STEP 1
# =========================

if st.session_state.step == 1:
    progress_bar(1)
    st.title("Kuesioner Awal")
    st.markdown('<div class="step-caption">Langkah 1 dari 3 — Data Diri</div>', unsafe_allow_html=True)

    # st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # st.markdown('<div class="section-label">📋 Informasi Umum</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        usia = st.selectbox("Usia", ["< 19", "19–21", "22–24", "> 24"])
    with col2:
        gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"], horizontal=True)

    col3, col4 = st.columns(2)
    with col3:
        semester = st.selectbox("Semester", ["2", "4", "6", "8", "> 8"])
    with col4:
        tempat = st.radio("Tempat Tinggal", ["Bersama orang tua", "Kost / kontrakan"])

    # st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    # st.markdown('<div class="section-label">🏃 Gaya Hidup</div>', unsafe_allow_html=True)

    col5, col6 = st.columns(2)
    with col5:
        tidur = st.selectbox("Jam tidur per hari", ["< 5 jam", "5–6 jam", "6–7 jam", "> 7 jam"])
    with col6:
        olahraga = st.selectbox("Frekuensi olahraga", ["Tidak pernah", "1–2 kali", "3–4 kali", "> 4 kali"])

    if st.button("Selanjutnya →"):
        st.session_state.dataA = [usia, gender, semester, tempat, tidur, olahraga]
        st.session_state.step = 2
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# STEP 2
# =========================

elif st.session_state.step == 2:
    progress_bar(2)
    st.title("Kuesioner Aktivitas Digital")
    st.markdown('<div class="step-caption">Langkah 2 dari 3 — Pilih jawaban yang sesuai</div>', unsafe_allow_html=True)

    scale = {
        "Sangat Tidak Sesuai": 1,
        "Tidak Sesuai": 2,
        "Netral": 3,
        "Sesuai": 4,
        "Sangat Sesuai": 5
    }

    def q(text, key=None):
        return st.radio(text, list(scale.keys()), horizontal=True, key=key)

    # ── Bagian A: Intensitas Penggunaan Digital ──
    # st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # st.markdown('<div class="section-label">💻 Intensitas Penggunaan Digital</div>', unsafe_allow_html=True)

    q9  = q("Saya menggunakan perangkat digital (HP/laptop) untuk keperluan akademik selama lebih dari 6 jam per hari.", "q9")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q10 = q("Lebih dari 70% aktivitas akademik saya dilakukan menggunakan perangkat digital (HP/laptop).", "q10")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q11 = q("Saya sering menggunakan lebih dari satu perangkat digital secara bersamaan (misalnya laptop dan HP) selama minimal 1 jam dalam sehari.", "q11")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)

    # # ── Bagian B: Beban Pemrograman ──
    # st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # st.markdown('<div class="section-label">🖥️ Beban Pemrograman & Praktikum</div>', unsafe_allow_html=True)

    q12 = q("Aktivitas pemrograman dan praktikum biasanya menghabiskan waktu lebih dari 8 jam dalam satu minggu.", "q12")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q13 = q("Saya sering menghabiskan waktu lebih dari 3 jam dalam satu sesi di depan layar untuk mengerjakan tugas pemrograman.", "q13")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q14 = q("Ketika mendekati deadline praktikum, durasi penggunaan perangkat digital saya meningkat menjadi lebih dari 8 jam dalam sehari.", "q14")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q15 = q("Proses debugging atau perbaikan error dalam pemrograman sering memakan waktu lebih dari 1 jam untuk satu masalah.", "q15")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)

    # # ── Bagian C: Gejala Depresi ──
    # st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # st.markdown('<div class="section-label">😔 Kondisi Emosional</div>', unsafe_allow_html=True)

    q16 = q("Selama menjalani aktivitas akademik berbasis digital, saya jarang merasakan perasaan positif seperti gembira atau bangga atas apa yang saya kerjakan.", "q16")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q17 = q("Saya sering merasa enggan atau sulit memulai tugas yang berkaitan dengan aktivitas akademik berbasis digital.", "q17")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q18 = q("Tuntutan dari aktivitas akademik berbasis digital membuat saya merasa tidak memiliki harapan terhadap hasil yang akan saya capai.", "q18")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q19 = q("Saat menghadapi aktivitas akademik berbasis digital, saya kerap merasa sedih dan tertekan secara emosional.", "q19")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q20 = q("Aktivitas akademik yang melibatkan penggunaan teknologi digital tidak lagi menimbulkan rasa antusias dalam diri saya.", "q20")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q21 = q("Ketika mengalami kesulitan dalam aktivitas akademik berbasis digital, saya merasa diri saya tidak cukup berharga.", "q21")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q22 = q("Keterlibatan saya dalam aktivitas akademik berbasis digital membuat saya memandang hidup sebagai sesuatu yang kurang berarti.", "q22")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)

    # # ── Bagian D: Gejala Kecemasan ──
    # st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # st.markdown('<div class="section-label">😰 Gejala Fisik & Kecemasan</div>', unsafe_allow_html=True)

    q23 = q("Saat berhadapan dengan tugas akademik berbasis digital, saya merasakan mulut menjadi kering.", "q23")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q24 = q("Dalam situasi tertentu saat mengerjakan aktivitas digital, saya merasa napas menjadi tidak teratur meskipun tidak sedang beraktivitas fisik.", "q24")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q25 = q("Ketika mengerjakan pemrograman atau tugas digital, tubuh saya menunjukkan tanda gemetar, terutama pada bagian tangan.", "q25")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q26 = q("Saya sering khawatir tidak mampu mengendalikan diri dan melakukan kesalahan saat mengikuti praktikum pemrograman atau aktivitas akademik berbasis digital.", "q26")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q27 = q("Tekanan yang muncul dari aktivitas akademik berbasis digital membuat saya merasa hampir kehilangan kendali.", "q27")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q28 = q("Tanpa melakukan aktivitas fisik, saya dapat merasakan perubahan detak jantung ketika menghadapi tuntutan tugas digital.", "q28")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q29 = q("Ketika terlibat dalam aktivitas akademik berbasis digital, saya merasakan ketakutan yang muncul tanpa sebab yang jelas.", "q29")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)

    # # ── Bagian E: Gejala Stres ──
    # st.markdown('<div class="main-card">', unsafe_allow_html=True)
    # st.markdown('<div class="section-label">😤 Gejala Stres</div>', unsafe_allow_html=True)

    q30 = q("Saya merasa sulit beristirahat setelah lama melakukan aktivitas akademik berbasis digital.", "q30")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q31 = q("Saya mudah bereaksi berlebihan saat menghadapi masalah dalam tugas digital.", "q31")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q32 = q("Saya merasa kelelahan dan kehilangan energi akibat tuntutan tugas digital.", "q32")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q33 = q("Saya merasa gelisah saat harus mengerjakan aktivitas akademik berbasis digital.", "q33")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q34 = q("Saya sulit merasa tenang ketika menjalani aktivitas digital untuk perkuliahan.", "q34")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q35 = q("Saya sulit bersabar saat mengalami gangguan ketika mengerjakan tugas digital.", "q35")
    st.markdown('<hr class="q-divider">', unsafe_allow_html=True)
    q36 = q("Perasaan saya mudah tersentuh oleh hasil atau penilaian dari tugas digital.", "q36")

    if st.button("Lihat Hasil Prediksi →"):
        st.session_state.dataB = [
            scale[q9], scale[q10], scale[q11],
            scale[q12], scale[q13], scale[q14], scale[q15],
            scale[q16], scale[q17], scale[q18], scale[q19],
            scale[q20], scale[q21], scale[q22],
            scale[q23], scale[q24], scale[q25], scale[q26],
            scale[q27], scale[q28], scale[q29],
            scale[q30], scale[q31], scale[q32], scale[q33],
            scale[q34], scale[q35], scale[q36]
        ]
        st.session_state.step = 3
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)



# =========================
# STEP 3
# =========================

elif st.session_state.step == 3:
    progress_bar(3)
    st.title("Hasil Prediksi")
    st.markdown('<div class="step-caption">Langkah 3 dari 3 — Hasil Analisis Kesehatan Mental</div>', unsafe_allow_html=True)

    # ── Normalization ──
    usia_map     = {"< 19": 0, "19–21": 1, "22–24": 2, "> 24": 3}
    gender_map   = {"Laki-laki": 0, "Perempuan": 1}
    semester_map = {"2": 0, "4": 1, "6": 2, "8": 3, "> 8": 4}
    tempat_map   = {"Bersama orang tua": 0, "Kost / kontrakan": 1}
    tidur_map    = {"< 5 jam": 0, "5–6 jam": 1, "6–7 jam": 2, "> 7 jam": 3}
    olahraga_map = {"Tidak pernah": 0, "1–2 kali": 1, "3–4 kali": 2, "> 4 kali": 3}

    def normalize(val, n):
        return val / (n - 1)

    def normalize_likert(val):
        return (val - 1) / 4

    A = st.session_state.dataA
    B = st.session_state.dataB

    fitur = [
        normalize(usia_map[A[0]],     4),
        normalize(gender_map[A[1]],   2),
        normalize(semester_map[A[2]], 5),
        normalize(tempat_map[A[3]],   2),
        normalize(tidur_map[A[4]],    4),
        normalize(olahraga_map[A[5]], 4),
    ]
    fitur.extend([normalize_likert(v) for v in B])
    fitur = np.array(fitur).reshape(1, -1)

    pred  = model.predict(fitur)[0]
    proba = model.predict_proba(fitur)[0]

    # ── Label config ──
    label_cfg = {
        0: {"label": "Kecenderungan Depresi",  "css": "depresi", "icon": "😔",
            "desc": "Hasil analisis mendeteksi kecenderungan depresi. Disarankan untuk berbicara dengan konselor atau psikolog kampus untuk mendapatkan dukungan lebih lanjut."},
        1: {"label": "Kecenderungan Kecemasan","css": "cemas",   "icon": "😰",
            "desc": "Hasil analisis mendeteksi kecenderungan kecemasan. Teknik relaksasi dan manajemen waktu yang baik dapat membantu mengurangi gejala ini."},
        2: {"label": "Kecenderungan Stres",    "css": "stres",   "icon": "😤",
            "desc": "Hasil analisis mendeteksi kecenderungan stres. Disarankan untuk mengelola beban akademik secara bijak dan menjaga keseimbangan aktivitas digital."},
        3: {"label": "Normal",                 "css": "normal",  "icon": "😊",
            "desc": "Hasil analisis menunjukkan kondisi mental yang normal. Pertahankan pola hidup sehat dan keseimbangan aktivitas digital Anda."},
    }
    cfg    = label_cfg[pred]
    hasil  = cfg["label"]
    css_cl = cfg["css"]
    icon   = cfg["icon"]
    desc   = cfg["desc"]
    conf   = round(proba[pred] * 100, 1)

    # ── Hero result ──
    st.markdown(f"""
    <div class="result-hero" style="text-align:center !important;">
        <div class="result-icon" style="text-align:center !important; display:block;">{icon}</div>
        <div style="text-align:center !important; width:100%;">Kondisi Kesehatan Mental Anda</div>
        <div style="text-align:center !important; width:100%; display:flex; justify-content:center; margin: 8px 0;">
            <div class="result-label {css_cl}" style="text-align:center !important;">{hasil}</div>
        </div>
        <p class="result-desc" style="text-align:center !important; margin:0 auto;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats row ──
    classes = model.classes_
    proba_pct = {c: round(proba[i]*100, 1) for i, c in enumerate(classes)}

    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-value">{conf}%</div>
            <div class="stat-label">Keyakinan Model</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">62.5%</div>
            <div class="stat-label">Akurasi Model</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">313</div>
            <div class="stat-label">Data Latih</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Confusion Matrix (training result, fixed) ──
    cm_path = os.path.join(os.path.dirname(__file__), "confusion_matrix_90_10.csv")
    cm = pd.read_csv(cm_path).values  # shape (4,4)

    col_labels = ["Depresi", "Kecemasan", "Stres", "Normal"]
    row_labels  = ["Kecenderungan Depresi", "Kecenderungan Kecemasan", "Kecenderungan Stres", "Normal"]

    th_cols = "".join([f"<th>{c}</th>" for c in col_labels])

    tbody = ""
    for i, row_lbl in enumerate(row_labels):
        cells = ""
        for j in range(len(col_labels)):
            val = int(cm[i][j])
            css = 'class="diagonal"' if i == j else ""
            cells += f"<td {css}>{val}</td>"
        tbody += f"<tr><td class='row-label'>{row_lbl}</td>{cells}</tr>"

    st.markdown(f"""
    <div class="cm-wrap">
        <div class="cm-title">📊 Confusion Matrix — Hasil Pelatihan Model</div>
        <table class="cm-table">
            <thead>
                <tr>
                    <th style="text-align:left">Aktual \\ Prediksi</th>
                    {th_cols}
                </tr>
            </thead>
            <tbody>{tbody}</tbody>
        </table>
        <div class="badge-row">
            <span class="badge badge-normal">Normal</span>
            <span class="badge badge-stres">Kecenderungan Stres</span>
            <span class="badge badge-cemas">Kecenderungan Kecemasan</span>
            <span class="badge badge-depresi">Kecenderungan Depresi</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Disclaimer ──
    st.markdown("""
    <div class="info-box">
        ⚠️ <strong>Catatan:</strong> Hasil ini merupakan prediksi berbasis data aktivitas digital dan akademik menggunakan model <em>Random Forest</em>.
        Ini bukan diagnosis klinis. Jika Anda merasa mengalami tekanan mental yang signifikan, disarankan untuk berkonsultasi dengan profesional kesehatan mental.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Isi Ulang Kuesioner"):
        st.session_state.step = 1
        st.rerun()