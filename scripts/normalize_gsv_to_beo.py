#!/usr/bin/env python3
"""Normalize frozen BLOON GSV CSV snapshots into BEO; standard library only."""
from __future__ import annotations
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "normalized" / "gsv_normalized_observations.csv"
SOURCE_REPOSITORY = "stephanus-supandi/bloon_gsv_survey"
EXPECTED_BLOBS = {
    "BLOON_MAP_Taman_Galaxy_master.csv": "be24e04943794dfbf92064ba4c7a9fd4cbb94a37",
    "survey_log.csv": "a66cfa46aac4cc1973247f357184bac75c5e7de6",
    "kranji_master_41_poi.csv": "86e3253ecb07cb6e469968e5cb2a38d8ce92153c"
}
CATEGORY_MAP = {
    "akomodasi / penginapan": "HOS-ACC",
    "apotek": "HLT-PHA",
    "bank": "FIN-COM",
    "barbershop": "PER-BAR",
    "bengkel / servis mobil": "AUT-WRK",
    "detailing / coating mobil": "AUT-DET",
    "f&b": "FNB-RES",
    "jasa kurir / pengiriman": "LOG-COU",
    "kafe": "FNB-CAF",
    "klinik / fisioterapi": "HLT-CLI",
    "klinik gigi": "HLT-CLI",
    "klinik perawatan kulit": "HLT-CLI",
    "kursus komputer": "EDU-CRS",
    "laundry": "PER-LAU",
    "laundry / dry cleaner": "PER-LAU",
    "makanan cepat saji / camilan": "FNB-RES",
    "minimarket": "RET-MIN",
    "minimarket / toko kelontong": "RET-MIN",
    "pedagang minuman / gerobak": "FNB-CAF",
    "percetakan / sticker / label / uv printing / sablon": "PRO-BIZ",
    "refleksi / bekam": "PER-FIT",
    "refleksi / sport massage": "PER-FIT",
    "restoran indonesia / sunda-jawa": "FNB-RES",
    "restoran bakmi": "FNB-RES",
    "restoran bakso": "FNB-RES",
    "restoran bebek goreng": "FNB-RES",
    "restoran mi aceh": "FNB-RES",
    "restoran mi ayam": "FNB-RES",
    "restoran nasi kebuli": "FNB-RES",
    "restoran pempek": "FNB-RES",
    "restoran sate kambing": "FNB-RES",
    "restoran soto mie": "FNB-RES",
    "restoran steak": "FNB-RES",
    "salon kecantikan": "PER-BAR",
    "salon rambut": "PER-BAR",
    "servis komputer": "PER-REP",
    "studio foto / percetakan": "PRO-BIZ",
    "toko ayam / makanan": "RET-GRO",
    "toko baju / clothing store": "RET-SPE",
    "toko baju / distro": "RET-SPE",
    "toko ban / suku cadang motor (kategori perlu cek)": "AUT-TIR",
    "toko bangunan": "PRP-MAT",
    "toko bangunan/cat (dugaan; kategori perlu cek)": "PRP-MAT",
    "toko bayi": "RET-SPE",
    "toko bayi dan perlengkapan anak": "RET-SPE",
    "toko beras": "RET-GRO",
    "toko busana pengantin / muslimah": "RET-SPE",
    "toko cat / bahan bangunan": "PRP-MAT",
    "toko cat / bahan bangunan (dugaan)": "PRP-MAT",
    "toko handphone": "RET-SPE",
    "toko kue / bakery": "FNB-BAK",
    "toko pakaian / denim (dugaan)": "RET-SPE",
    "toko susu / distributor": "RET-GRO",
    "warteg / rumah makan": "FNB-RES",
    "celluler": "RET-SPE",
    "finansial": "FIN-OTH",
    "finansial_gadai": "FIN-PWN",
    "furnitur": "RET-SPE",
    "groseri": "RET-GRO",
    "grosir_hasil_bumi": "RET-WHO",
    "gym": "PER-FIT",
    "hotel": "HOS-ACC",
    "jasa": "PRO-BIZ",
    "jasa_barber": "PER-BAR",
    "jasa_copy": "PRO-BIZ",
    "jasa_otomotif": "AUT-WRK",
    "kesehatan": "HLT-CLI",
    "klinik": "HLT-CLI",
    "konter": "RET-SPE",
    "mall": "HOS-REC",
    "material bangunan": "PRP-MAT",
    "material_bangunan": "PRP-MAT",
    "optik": "HLT-PHA",
    "pastry": "FNB-BAK",
    "ritel_furnitur": "RET-SPE",
    "ritel_helm": "RET-SPE",
    "ritel_plastik": "RET-SPE",
    "ritel_rumah": "RET-SPE",
    "ritel_sembako": "RET-GRO",
    "salon": "PER-BAR",
    "sekolah": "EDU-SCH",
    "toko musik": "RET-SPE"
}
FIELDS = [
    "observation_id",
    "source_repository",
    "source_file",
    "source_blob_sha",
    "source_record_id",
    "source_row_number",
    "name_raw",
    "category_raw",
    "category_code",
    "location_raw",
    "latitude",
    "longitude",
    "observation_date",
    "observation_date_raw",
    "rating_raw",
    "review_count_raw",
    "price_range_raw",
    "opening_hours_raw",
    "operational_status",
    "operational_status_raw",
    "verification_status",
    "verification_status_raw",
    "evidence_type",
    "evidence_reference",
    "duplicate_status",
    "notes",
    "mapping_status"
]

def git_blob_sha(content: bytes) -> str:
    return hashlib.sha1(f"blob {len(content)}\\0".encode("ascii") + content).hexdigest()

def first(row: dict[str, str], *keys: str) -> str:
    for key in keys:
        value = (row.get(key) or "").strip()
        if value:
            return value
    return ""

def normalize_file(filename: str, expected_sha: str) -> list[dict[str, str]]:
    path = RAW / filename
    if not path.is_file():
        raise FileNotFoundError(f"Missing frozen source snapshot: {path}")
    content = path.read_bytes()
    actual_sha = git_blob_sha(content)
    if actual_sha != expected_sha:
        raise ValueError(
            f"Source SHA mismatch for {filename}: expected {expected_sha}, got {actual_sha}. "
            "Review source changes before updating EXPECTED_BLOBS."
        )
    result = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row_number, source in enumerate(csv.DictReader(handle), start=2):
            galaxy = filename == "BLOON_MAP_Taman_Galaxy_master.csv"
            index = row_number - 1
            prefix = "TG" if galaxy else ("SURVEY" if filename == "survey_log.csv" else "KRANJI")
            source_id = first(source, "record_id") if galaxy else first(source, "no")
            source_id = source_id or f"ROW-{index}"
            name = first(source, "nama_usaha") if galaxy else first(source, "poi")
            location = " | ".join(filter(None, (
                first(source, "wilayah_subarea"), first(source, "jalan_lokasi_catatan")
            ))) if galaxy else first(source, "cluster")
            raw_date = first(source, "tanggal_observasi_foto_catatan") if galaxy else first(source, "citra")
            operational_raw = first(source, "status_operasional_catatan") if galaxy else ""
            verification_raw = first(source, "status_verifikasi") if galaxy else ""
            duplicate_raw = first(source, "penanda_duplikat") if galaxy else ""
            category_raw = first(source, "kategori")
            code = CATEGORY_MAP.get(category_raw.casefold(), "UNK-UNK")
            notes = " | ".join(filter(None, (
                first(source, "catatan_visual_dan_konteks"),
                first(source, "sumber_data"), first(source, "catatan_verifikasi")
            ))) if galaxy else (
                "Source row has no explicit evidence-type or verification field; preserve raw snapshot."
            )
            result.append({
                "observation_id": f"GSV-{prefix}-{index:04d}",
                "source_repository": SOURCE_REPOSITORY,
                "source_file": filename,
                "source_blob_sha": actual_sha,
                "source_record_id": source_id,
                "source_row_number": str(row_number),
                "name_raw": name,
                "category_raw": category_raw,
                "category_code": code,
                "location_raw": location,
                "latitude": first(source, "latitude") if galaxy else "",
                "longitude": first(source, "longitude") if galaxy else "",
                "observation_date": raw_date if len(raw_date) == 10 and raw_date[4:5] == "-" and raw_date[7:8] == "-" else "",
                "observation_date_raw": raw_date,
                "rating_raw": first(source, "rating_catatan", "rating"),
                "review_count_raw": first(source, "jumlah_ulasan_catatan"),
                "price_range_raw": first(source, "kisaran_harga_catatan") if galaxy else "",
                "opening_hours_raw": first(source, "jam_operasional_catatan", "jam_buka"),
                "operational_status": "reported_closed" if "dilaporkan tutup" in operational_raw.casefold() else "unknown",
                "operational_status_raw": operational_raw,
                "verification_status": "not_checked" if not verification_raw or "belum diverifikasi" in verification_raw.casefold() else "unresolved",
                "verification_status_raw": verification_raw,
                "evidence_type": "user_note" if galaxy else "other",
                "evidence_reference": f"https://github.com/{SOURCE_REPOSITORY}/blob/master/{filename}#L{row_number}",
                "duplicate_status": "possible_duplicate" if "kemungkinan duplikat" in duplicate_raw.casefold() else "unresolved",
                "notes": notes,
                "mapping_status": "unmapped_review_required" if code == "UNK-UNK" else "mapped_explicit",
            })
    return result

def main() -> int:
    rows = []
    for filename, expected_sha in EXPECTED_BLOBS.items():
        batch = normalize_file(filename, expected_sha)
        print(f"[OK] {filename}: {len(batch)} rows; source SHA verified")
        rows.extend(batch)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    mapped = sum(row["mapping_status"] == "mapped_explicit" for row in rows)
    print(f"[DONE] {len(rows)} rows written to {OUT.relative_to(ROOT)}")
    print(f"[SUMMARY] mapped={mapped}; unmapped_review_required={len(rows)-mapped}")
    print("[NOTE] Rows are not unique-business counts; no automatic OBSERVED/open status.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
