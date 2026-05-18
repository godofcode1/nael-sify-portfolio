from pathlib import Path
import shutil
import stat

from app import app, MY_PROJECTS, SERVICES, STATS


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "dist"


def _clear_readonly(func, path, _exc_info) -> None:
    Path(path).chmod(stat.S_IWRITE)
    func(path)


def _reset_output_dir() -> None:
    if not OUT_DIR.exists():
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        return

    for child in OUT_DIR.iterdir():
        if child.name == ".git":
            continue
        if child.is_dir():
            shutil.rmtree(child, onexc=_clear_readonly)
        else:
            child.unlink()


def build() -> None:
    _reset_output_dir()
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
