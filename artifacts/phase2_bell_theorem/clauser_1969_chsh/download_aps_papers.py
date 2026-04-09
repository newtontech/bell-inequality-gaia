#!/usr/bin/env python3
"""Download APS physics papers using undetected-chromedriver.

Restarts Chrome for each paper to avoid crashes.
Uses cookies obtained from the browser session to download PDFs via requests.
"""

import os
import sys
import time
import requests
import undetected_chromedriver as uc


PAPERS = [
    {
        "name": "Einstein 1935 EPR",
        "abstract_url": "https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777",
        "pdf_url": "https://journals.aps.org/pr/pdf/10.1103/PhysRev.47.777",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase1_epr_paradox/einstein_1935_epr/einstein_podolsky_rosen_1935.pdf",
    },
    {
        "name": "Bohr 1935 Reply",
        "abstract_url": "https://journals.aps.org/pr/abstract/10.1103/PhysRev.48.696",
        "pdf_url": "https://journals.aps.org/pr/pdf/10.1103/PhysRev.48.696",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase1_epr_paradox/bohr_1935_reply/bohr_1935_reply.pdf",
    },
    {
        "name": "Bell 1964",
        "abstract_url": "https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.1.195",
        "pdf_url": "https://journals.aps.org/ppf/pdf/10.1103/PhysicsPhysiqueFizika.1.195",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase2_bell_theorem/bell_1964/bell_1964_inequality.pdf",
    },
    {
        "name": "CHSH 1969",
        "abstract_url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.23.880",
        "pdf_url": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.23.880",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase2_bell_theorem/clauser_1969_chsh/clauser_horne_shimony_holt_1969.pdf",
    },
    {
        "name": "Aspect 1982",
        "abstract_url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.49.91",
        "pdf_url": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.49.91",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase3_experiments/aspect_1982/aspect_grangier_rogier_1982.pdf",
    },
    {
        "name": "Weihs 1998",
        "abstract_url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.81.5039",
        "pdf_url": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.81.5039",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase3_experiments/weihs_1998/weihs_et_al_1998.pdf",
    },
    {
        "name": "Shalm 2015",
        "abstract_url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.115.250402",
        "pdf_url": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250402",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase3_experiments/shalm_2015/shalm_et_al_2015.pdf",
    },
    {
        "name": "Giustina 2015",
        "abstract_url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.115.250401",
        "pdf_url": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250401",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase3_experiments/giustina_2015/giustina_et_al_2015.pdf",
    },
    {
        "name": "Handsteiner 2017",
        "abstract_url": "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.118.060401",
        "pdf_url": "https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.118.060401",
        "save_path": "/home/yhm/desktop/code/bell-inequality-gaia/artifacts/phase4_modern/handsteiner_2017/handsteiner_et_al_2017.pdf",
    },
]


def wait_for_cloudflare(driver, max_wait=60):
    """Wait for Cloudflare challenge to resolve."""
    start = time.time()
    while time.time() - start < max_wait:
        try:
            title = driver.title
            if title != "Just a moment...":
                return True
        except Exception:
            pass
        time.sleep(2)
    return False


def download_paper(paper):
    """Download a single paper PDF with a fresh browser instance."""
    save_dir = os.path.dirname(paper["save_path"])
    os.makedirs(save_dir, exist_ok=True)

    # Skip if already downloaded
    if os.path.exists(paper["save_path"]):
        size = os.path.getsize(paper["save_path"])
        # Verify it's a real PDF
        with open(paper["save_path"], 'rb') as f:
            header = f.read(5)
        if header == b'%PDF-':
            print(f"  Already downloaded: {paper['save_path']} ({size} bytes)")
            return True

    print(f"\n--- Downloading: {paper['name']} ---")

    driver = None
    try:
        # Launch a fresh Chrome instance
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = uc.Chrome(headless=False, options=options, version_main=144)

        # Step 1: Navigate to abstract page to pass Cloudflare
        print(f"  Step 1: Loading abstract page...")
        driver.get(paper["abstract_url"])
        print(f"  Initial title: {driver.title}")

        if not wait_for_cloudflare(driver, max_wait=60):
            print(f"  FAILED: Cloudflare did not resolve on abstract page")
            return False

        print(f"  Cloudflare resolved! Title: {driver.title}")
        time.sleep(2)

        # Step 2: Get cookies from browser session
        selenium_cookies = driver.get_cookies()
        user_agent = driver.execute_script('return navigator.userAgent')

        # Step 3: Close the browser (we don't need it anymore)
        driver.quit()
        driver = None

        # Step 4: Download PDF using requests with the Cloudflare cookies
        print(f"  Step 2: Downloading PDF via requests...")
        session = requests.Session()
        for cookie in selenium_cookies:
            session.cookies.set(cookie['name'], cookie['value'])

        session.headers.update({
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': paper["abstract_url"],
        })

        resp = session.get(paper["pdf_url"], allow_redirects=True, timeout=60)
        content_type = resp.headers.get('content-type', 'N/A')

        print(f"  Response: status={resp.status_code}, content-type={content_type}, size={len(resp.content)}")

        # Check if we got a PDF
        if resp.status_code == 200 and (resp.content[:5] == b'%PDF-' or 'pdf' in content_type):
            with open(paper["save_path"], 'wb') as f:
                f.write(resp.content)
            print(f"  SAVED: {paper['save_path']} ({len(resp.content)} bytes)")
            return True
        else:
            print(f"  FAILED: Not a PDF (status={resp.status_code}, type={content_type})")
            return False

    except Exception as e:
        print(f"  Error: {e}")
        return False
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass


def main():
    print("=" * 60)
    print("APS Paper Downloader")
    print("Strategy: Fresh Chrome per paper, cookies -> requests")
    print("=" * 60)
    print(f"Total papers: {len(PAPERS)}")

    results = []
    for i, paper in enumerate(PAPERS):
        print(f"\n[{i+1}/{len(PAPERS)}] {paper['name']}")
        success = download_paper(paper)
        results.append((paper["name"], success))

    print("\n\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    success_count = 0
    for name, success in results:
        status = "OK" if success else "FAILED"
        print(f"  [{status}] {name}")
        if success:
            success_count += 1

    print(f"\nSuccess: {success_count}/{len(PAPERS)}")
    return 0 if success_count == len(PAPERS) else 1


if __name__ == "__main__":
    sys.exit(main())
