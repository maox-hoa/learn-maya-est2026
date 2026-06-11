# Conversion Table — ALMG 1984 ↔ Nueva Maya

## Consonant substitutions

| ALMG | Nueva Maya | IPA | Example ALMG | Example Nueva |
|------|-----------|-----|-------------|---------------|
| p' | f | /pʼ/ | p'aak | faag |
| t' | d | /tʼ/ | t'aan | daahn |
| k' | g | /kʼ/ | k'iin | giin |
| ch' | c | /t͡ʃʼ/ | ch'iich' | ciich |
| ts' | dz | /t͡sʼ/ | ts'ak | dzag |
| ' (saltillo) | h | /ʔ/ | maaya' | maayah |

## Characters unchanged from ALMG

`p t k b s x j r m n l w y ch ts aa ee ii oo uu`

All tone marks unchanged: `á é í ó ú` (high tone), `à è ì ò ù` (low tone).

## Word examples

| English | ALMG 1984 | Nueva Maya |
|---------|-----------|-----------|
| speech / language | t'àan | daàhn |
| sun / day | k'iin | giin |
| star | eek' | eegh |
| bird | ch'iich' | ciich |
| medicine | ts'ak | dzag |
| tomato | p'aak | faag |
| Maya (language) | maaya' t'àan | maayah daahn |
| free | jáalk'ab | jáalgab |
| jaguar | balam | balam |
| house | nah | nah |
| water | ha' | hah |
| sky | kaan | kaan |

## Automatic conversion rules
p'  →  f
t'  →  d
k'  →  g
ch' →  c
ts' →  dz
'   →  h   (saltillo / glottal stop)

Run: `python tools/almg_to_nueva.py input.txt output.txt`

