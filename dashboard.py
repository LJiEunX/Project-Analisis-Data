import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def main():
    st.title("Proyek Analisis Penyewaan Sepeda")

    # Membaca data yang dibutuhkan
    day_df = pd.read_csv("day.csv")
    total_per_hari_seluruh_musim = day_df.groupby(['weekday'])['cnt'].mean().sort_values(ascending=False)

    # Pelabelan
    weekday_mapping = {0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'}

    # Apply weekday mapping to the index
    total_per_hari_seluruh_musim.index = total_per_hari_seluruh_musim.index.map(weekday_mapping)

    # Pertanyaan 1
    st.header("Rata rata penyewaan sepeda terbanyak")
    st.write("Grafik di bawah ini menunjukkan pada hari apa sepeda banyak disewa oleh para pelanggan")
    fig, ax = plt.subplots(figsize=(10, 6))
    total_per_hari_seluruh_musim.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Rata rata Hari Penyewaan Sepeda pada Seluruh Musim')
    ax.set_xlabel('Hari Dalam Seminggu')
    ax.set_ylabel('Total Penyewa Sepeda')
    ax.set_xticklabels(total_per_hari_seluruh_musim.index, rotation=0)  # Rotasi label x menjadi horizontal
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)  # Display the Matplotlib plot in Streamlit
    st.write("Dapat terlihat di dalam grafik bahwa peningkatan terjadi pada hari Jumat dan disusul hari hari lainnya ")

    # Pertanyaan 2 

    day_df = pd.read_csv("day.csv")

    st.header("Lonjakan Penyewaan Pada Musim Gugur")
    st.write("Grafik di bawah ini menunjukkan pada musim apa sepeda paling banyak disewa")

    total_per_musim = day_df.groupby('season')['cnt'].sum().sort_values(ascending=False)
    season_mapping = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}
    total_per_musim.index = total_per_musim.index.map(season_mapping)

    fig, ax = plt.subplots(figsize=(8, 8))
    colors = ['orange', 'maroon', 'cyan', 'brown']  # Warna yang diminta
    ax.pie(total_per_musim, labels=total_per_musim.index, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.set_title('Total Penyewa Sepeda Permusim')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    st.write("Sepeda Paling Banyak Disewa Pada Musim Gugur ")


if __name__ == "__main__":
    main()
