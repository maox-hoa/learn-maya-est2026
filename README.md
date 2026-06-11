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
