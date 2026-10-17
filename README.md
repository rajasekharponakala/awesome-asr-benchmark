# Awesome ASR Benchmark [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of **Automatic Speech Recognition (ASR) benchmarks**, starting with **Indic (Indian-language) ASR**: evaluation sets, training corpora, leaderboards, models, metrics and recent trends.

India has 22 scheduled languages, hundreds of dialects, heavy code-mixing with English, and a lot of speech that arrives over the phone, outdoors, or in noisy rooms. Benchmarks built for English miss most of this, so this list collects the resources made specifically for Indian-language ASR.

_Last updated: October 2026._

---

## Contents

- [Latest Trends (2025–2026)](#-latest-trends-20252026)
- [What's New](#-whats-new)
- [Evaluation Benchmarks](#-evaluation-benchmarks)
  - [Multilingual Indic benchmarks](#multilingual-indic-benchmarks)
  - [Conversational, telephony and diarization](#conversational-telephony-and-diarization)
  - [Accent, dialect and code-switching](#accent-dialect-and-code-switching)
  - [Global multilingual benchmarks with Indic coverage](#global-multilingual-benchmarks-with-indic-coverage)
- [Training Corpora](#-training-corpora)
- [Leaderboards](#-leaderboards)
- [Models](#-models)
  - [Open models](#open-models)
  - [Commercial APIs](#commercial-apis)
- [Metrics and Text Normalization](#-metrics-and-text-normalization)
- [Evaluation Tooling](#-evaluation-tooling)
- [Papers and Surveys](#-papers-and-surveys)
- [Language Coverage](#-language-coverage)
- [Contributing](#contributing)

---

## 🔥 Latest Trends (2025–2026)

1. **Real-world speech instead of read speech.** New benchmarks use unscripted phone calls, far-field recordings and in-the-wild audio rather than clean read sentences. Examples are [Voice of India](https://arxiv.org/abs/2604.19151) (536 h of telephone speech) and [Indic DiarBench](https://arxiv.org/abs/2607.23808) (multi-speaker meetings and far-field audio).
2. **Spelling-aware metrics.** Plain WER penalises valid spelling variants and English words written in either Latin or native script. Newer benchmarks use multi-reference or lattice scoring, such as **OIWER** (orthographically-informed WER) in Voice of India and the Monsoon hi-IN leaderboard set. Some groups have also proposed LLM-based judges for Indic transcripts ([Sarvam](https://www.sarvam.ai/blogs/evaluating-indian-language-asr)).
3. **Private, held-out test sets.** Voice of India and the [Monsoon](https://huggingface.co/datasets/VoiceArena/MonsoonASR-Open-ASR-leaderboard-hi-IN) sets keep private splits to limit test-set contamination of web-scale models, and publish only a small public sample.
4. **Indic languages on global leaderboards.** The Hugging Face [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) added Indian English (Monsoon en-IN) and Hindi (Monsoon hi-IN) in 2026, its first Global South language.
5. **Diarization combined with ASR.** "Who spoke what" is evaluated together with transcription (cpWER/DER-style metrics) for meetings and call-centre audio ([Indic DiarBench](https://arxiv.org/abs/2607.23808)).
6. **Speech LLMs and audio-native foundation models.** Multimodal LLMs (Gemini, GPT-4o-transcribe and similar) and Indic speech-LLM systems (for example Sarvam's Saaras v3/v4) are now routine baselines alongside CTC/RNN-T models.
7. **Coverage of all 22 scheduled languages.** Models and data now target all 22 scheduled languages, including low-resource ones such as Bodo, Dogri, Kashmiri, Konkani, Maithili, Manipuri, Santali and Sindhi ([IndicVoices](https://arxiv.org/abs/2403.01926), [IndicConformer](https://github.com/AI4Bharat/IndicConformerASR)). Very-large-scale models like [Omnilingual ASR](https://arxiv.org/abs/2511.09690) (1,600+ languages) go further into the long tail.
8. **District-level and demographic breakdowns.** Results are reported by region, gender, age and device rather than as one national average ([Vaani](https://vaani.iisc.ac.in), Voice of India). Work on underserved speakers, such as [rural Bhojpuri women](https://arxiv.org/abs/2506.09653), is also growing.
9. **Synthetic speech for fine-tuning.** TTS-generated training data is being tested for low-resource Indic ASR, with mixed results ([2606.17662](https://arxiv.org/abs/2606.17662)).
10. **Code-switching is the default.** Hindi–English, Tamil–English and other mixed speech is treated as a core test condition, not an edge case.

---

## 🆕 What's New

| Date | Item | Notes |
|---|---|---|
| 2026-08 | **Monsoon en-IN / hi-IN** on Open ASR Leaderboard | Indian English and Hindi sets from Voice Arena; public and private splits; Hindi scored with OIWER |
| 2026-08 | **Saaras v4** (Sarvam) | Successor to Saaras v3 and Saarika v2.5; vendor-reported SOTA on 22 Indian languages |
| 2026-07 | **Indic DiarBench** | Joint diarization + ASR benchmark, ~108 h, all 22 scheduled languages (Sarvam + AI4Bharat, Interspeech 2026) |
| 2026-04 | **Voice of India** | 15 languages, 536 h, 36,691 speakers, 139 regional clusters; telephone speech; OIWER (Josh Talks + AI4Bharat) |
| 2025-11 | **Omnilingual ASR** (Meta) | 300M–7B open models for 1,600+ languages; Apache 2.0 |
| 2025-02 | **Vaani × Hugging Face** | IISc/ARTPARK + Google district-level speech data made available on the Hub |

---

## 📊 Evaluation Benchmarks

### Multilingual Indic benchmarks

| Benchmark | Year | Languages | Domain | Notes | Links |
|---|---|---|---|---|---|
| **Vistaar** | 2023 | 12 | Mixed (59 benchmark sets) | Collects test sets across languages and domains; also released IndicWhisper | [Paper](https://arxiv.org/abs/2305.15386) · [Code](https://github.com/AI4Bharat/vistaar) |
| **IndicVoices** | 2024 | 22 | Read, extempore, conversational | 7,348 h (paper release) from 16,237 speakers in 145 districts | [Paper](https://arxiv.org/abs/2403.01926) · [Data](https://huggingface.co/datasets/ai4bharat/IndicVoices) |
| **Kathbath** (IndicSUPERB) | 2022 | 12 | Read speech | 1,684 h; clean and noisy test sets; part of the IndicSUPERB benchmark | [Paper](https://arxiv.org/abs/2208.11761) · [Code](https://github.com/AI4Bharat/IndicSUPERB) |
| **SPRING-INX** | 2023 | 10 | Mixed | Open Indic ASR data and baselines from IIT Madras | [Paper](https://arxiv.org/abs/2310.14654) |

### Conversational, telephony and diarization

| Benchmark | Year | Languages | Domain | Notes | Links |
|---|---|---|---|---|---|
| **Voice of India** | 2026 | 15 | Unscripted telephone | 536 h, 306k utterances; private held-out set; OIWER | [Paper](https://arxiv.org/abs/2604.19151) · [Site](https://ai.joshtalks.com/) |
| **Indic DiarBench** | 2026 | 22 | Meetings, far-field, in-the-wild | ~108 h of multi-speaker audio with overlap and code-mixing; joint diarization + ASR | [Paper](https://arxiv.org/abs/2607.23808) · [Blog](https://www.sarvam.ai/blogs/indic-diarbench) |
| **Monsoon hi-IN / en-IN** | 2026 | Hindi, Indian English | Short conversational clips | 4,888 speakers; public + private splits; used by the Open ASR Leaderboard | [hi-IN data](https://huggingface.co/datasets/VoiceArena/MonsoonASR-Open-ASR-leaderboard-hi-IN) |
| **Gram Vaani** | 2022 | Hindi (regional variants) | Telephone | Interspeech 2022 challenge on spontaneous phone speech | [OpenSLR 118](https://www.openslr.org/118/) |

### Accent, dialect and code-switching

| Benchmark | Year | Languages | Focus | Links |
|---|---|---|---|---|
| **Lahaja** | 2024 | Hindi | Accent/dialect diversity across speakers' native languages | [Paper](https://arxiv.org/abs/2408.11440) · [Data](https://huggingface.co/datasets/ai4bharat/Lahaja) |
| **Svarah** | 2023 | Indian English | Accent diversity across Indian states | [Paper](https://arxiv.org/abs/2305.15760) · [Code](https://github.com/AI4Bharat/Svarah) |
| **NPTEL2020** | 2020 | Indian English | Lecture speech | [Repo](https://github.com/AI4Bharat/NPTEL2020-Indian-English-Speech-Dataset) |
| **MUCS 2021** | 2021 | 6 + 2 code-switched pairs | Multilingual and Hindi–English / Bengali–English code-switching | [Paper](https://arxiv.org/abs/2104.00235) · [OpenSLR 103](https://www.openslr.org/103/) · [OpenSLR 104](https://www.openslr.org/104/) |
| **HiACC** | 2025 | Hinglish | Code-switched adult and child speech | [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12329218/) |

### Global multilingual benchmarks with Indic coverage

| Benchmark | Notes | Links |
|---|---|---|
| **FLEURS** | 102 languages, including many Indic ones; read Wikipedia sentences | [Paper](https://arxiv.org/abs/2205.12446) · [Data](https://huggingface.co/datasets/google/fleurs) |
| **Common Voice** | Crowd-sourced read speech; Indic coverage varies a lot by language | [Site](https://commonvoice.mozilla.org) |

---

## 🗂 Training Corpora

| Corpus | Languages | Size / notes | Links |
|---|---|---|---|
| **IndicVoices** | 22 | Natural speech from 145+ districts; train/valid/test splits | [Data](https://huggingface.co/datasets/ai4bharat/IndicVoices) |
| **Shrutilipi** | 12 | ~6,400 h mined from All India Radio news | [Paper](https://arxiv.org/abs/2208.12666) · [Data](https://huggingface.co/datasets/ai4bharat/Shrutilipi) |
| **Vaani** | 100+ | District-level, image-prompted speech (IISc/ARTPARK + Google); target of 150k h speech and 15k h transcribed | [Site](https://vaani.iisc.ac.in) · [Data](https://huggingface.co/datasets/ARTPARK-IISc/Vaani) |
| **Kathbath** | 12 | 1,684 h read speech | [Data](https://github.com/AI4Bharat/IndicSUPERB) |
| **Vistaar training set** | 12 | Combined public Indic ASR training data | [Code](https://github.com/AI4Bharat/vistaar) |
| **SPRING-INX** | 10 | ~2,000 h | [Paper](https://arxiv.org/abs/2310.14654) |
| **IndicVoices-R** | 22 | 1,704 h, TTS-quality subset (useful for synthetic-data work) | [Paper](https://arxiv.org/abs/2409.05356) |

---

## 🏆 Leaderboards

- [Open ASR Leaderboard (Hugging Face)](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard). Includes Monsoon en-IN in the main average and Monsoon hi-IN in the multilingual view.
- [Vistaar](https://github.com/AI4Bharat/vistaar). Reference results across 59 Indic benchmark sets.
- [Voice of India](https://ai.joshtalks.com/). Held-out national benchmark with breakdowns by region, gender and device.

> ⚠️ Vendor-published numbers (on any benchmark) are usually computed with the vendor's own normalisation. Re-score with one shared pipeline before comparing them.

---

## 🤖 Models

### Open models

| Model | Org | Languages | Architecture | Links |
|---|---|---|---|---|
| **IndicConformer** (600M multilingual) | AI4Bharat | 22 | Conformer, hybrid CTC + RNN-T | [Code](https://github.com/AI4Bharat/IndicConformerASR) · [HF](https://huggingface.co/ai4bharat/indic-conformer-600m-multilingual) |
| **IndicWhisper** | AI4Bharat | 12 | Whisper fine-tuned on Vistaar training data | [Code](https://github.com/AI4Bharat/vistaar) |
| **IndicWav2Vec** | AI4Bharat | 40 (pretrain), 9 (fine-tuned) | wav2vec 2.0 | [Paper](https://arxiv.org/abs/2111.03945) · [Code](https://github.com/AI4Bharat/IndicWav2Vec) |
| **Omnilingual ASR** | Meta | 1,600+ | wav2vec 2.0 encoder + CTC/LLM decoder, 300M–7B | [Paper](https://arxiv.org/abs/2511.09690) · [Code](https://github.com/facebookresearch/omnilingual-asr) |
| **MMS** | Meta | 1,100+ | wav2vec 2.0 + CTC with per-language adapters | [Paper](https://arxiv.org/abs/2305.13516) |
| **Whisper** (large-v3 / turbo) | OpenAI | ~99 | Encoder–decoder | [Paper](https://arxiv.org/abs/2212.04356) · [Code](https://github.com/openai/whisper) |
| **SeamlessM4T v2** | Meta | ~100 | Multitask speech/text | [Paper](https://arxiv.org/abs/2308.11596) |
| **OWSM** | CMU / ESPnet | Multilingual | Open Whisper-style model | [Paper](https://arxiv.org/abs/2309.13876) |
| **Vakyansh / CLSRIL-23** | EkStep | 23 | wav2vec 2.0 | [Paper](https://arxiv.org/abs/2107.07402) · [Models](https://github.com/Open-Speech-EkStep/vakyansh-models) |

### Commercial APIs

Commonly used as baselines in Indic benchmarks. Check each provider's current docs for language support.

- **Sarvam:** Saaras v4 / v3, Saarika v2.5 (legacy). See [Saaras v4 announcement](https://www.sarvam.ai/blogs/introducing-saaras-v4).
- **Google:** Cloud Speech-to-Text (Chirp / USM, [paper](https://arxiv.org/abs/2303.01037)) and Gemini audio models.
- **OpenAI:** gpt-4o-transcribe family and the Whisper API.
- **Others** frequently evaluated: ElevenLabs Scribe, Deepgram, AssemblyAI, Azure Speech, AWS Transcribe and Bhashini.

---

## 📏 Metrics and Text Normalization

| Metric | When to use |
|---|---|
| **WER** | The default, but it is inflated for agglutinative languages (Tamil, Malayalam, Telugu, Kannada) and by spelling variation. |
| **CER** | More stable across scripts and for morphologically rich languages. Report it next to WER. |
| **OIWER** (orthographically-informed WER) | Accepts multiple valid spellings and either-script English words. Used by Voice of India and Monsoon hi-IN. |
| **cpWER / DER** | Multi-speaker transcription together with diarization (Indic DiarBench). |
| **LLM-judged metrics** | Proposed for semantic correctness of Indic transcripts. Not yet standard; report alongside WER/CER, not instead of them. |

**Normalisation pitfalls specific to Indic scripts:**

- Whisper's `BasicTextNormalizer` strips combining marks (matras, viramas) in Indic scripts. Scores look much better than they really are. Use a script-aware normaliser instead (for example the [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library) or the normalisation in [Vistaar](https://github.com/AI4Bharat/vistaar)).
- Normalise Unicode (NFC/NFKC), nukta forms and zero-width joiners the same way on references and hypotheses.
- Choose and document one policy for English words: native script, Latin script, or both accepted.
- Handle numbers consistently: digits vs. words, and Indic vs. Latin digits.
- Report **corpus-level** WER, not the mean of per-utterance WER.

---

## 🛠 Evaluation Tooling

- [jiwer](https://github.com/jitsi/jiwer): WER/CER computation.
- [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library): script-aware normalisation and tokenisation.
- [Vistaar](https://github.com/AI4Bharat/vistaar): end-to-end Indic ASR evaluation scripts.
- [Open ASR Leaderboard code](https://github.com/huggingface/open_asr_leaderboard): reproducible evaluation harness.
- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo), [ESPnet](https://github.com/espnet/espnet), [SpeechBrain](https://github.com/speechbrain/speechbrain), [k2 / icefall](https://github.com/k2-fsa/icefall): training and inference toolkits.

---

## 📚 Papers and Surveys

**2026**
- Voice of India: A Large-Scale Benchmark for Real-World Speech Recognition in India. [arXiv:2604.19151](https://arxiv.org/abs/2604.19151)
- Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages. [arXiv:2607.23808](https://arxiv.org/abs/2607.23808)
- Factors affecting ASR performance: A study using state of the art ASR models in Indic Languages. [arXiv:2606.09335](https://arxiv.org/abs/2606.09335)
- An Analysis of the Effectiveness of Synthetic Speech Data for ASR Fine-tuning in Selected Indic Languages. [arXiv:2606.17662](https://arxiv.org/abs/2606.17662)

**2025**
- Omnilingual ASR: Open-Source Multilingual Speech Recognition for 1600+ Languages. [arXiv:2511.09690](https://arxiv.org/abs/2511.09690)
- Recognizing Every Voice: Towards Inclusive ASR for Rural Bhojpuri Women. [arXiv:2506.09653](https://arxiv.org/abs/2506.09653)

**2024 and earlier**
- IndicVoices: Towards building an Inclusive Multilingual Speech Dataset for Indian Languages. [arXiv:2403.01926](https://arxiv.org/abs/2403.01926)
- IndicVoices-R: Unlocking a Massive Multilingual Multi-speaker Speech Corpus for Scaling Indian TTS. [arXiv:2409.05356](https://arxiv.org/abs/2409.05356)
- LAHAJA: A Robust Multi-accent Benchmark for Evaluating Hindi ASR Systems. [arXiv:2408.11440](https://arxiv.org/abs/2408.11440)
- Decoding the Diversity: A Review of the Indic AI Research Landscape. [arXiv:2406.09559](https://arxiv.org/abs/2406.09559)
- Vistaar: Diverse Benchmarks and Training Sets for Indian Language ASR. [arXiv:2305.15386](https://arxiv.org/abs/2305.15386)
- Svarah: Evaluating English ASR Systems on Indian Accents. [arXiv:2305.15760](https://arxiv.org/abs/2305.15760)
- IndicSUPERB: A Speech Processing Universal Performance Benchmark for Indian languages. [arXiv:2208.11761](https://arxiv.org/abs/2208.11761)
- Towards Building ASR Systems for the Next Billion Users (IndicWav2Vec). [arXiv:2111.03945](https://arxiv.org/abs/2111.03945)
- MUCS 2021: Multilingual and Code-Switching ASR Challenges for Low Resource Indian Languages. [arXiv:2104.00235](https://arxiv.org/abs/2104.00235)

---

## 🌐 Language Coverage

The 22 languages in the Eighth Schedule of the Indian Constitution:

Assamese · Bengali · Bodo · Dogri · Gujarati · Hindi · Kannada · Kashmiri · Konkani · Maithili · Malayalam · Manipuri · Marathi · Nepali · Odia · Punjabi · Sanskrit · Santali · Sindhi · Tamil · Telugu · Urdu

Benchmarks that cover **all 22**: IndicVoices, Indic DiarBench. Most other sets cover the 10–15 most widely spoken languages. Indian English and Hinglish are evaluated separately (Svarah, NPTEL2020, Monsoon en-IN, MUCS, HiACC).

---

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Please include the year, the languages covered, the size, the license, and a link to the paper or dataset.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is released under [CC0 1.0](LICENSE). Each linked dataset and model has its own license.
