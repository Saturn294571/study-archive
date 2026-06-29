from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Iterable


AUDIO_EXTENSIONS = {".m4a", ".mp3", ".wav", ".mp4", ".aac", ".flac", ".ogg", ".webm"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Transcribe lecture audio with OpenAI Whisper. "
            "Designed for Korean lectures and mixed English/Korean classes."
        )
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Audio file or directory containing audio files such as .m4a",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to save outputs. Defaults to '<input parent>/transcripts'.",
    )
    parser.add_argument(
        "--model",
        default="small",
        help="Whisper model name. Examples: base, small, medium, large",
    )
    parser.add_argument(
        "--mode",
        choices=["finance", "accounting", "auto"],
        default="auto",
        help=(
            "Preset tuned for your class type. "
            "'finance' assumes mostly Korean. "
            "'accounting' assumes English lecture with Korean mixed in. "
            "'auto' keeps language detection broad."
        ),
    )
    parser.add_argument(
        "--language",
        choices=["ko", "en", "auto"],
        default=None,
        help=(
            "Override Whisper language. "
            "Use 'ko' for mostly Korean, 'en' for mostly English, "
            "or 'auto' to let Whisper detect."
        ),
    )
    parser.add_argument(
        "--task",
        choices=["transcribe", "translate"],
        default="transcribe",
        help="Whisper task. Usually keep 'transcribe' for lecture notes.",
    )
    parser.add_argument(
        "--beam-size",
        type=int,
        default=5,
        help="Beam size passed to Whisper decoding.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature. Keep near 0.0 for stable lecture transcription.",
    )
    parser.add_argument(
        "--append-preset-prompt",
        default="",
        help="Extra prompt appended after the built-in preset prompt.",
    )
    return parser.parse_args()


def resolve_audio_files(input_path: Path) -> list[Path]:
    if not input_path.exists():
        raise FileNotFoundError(f"입력 경로를 찾을 수 없습니다: {input_path}")

    if input_path.is_file():
        if input_path.suffix.lower() not in AUDIO_EXTENSIONS:
            raise ValueError(f"지원하지 않는 확장자입니다: {input_path.suffix}")
        return [input_path]

    files = sorted(
        path for path in input_path.rglob("*") if path.is_file() and path.suffix.lower() in AUDIO_EXTENSIONS
    )
    if not files:
        raise FileNotFoundError(f"오디오 파일을 찾지 못했습니다: {input_path}")
    return files


def ensure_dependencies() -> None:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "ffmpeg를 찾지 못했습니다. OpenAI Whisper는 ffmpeg가 필요합니다.\n"
            "예시: winget install Gyan.FFmpeg 또는 ffmpeg를 PATH에 추가하세요."
        )

    try:
        import whisper  # noqa: F401
    except ImportError as exc:
        raise RuntimeError(
            "Python 패키지 'whisper'를 찾지 못했습니다.\n"
            "설치 예시: python -m pip install -U openai-whisper"
        ) from exc


def choose_language(args: argparse.Namespace) -> str | None:
    if args.language is not None:
        return None if args.language == "auto" else args.language
    if args.mode == "finance":
        return "ko"
    if args.mode == "accounting":
        return None
    return None


def build_initial_prompt(args: argparse.Namespace) -> str:
    prompts = {
        "finance": (
            "이 음성은 한국어 중심의 금융계량경제학 강의이다. "
            "계량경제학, 금융계량, 회귀분석, 시계열, 추정, 검정, 변수, 모형 같은 용어를 정확히 적는다. "
            "수식이나 영어 용어는 가능한 한 원어를 보존한다."
        ),
        "accounting": (
            "This audio is an accounting lecture delivered mainly in English with Korean mixed in. "
            "Preserve accounting terms such as asset, liability, equity, revenue, expense, journal entry, "
            "debit, credit, balance sheet, income statement, cash flow, accrual, and adjustment. "
            "한국어 설명이 섞이면 자연스럽게 그대로 적는다."
        ),
        "auto": (
            "This is a university lecture recording. "
            "Preserve specialized academic terms, English keywords, Korean explanations, and numbers accurately."
        ),
    }
    base = prompts[args.mode]
    extra = args.append_preset_prompt.strip()
    return f"{base} {extra}".strip()


def format_timestamp(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    hours, rem = divmod(total_ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, ms = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{ms:03d}"


def write_text_output(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_segments_output(path: Path, segments: Iterable[dict]) -> None:
    serializable = list(segments)
    path.write_text(json.dumps(serializable, ensure_ascii=False, indent=2), encoding="utf-8")


def transcribe_one(model, audio_path: Path, output_dir: Path, args: argparse.Namespace) -> None:
    import whisper

    language = choose_language(args)
    prompt = build_initial_prompt(args)

    print(f"[START] {audio_path.name}")
    result = model.transcribe(
        str(audio_path),
        task=args.task,
        language=language,
        initial_prompt=prompt,
        beam_size=args.beam_size,
        temperature=args.temperature,
        verbose=False,
        fp16=False,
    )

    stem_dir = output_dir / audio_path.stem
    stem_dir.mkdir(parents=True, exist_ok=True)

    transcript_path = stem_dir / f"{audio_path.stem}.txt"
    segments_path = stem_dir / f"{audio_path.stem}.segments.json"

    write_text_output(transcript_path, result["text"])

    segments = []
    for segment in result.get("segments", []):
        segments.append(
            {
                "id": segment.get("id"),
                "start": segment.get("start"),
                "end": segment.get("end"),
                "start_ts": format_timestamp(segment.get("start", 0.0)),
                "end_ts": format_timestamp(segment.get("end", 0.0)),
                "text": segment.get("text", "").strip(),
            }
        )
    write_segments_output(segments_path, segments)
    print(f"[DONE] {audio_path.name} -> {transcript_path}")


def main() -> int:
    args = parse_args()

    try:
        ensure_dependencies()
        import whisper
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    try:
        audio_files = resolve_audio_files(args.input)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    output_dir = args.output_dir
    if output_dir is None:
        base_dir = args.input.parent if args.input.is_file() else args.input
        output_dir = base_dir / "transcripts"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"모델 로드 중: {args.model}")
    model = whisper.load_model(args.model)

    for audio_path in audio_files:
        try:
            transcribe_one(model, audio_path, output_dir, args)
        except Exception as exc:
            print(f"[ERROR] {audio_path.name}: {exc}", file=sys.stderr)

    print(f"출력 폴더: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
