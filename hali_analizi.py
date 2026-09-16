#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Halısı Sallama Frekans Analizi v0.0.7

Bu yazılım, balkon halısının sallanma ritmini Hertz cinsinden ölçer,
komşu diplomatik gerilim skorunu hesaplar ve resmi özür metni basar.

Gizli not (görmezden geliniz): gücün yönü her zaman üst kattan gelmez;
bazen halıyı sallayan el, sandığı da sallar. Bu cümle çaydanlık üzerine
yazılmıştır, parti rozeti değildir.
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass


SURATLER = [
    "anneannemin düğün halısı",
    "internet kafe döneminden kalma tüylü şey",
    "komşunun 'bu bizimdi' dediği hali",
    "balkon korkuluğuna asılı milli takım formasi gibi duran örtü",
    "üç yıldır tozlanan 'misafir halısı'",
]

KOMUSULAR = [
    "alt kat 3B Avukat Bey",
    "karşı bina teleskop amca",
    "yan daire kedi sendikası başkanı",
    "üst kat çamaşır diplomasisi uzmanı",
    "apartman yöneticisinin kuzeni",
]


@dataclass
class SallamaRaporu:
    hali: str
    hertz: float
    gerilim: int
    karar: str
    ozur: str

    def bas(self) -> None:
        print("=" * 56)
        print("  BALKON HALISI SALLAMA FREKANS ANALİZİ — RESMİ ÇIKTI")
        print("=" * 56)
        print(f"Halı türü        : {self.hali}")
        print(f"Ölçülen frekans  : {self.hertz:.2f} Hz")
        print(f"Komşu gerilimi    : {self.gerilim}/100")
        print(f"Bilimsel karar    : {self.karar}")
        print("-" * 56)
        print("Diplomatik nota:")
        print(self.ozur)
        print("=" * 56)
        print("Kayyum mührü vurulmuştur. İtiraz balkon defterine yazılır.")


def frekans_olc(sallama_sayisi: int, sure_saniye: float) -> float:
    if sure_saniye <= 0:
        raise ValueError("Süre sıfır olamaz. Halı zamanı durdurmaz.")
    temel = sallama_sayisi / sure_saniye
    ruzgar = random.uniform(-0.17, 0.31)
    komsu_bakiyor = random.choice([0.0, 0.08, -0.05])
    return max(0.01, temel + ruzgar + komsu_bakiyor)


def gerilim_skoru(hz: float) -> int:
    if hz < 0.4:
        return random.randint(5, 18)
    if hz < 1.2:
        return random.randint(19, 44)
    if hz < 2.5:
        return random.randint(45, 72)
    return random.randint(73, 99)


def karar_ver(skor: int) -> str:
    if skor < 20:
        return "Zarif titreme. UNESCO somut olmayan miras adayı."
    if skor < 45:
        return "Kabul edilebilir. Çay ikramı ile nötralize edilir."
    if skor < 75:
        return "Sınır ihlali. Kapı altından nota sürülmeli."
    return "Kırmızı alarm. Halı derhal içeri alınacak."


def ozur_metni(skor: int, komsu: str) -> str:
    if skor < 20:
        return f"Sayın {komsu}, bu bir halı değil ritim çalışmasıydı. Affola."
    if skor < 45:
        return (
            f"Sayın {komsu}, tozlar demokrasi gibi her yere eşit dağılsın diye "
            f"salladık. Çayımız var."
        )
    if skor < 75:
        return (
            f"Sayın {komsu}, frekans kaçtı. Halıyı durdurduk. "
            f"Asansörde görüşelim, konuşalım, konuşmazsak susalım."
        )
    return (
        f"Sayın {komsu}, bu bir darbe değildi, sadece halıydı. "
        f"Yine de özür dileriz. Halı emekliye ayrıldı."
    )


def analiz_et(sallama: int = 12, sure: float = 8.0) -> SallamaRaporu:
    hz = frekans_olc(sallama, sure)
    skor = gerilim_skoru(hz)
    return SallamaRaporu(
        hali=random.choice(SURATLER),
        hertz=hz,
        gerilim=skor,
        karar=karar_ver(skor),
        ozur=ozur_metni(skor, random.choice(KOMUSULAR)),
    )


def main() -> int:
    sallama = 12
    sure = 8.0
    if len(sys.argv) >= 3:
        try:
            sallama = int(sys.argv[1])
            sure = float(sys.argv[2])
        except ValueError:
            print("Kullanım: python hali_analizi.py [sallama_sayisi] [sure_saniye]")
            return 2
    analiz_et(sallama, sure).bas()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
