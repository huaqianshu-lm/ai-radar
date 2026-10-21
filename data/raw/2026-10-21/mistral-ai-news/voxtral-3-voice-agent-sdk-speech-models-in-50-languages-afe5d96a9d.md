---
title: "Voxtral 3: Voice Agent SDK & Speech Models in 50+ Languages"
url: "https://mistral.ai/news/voxtral-3"
source_url: "https://mistral.ai/news/voxtral-3"
canonical_url: "https://mistral.ai/news/voxtral-3"
source: "Mistral AI News"
source_type: "official"
published_at: ""
fetched_at: "2026-10-21T01:22:03+00:00"
content_type: "markdown"
is_list_page: false
---

Merci de recevoir ce patient pour un avis dermatologique. Traitement en cours : crème à l’hydrocortisone. Dr Martin, Clinique du Parc.

Agent

It says, "Merci de recevoir ce patient pour un avis dermatologique." Your doctor is asking a dermatologist, Dr Martin, to see you. The next slot is Tuesday at 5:45 pm. Shall I book it?

Tool call

book\_appointment(slot="Nov 3 17:45")

Result

confirmed

Agent

Done. Bring the letter, your carte Vitale, and I'll text you the details in English.

Voxtral 3

Béatrice

Hi, my doctor gave me a referral letter in French. Can you book it for me?

Béatrice

4402... sorry, 4420 1187.

Béatrice

Yes, please.

Thinking

Summary

Voxtral 3 introduces a cutting-edge voice agent SDK and state-of-the-art speech models designed for real-time, multi-step conversations across 50+ languages. It combines accurate transcription, natural speech synthesis with emotional adaptability, and deep tool integration for seamless workflow automation. Available via Mistral’s EU-hosted API or self-deployment, it ensures data sovereignty while delivering low-latency, human-like interactions for contact centers, virtual assistants, and hands-free copilots.

Speech transcription and voice generation have come a long way, but building end-to-end voice agents that can listen, reason, interact, and handle complex workflows remains difficult.

A reliable voice agent needs to do four things very well (and simultaneously):

Listen accurately across languages, accents, speakers, and interruptions,

Reasondeeply about what users mean in specific contexts,

Speak naturally with emotion and expression, and

Take action over multiple steps through connected systems.

Getting all four to work together reliably in real time remains a challenge.

To address this, we introduce Voxtral 3: a new family of state-of-the-art speech-to-text and text-to-speech models, alongside a voice agent SDK that brings listening, thinking, tool calling, and speaking into a single real-time streaming pipeline.

Voxtral 3 is built to create natural conversational experiences, from contact-center agents and service desks to virtual assistants and hands-free copilots. With support for dozens of languages, expressive speech, complex reasoning, and deep integration with your own tools and data, agents built with Voxtral can interpret nuanced intent, reason through sophisticated requests, and execute multi-step actions across connected systems.

As with other Mistral models, the Voxtral 3 family is designed for sovereign deployment. Available today through Mistral's EU-hosted API or for self-deployment on your own infrastructure, it gives organizations control over where audio is processed, how data is handled, and whether conversations are retained.

Highlights

Accurate transcription across 50+ languages. The speech-to-text model, Voxtral Small Transcribe 3, is state-of-the-art in multilingual transcription, identifying who said what (diarization), using keyphrases to improve its accuracy (context-biasing). It detects when someone has finished speaking so agents can respond without delay (end-of-turn detection).

Natural speech that adapts to the conversation. The text-to-speech model, Voxtral Mini TTS 3, introduces new voices that adjust their emotion, pace, and emphasis based on conversational context, with support for 35+ languages and 50+ dialects.

Human-like intelligence at your (spoken) command. The new voice agent SDK combines listening, reasoning, tool calling, and speaking into a real-time experience. Agents can retrieve information, interact with business systems, and complete tasks during live conversations over phone or web.

Pro Voice for distinctly accurate voice adaptation. For professional use cases where basic voice cloning does not suffice, Voxtral’s Pro Voice adaptation is able to reproduce a speaker’s distinctive character, emotional range, and speaking style across languages, using just 30 minutes of audio.

Your voice AI, on your infrastructure. Use Mistral's EU-hosted API or deploy Voxtral 3 on your own infrastructure. Keep sensitive conversations within your environment and control whether any audio is retained.

It hears 50+ languages, with state-of-the-art accuracy.

Voxtral Transcribe 3 represents a significant milestone across transcription, diarization (who spoke when) and context biasing capabilities. The supported list of languages is expanded to 50, including 24 official EU languages and many low-resource Asian and Indic languages.

The Small version achieves state-of-the-art results across diarization and multilingual transcription, including in English, French and Spanish. It outperforms Whisper, Scribe v2 and Gemini 3.5 Transcribe. The Mini variant is 4B parameters, enabling fast and accurate transcriptions at a price of $0.0035/min.

Both models support context biasing, where key terms and free-form text can be given to bias the transcription and improve recall on technical terms. This enables them to be used in production settings with domain-specific vocabulary without the need for fine-tuning.

Voxtral Realtime Transcribe 3 is a realtime transcription model built for agentic use-cases. It achieves high-quality transcriptions at sub-500ms latency in over 35 languages, including with diarization and context biasing.

End-of-turn prediction is natively supported, incorporating both acoustic and semantic information to accurately predict when a user is finished speaking. This allows for low-latency voice agent applications, while minimizing false cut-off rates when the user is prematurely interrupted.

It answers with the right emotion, in your or your customer’s brand's own voice and local dialect.

Voxtral Mini TTS 3.0, available in batch and realtime, achieves state-of-the-art expressiveness and instruction following for 35+ languages and 50+ dialects. At $13 per 1M characters, Voxtral Speech 3 costs less to run than comparable models from OpenAI TTS-1, Deepgram, ElevenLabs Flash and Gemini Flash.

The speech model implicitly interprets the semantic meaning of context better, producing natural speech across a diverse range of emotions and languages. New and improved features include voice cloning from 30+ minutes of sampled audio, custom prompt instruction following (IF), contextual TTS, and a vocabulary library, all of which serve the goal of speech reliability in deployment. Variables for Explicit IF include emotion, pacing, and emphasis.

Prompt

Let's end the debate here: it's GIF.

Let's end the debate here. It's GIF.

Let's end the debate here. It's GIF.

Default

Non-standard phoneme hint: dʒ ɪ f

Prompt

Attends… Ce n’est pas possible. Ce tableau vient de Reims ? Mais alors… C’est celui que ma grand-mère cherchait depuis cinquante ans !

Attends, ce n'est pas possible? Ce tableau vient de Reims? Mais alors, c'est celui que ma grand-mère cherchait depuis 50 ans?

Attends, ce n'est pas possible? Ce tableau viend de Reims? Mais alors? C'est celui que ma grand-mère cherchait depuis 50 ans.

Default

Non-standard phoneme hint: ʁ e i m s

Prompt

Il nostro nuovo assistente si chiama Quivello.

Il nostro nuovo assistente si chiama Quivello.

Il nostro nuovo assistente si chiama Quivello.

Default

Non-standard phoneme hint: tʃ i v ɛ l l o

Prompt

Hallo! Ich bin Xyra, deine persönliche Assistentin.

Hallo, ich bin Xyra, deine persönliche Assistentin.

Hallo, ich bin Xyra, deine persönliche Assistentin.

Default

Non-standard phoneme hint: z aɪ ɹ ə

All natural-sounding speech relies on emotion, which determines its prosody, rhythm, pacing, emphasis, and transitions. Voxtral TTS natively interprets a prompt’s text context to determine the emotion and voice style, making the model inherently better at natural speech without requiring additional instructions or voice prompts.

Illustrating Voxtral hill-climbing in expressiveness, numbers and unique names.

Prompt

Thank you for calling Mistral! I understand you're having difficulty logging into AI Studio. Can I confirm your email address? I have here elena.vance82@yahoo.com, is that correct?

Thank you for calling Mistral I understand you're having difficulty logging into AI Studio. Can I confirm your email address? I have here elena.vance82 @ yahoo.com. Is that correct?

Thank you for calling Mistral. I understand you're having difficulty logging into AI Studio. Can I confirm your email address? I have here elena.vance82 @ yahoo.com. Is that correct?

Voxtral 1

Voxtral 3

Prompt

Gosh that was quick, I've found a flight for your upcoming travel. How about the Emirates flight at 21:00pm on 10/10 returning 10/25 at 22:00pm for £1881? Say the word, and I'll book a window seat now.

Gosh, that was quick. I've found a flight for your upcoming travel. How about the Emirates flight at 21,000pm on 10 over 10, returning 10 over 25 at 22,000pm for £1,881? Say the word and I'll book a window seat now.

Gosh, that was quick. I found a flight for your upcoming travel. How about the Emirates flight at 21pm on October 10th, returning October 25th at 22pm for £1,881? Say the word and I'll book a window seat now.

Voxtral 1

Voxtral 3

Prompt

Wow I can't believe you're pregnant! This is so exciting, congratulations Corina, I'm so happy for you!

Wow, I can't believe you're pregnant. This is so exciting. Congratulations, Karina. I'm so happy for you.

Wow, I can't believe you're pregnant. This is so exciting. Congratulations, Karina. I'm so happy for you.

Voxtral 1

Voxtral 3

Prompt

What do you mean my passport won't be finished this week -- I've told you several times how I need to go to Paris for work. This is ridiculous. I can't even begin to describe how infuriating this has been.

What do you mean my passport won't be finished this week? I've told you several times how I need to go to Paris for work. This is ridiculous. I can't even begin to describe how infuriating this has been.

What do you mean my passport won't be finished this week? I've told you several times how I need to go to Paris for work. This is ridiculous. I can't even begin to describe how infuriating this has been.

Voxtral 1

Voxtral 3

Speech sounds local in 35 languages and over 50 dialects.

Voxtral TTS supports over 35 languages and regional dialects. Our multilingual evals adhere to dialect differences in pronunciation, formal vs. informal register, spelling, verbosity, and locale conventions (time, dates, temperatures, addresses, currencies).

Voxtral 3 multilingual library

Voice Presets are available in 18 languages: Arabic (Emirati, Modern Standard), Brazilian (Portuguese), Catalan, Chinese (Mandarin), Dutch, English (American, British), French (France), German, Greek, Hindi, Italian, Korean, Norwegian, Russian, Spanish (Spain), and Vietnamese.

The voice agent is in control of the whole conversation.

Voxtral 3 introduces a voice agent SDK, built on LiveKit, that runs speech in, reasoning, and speech out as one streaming pipeline. Voxtral Mini Transcribe Realtime 3 listens and detects when the caller has finished speaking, a general model—like Mistral Small—reasons and calls tools, and Voxtral Speech 3 replies in the tone of the conversation so far. No stage waits for the one before it, so each turn completes in under one second, and the agent stops talking when the caller cuts in.

During a call, the agent can verify a caller's identity, check a bill, or book an appointment, using function calling, web search, and retrieval over your own systems. It answers and places calls over SIP, runs in browsers and apps over WebRTC, and connects to the telephony, IVR, and contact-center software you already use.

Each stage is a separate model, so you can change the LLM, the voice, or the language without rewriting the agent, and run the whole stack on Mistral's API in Europe or on your own infrastructure.

Get started.

Voxtral 3 is available today through the Mistral API, hosted through our European, US, and global endpoints.

You can test out voice agents, audio transcription, speech generation, and voice cloning in the Studio playgrounds.

Voice agent API with Mistral Small 4 for reasoning

0.04$/min

Voice agent API with any other reasoning model

0.08$/min

To run the full stack on-premises or in a private cloud, talk to our team.

Voxtral Small Transcribe 3

New

Highest accuracy speech transcription model. State-of-the-art multilingual transcription and diarization, with support for over 50 languages and context biasing.

Transcription

Audio

$0.004

/min

Voxtral Mini Transcribe 3

New

Efficient, low-latency speech transcription model. Supports multilingual transcription, diarization and context biasing in over 50 languages.

Transcription

Audio (Batch)

$0.0035

/min

Voxtral Mini Transcribe Realtime 3

A realtime transcription model built for agentic use-cases, delivering high-quality transcriptions at sub-500ms latency across 40+ languages.

Transcription

Audio

$0.008

/min

Voxtral Speech 3

State-of-the-art expressiveness and instruction following across 35+ languages and 50+ dialects
