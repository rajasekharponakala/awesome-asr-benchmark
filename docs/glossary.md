---
layout: default
title: Glossary
---

# Glossary — ASR and Indic Speech Terms

**ASR (Automatic Speech Recognition).** Converting spoken audio into text.

**Accent / dialect.** Regional variation in pronunciation; a major source of error in Indic ASR.

**Agglutinative language.** A language (Tamil, Malayalam, Telugu, Kannada) that builds words by concatenating morphemes; inflates WER.

**Babel / GlobalPhone.** Early multilingual speech corpora/programmes (2010s) that included Indian languages.

**CER (Character Error Rate).** Edit distance at character level; more stable than WER for Indic scripts.

**Code-mixing / code-switching.** Mixing two languages in one utterance (e.g. Hindi–English Hinglish); the default condition in India.

**Conformer.** Transformer variant combining self-attention with convolution; backbone of IndicConformer.

**CTC (Connectionist Temporal Classification).** Loss/decoding for sequence models that aligns audio frames to text without explicit segmentation.

**cpWER (concatenated minimum-permutation WER).** WER for multi-speaker transcription after optimal speaker assignment.

**DER (Diarization Error Rate).** Error in "who spoke when".

**Diarization.** Partitioning audio into speaker turns.

**HMM-GMM.** Hidden Markov Model with Gaussian Mixture acoustic models; the pre-deep-learning standard.

**Indic (Indian) languages.** The 22 scheduled languages of India plus Indian English and Hinglish.

**Kaldi.** Open-source toolkit for hybrid HMM-DNN ASR; long-standing standard before end-to-end models.

**LLM-judged metric.** Using a language model to score semantic correctness of transcripts; proposed, not yet standard.

**MUCS.** Multilingual and Code-Switching ASR Challenge (2021) for low-resource Indian languages.

**OIWER (Orthographically-Informed WER).** WER accepting multiple valid spellings and either-script English words; used by Voice of India and Monsoon hi-IN.

**RNN-T (RNN Transducer).** Streaming-friendly end-to-end ASR architecture; used in hybrid decoding.

**Scheduled languages.** The 22 languages in the Eighth Schedule of the Indian Constitution.

**Self-supervised pretraining.** Training on raw speech (e.g. wav2vec 2.0) before fine-tuning on labelled ASR data.

**SN-WER (Script-Normalised WER).** WER after transliterating reference and hypothesis to a canonical script.

**Speech LLM.** A large language model that also processes audio (e.g. Saaras, Gemini audio).

**TTS (Text-to-Speech).** Generating speech from text; used to create synthetic training data.

**Vistaar.** AI4Bharat benchmark suite covering 59 Indic benchmark sets.

**wav2vec 2.0.** Self-supervised speech representation model; basis of IndicWav2Vec, MMS, Omnilingual ASR.

**WER (Word Error Rate).** Edit distance at word level; the default metric but inflated for agglutinative languages.

**Tokenisation.** Splitting text into subword/word units for model input.

**Transliteration.** Converting text from one script to another (e.g. Devanagari to Latin).

**Virama / halant.** Combining mark that suppresses the inherent vowel and forms conjuncts in Brahmic scripts.

**ZWJ / ZWNJ.** Zero-width joiner/non-joiner controlling conjunct formation in Indic scripts.