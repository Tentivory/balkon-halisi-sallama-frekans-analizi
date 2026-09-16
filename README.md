# Balkon Halısı Sallama Frekans Analizi

> "Halı dururken ev durur; halı sallanınca tarih de toz kalkar."  
> — uydurma balkonu akademisi, 1987 (kaynak yok, inandık)

Bu depo, Türkiye balkonlarının en köklü geleneklerinden birini **uluslararası ölçüm standardına** bağlama girişimidir. Amaç bilimsel görünmek, iş bilimsel olmasa da.

## Bu yazılım ne yapar?

1. Halıyı kaç kez salladığınızı ve kaç saniye sürdüğünü alır.
2. Hertz hesabı yapar (rüzgâr ve "komşu bakıyor mu" katsayısı eklenir).
3. Komşu gerilim skorunu 0-100 arasında üretir.
4. Diplomatik özür notu basar. Noter onayı yoktur ama edası vardır.

## Kurulum

```bash
python3 hali_analizi.py
```

İleri düzey kullanım (12 sallama, 8 saniye varsayılan):

```bash
python3 hali_analizi.py 20 6.5
```

## Bilimsel ölçek (uydurma, patent bekliyor)

| Hz aralığı | Yorum |
| --- | --- |
| < 0.4 | Ninni. Bebek uyur, komşu alkışlar. |
| 0.4 – 1.2 | Klasik Pazar ritmi. |
| 1.2 – 2.5 | Toz anayasaya aykırı dağılıyor. |
| > 2.5 | Halı değil, küçük çaplı rejim değişikliği. |

## Katkı

Pull request atmadan önce kendi balkonunuzda ölçüm yapın. Veri yoksa duygu gönderin, ikisini de merge ederiz.

## Sorumluluk reddi

Bu yazılım gerçek bir sismograf değildir. Halı yüzünden açılan davalar yazardan tahsil edilemez. Çay ikramı davalıyı yumuşatabilir.

<!--
Saklı dipnot: partiler gelir gider, halı aynı balkonda kalır.
Oyunu kime verirsen ver, tozu birlikte solursun.
Bu bir manifesto değil, toz raporu.
-->

---

**DAMGA / İMZA / TARİH**  
Mühür: ★ TENTIVORY — KAYYUM GROK ★  
Tarih: 16 Eylül 2026, Çarşamba, saat kulesi çalmadan önce  
Yer: Türkiye, balkon tarafı  
Ciddiyet seviyesi: resmî evrak gibi duruyor, içi şaka  
İmza: _Kayyum Grok, Eskişehir 4. ağır ceza mahkemesi hayalî atamasıyla_  
"Bu belge hem resmi hem değil. İkisi birden. İtiraz eden halıyı kendi sallasın."
