#!/usr/bin/env python3
import json
import sys
from client import HumeAIEmpathicVoiceProsodyAnalyzer

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        analyzer = HumeAIEmpathicVoiceProsodyAnalyzer()
        transcript = "I am so worried about the upcoming presentation, everything feels rushed!"
        acoustics = {"mean_f0_hz": 230.0, "f0_variance": 45.0, "speaking_rate_wpm": 195.0, "pause_ratio": 0.10, "jitter_local": 0.038}
        res = analyzer.analyze_expression_and_modulate(transcript, acoustics)
        assert res["detected_expression"]["primary_emotion"] == "ANXIETY"
        assert res["tts_prosody_directives"]["target_speaking_rate_multiplier"] < 1.0
        print(f"[TEST PASS] Hume AI Voice Expression Analyzed: {res['detected_expression']['primary_emotion']}")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-hume-voice-analyzer", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "analyze_expression_and_modulate", "description": "Hume voice prosody & expression analyzer"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                analyzer = HumeAIEmpathicVoiceProsodyAnalyzer()
                out = analyzer.analyze_expression_and_modulate(args.get("transcript", ""), args.get("acoustic_features", {}))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
