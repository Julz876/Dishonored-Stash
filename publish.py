import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
BLENDER_PATHS = [r'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe', r'C:\Program Files\Blender Foundation\Blender\blender.exe']

def run(cmd, description):
    print('\n[+] ' + description + '...', flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)

def main():
    blender = shutil.which('blender') or next((p for p in BLENDER_PATHS if Path(p).is_file()), None)
    if not blender:
        raise RuntimeError('Blender executable not found')
    env = os.environ.copy()
    # Keep publishing independent of local OCIO settings and startup add-ons.
    env.pop('OCIO', None)
    env.pop('SSLKEYLOGFILE', None)
    print('[+] Generating Asset Listing & Previews...', flush=True)
    # Drive can lock directories while Blender replaces its thumbnail cache.
    with tempfile.TemporaryDirectory(prefix='fh_asset_listing_') as tmp:
        staging = Path(tmp)
        for source in ROOT.rglob('*.blend'):
            if '.git' in source.relative_to(ROOT).parts:
                continue
            target = staging / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        for source in [ROOT / '_asset-library-meta.json', *ROOT.rglob('blender_assets.cats.txt')]:
            if source.is_file():
                target = staging / source.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        subprocess.run([blender, '--background', '--factory-startup', '-c', 'asset_listing', 'generate', str(staging)], cwd=ROOT, env=env, check=True)
        for source in staging.rglob('*'):
            if source.is_file() and source.suffix != '.blend' and source.name != 'blender_assets.cats.txt':
                target = ROOT / source.relative_to(staging)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
    status = subprocess.check_output(['git', 'status', '--porcelain'], cwd=ROOT, text=True)
    if status.strip():
        message = input('\nEnter commit summary (or press Enter for default): ').strip() or 'Update remote asset library'
        run(['git', 'add', '.'], 'Staging files')
        run(['git', 'commit', '-m', message], 'Committing changes')
    run(['git', 'fetch', 'origin'], 'Fetching GitHub changes')
    # Preserve local and remote commits; stop for review if a conflict occurs.
    run(['git', 'merge', '--no-edit', '@{upstream}'], 'Integrating GitHub changes')
    run(['git', 'push'], 'Pushing to GitHub')
    print('\n[OK] Remote asset library published successfully!')

if __name__ == '__main__':
    try:
        main()
    except (subprocess.CalledProcessError, RuntimeError) as exc:
        print('\n[-] Publishing stopped: ' + str(exc))
        sys.exit(1)
