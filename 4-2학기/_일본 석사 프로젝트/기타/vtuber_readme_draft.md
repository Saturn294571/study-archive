# Fanart Shelf

Local-first AI-assisted organizer for anime / VTuber fanart.

This project is not a general photo manager.  
It is a **fanart inbox sorter** that classifies images and GIFs into human-readable folder structures using reference-image retrieval, visual tag extraction, and optional multimodal model verification.

## 1. Project Goal

The goal of this project is to organize a large unsorted fanart folder into a structured local archive.

Typical use case:

```text
Before:
  Downloads/Fanart_Unsorted/
    image001.png
    image002.gif
    watame_final.jpg
    download_13.webp

After:
  Fanart/
    01_Characters/
      Hololive/
        Tsunomaki_Watame/
          image/
          gif/
        Sakura_Miko/
          image/
          gif/
      Hololive_EN/
        Amelia_Watson/
          image/
          gif/

    02_Collab_or_Multiple/
      Watame_Miko/
      Hololive_Group/

    03_Review/
      unknown_character/
      low_confidence/
      duplicate_candidate/

    90_Index/
      fanart_index.sqlite
      classification_log.jsonl
      fanart_export.csv
````

The application should preserve the user's preferred local folder-based workflow while adding AI-assisted classification and review.

## 2. Non-Goals

This project is not intended to replace mature photo managers such as digiKam, Hydrus Network, Eagle, Immich, or PhotoPrism.

It is also not intended to become a full booru client or imageboard scraper.

Non-goals:

```text
- Full photo management suite
- RAW photo workflow
- Cloud photo backup
- Social media scraping
- Pixiv/Twitter/X crawler
- General-purpose image classifier
- Fully autonomous high-risk file movement without review
```

The intended role is narrower:

```text
Unsorted fanart inbox
↓
AI-assisted classification
↓
Human review
↓
Folder-based organization
↓
Optional metadata export for other tools
```

## 3. Core Design Philosophy

### 3.1 Folders as the Human Interface

The primary user interface is still the local file system.

The user should be able to browse the sorted result with an ordinary file explorer.

```text
Fanart/01_Characters/Hololive/Tsunomaki_Watame/image/
Fanart/01_Characters/Hololive/Tsunomaki_Watame/gif/
Fanart/01_Characters/Hololive_EN/Amelia_Watson/image/
```

The database is not the main interface.
It is only an index, audit log, and recovery mechanism.

### 3.2 Database as Supporting Memory

The database stores:

```text
- Original path
- New path
- File hash
- Perceptual hash
- Extracted tags
- Candidate characters
- Confidence score
- User correction history
- Reference image membership
- Move log
```

The user should not need to write SQL for normal use.

### 3.3 Review-First Automation

The app must assume that AI classification can be wrong.

Therefore:

```text
High confidence      → auto-sort candidate
Medium confidence    → review queue
Low confidence       → unknown / manual review
Duplicate candidate  → duplicate review
```

No destructive move should happen without logging.

Undo should be supported.

### 3.4 Reference DB Instead of Immediate Fine-Tuning

This project does not initially fine-tune a model.

Instead, it uses a reference-image database:

```text
Character reference images
↓
Image embeddings
↓
Nearest-neighbor / prototype-based matching
↓
User confirmation
↓
Reference DB update
```

This gives the user an "online-learning-like" experience without modifying model weights.

Strictly speaking, this is not model-level online learning.
It is **reference database adaptation**.

## 4. Difference from digiKam

digiKam is a general-purpose photo manager with tagging, metadata management, albums, face recognition, and general auto-tagging.

This project focuses on a different problem.

### digiKam-style problem

```text
What objects are visible in this image?
```

Possible output:

```text
person
woman
cartoon
illustration
hat
blonde hair
```

### Fanart Shelf problem

```text
Which VTuber / anime character is this fanart likely depicting?
```

Possible output:

```text
character:tsunomaki_watame
group:hololive
media_type:fanart
confidence:0.86
target_path:01_Characters/Hololive/Tsunomaki_Watame/image/
```

### Key Differentiation

```text
digiKam:
  - General photo management
  - General object tags
  - Album / metadata workflow
  - Real-world photo orientation

Fanart Shelf:
  - Anime / VTuber fanart organization
  - Character-specific reference DB
  - New outfit / new character prototype updates
  - Folder schema-based movement
  - Review queue for uncertain predictions
```

This project can be used before digiKam.

```text
Fanart Shelf = inbox sorter / preprocessing tool
digiKam      = long-term photo library manager
```

## 5. Model Architecture

The classification system should not rely on a single multimodal model.

Recommended architecture:

```text
Input image / GIF
↓
File scanner
↓
Hashing and duplicate detection
↓
Media type detection
↓
Visual tag extraction
↓
Embedding extraction
↓
Reference DB retrieval
↓
Candidate scoring
↓
Optional VLM verification
↓
Folder routing decision
↓
User review
↓
Move / log / update reference DB
```

## 6. Model Components

### 6.1 File Scanner

Responsibilities:

```text
- Scan inbox directory
- Detect supported formats
- Ignore unsupported files
- Extract basic file metadata
- Preserve original filename
- Generate normalized internal file record
```

Supported formats:

```text
Images:
  - .jpg
  - .jpeg
  - .png
  - .webp

Animated:
  - .gif

Optional later:
  - .mp4
  - .webm
  - .avif
```

### 6.2 Hashing Module

Two kinds of hashes are needed.

#### Cryptographic Hash

Used for exact duplicate detection.

```text
sha256(file_bytes)
```

If two files have the same SHA-256 hash, they are exactly identical.

#### Perceptual Hash

Used for near-duplicate detection.

Possible implementation:

```text
imagehash.phash
imagehash.average_hash
imagehash.dhash
```

Use cases:

```text
- Same image with different filename
- Resized image
- Recompressed image
- Cropped or lightly modified image
```

### 6.3 GIF Frame Extractor

GIFs should not be classified directly as one opaque file.

Instead:

```text
GIF
↓
Extract representative frames
↓
Classify each frame
↓
Aggregate result
```

Possible strategy:

```text
- First frame
- Middle frame
- Last frame
- Up to N evenly spaced frames
```

Result aggregation:

```text
If most frames agree:
  use majority character

If frames disagree:
  send to review/multiple
```

### 6.4 Visual Tag Extractor

Use an anime-oriented tagger such as WD14 / Danbooru-style tagger.

Purpose:

```text
- Extract visual attributes
- Reduce candidate search space
- Provide interpretable evidence
```

Example tags:

```text
blonde hair
pink hair
sheep horns
detective hat
miko outfit
animal ears
solo
multiple girls
chibi
looking at viewer
```

This component does not need to identify the exact character.
Its role is to provide visual evidence.

### 6.5 Embedding Extractor

Use a vision-language embedding model.

Possible model families:

```text
- CLIP
- OpenCLIP
- SigLIP
- anime-specialized CLIP variants, if available
```

Purpose:

```text
Input image
↓
Embedding vector
↓
Similarity search against reference DB
```

This is the core character matching layer.

### 6.6 Reference Image Database

Each character has a set of confirmed reference images.

Example:

```text
references/
  hololive/
    tsunomaki_watame/
      default/
      new_outfit/
      chibi/
      closeup/
    sakura_miko/
      default/
      casual/
      chibi/
    hololive_en/
      amelia_watson/
        default/
        detective/
        casual/
```

Each reference image is embedded and stored in the index.

Reference entry fields:

```text
reference_id
character_id
group_id
outfit_id
image_path
embedding_vector
source
created_at
confirmed_by_user
```

### 6.7 Prototype Layer

A character should not be represented by one average vector only.

Instead, use multiple prototypes:

```text
Tsunomaki_Watame:
  - default outfit prototype
  - new outfit prototype
  - chibi prototype
  - closeup face prototype
  - full-body prototype
```

Candidate score:

```text
score(character) = max similarity over that character's prototypes
```

This handles:

```text
- New outfits
- Different artists
- Chibi versions
- Bust-up vs full-body images
- Seasonal costumes
```

### 6.8 Candidate Scoring

Candidate score can combine:

```text
- Embedding similarity
- Visual tag match
- Character alias match from filename
- Group-level hints
- User correction history
```

Example scoring formula:

```text
final_score =
  0.65 * embedding_score
+ 0.20 * tag_score
+ 0.10 * filename_hint_score
+ 0.05 * prior_score
```

This should be configurable.

### 6.9 Optional Multimodal VLM Verification

A multimodal model can be used after candidate retrieval.

Do not ask the VLM an open-ended question such as:

```text
Who is this character?
```

Instead, provide a constrained candidate list:

```text
Choose the closest candidate from the list.
If uncertain, return Unknown.

Candidates:
1. Tsunomaki Watame
2. Amelia Watson
3. Sakura Miko
4. Unknown
```

Expected JSON output:

```json
{
  "selected_character": "tsunomaki_watame",
  "confidence": 0.84,
  "evidence": [
    "sheep horns",
    "blonde hair",
    "fluffy outfit"
  ],
  "uncertainty": "medium"
}
```

The VLM should be treated as a verifier, not as the only classifier.

## 7. Data Flow

### 7.1 Initial Scan

```text
User selects inbox folder
↓
Scanner reads files
↓
File metadata extracted
↓
Records inserted into database
```

Record example:

```json
{
  "file_id": "uuid",
  "original_path": "00_Inbox/unsorted/image001.png",
  "extension": ".png",
  "media_type": "image",
  "size_bytes": 2048123,
  "created_at": "2026-05-27T21:00:00+09:00"
}
```

### 7.2 Deduplication

```text
File
↓
SHA-256 hash
↓
Exact duplicate check
↓
Perceptual hash
↓
Near duplicate check
↓
Duplicate candidate queue if needed
```

Duplicate result example:

```json
{
  "file_id": "uuid",
  "sha256": "abc123...",
  "phash": "ff00aa...",
  "duplicate_status": "near_duplicate_candidate",
  "matched_file_id": "uuid2",
  "distance": 4
}
```

### 7.3 Classification

```text
File
↓
Visual tags
↓
Image embedding
↓
Reference DB search
↓
Candidate ranking
↓
Optional VLM verification
↓
Routing decision
```

Classification result example:

```json
{
  "file_id": "uuid",
  "candidates": [
    {
      "character_id": "tsunomaki_watame",
      "display_name": "Tsunomaki Watame",
      "score": 0.87
    },
    {
      "character_id": "amelia_watson",
      "display_name": "Amelia Watson",
      "score": 0.61
    }
  ],
  "selected_character": "tsunomaki_watame",
  "confidence": 0.87,
  "status": "auto_sort_candidate"
}
```

### 7.4 Folder Routing

Folder routing is based on a YAML schema.

Example:

```yaml
root: Fanart

confidence:
  auto_move: 0.80
  review: 0.50

folders:
  inbox: "00_Inbox/unsorted"
  character: "01_Characters/{group}/{character}/{media_type}"
  multiple: "02_Collab_or_Multiple/{group_name}/{media_type}"
  unknown: "03_Review/unknown_character"
  low_confidence: "03_Review/low_confidence"
  duplicate: "03_Review/duplicate_candidate"
  index: "90_Index"
```

If the classifier returns:

```json
{
  "group": "Hololive",
  "character": "Tsunomaki_Watame",
  "media_type": "gif",
  "confidence": 0.86
}
```

Then the router returns:

```text
Fanart/01_Characters/Hololive/Tsunomaki_Watame/gif/
```

### 7.5 Review Queue

Files should be reviewed when:

```text
- Confidence is below threshold
- Multiple candidates are too close
- Multiple characters are detected
- Duplicate candidate exists
- NSFW/sensitive classification is uncertain
- GIF frames disagree
```

Review status examples:

```text
auto_sort_candidate
needs_review
low_confidence
unknown_character
multiple_character
duplicate_candidate
manually_confirmed
manually_corrected
```

### 7.6 Move and Log

When the user approves movement:

```text
Current path
↓
Target path
↓
Move file
↓
Write log
↓
Update database
```

Move log example:

```json
{
  "timestamp": "2026-05-27T21:10:00+09:00",
  "file_id": "uuid",
  "original_path": "00_Inbox/unsorted/a.png",
  "new_path": "01_Characters/Hololive/Tsunomaki_Watame/image/a.png",
  "character": "tsunomaki_watame",
  "confidence": 0.87,
  "status": "moved",
  "approved_by_user": true
}
```

### 7.7 User Correction and Reference DB Update

If the user corrects a prediction:

```text
Predicted: Sakura Miko
Corrected: Hoshimachi Suisei
↓
Update classification record
↓
Add image embedding as Suisei positive example
↓
Optionally add as Miko negative example
↓
Update prototype statistics
```

This is the main adaptation loop.

## 8. Suggested Tech Stack

### 8.1 Frontend

Recommended:

```text
Electron
React
TypeScript
TailwindCSS
```

Alternative:

```text
PySide6
Qt for Python
```

Electron is preferred if the goal is a GitHub-distributed desktop app with a modern UI.

PySide6 is preferred if the goal is a Python-native local utility.

### 8.2 Backend

Recommended:

```text
Python 3.11+
FastAPI or simple local IPC layer
Pydantic
PyYAML
SQLite
Pillow
imagehash
OpenCV optional
onnxruntime optional
```

### 8.3 AI / Vision Components

Possible components:

```text
WD14 / Danbooru-style tagger
CLIP / OpenCLIP / SigLIP embedding model
Ollama-hosted VLM for optional verification
Qwen2.5-VL or similar VLM
```

### 8.4 Storage

```text
SQLite:
  - file index
  - embeddings metadata
  - classification records
  - move logs
  - user corrections

JSONL:
  - append-only operation log

CSV:
  - export format for inspection

YAML:
  - folder schema
  - character definitions
  - model configuration
```

## 9. Directory Structure

Suggested repository layout:

```text
fanart-shelf/
  README.md
  LICENSE
  .gitignore

  frontend/
    package.json
    src/
      main/
      renderer/
      components/
      pages/
      styles/

  backend/
    pyproject.toml
    fanart_shelf/
      __init__.py
      scanner.py
      hashing.py
      media.py
      gif_frames.py
      tagger.py
      embedding.py
      reference_db.py
      classifier.py
      router.py
      mover.py
      db.py
      schemas.py
      config.py
      api.py

  configs/
    folder_schema.example.yaml
    characters.example.yaml
    model.example.yaml

  docs/
    architecture.md
    data_flow.md
    schema.md
    roadmap.md

  tests/
    test_hashing.py
    test_router.py
    test_classifier.py
    test_mover.py

  examples/
    sample_inbox/
    sample_references/
```

## 10. Config Examples

### 10.1 Character Config

```yaml
groups:
  - id: hololive
    display_name: Hololive

  - id: hololive_en
    display_name: Hololive EN

characters:
  - id: tsunomaki_watame
    display_name: Tsunomaki Watame
    group: hololive
    aliases:
      - Watame
      - 角巻わため
      - わため
    visual_hints:
      - sheep horns
      - blonde hair
      - fluffy outfit
      - sheep motif

  - id: amelia_watson
    display_name: Amelia Watson
    group: hololive_en
    aliases:
      - Watson
      - Amelia Watson
      - ワトソン・アメリア
    visual_hints:
      - blonde hair
      - detective hat
      - magnifying glass
      - detective outfit
```

### 10.2 Model Config

```yaml
models:
  tagger:
    type: wd14
    device: auto
    threshold: 0.35

  embedding:
    type: openclip
    model_name: ViT-B-32
    device: auto

  vlm:
    enabled: true
    provider: ollama
    model: qwen2.5vl:7b
    confidence_threshold: 0.75

classification:
  auto_move_threshold: 0.80
  review_threshold: 0.50
  top_k_candidates: 5
  use_filename_hints: true
  use_visual_tags: true
  use_vlm_verification: true
```

## 11. Database Schema Draft

### files

```sql
CREATE TABLE files (
  id TEXT PRIMARY KEY,
  original_path TEXT NOT NULL,
  current_path TEXT NOT NULL,
  original_filename TEXT NOT NULL,
  extension TEXT NOT NULL,
  media_type TEXT NOT NULL,
  size_bytes INTEGER,
  width INTEGER,
  height INTEGER,
  sha256 TEXT,
  phash TEXT,
  created_at TEXT,
  updated_at TEXT
);
```

### characters

```sql
CREATE TABLE characters (
  id TEXT PRIMARY KEY,
  display_name TEXT NOT NULL,
  group_id TEXT,
  aliases_json TEXT,
  visual_hints_json TEXT
);
```

### classifications

```sql
CREATE TABLE classifications (
  id TEXT PRIMARY KEY,
  file_id TEXT NOT NULL,
  selected_character_id TEXT,
  confidence REAL,
  status TEXT,
  evidence_tags_json TEXT,
  candidates_json TEXT,
  created_at TEXT,
  FOREIGN KEY(file_id) REFERENCES files(id)
);
```

### moves

```sql
CREATE TABLE moves (
  id TEXT PRIMARY KEY,
  file_id TEXT NOT NULL,
  from_path TEXT NOT NULL,
  to_path TEXT NOT NULL,
  approved_by_user INTEGER,
  created_at TEXT,
  undone_at TEXT,
  FOREIGN KEY(file_id) REFERENCES files(id)
);
```

### reference_images

```sql
CREATE TABLE reference_images (
  id TEXT PRIMARY KEY,
  character_id TEXT NOT NULL,
  outfit_id TEXT,
  image_path TEXT NOT NULL,
  embedding_id TEXT,
  confirmed_by_user INTEGER,
  created_at TEXT,
  FOREIGN KEY(character_id) REFERENCES characters(id)
);
```

## 12. UI Design

### Main Screens

```text
1. Inbox Setup
2. Scan Results
3. Classification Queue
4. Review Queue
5. Reference Manager
6. Folder Schema Editor
7. Move Log / Undo
8. Settings
```

### Classification Queue View

Required elements:

```text
- Thumbnail preview
- Filename
- Media type
- Top candidate character
- Confidence score
- Evidence tags
- Target folder path
- Approve button
- Correct button
- Send to review button
```

### Review Queue View

Required elements:

```text
- Large image preview
- Top-k candidates
- Manual character selector
- Unknown button
- Multiple character option
- Add as reference checkbox
- Move target preview
```

### Reference Manager

Required elements:

```text
- Character list
- Reference image grid
- Outfit/prototype grouping
- Add reference images
- Remove bad references
- Recompute embeddings
```

## 13. Safety and File Handling

The app must not silently destroy or overwrite files.

Rules:

```text
- Never delete files automatically
- Never overwrite without explicit policy
- Always log move operations
- Support undo
- Preserve original filename in database
- Handle filename collisions
- Prefer copy mode during early development
```

Filename collision policy:

```text
If target filename already exists:
  filename.png
  filename__duplicate_001.png
  filename__duplicate_002.png
```

Recommended early mode:

```text
dry_run: true
copy_instead_of_move: true
```

Only after testing:

```text
dry_run: false
copy_instead_of_move: false
```

## 14. MVP Scope

### MVP 0: CLI Core

```text
- Scan folder
- Detect media type
- Compute SHA-256
- Compute perceptual hash
- Route files by extension
- Dry-run move plan
- JSONL log
```

### MVP 1: Folder Schema Sorter

```text
- YAML folder schema
- Character config
- Manual character assignment
- Move execution
- Undo support
```

### MVP 2: Embedding-Based Classifier

```text
- Reference folder support
- Image embedding extraction
- Similarity search
- Top-k candidates
- Confidence score
```

### MVP 3: AI-Assisted Review UI

```text
- Electron UI
- Thumbnail grid
- Review queue
- Approve/correct/unknown workflow
- Classification log viewer
```

### MVP 4: VLM Verification

```text
- Optional Ollama integration
- Candidate-constrained VLM prompt
- JSON output validation
- Evidence display
```

### MVP 5: digiKam Compatibility

```text
- CSV export
- Optional XMP sidecar export
- Clean folder structure usable by digiKam
```

## 15. Development Principles

```text
1. Build the Python core before the GUI.
2. Treat AI output as uncertain.
3. Prefer review-first workflows.
4. Keep original files recoverable.
5. Avoid model fine-tuning until enough labeled data exists.
6. Use reference DB adaptation first.
7. Keep folder structure human-readable.
8. Keep database as support, not as the main interface.
9. Make all file movement reversible.
10. Keep components modular.
```

## 16. Future Ideas

```text
- Multi-character detection
- Symbolic links for multi-tag folder views
- Artist detection
- Pixiv/source URL metadata
- NSFW/sensitive content filtering
- Local booru export
- Hydrus-compatible tag export
- digiKam sidecar compatibility
- Duplicate merge assistant
- Batch reference curation
- Active learning: ask user only for high-value uncertain samples
- LoRA or classifier fine-tuning after enough labels are collected
```

## 17. One-Sentence Summary

Fanart Shelf is a local-first AI-assisted fanart inbox sorter that uses reference-image retrieval, visual tags, and review-first folder routing to organize anime and VTuber images into human-readable local folders.

```

핵심은 README에서 **“이미지 분류기”가 아니라 “fanart inbox sorter”**라고 못박는 것입니다. 그래야 digiKam, Hydrus, Eagle 같은 기존 도구와 정면충돌하지 않고, 프로젝트 범위도 관리됩니다.
