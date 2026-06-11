# Nueva Maya

A reformed Latin orthography for Yucatec Maya — designed to preserve all
phonemic distinctions of the ALMG 1984 standard while eliminating the
apostrophe character entirely, making the language fully ASCII-compatible
for digital use.

## The problem with current ALMG orthography

The 1984 ALMG standard uses apostrophes to mark ejective consonants and
glottal stops: `k'`, `t'`, `ch'`, `ts'`, `p'`, and the saltillo `'`.
This creates practical problems:

- apostrophe conflicts with SQL, Python strings, URLs, and filenames
- difficult to type on standard keyboards
- legal name systems often reject the character
- inconsistent rendering across fonts and platforms

## The Nueva Maya solution

Six substitutions, zero apostrophes, 100% phonemic parity:

| IPA | ALMG 1984 | Nueva Maya | Notes |
|-----|-----------|------------|-------|
| /pʼ/ | `p'` | `f` | /f/ absent in native Maya |
| /tʼ/ | `t'` | `d` | /d/ absent in native Maya |
| /kʼ/ | `k'` | `g` | /g/ absent in native Maya |
| /t͡ʃʼ/ | `ch'` | `c` | /c/ unused in ALMG |
| /t͡sʼ/ | `ts'` | `dz` | restores colonial orthography |
| /ʔ/ | `'` (saltillo) | `h` | /h/ freed up since `j` covers /χ/ |

All other characters remain identical to ALMG 1984. The conversion is
fully reversible and automatable.

## Quick comparison
ALMG 1984:   maayaʼ tʼàan    k'iin    ch'iich'    ts'ak
Nueva Maya:  maayah daahn     giin     ciich       dzag

## Vowel system

Yucatec Maya has five base vowels, each appearing in five forms:

| Form | Pattern | Example | Meaning |
|------|---------|---------|---------|
| Short | `a` | `bak` | bone |
| Long | `aa` | `kaan` | sky |
| Long high-tone | `áa` | `gíin` | sun |
| Glottal-stopped | `ah` | `maayah` | Maya |
| Long glottal | `aah` | `oob` (→ `ooh`) | plural suffix |

## Repository structure
nueva-maya/
├── README.md
├── orthography/
│   ├── alphabet.md
│   └── conversion-table.md
├── lessons/
│   └── lesson-01/
│       ├── README.md
│       └── vocabulary.md
└── tools/
└── almg_to_nueva.py
## Lessons

| # | Title | Topics |
|---|-------|--------|
| [01](lessons/lesson-01/) | Xok Yok'ol Maayah Daahn | Greetings, thanks, family, pronouns |

## Design principles

1. **Pure ASCII** — every character has code point ≤127
2. **Repurpose unused letters** — `f d g c` do not exist in native Maya vocabulary
3. **Full phonemic parity** — one-to-one mapping with IPA, no information lost
4. **Maximum backwards compatibility** — only 6 characters change from ALMG
5. **Automatable** — lossless bidirectional conversion by script

## Conversion tool

```bash
python tools/almg_to_nueva.py input.txt output.txt
```

## Status

This is a proposed orthography — not yet officially recognized by INALI
or ALMG. Community feedback from native Yucatec Maya speakers is actively
sought.

## Contributing

Pull requests welcome. Priority needs:
- Native speaker review of phonemic accuracy
- Lesson content (lessons 02+)
- Audio recordings for vocabulary
- Expanded conversion dictionary

## References

- ALMG (1984). *Unified alphabet for Mayan languages of Guatemala.*
- Bricker, V. (1998). *Dictionary of the Maya Language as Spoken in Hocabá.*
- Burns, A. (1983). *An Epoch of Miracles: Oral Literature of the Yucatec Maya.*
- Na'atik Language & Culture Institute — naatikmexico.org

## License

Content: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
Code: [MIT](LICENSE)
