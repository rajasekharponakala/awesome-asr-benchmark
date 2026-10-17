---
layout: default
title: NLP and Techno-Linguistic Considerations
---

# NLP and Techno-Linguistic Considerations for Indic ASR

ASR is not only acoustic modelling. Indian languages pose NLP and linguistic challenges that shape both model design and evaluation. This page collects them; the [literature review](literature-review.md) covers models and benchmarks.

## 1. Script and orthography

- **Unicode normalisation.** NFC/NFKC, nukta forms, zero-width joiners (ZWJ/ZWNJ), and matra/virama ordering must be handled identically on references and hypotheses. Inconsistent normalisation alone can move WER several points.
- **Conjuncts and viramas.** Brahmic scripts build consonant clusters with viramas; Whisper's `BasicTextNormalizer` strips combining marks, inflating scores. Use script-aware normalisers (Indic NLP Library, Vistaar).
- **Multiple scripts for one language.** Urdu (Perso-Arabic) vs. Hindi (Devanagari); Romanised Hindi; Kashmiri, Sindhi, Manipuri scripts. Models and metrics must declare a script policy.
- **English words in native script vs. Latin.** A single policy (native, Latin, or both accepted) must be documented and used in OIWER/SN-WER.

## 2. Tokenisation and subword units

- **Subword vocabularies** (BPE, SentencePiece, Unigram) trained on English-centric corpora under-represent Indic scripts; rare conjuncts become many tokens.
- **Script-aware tokenisers** (e.g. IndicBERT-style, Aksharantar) and byte-level models (UTF-8) reduce cross-script token-budget disparities.
- **Morpheme- and akshara-aware segmentation** can improve both LM and ASR decoding for agglutinative languages.

## 3. Transliteration and romanisation

- **Romanised Indic** is common in SMS, social media and code-mixed speech; ASR hypotheses may be romanised while references are native-script.
- **SN-WER** and transliteration pipelines (Aksharantar, IndicXlit) reconcile scripts before scoring.
- **Cross-script transfer:** shared phoneme spaces across scripts (e.g. Hindi–Urdu) enable multilingual modelling.

## 4. Code-switching linguistics

- **Matrix vs. embedded language**, switching points, and intra-word mixing (e.g. "download kar do").
- **Hinglish/Tanglish** are not noise but a register; models must handle embedded English phonology and grammar.
- **Language identification (LID)** at utterance or frame level is a prerequisite for routed/multilingual decoding.

## 5. Morphology and sandhi

- **Agglutination** (Tamil, Malayalam, Telugu, Kannada) makes WER word-based and unfair; CER and morpheme-aware metrics help.
- **Sandhi** (phonological merging at word boundaries in Sanskrit-derived languages) means one spoken unit maps to multiple written words.
- **Compound words and reduplication** need consistent segmentation policy in references.

## 6. Numerals, entities and formatting

- **Digits vs. words** and Indic vs. Latin digits must be normalised consistently.
- **Named entities** (names, places, brands, addresses, currency) dominate real-world error cost (see TTS–STT flywheel work).
- **Punctuation, capitalisation and casing** are usually absent from references but matter for downstream use; SCRIBE-style rich transcription addresses this.

## 7. Dialect, register and socio-linguistics

- **Dialect and accent** variation across districts and social groups; geographic distance correlates with WER.
- **Register, formality, and gender/age skew** in training data produce uneven performance.
- **Underserved speakers** (rural, women, children, elderly) are under-represented; district-level reporting exposes gaps.

## 8. Evaluation beyond WER

- **Semantic correctness** via LLM judges (proposed, not standard).
- **Downstream utility:** search, indexing, MT, summarisation, named-entity extraction on transcripts.
- **Fairness metrics** across demographic groups and regions.
- **Human cost of errors:** entity errors cost more than function-word errors.

## 9. Open gaps

- No shared, script-aware normalisation pipeline across the ecosystem.
- Tokenisers and LMs still English-centric; Indic-aware segmentation under-explored.
- Code-switching treated as noise rather than a first-class linguistic phenomenon in many evaluations.
- Socio-linguistic coverage (dialect, gender, age, region) rarely reported.
- Semantic/downstream evaluation not standardised.

See also the [glossary](glossary.md) and [literature review](literature-review.md).