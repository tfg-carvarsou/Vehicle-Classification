import subprocess

def download_dataset(script):
    subprocess.run(["chmod", "+x", script])
    subprocess.run([script])

def debug_mode():
    download = True
    return download

def main():
    download = debug_mode()

    if download:
        print("\n📥 Downloading dataset...")
        download_dataset('./scripts/uc3m_dataset.sh')

if __name__ == '__main__':
    main()