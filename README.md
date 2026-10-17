# genpark-hume-ai-empathic-voice-prosody-expression-analyzer-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](https://www.genpark.ai)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

Hume AI & Meta Muse-inspired Empathic Voice Prosody & Expression Analyzer. Decodes acoustic fundamental frequency (F0), speech tempo, jitter, and semantic sentiment into high-dimensional emotional states to direct real-time expressive TTS modulation.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import HumeAIEmpathicVoiceProsodyAnalyzer

def main():
    analyzer = HumeAIEmpathicVoiceProsodyAnalyzer()
    text = "We just hit our milestone goal, I cannot believe how well the team performed!"
    acoustics = {"mean_f0_hz": 210.0, "f0_variance": 42.0, "speaking_rate_wpm": 165.0, "pause_ratio": 0.08, "jitter_local": 0.012}
    result = analyzer.analyze_expression_and_modulate(text, acoustics)
    print("--- Hume AI Voice Expression & Prosody Modulation ---")
    print(f"Detected Emotion: {result['detected_expression']['primary_emotion']} (Confidence: {result['detected_expression']['affect_confidence']*100:.1f}%)")
    print(f"TTS Tone Directive: {result['tts_prosody_directives']['response_tone']}")
    print(f"Rate Multiplier: {result['tts_prosody_directives']['target_speaking_rate_multiplier']}x | Pitch Shift: {result['tts_prosody_directives']['target_pitch_shift_semitones']} semitones")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
