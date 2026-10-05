#!/usr/bin/env python3
"""Study Archive를 검증하고 main 푸시로 GitHub Pages 배포를 시작한다."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEPLOY_BRANCH = "main"
PRIVATE_ROOTS = ("contents/", "_notes/", ".venv/", "site/")
PRIVATE_LINK = re.compile(
    r"]\(\s*<?(?:file:/{0,3}|/(?:home|Users)/|/[A-Za-z]:/|[A-Za-z]:[\\/])",
    re.IGNORECASE,
)


class DeployError(RuntimeError):
    """안전한 배포를 진행할 수 없을 때 발생한다."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--push",
        action="store_true",
        help="검증 후 origin/main에 푸시하여 GitHub Actions 배포를 시작합니다.",
    )
    parser.add_argument(
        "--remote",
        default="origin",
        help="푸시할 Git 원격 이름입니다. 기본값: origin",
    )
    return parser.parse_args()


def run(
    command: list[str],
    *,
    capture: bool = False,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=capture,
        check=False,
    )
    if check and result.returncode:
        detail = (result.stderr or result.stdout or "명령 실행 실패").strip()
        raise DeployError(f"{' '.join(command)}\n{detail}")
    return result


def git(*arguments: str, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return run(["git", *arguments], capture=capture)


def require_repository() -> None:
    result = git("rev-parse", "--show-toplevel", capture=True)
    if Path(result.stdout.strip()).resolve() != ROOT:
        raise DeployError(f"저장소 루트가 예상 경로와 다릅니다: {result.stdout.strip()}")


def require_deploy_branch() -> None:
    branch = git("branch", "--show-current", capture=True).stdout.strip()
    if branch != DEPLOY_BRANCH:
        raise DeployError(
            f"현재 브랜치는 {branch or '(detached HEAD)'}입니다. "
            f"배포는 {DEPLOY_BRANCH}에서만 가능합니다."
        )


def require_clean_worktree() -> None:
    status = git("status", "--porcelain", "--untracked-files=normal", capture=True).stdout
    if status.strip():
        raise DeployError(
            "커밋되지 않은 변경이 있어 푸시하지 않습니다.\n"
            "먼저 검토하고 커밋하세요:\n" + status.rstrip()
        )


def check_private_files() -> None:
    tracked = git("ls-files", "-z", capture=True).stdout.split("\0")
    leaked = sorted(
        path for path in tracked
        if path and any(path == root.rstrip("/") or path.startswith(root) for root in PRIVATE_ROOTS)
    )
    if leaked:
        raise DeployError("비공개·생성 경로가 Git에 추적되고 있습니다:\n" + "\n".join(leaked))


def check_private_links() -> None:
    leaked: list[str] = []
    for path in sorted((ROOT / "docs").rglob("*.md")):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if PRIVATE_LINK.search(line):
                leaked.append(f"{path.relative_to(ROOT)}:{number}")
    if leaked:
        raise DeployError("공개 Markdown에 로컬 절대경로 링크가 있습니다:\n" + "\n".join(leaked))


def check_diff() -> None:
    git("diff", "--check", "HEAD", "--")


def mkdocs_command() -> list[str]:
    local = ROOT / ".venv" / "bin" / "mkdocs"
    if local.is_file():
        return [str(local)]
    executable = shutil.which("mkdocs")
    if executable:
        return [executable]
    raise DeployError(
        "MkDocs를 찾을 수 없습니다. 먼저 가상환경과 의존성을 설치하세요:\n"
        "python3 -m venv .venv\n"
        ".venv/bin/python -m pip install -r requirements.txt"
    )


def build_site() -> None:
    print("[검사] MkDocs 엄격 빌드")
    run([*mkdocs_command(), "build", "--strict"])


def push(remote: str) -> None:
    print(f"[확인] {remote}/{DEPLOY_BRANCH} 최신 상태 조회")
    git("fetch", remote, DEPLOY_BRANCH)
    comparison = git(
        "rev-list", "--left-right", "--count",
        f"HEAD...refs/remotes/{remote}/{DEPLOY_BRANCH}",
        capture=True,
    ).stdout.split()
    if len(comparison) != 2:
        raise DeployError("로컬과 원격 커밋 차이를 계산하지 못했습니다.")
    ahead, behind = map(int, comparison)
    if behind:
        raise DeployError(
            f"로컬 {DEPLOY_BRANCH}이 {remote}/{DEPLOY_BRANCH}보다 "
            f"{behind}개 커밋 뒤에 있습니다. 먼저 pull한 뒤 다시 검증하세요."
        )
    if not ahead:
        print("[완료] 원격에 새로 푸시할 커밋이 없습니다.")
        return
    print(f"[배포] 검증된 {ahead}개 커밋을 {remote}/{DEPLOY_BRANCH}에 푸시")
    git("push", remote, f"HEAD:{DEPLOY_BRANCH}")
    print("[완료] 푸시했습니다. GitHub Actions의 Pages 배포가 시작됩니다.")


def main() -> int:
    args = parse_args()
    try:
        require_repository()
        require_deploy_branch()
        print("[검사] 비공개 파일과 로컬 경로")
        check_private_files()
        check_private_links()
        check_diff()
        build_site()
        if args.push:
            require_clean_worktree()
            push(args.remote)
        else:
            print("[완료] 사전검사를 통과했습니다. 실제 배포는 --push 옵션을 사용하세요.")
        return 0
    except DeployError as error:
        print(f"[중단] {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
