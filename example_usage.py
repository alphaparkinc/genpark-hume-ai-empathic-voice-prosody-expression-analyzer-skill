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
