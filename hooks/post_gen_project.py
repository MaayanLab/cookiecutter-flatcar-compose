import sys
import pathlib
import subprocess

cookiecutter_path = pathlib.Path("{{ cookiecutter.filename }}.yaml").absolute()
file_path = (cookiecutter_path.parent.parent/cookiecutter_path.name).with_suffix('.yaml')
cookiecutter_path.rename(file_path)
cookiecutter_path.parent.rmdir()
print(f"Translate {file_path.name} with butane to {file_path.stem}.ignition.json? [Y/n]")
if input().lower() in {'','y'}:
  subprocess.run(
    f'docker run --rm -i quay.io/coreos/butane:latest < "{file_path}" | tee "{file_path.with_suffix(".ignition.json")}"',
    shell=True,
    cwd=file_path.parent,
    stdin=sys.stdin,
    stdout=sys.stdout,
    stderr=sys.stderr,
  )