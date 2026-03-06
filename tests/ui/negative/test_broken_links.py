import pytest
import allure
from concurrent.futures import ThreadPoolExecutor


@pytest.mark.ui
@pytest.mark.negative
@allure.epic("UI Resilience")
@allure.feature("Links Integrity")
@allure.title("Negative: High-speed broken links check")
def test_homepage_broken_links(home_page, api_client):
    """
    Test collects all links from the homepage and verifies them
    using parallel API HEAD requests for maximum speed.
    """

    # Step 1: Access the application
    home_page.open()

    # Step 2: Extract and filter links
    with allure.step("Collect and filter links from the page"):
        raw_links = home_page.page.locator("a").evaluate_all(
            "list => list.map(element => element.href)"
        )

        # Filter for unique HTTP links, excluding anchors and JS stubs
        unique_links = list(set([
            l for l in raw_links
            if l and l.startswith("http") and "#" not in l and "javascript" not in l
        ]))

        # Logging link count for visibility
        link_count = len(unique_links)
        print(f"\n[INFO] Collected {link_count} unique links for validation")
        allure.attach(f"Total: {link_count}\n" + "\n".join(unique_links),
                      name="Checked URLs List",
                      attachment_type=allure.attachment_type.TEXT)

    broken_links = []

    # Worker function for parallel execution
    def check_link(link):
        try:
            # HEAD is faster as it retrieves headers only
            response = api_client.head(link, timeout=5)

            # Fallback to GET if HEAD is not supported (405 Method Not Allowed)
            if response.status_code == 405:
                response = api_client.get(link, timeout=5, stream=True)

            if response.status_code >= 400:
                broken_links.append(f"{link} (Status: {response.status_code})")
        except Exception as e:
            broken_links.append(f"{link} (Error: {str(e)})")

    # Step 3: Multi-threaded validation
    # use 11 threads as a limit, but adjust down if there are fewer links
    num_threads = min(11, len(unique_links))

    with allure.step(f"Validate {link_count} links via {num_threads} parallel threads"):
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            executor.map(check_link, unique_links)

    # Step 4: Final verification
    with allure.step("Verify all links are healthy"):
        assert not broken_links, f"Found broken links: {broken_links}"