---
title: "LFM2.5-VL-3B for Better and Faster Vision Capabilities for the Edge"
url: "https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b"
source_url: "https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b"
canonical_url: "https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b"
source: "Hugging Face Blog"
source_type: "developer"
published_at: "2026-08-12T14:00:51+00:00"
fetched_at: "2026-08-13T23:42:16+00:00"
content_type: "markdown"
is_list_page: false
---

# LFM2.5-VL-3B for Better and Faster Vision Capabilities for the Edge

LFM2.5-VL-3B extends the vision-language capabilities of our previous releases with four major improvements:

- **Screen/UI understanding:** Strong understanding of digital screens across different devices.
- **Grounding:** Improved grounding and object detection with natural language queries.
- **Multi-image input:** Improved reasoning across multiple images.
- **Function calling:** Significantly stronger at function calling, in text-only and vision-text situations.

## How we trained our most capable vision-language model

LFM2.5-VL-3B pairs a SigLIP2 400M NaFlex vision encoder with the same pre-trained backbone as our LFM2.5-2.6B text model. It is pre-trained on about 34T tokens, with 4x more vision data than before, drawn from curated and synthetic image-caption, OCR, grounding, and instruction-following sets. To support non-Latin scripts, we doubled the vocabulary to 128K by extending the tokenizer in place rather than retraining from scratch.

Post-training runs in two stages: First is supervised fine-tuning (SFT), with knowledge distillation from a larger teacher and Antidoom training. Second is multi-reward reinforcement learning (RL).

## Benchmark results

We evaluated LFM2.5-VL-3B across both vision and text benchmarks.

The **vision benchmarks** cover multilingual visual comprehension, instruction following, visual math and scientific reasoning, document understanding, object detection, multi-image understanding, and screen understanding. LFM2.5-VL-3B leads its size class on real-world image tasks, while also reading digital content well, from documents and charts to on-screen UI elements.

| Task | Benchmark | LFM2.5-VL-3B (3.1B) | LFM2-VL-3B (3.1B) | gemma-4-E2B-it (5.1B) | gemma-4-E4B-it (8B) | InternVL 3.5 2B (2.4B) | InternVL 3.5 4B (4.7B) | Qwen3.5-2B (2.3B) | Qwen3.5-4B (4.7B) | 
|---|---|---|---|---|---|---|---|---|---|
| **General** | **MMStar** | 63.3 | 57.7 | 45.3 | 52.9 | 57.7 | 65.5 | 55.1 | 59.3 | 
|  | **MME** | 73.1 | 73.0 | 54.9 | 67.6 | 73.6 | 81.0 | 76.2 | 79.5 | 
|  | **RealWorldQA** | 73.1 | 71.1 | 60.0 | 64.3 | 61.6 | 67.7 | 65.1 | 67.1 | 
|  | **SimpleVQA** | 35.4 | 33.0 | 27.3 | 30.4 | 30.5 | 33.7 | 35.2 | 40.7 | 
|  | **SEED-Bench (image)** | 77.7 | 76.6 | 71.4 | 75.3 | 75.4 | 76.4 | 75.8 | 76.1 | 
|  | **MMBench (dev EN v1.1)** | 81.0 | 80.0 | 64.2 | 71.6 | 76.2 | 81.1 | 73.1 | 78.4 | 
|  | **CountBenchQA** | 87.3 | 92.2 | 70.4 | 80.5 | 70.4 | 82.5 | 83.8 | 86.7 | 
| **Multilingual** | **MMMB** | 83.0 | 81.9 | 73.3 | 80.4 | 76.3 | 81.5 | 75.9 | 82.0 | 
|  | **Multilingual MMBench** | 79.5 | 76.3 | 62.8 | 71.2 | 70.9 | 76.6 | 69.9 | 77.0 | 
| **Multimodal IF** | **MM-IFEval** | 60.6 | 51.4 | 65.6 | 68.2 | 47.1 | 54.5 | 55.4 | 63.1 | 
| **STEM** | **LogicVista** | 37.4 | 32.2 | 29.5 | 34.5 | 30.9 | 36.2 | 34.0 | 37.6 | 
|  | **MathVista (mini)** | 68.5 | 62.1 | 37.8 | 45.2 | 56.8 | 67.1 | 48.7 | 63.6 | 
|  | **MMMU-Pro** | 30.5 | 28.7 | 26.9 | 32.6 | 21.3 | 22.7 | 24.9 | 36.0 | 
|  | **MMMU (val)** | 48.4 | 45.6 | 41.1 | 49.3 | 52.0 | 60.7 | 44.1 | 50.3 | 
| **Document, OCR & Chart** | **ChartQA (test)** | 81.3 | 80.4 | 43.2 | 42.1 | 81.7 | 86.2 | 78.4 | 84.2 | 
|  | **DocVQA (val)** | 91.1 | 89.8 | 85.7 | 87.4 | 88.4 | 91.8 | 92.6 | 94.8 | 
|  | **InfographicVQA (val)** | 70.2 | 67.8 | 54.4 | 60.9 | 69.3 | 76.9 | 73.5 | 80.3 | 
|  | **OCRBench v1** | 84.2 | 81.7 | 70.2 | 73.5 | 83.9 | 82.0 | 84.4 | 85.6 | 
|  | **OCRBench v2 (En)** | 47.5 | 43.9 | 44.4 | 48.8 | 45.5 | 49.1 | 47.7 | 58.7 | 
|  | **TextVQA (val)** | 84.3 | 83.0 | 62.5 | 69.0 | 76.6 | 77.5 | 77.3 | 81.2 | 
| **Grounding** | **RefCOCO-avg** | 87.9 | 57.1 | 67.3 | 72.1 | 82.9 | 88.8 | 78.5 | 86.6 | 
| **Multi-Image** | **BLINK** | 61.5 | 50.2 | 45.2 | 52.2 | 52.0 | 57.2 | 48.6 | 58.7 | 
|  | **MuirBench** | 58.3 | 34.9 | 32.9 | 51.8 | 45.0 | 53.5 | 48.2 | 62.0 | 
| **Hallucination** | **HallusionBench** | 47.2 | 46.4 | 41.8 | 49.8 | 47.6 | 52.1 | 49.3 | 51.7 | 
|  | **POPE** | 88.7 | 89.2 | 84.0 | 86.9 | 88.0 | 88.9 | 88.6 | 86.0 | 
| **GUI** | **ScreenSpot-v2 Desktop** | 78.7 | 6.0 | 28.1 | 45.8 | 79.9 | 82.0 | 63.8 | 76.3 | 
|  | **ScreenSpot-v2 Mobile** | 81.2 | 7.6 | 42.9 | 60.3 | 86.2 | 87.8 | 69.7 | 81.4 | 
|  | **ScreenSpot-v2 Web** | 82.2 | 2.5 | 22.4 | 47.6 | 79.9 | 82.6 | 65.9 | 77.8 | 
| **Average** | **-** | 69.4 | 57.2 | 52.0 | 59.7 | 64.6 | 69.4 | 63.7 | 70.1 | 

*All values in the table are normalized to 0–100. Evaluation is done using vLLM 0.26.0 and each model’s recommended generation parameters when available. Non-reasoning mode is used everywhere, and models are prompted to directly answer without reasoning.

We also evaluated LFM2.5-VL-3B on **text-only benchmarks** for instruction following and tool use. Instruction following climbs across the board, and tool use improves sharply. On tool use, LFM2.5-VL-3B is on par with Gemma-4-E2B and Qwen3.5-2B.

| Task | Benchmark | LFM2.5-VL-3B (3.1B) | LFM2-VL-3B (3.1B) | gemma-4-E2B-it (5.1B) | gemma-4-E4B-it (8B) | InternVL 3.5 2B (2.4B) | InternVL 3.5 4B (4.7B) | Qwen3.5-2B (2.3B) | Qwen3.5-4B (4.7B) | 
|---|---|---|---|---|---|---|---|---|---|
| **Instruction following** | **IFEval** | 82.3 | 72.9 | 83.0 | 87.9 | 32.4 | 35.4 | 73.6 | 86.2 | 
|  | **IFBench** | 25.8 | 20.8 | 34.1 | 39.2 | 24.4 | 24.5 | 28.9 | 33.5 | 
|  | **Multi-IF** | 59.4 | 46.5 | 69.4 | 77.4 | 16.3 | 16.9 | 53.5 | 66.7 | 
| **Tool use & function calling** | **ToolSandbox** | 59.5 | 26.4 | 56.5 | 61.6 | N/A | N/A | 47.7 | 65.0 | 
|  | **BFCL V4** | 32.5 | 20.5 | 33.2 | 40.0 | N/A | N/A | 33.9 | 53.6 | 

*InternVL 3.5 models do not support function-calling.

These results demonstrate that LFM2.5-VL-3B is a strong, general-purpose vision-language model. It covers everyday tasks (captioning, visual question answering, document understanding) and is especially good at grounding objects, reading screens and documents, and calling tools.

## Inference speed on CPU and GPU

LFM2.5-VL-3B ships with day-one support across the inference ecosystem, including llama.cpp, MLX, vLLM, SGLang, and ONNX.

**On-device inference.** LFM2.5-VL-3B decodes 228 tokens/s on an M5 Max and 116 tokens/s on a Ryzen AI Max+ 395, and fits in about 3 GB of memory. It even reaches 20 tokens/s on a Galaxy S26 Ultra, so you can run it fully on-device.

**GPU inference.** LFM2.5-VL-3B keeps latency consistently low and is the fastest on multi-frame inputs.

LFM2.5-VL-3B is also the fastest on output throughput out of all models we tested, reaching about 11K tokens per second at high concurrency. That is roughly 2× the larger 4B-class models and ahead of even the smaller 2B-class models, which adds up to nearly 1B output tokens per day on a single H100.

## How to use LFM2.5-VL-3B

Reach for LFM2.5-VL-3B when you need on-device intelligence for high-volume workloads.

Install the latest version of `transformers` (compatible with `transformers>=5.0.0`):

```
%pip install -q torch torchvision accelerate "transformers>=5.10.1"
```
Then load and run the model:

```
import torch
from transformers.image_utils import load_image
from transformers import AutoModelForImageTextToText, AutoProcessor
from IPython.display import display
MODEL_ID = "LiquidAI/LFM2.5-VL-3B" 
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForImageTextToText.from_pretrained(
    MODEL_ID,
    device_map="auto",
    dtype="bfloat16",
)
img_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/coco_sample.png"
input_image = load_image(img_url)
display(input_image)
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": input_image},
            {"type": "text", "text": "Describe this image in two concise sentences."},
        ],
    }
]
inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)
with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        do_sample=True,
        temperature=0.2,
        top_k=50,
        repetition_penalty=1.0,
        max_new_tokens=256,
    )
output = processor.batch_decode(outputs[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)[0]
print(output)
```
```
Two cats are sleeping on a pink couch with two remote controls.
```
You can find more hands-on examples on how to use LFM2.5-VL3B for multi-image inputs, grounding, OCR, tool calling, and more in our documentation. Check out our release blog for video examples.

## LFM2.5-VL-3B demo

Check out this browser demo of LFM2.5-VL-3B powering a vision-capable chat interface. It allows you to take or upload multiple images and let the model interact with them, including grounding, OCR, and tool use.

## Get Started

LFM2.5-VL-3B is available on Hugging Face today.

With LFM2.5, we're delivering on our vision of AI that runs anywhere. These models are:

- **Download:** LFM2.5-VL-3B on Hugging Face.
- **Try:** run the WebGPU demo in your browser, no setup needed.
- **Fine-tune:** adapt LFM2.5-VL-3B to your task with our fine-tuning tutorials.

We can't wait to see what you build.

## Citation

Please cite this article as:

```
Liquid AI, "LFM2.5-VL-3B: A Better and Faster Vision-Language Model for the Edge", Liquid AI Blog, Aug 2026.
```
Or use the BibTeX citation:

```
@article{liquidAI2026VL3B,
  author  = {Liquid AI},
  title   = {LFM2.5-VL-3B: A Better and Faster Vision-Language Model for the Edge},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm2-5-vl-3b},
}
```
