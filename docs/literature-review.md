---
layout: default
title: Literature Review — Indic ASR Models
---

# Literature Review: Indic Speech Recognition Models

**Scope.** Models (open and commercial) for automatic speech recognition (ASR) in Indian languages, from the pre-deep-learning foundations (late 2010s) through 2026. Companion to the [awesome list](../README.md). Focus on architectures, training data, multilingual coverage, evaluation, and open gaps.

**Method.** Sources: arXiv, OpenAlex, Semantic Scholar, and the project repositories linked below. Inclusion: a paper or official page documenting a model or a method specifically evaluated on Indic languages. Exclusion: datasets/benchmarks without a model (those live in the main list).

## 1. Background

India has 22 scheduled languages, hundreds of dialects, heavy code-mixing with English, and speech captured over telephone, outdoors, and in noisy rooms. Models trained on English or clean read speech transfer poorly. The field has moved from monolingual HMM-GMM/Kaldi pipelines and early DNN acoustic models, through multilingual self-supervised encoders, to speech LLMs and audio-native foundation models.

## 0. Foundations (pre-2021)

Before the current wave, Indian-language ASR was built on **HMM-GMM and hybrid DNN-HMM systems** (Kaldi/HTK recipes), with language-specific acoustic and language models, and small in-house corpora. Key milestones:

- **Babel / GlobalPhone era (2010s).** Indian languages (e.g. Tamil, Hindi) appeared in multilingual data-collection programmes and the GlobalPhone corpus, giving the first cross-language acoustic models.
- **IIIT-Hyderabad and IIT corpora.** Early read-speech datasets for Telugu, Hindi and other languages, plus festival/TTS-aligned resources, fed the first monolingual recognisers.
- **NPTEL2020** — Indian-English lecture speech benchmark and dataset (2020). — [Repo](https://github.com/AI4Bharat/NPTEL2020-Indian-English-Speech-Dataset).
- **MUCS 2021** — first large multilingual + code-switching challenge for low-resource Indian languages (6 languages + 2 code-switched pairs), marking the transition to end-to-end models. — [arXiv:2104.00235](https://arxiv.org/abs/2104.00235).
- **Vakyansh / CLSRIL-23** and **IndicWav2Vec** (2021) brought self-supervised pretraining to Indic ASR, setting the template (raw-speech pretraining → fine-tuning) still used today. — [arXiv:2107.07402](https://arxiv.org/abs/2107.07402) · [arXiv:2111.03945](https://arxiv.org/abs/2111.03945).

For a broader survey of this transition, see *Decoding the Diversity: A Review of the Indic AI Research Landscape* — [arXiv:2406.09559](https://arxiv.org/abs/2406.09559).

## 2. Model families

### 2.1 Self-supervised pretraining (wav2vec 2.0 / Conformer)

- **IndicWav2Vec** (AI4Bharat). Pretrained on ~17,000 h of raw speech across 40 Indian languages; fine-tuned for ASR on 9 languages. State of the art on very low-resource languages (Sinhala, Nepali) at release. *Javed et al., 2021* — [arXiv:2111.03945](https://arxiv.org/abs/2111.03945).
- **IndicConformer** (AI4Bharat). 600M-parameter Conformer with hybrid CTC + RNN-T decoding, 22 scheduled languages. Open weights on Hugging Face. — [Code](https://github.com/AI4Bharat/IndicConformerASR).
- **CLSRIL-23 / Vakyansh** (EkStep). wav2vec 2.0 pretraining over 23 Indian languages. — [arXiv:2107.07402](https://arxiv.org/abs/2107.07402) · [Models](https://github.com/Open-Speech-EkStep/vakyansh-models).
- **IndicWhisper** (AI4Bharat). Whisper fine-tuned on the Vistaar training set for 12 languages. — [Code](https://github.com/AI4Bharat/vistaar).

### 2.2 Encoder–decoder multilingual (Whisper family)

- **Whisper** (OpenAI). ~99-language encoder–decoder; strong zero-shot baseline on Indic languages but weaker on low-resource and code-mixed speech. — [arXiv:2212.04356](https://arxiv.org/abs/2212.04356).
- **OWSM** (CMU/ESPnet). Open Whisper-style multilingual model. — [arXiv:2309.13876](https://arxiv.org/abs/2309.13876).
- **SeamlessM4T v2** (Meta). Multitask speech/text translation and recognition. — [arXiv:2308.11596](https://arxiv.org/abs/2308.11596).

### 2.3 Massively multilingual (Meta)

- **MMS** (Meta). wav2vec 2.0 + CTC with per-language adapters across 1,100+ languages, including most Indic ones. — [arXiv:2305.13516](https://arxiv.org/abs/2305.13516).
- **Omnilingual ASR** (Meta). 300M–7B open models for 1,600+ languages (Apache 2.0), reaching the long tail beyond the 22 scheduled languages. — [arXiv:2511.09690](https://arxiv.org/abs/2511.09690).

### 2.4 Speech LLMs and audio-native foundation models

- **Sarvam** — Saaras v3/v4 and Saarika v2.5. Indic speech-LLM systems; vendor-reported SOTA across 22 Indian languages. See the [Saaras v4 announcement](https://www.sarvam.ai/blogs/introducing-saaras-v4) and the [Indic DiarBench post](https://www.sarvam.ai/blogs/indic-diarbench).
- **Google** — Cloud Speech-to-Text (Chirp/USM) and Gemini audio models. — [arXiv:2303.01037](https://arxiv.org/abs/2303.01037).
- **OpenAI** — gpt-4o-transcribe family and the Whisper API.
- Other baselines frequently evaluated: ElevenLabs Scribe, Deepgram, AssemblyAI, Azure Speech, AWS Transcribe, Bhashini.

### 2.5 Specialised / domain models

- **SCRIBE** (Manohar et al.). Rich-transcription models for Hindi, Malayalam, Kannada with categorical error decomposition (lexical, punctuation, numeral, domain-entity). *Interspeech 2026* — [arXiv:2605.20712](https://arxiv.org/abs/2605.20712).
- **TTS–STT flywheel** (Menta). LoRA fine-tuning on entity-dense synthetic Telugu/Hindi/Tamil audio; large gains on niche domains (digits, currency, addresses) at low cost. — [arXiv:2605.03073](https://arxiv.org/abs/2605.03073).
- **SraVaani 1.0** — scaling inclusive speech recognition for Indic languages. — [arXiv:2608.08235](https://arxiv.org/abs/2608.08235).

## 3. Training data and multilingual coverage

| Corpus | Languages | Size / notes | Link |
|---|---|---|---|
| IndicVoices | 22 | 7,348 h (paper release), 16,237 speakers, 145 districts | [arXiv:2403.01926](https://arxiv.org/abs/2403.01926) · [HF](https://huggingface.co/datasets/ai4bharat/IndicVoices) |
| Shrutilipi | 12 | ~6,400 h mined from All India Radio | [arXiv:2208.12666](https://arxiv.org/abs/2208.12666) |
| Vaani | 100+ | District-level, image-prompted; target 150k h speech / 15k h transcribed | [site](https://vaani.iisc.ac.in) · [HF](https://huggingface.co/datasets/ARTPARK-IISc/Vaani) |
| Kathbath | 12 | 1,684 h read speech | [arXiv:2208.11761](https://arxiv.org/abs/2208.11761) |
| IndicVoices-R | 22 | 1,704 h TTS-quality subset | [arXiv:2409.05356](https://arxiv.org/abs/2409.05356) |
| Raw pretraining (IndicWav2Vec) | 40 | 17,000 h raw speech | [arXiv:2111.03945](https://arxiv.org/abs/2111.03945) |

Coverage of all 22 scheduled languages is now routine for the major open models (IndicVoices, IndicConformer, Indic DiarBench). The long tail (Bodo, Dogri, Kashmiri, Konkani, Maithili, Manipuri, Santali, Sindhi) is the remaining frontier, addressed by massively multilingual models such as Omnilingual ASR.

## 4. Evaluation and metrics

- **WER** remains the default but is inflated for agglutinative languages and by spelling variation.
- **CER** is more stable across scripts; report alongside WER.
- **OIWER** (orthographically-informed WER) accepts multiple valid spellings and either-script English words; used by Voice of India and Monsoon hi-IN.
- **SN-WER** (script-normalised WER) transliterates both reference and hypothesis into a canonical script before scoring; reduces inflated gaps by up to 12% on FLEURS. — [arXiv:2606.02548](https://arxiv.org/abs/2606.02548).
- **cpWER / DER** for multi-speaker transcription with diarization (Indic DiarBench).
- **LLM-judged metrics** proposed for semantic correctness; not yet standard.

**Normalisation pitfalls.** Whisper's `BasicTextNormalizer` strips combining marks (matras, viramas) in Indic scripts, inflating scores. Use a script-aware normaliser (Indic NLP Library, Vistaar). Normalise Unicode (NFC/NFKC), nukta, ZWJ consistently. Document the English-word script policy and number policy. Report corpus-level WER.

## 5. Code-switching, accent and low-resource

- **MUCS 2021** — 6 languages + 2 code-switched pairs (Hindi–English, Bengali–English). — [arXiv:2104.00235](https://arxiv.org/abs/2104.00235).
- **Svarah** — Indian-English accent diversity. — [arXiv:2305.15760](https://arxiv.org/abs/2305.15760).
- **Lahaja** — multi-accent Hindi. — [arXiv:2408.11440](https://arxiv.org/abs/2408.11440).
- **HiACC** — code-switched adult and child Hinglish. — [PMC12329218](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12329218/).
- **Dual Script E2E** — common label set for multilingual/code-switched ASR. — [arXiv:2106.01400](https://arxiv.org/abs/2106.01400).
- **Continual learning** for sequential language addition without catastrophic forgetting (EWC/MAS/LwF on IndicSUPERB). — [arXiv:2508.06280](https://arxiv.org/abs/2508.06280).
- **Rural/underserved speakers** — rural Bhojpuri women. — [arXiv:2506.09653](https://arxiv.org/abs/2506.09653).
- **Region/district effects** — geographic distance correlates with WER; district-level reporting. — [arXiv:2606.09345](https://arxiv.org/abs/2606.09345) · Voice of India.

## 6. Benchmarks for model evaluation (see main list)

Voice of India (telephone, 15 langs), Indic DiarBench (meetings/far-field, 22 langs), Monsoon en-IN/hi-IN (Open ASR Leaderboard), FLEURS, Common Voice, IndicVoices, Kathbath, Svarah, Lahaja, MUCS, Gram Vaani, NPTEL2020.

## 7. Trends (2025–2026)

1. Real-world speech (telephone, far-field, in-the-wild) replaces read speech.
2. Spelling-aware metrics (OIWER, SN-WER, multi-reference).
3. Private held-out test sets to limit contamination.
4. Indic languages on global leaderboards (Open ASR Leaderboard).
5. Diarization + ASR jointly (cpWER/DER).
6. Speech LLMs and audio-native foundation models as baselines.
7. Coverage of all 22 scheduled languages + long tail.
8. District/demographic breakdowns.
9. Synthetic speech for fine-tuning (mixed results).
10. Code-switching as the default test condition.

## 8. Open gaps

- Long-tail and low-resource languages (Bodo, Dogri, Kashmiri, Konkani, Maithili, Manipuri, Santali, Sindhi) still under-served by open models.
- Underserved demographics (rural, women, children, elderly) under-represented in training data.
- No single shared normalisation pipeline; vendor numbers not comparable.
- LLM-judged metrics not yet standard; need reporting alongside WER/CER.
- Continual/multilingual training under privacy constraints (no replay) under-explored.
- Entity-dense domains (digits, currency, addresses) remain weak even for commercial systems.
- Script handling in metrics (SN-WER) still being adopted.

## 9. Verified citations

- Javed et al. (2021). Towards Building ASR Systems for the Next Billion Users. [arXiv:2111.03945](https://arxiv.org/abs/2111.03945).
- MUCS 2021. Multilingual and Code-Switching ASR Challenges for Low Resource Indian Languages. [arXiv:2104.00235](https://arxiv.org/abs/2104.00235).
- Dual Script E2E. [arXiv:2106.01400](https://arxiv.org/abs/2106.01400).
- Vakyansh/CLSRIL-23. [arXiv:2107.07402](https://arxiv.org/abs/2107.07402).
- IndicSUPERB/Kathbath. [arXiv:2208.11761](https://arxiv.org/abs/2208.11761).
- Shrutilipi. [arXiv:2208.12666](https://arxiv.org/abs/2208.12666).
- Whisper. [arXiv:2212.04356](https://arxiv.org/abs/2212.04356).
- USM/Chirp. [arXiv:2303.01037](https://arxiv.org/abs/2303.01037).
- Vistaar. [arXiv:2305.15386](https://arxiv.org/abs/2305.15386).
- Svarah. [arXiv:2305.15760](https://arxiv.org/abs/2305.15760).
- MMS. [arXiv:2305.13516](https://arxiv.org/abs/2305.13516).
- SeamlessM4T v2. [arXiv:2308.11596](https://arxiv.org/abs/2308.11596).
- OWSM. [arXiv:2309.13876](https://arxiv.org/abs/2309.13876).
- IndicVoices. [arXiv:2403.01926](https://arxiv.org/abs/2403.01926).
- IndicVoices-R. [arXiv:2409.05356](https://arxiv.org/abs/2409.05356).
- Lahaja. [arXiv:2408.11440](https://arxiv.org/abs/2408.11440).
- Rural Bhojpuri women. [arXiv:2506.09653](https://arxiv.org/abs/2506.09653).
- Omnilingual ASR. [arXiv:2511.09690](https://arxiv.org/abs/2511.09690).
- Continual learning CL. [arXiv:2508.06280](https://arxiv.org/abs/2508.06280).
- Voice of India. [arXiv:2604.19151](https://arxiv.org/abs/2604.19151).
- Indic DiarBench. [arXiv:2607.23808](https://arxiv.org/abs/2607.23808).
- SCRIBE. [arXiv:2605.20712](https://arxiv.org/abs/2605.20712).
- TTS–STT flywheel. [arXiv:2605.03073](https://arxiv.org/abs/2605.03073).
- SN-WER. [arXiv:2606.02548](https://arxiv.org/abs/2606.02548).
- Region-specific data. [arXiv:2606.09345](https://arxiv.org/abs/2606.09345).
- Factors affecting ASR performance. [arXiv:2606.09335](https://arxiv.org/abs/2606.09335).
- Synthetic speech for ASR. [arXiv:2606.17662](https://arxiv.org/abs/2606.17662).
- NPTEL2020 (Indian English lecture speech). [Repo](https://github.com/AI4Bharat/NPTEL2020-Indian-English-Speech-Dataset).
- Decoding the Diversity: A Review of the Indic AI Research Landscape. [arXiv:2406.09559](https://arxiv.org/abs/2406.09559).

---

*Generated as part of the awesome-asr-benchmark project. See [CONTRIBUTING.md](../CONTRIBUTING.md).*