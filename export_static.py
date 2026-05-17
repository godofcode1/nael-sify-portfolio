from pathlib import Path
import shutil

from app import app, MY_PROJECTS, SERVICES, STATS


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "dist"


def build() -> None:
    if OUT_DIR.exists():
        git_dir = OUT_DIR / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir, ignore_errors=True)
        shutil.rmtree(OUT_DIR)

    (OUT_DIR / "static").mkdir(parents=True, exist_ok=True)

    with app.test_request_context("/"):
        html = app.jinja_env.get_template("index.html").render(
            projects=MY_PROJECTS,
            stats=STATS,
            services=SERVICES,
        )

    html = html.replace('/static/', 'static/')
    (OUT_DIR / "index.html").write_text(html, encoding="utf-8")

    shutil.copytree(ROOT / "static", OUT_DIR / "static", dirs_exist_ok=True)
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    build()
