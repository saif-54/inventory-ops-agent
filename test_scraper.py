from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com")
    
    quote = page.locator(".quote .text").first.inner_text()
    author = page.locator(".quote .author").first.inner_text()
    
    output = f"Quote: {quote}\nAuthor: {author}"
    print("\n--- Scraped Successfully ---")
    print(output)
    print("----------------------------\n")
    
    with open("C:/Users/saifh/agent_workspace/scraped_data.txt", "w", encoding="utf-8") as f:
        f.write(output)
        
    browser.close()