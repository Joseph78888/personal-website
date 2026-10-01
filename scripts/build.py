"""Build the existing static site for Sites, without framework dependencies."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
out = root / 'dist'
out.mkdir(exist_ok=True)
shutil.copy2(root / 'index.html', out / 'index.html')
for directory in ['css', 'js', 'assets']:
    shutil.copytree(root / directory, out / directory, dirs_exist_ok=True)
print('Static site built in dist/')
