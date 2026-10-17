"""
Hume AI-inspired Empathic Voice Prosody & Expression Analyzer (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
import re
import math
from typing import Dict, Any, List, Optional

class HumeAIEmpathicVoiceProsodyAnalyzer:
    EMOTIONAL_PROFILES = {
        "EXCITEMENT": {"f0_boost": 1.25, "rate_boost": 1.15, "pitch_variance_min": 35.0},
        "ANXIETY": {"f0_boost": 1.20, "rate_boost": 1.25, "jitter_threshold": 0.035},
        "SADNESS": {"f0_boost": 0.85, "rate_boost": 0.80, "pause_ratio_min": 0.28},
        "CONFIDENCE": {"f0_boost": 0.95, "rate_boost": 1.00, "pitch_variance_min": 20.0},
        "CALM": {"f0_boost": 0.90, "rate_boost": 0.90, "pause_ratio_min": 0.20}
    }

    def __init__(self, agent_name: str = "Hume-Empathic-Voice-EVI"):
        self.agent_name = agent_name

    def infer_primary_emotion(self, text: str, acoustics: Dict[str, float]) -> Dict[str, Any]:
        f0_var = float(acoustics.get("f0_variance", 20.0))
        rate_wpm = float(acoustics.get("speaking_rate_wpm", 140.0))
        pause_r = float(acoustics.get("pause_ratio", 0.15))
        jitter = float(acoustics.get("jitter_local", 0.015))
        
        words = set(re.findall(r"\w+", text.lower()))
        
        if jitter > 0.030 or (rate_wpm > 180.0 and f0_var > 40.0) or words & {"worried", "panic", "stressed", "hurry"}:
            state = "ANXIETY"
            confidence = 0.88
        elif f0_var > 35.0 or words & {"amazing", "incredible", "love", "awesome", "yay"}:
            state = "EXCITEMENT"
            confidence = 0.92
        elif pause_r > 0.25 or words & {"tired", "down", "sad", "disappointed", "alone"}:
            state = "SADNESS"
            confidence = 0.85
        elif 120.0 <= rate_wpm <= 160.0 and f0_var < 25.0:
            state = "CALM"
            confidence = 0.90
        else:
            state = "CONFIDENCE"
            confidence = 0.78
            
        return {"primary_emotion": state, "affect_confidence": confidence}

    def synthesize_tts_modulation(self, emotion: str) -> Dict[str, Any]:
        profile = self.EMOTIONAL_PROFILES.get(emotion, self.EMOTIONAL_PROFILES["CALM"])
        # Generate responsive mirror/soothe directives
        if emotion in ["ANXIETY", "SADNESS"]:
            # Soothing response: slower, warm, reassuring cadence
            return {
                "target_speaking_rate_multiplier": 0.92,
                "target_pitch_shift_semitones": -1.2,
                "breathiness_gain": 0.15,
                "response_tone": "Warmly reassuring, grounded, steady cadence"
            }
        elif emotion == "EXCITEMENT":
            # Dynamic resonance response
            return {
                "target_speaking_rate_multiplier": 1.08,
                "target_pitch_shift_semitones": 0.8,
                "breathiness_gain": 0.05,
                "response_tone": "Energetic, engaging, upward lilt"
            }
        else:
            return {
                "target_speaking_rate_multiplier": 1.0,
                "target_pitch_shift_semitones": 0.0,
                "breathiness_gain": 0.0,
                "response_tone": "Balanced, articulate, professional warmth"
            }

    def analyze_expression_and_modulate(self, transcript: str, acoustic_features: Dict[str, float]) -> Dict[str, Any]:
        analysis = self.infer_primary_emotion(transcript, acoustic_features)
        tts_mods = self.synthesize_tts_modulation(analysis["primary_emotion"])
        
        return {
            "analyzer": self.agent_name,
            "detected_expression": analysis,
            "tts_prosody_directives": tts_mods,
            "verdict": "EMPATHIC_RESONANCE_TUNED"
        }
