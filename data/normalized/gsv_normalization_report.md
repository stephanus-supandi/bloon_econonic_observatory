# GSV → BEO Normalization Report

Prepared alongside `scripts/normalize_gsv_to_beo.py` from the pinned source snapshots. The script rebuilds the normalized CSV; this report records the reviewed crosswalk and provenance for this generated dataset.

## Input provenance

| Source file | Rows | Git blob SHA |
|---|---:|---|
| `BLOON_MAP_Taman_Galaxy_master.csv` | 69 | `be24e04943794dfbf92064ba4c7a9fd4cbb94a37` |
| `survey_log.csv` | 70 | `a66cfa46aac4cc1973247f357184bac75c5e7de6` |
| `kranji_master_41_poi.csv` | 41 | `86e3253ecb07cb6e469968e5cb2a38d8ce92153c` |

The snapshots match the BEO `data/raw/` copies byte-for-byte by Git blob SHA.

## Output

- Normalized source-observation rows: **180**.
- Explicitly mapped rows: **126**.
- Rows requiring category review (`UNK-UNK`): **54**.
- These are source rows, **not unique-business counts**.
- Only exact ISO dates populate `observation_date`; other date labels remain in `observation_date_raw`.
- No row is automatically promoted to observed or currently open.
- Provisional category labels containing "dugaan", "perlu cek", or "perlu konfirmasi" are held at `UNK-UNK`.

## Category crosswalk

| Raw category | Rows | BEO code |
|---|---:|---|
| Akomodasi / penginapan | 1 | HOS-ACC |
| apotek | 4 | HLT-PHA |
| Apotek | 1 | HLT-PHA |
| Bank | 3 | FIN-COM |
| Barbershop | 1 | PER-BAR |
| Bengkel / servis mobil | 1 | AUT-WRK |
| Biro perjalanan / money changer | 1 | UNK-UNK |
| celluler | 4 | RET-SPE |
| Depot air isi ulang | 1 | UNK-UNK |
| Detailing / coating mobil | 1 | AUT-DET |
| F&B | 17 | FNB-RES |
| finansial | 3 | UNK-UNK |
| finansial_gadai | 1 | FIN-PWN |
| furnitur | 2 | UNK-UNK |
| galeri | 1 | UNK-UNK |
| gateway | 1 | UNK-UNK |
| groseri | 2 | RET-GRO |
| Grosir / pengiriman bahan makanan (kategori catatan) | 1 | UNK-UNK |
| grosir_hasil_bumi | 1 | RET-WHO |
| gym | 1 | PER-FIT |
| hotel | 1 | HOS-ACC |
| jasa | 4 | UNK-UNK |
| Jasa kurir / pengiriman | 1 | LOG-COU |
| jasa_barber | 1 | PER-BAR |
| jasa_copy | 2 | PRO-BIZ |
| jasa_otomotif | 2 | UNK-UNK |
| kafe | 7 | FNB-CAF |
| Kafe | 1 | FNB-CAF |
| kesehatan | 6 | HLT-CLI |
| klinik | 3 | HLT-CLI |
| Klinik / fisioterapi | 1 | HLT-CLI |
| Klinik gigi | 1 | HLT-CLI |
| Klinik perawatan kulit | 1 | HLT-CLI |
| Kompleks perumahan | 1 | UNK-UNK |
| konter | 2 | RET-SPE |
| kriya | 2 | UNK-UNK |
| Kursus komputer | 1 | EDU-CRS |
| landmark | 2 | UNK-UNK |
| Laundry | 2 | PER-LAU |
| Laundry / dry cleaner | 1 | PER-LAU |
| Makanan cepat saji / camilan | 1 | FNB-RES |
| mall | 1 | UNK-UNK |
| material bangunan | 1 | PRP-MAT |
| material_bangunan | 1 | PRP-MAT |
| Minimarket | 4 | RET-MIN |
| Minimarket / toko kelontong | 1 | RET-MIN |
| optik | 2 | HLT-PHA |
| Outlet air / herbal (kategori perlu konfirmasi) | 1 | UNK-UNK |
| pasar | 1 | UNK-UNK |
| pastry | 1 | FNB-BAK |
| Pedagang minuman / gerobak | 1 | FNB-CAF |
| Percetakan / sticker / label / UV printing / sablon | 1 | PRO-BIZ |
| Permak / jahit pakaian | 1 | UNK-UNK |
| Refleksi / bekam | 1 | PER-FIT |
| Refleksi / sport massage | 1 | PER-FIT |
| residensial | 3 | UNK-UNK |
| Restoran bakmi | 1 | FNB-RES |
| Restoran bakso | 1 | FNB-RES |
| Restoran bebek goreng | 1 | FNB-RES |
| Restoran Indonesia / Sunda-Jawa | 1 | FNB-RES |
| Restoran mi Aceh | 1 | FNB-RES |
| Restoran mi ayam | 1 | FNB-RES |
| Restoran nasi kebuli | 1 | FNB-RES |
| Restoran pempek | 1 | FNB-RES |
| Restoran sate kambing | 1 | FNB-RES |
| Restoran soto mie | 1 | FNB-RES |
| Restoran steak | 1 | FNB-RES |
| ritel | 10 | UNK-UNK |
| ritel pasar | 1 | UNK-UNK |
| ritel_furnitur | 1 | RET-SPE |
| ritel_helm | 1 | RET-SPE |
| ritel_pasar | 1 | UNK-UNK |
| ritel_plastik | 2 | RET-SPE |
| ritel_rumah | 4 | RET-SPE |
| ritel_sembako | 2 | RET-GRO |
| salon | 1 | PER-BAR |
| Salon kecantikan | 2 | PER-BAR |
| Salon rambut | 1 | PER-BAR |
| sekolah | 1 | EDU-SCH |
| seni | 2 | UNK-UNK |
| Servis komputer | 1 | PER-REP |
| Studio foto / percetakan | 1 | PRO-BIZ |
| Toko ayam / makanan | 1 | RET-GRO |
| Toko baju / clothing store | 1 | RET-SPE |
| Toko baju / distro | 1 | RET-SPE |
| Toko ban / suku cadang motor (kategori perlu cek) | 1 | UNK-UNK |
| Toko bangunan | 1 | PRP-MAT |
| Toko bangunan/cat (dugaan; kategori perlu cek) | 1 | UNK-UNK |
| Toko bayi | 1 | RET-SPE |
| Toko bayi dan perlengkapan anak | 1 | RET-SPE |
| Toko beras | 1 | RET-GRO |
| Toko busana pengantin / muslimah | 1 | RET-SPE |
| Toko cat / bahan bangunan | 1 | PRP-MAT |
| Toko cat / bahan bangunan (dugaan) | 1 | UNK-UNK |
| Toko handphone | 1 | RET-SPE |
| Toko kue / bakery | 1 | FNB-BAK |
| toko musik | 2 | RET-SPE |
| Toko pakaian / denim (dugaan) | 1 | UNK-UNK |
| Toko susu / distributor | 1 | UNK-UNK |
| transit | 1 | UNK-UNK |
| UNVERIFIED | 2 | UNK-UNK |
| Usaha belum teridentifikasi | 2 | UNK-UNK |
| Usaha otomotif / motor (dugaan) | 1 | UNK-UNK |
| vacant | 1 | UNK-UNK |
| Warteg / rumah makan | 1 | FNB-RES |

## Limitations

This deterministic crosswalk is not independent verification of businesses, pins, coordinates, occupancy, or current operation. Original source wording and provenance are retained.
