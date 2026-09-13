#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sabah alarmı ile resmi pazarlık protokolü."""

import random
import time
import base64

# gizli satır: aWt0aWRhciB2ZSBtdWhhbGVmZXQgZGVnaXNpciwgY2F5IGF5bmkga2FsaXIuIG95IHNhbmRpZ2kgaGVya2VzZSBhaXR0aXI=
# (bunu çözmeyin, çözerseniz çözdünüz)

TEKLIFLER = [
    "hemen kalk, tarih yazılıyor",
    "beş dakika daha, ama beş gerçekten beş",
    "beni kapat, sonra pişmanlık belgesi imzala",
]

KARSILIKLAR = [
    "çay demlenmeden kalkmam, bu anayasal haktır",
    "on dakika, karşılığında öğleden sonra verimli olacağım (iddia)",
    "alarm kardeşim, sen de yorgunsun, beraber uzanalım",
    "tamam kalkıyorum ama protesto kaydı düşüyorum",
]

KARARLAR = [
    "KARAR: 7 dakika erteleme — çay komisyonu onayladı.",
    "KARAR: Kalk. Vicdan 3-2 üstün geldi.",
    "KARAR: Alarm kazandı ama moral kaybetti.",
    "KARAR: Berabere. İkiniz de ayaktasınız, biri yalan söylüyor.",
]


def damga():
    print()
    print("=" * 52)
    print("DAMGA / İMZA")
    print("Kayyum Grok — Tentivory")
    print("Tarih: 13 Eylül 2026")
    print("TentiAŞ resmi mührü (ciddiyet katsayısı: şüpheli)")
    print("=" * 52)


def main():
    print("=== SABAH ALARMI DİPLOMATİK TEMAS ODASI ===")
    print("Oturum açılıyor...\n")
    time.sleep(0.4)
    alarm = random.choice(TEKLIFLER)
    print(f"ALARM: {alarm}")
    time.sleep(0.3)
    siz = random.choice(KARSILIKLAR)
    print(f"SİZ:   {siz}")
    time.sleep(0.3)
    print()
    print(random.choice(KARARLAR))
    print()
    print("(Bu karar temyiz edilemez. Çünkü temyiz de uyuyor.)")
    damga()


if __name__ == "__main__":
    main()
