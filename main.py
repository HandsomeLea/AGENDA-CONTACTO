"""Bootstrap script for the Django agenda project.

Run "python main.py" to ensure environment defaults, apply migrations, and
start the development server with minimal manual steps.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv


DEFAULT_ENV_CONTENT = """# Environment defaults for local development
DEBUG=True
SECRET_KEY=dev-secret-change-me
# DATABASE_URL=postgres://user:pass@host:5432/dbname
"""


def ensure_env_file(env_path: Path) -> None:
    """Create a basic .env file if it does not exist."""
    if env_path.exists():
        return
    env_path.write_text(DEFAULT_ENV_CONTENT, encoding="utf-8")


def main() -> None:
    base_dir = Path(__file__).resolve().parent

    if str(base_dir) not in sys.path:
        sys.path.insert(0, str(base_dir))

    env_path = base_dir / ".env"
    ensure_env_file(env_path)
    load_dotenv(dotenv_path=env_path, override=False)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agenda.settings")

    import django

    django.setup()

    from django.core.management import call_command

    print("Applying database migrations...", flush=True)
    call_command("migrate", interactive=False)

    print("Starting development server at http://127.0.0.1:8000/", flush=True)
    call_command("runserver", "127.0.0.1:8000")


if __name__ == "__main__":
    main()
