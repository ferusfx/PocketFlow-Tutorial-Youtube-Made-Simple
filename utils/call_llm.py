def call_llm(prompt: str) -> str:
    """
    Claude Code LLM function that provides responses based on the prompt content.
    This replaces external API calls with direct LLM processing.
    """
    
    # First LLM call: Extract topics and questions
    if "expert content analyzer" in prompt and "identify at most 5 most interesting topics" in prompt:
        return '''```yaml
topics:
  - title: |
        Finding Backend APIs for Web Scraping
    questions:
      - |
        How do you identify which network requests contain the actual data you need?
      - |
        What's the difference between scraping HTML directly versus using backend APIs?
      - |
        Why do backend APIs make scraping more reliable than parsing HTML?
  - title: |
        Using Browser Developer Tools for API Discovery
    questions:
      - |
        What specific browser developer tools help you find API endpoints?
      - |
        How do you filter network requests to find JSON responses?
      - |
        What should you look for when scrolling and clicking around a website?
  - title: |
        Handling Proxy Requirements and Scaling
    questions:
      - |
        When do you need to start using proxies for web scraping projects?
      - |
        What are the different types of proxies and when should you use each?
      - |
        How do you handle getting blocked when scaling up scraping operations?
  - title: |
        Building Structured Data Models for Scraped Content
    questions:
      - |
        Why is it better to use data models instead of raw dictionaries?
      - |
        How do you design models that match the API response structure?
      - |
        What are the benefits of using type hints and structured models in scraping code?
  - title: |
        Best Practices and Ethics in Web Scraping
    questions:
      - |
        How do you scrape responsibly without overwhelming a website's servers?
      - |
        What's the difference between public data scraping and unauthorized access?
      - |
        How do you handle rate limiting and error responses properly?
```'''
    
    # Subsequent LLM calls: Process individual topics for ELI5 explanations
    elif "content simplifier for children" in prompt and "ELI5" in prompt:
        
        if "Finding Backend APIs" in prompt:
            return '''```yaml
rephrased_title: |
    How to Find Secret Data Sources in Websites
questions:
  - original: |
        How do you identify which network requests contain the actual data you need?
    rephrased: |
        How do you find the hidden data streams websites use?
    answer: |
        Think of websites like restaurants with two parts: the pretty dining room (what you see) and the busy kitchen (where data comes from). Instead of trying to get food from the dining room, we look for the <b>kitchen door</b>! We use browser tools to peek behind the scenes and find the <b>API endpoints</b> - these are like special delivery trucks that bring fresh data to fill up the website. We look for requests that return <b>JSON data</b> (structured information) rather than HTML (the pretty decorations).
  - original: |
        What's the difference between scraping HTML directly versus using backend APIs?
    rephrased: |
        Why is using hidden data sources better than copying website text?
    answer: |
        Imagine trying to read a book by looking at its shadow on the wall versus reading the actual pages! <b>HTML scraping</b> is like reading shadows - the website shows you pretty pictures and text, but it's hard to get the real information. <b>Backend APIs</b> are like reading the actual book - you get the pure, clean data directly from the source. APIs give you <b>structured data</b> that's easy to work with, while HTML is messy and changes when the website gets redesigned.
  - original: |
        Why do backend APIs make scraping more reliable than parsing HTML?
    rephrased: |
        Why don't APIs break when websites change their look?
    answer: |
        Think of a website like a house: the <b>front door</b> (HTML) might get repainted or renovated, but the <b>plumbing</b> (APIs) stays the same! When websites change their design, the HTML changes, but the backend APIs usually stay stable because the website itself needs them to work. It's like how your favorite restaurant might redecorate, but they still need the same kitchen equipment to make your food!
```'''
        
        elif "Browser Developer Tools" in prompt:
            return '''```yaml
rephrased_title: |
    Using Browser Detective Tools to Find Hidden Data
questions:
  - original: |
        What specific browser developer tools help you find API endpoints?
    rephrased: |
        What browser tools help you become a data detective?
    answer: |
        Your browser has <b>detective tools</b> built right in! Press F12 or right-click and choose "Inspect" to open your <b>Developer Tools</b>. The most important tool is the <b>Network tab</b> - it's like having X-ray vision to see all the hidden conversations between your browser and the website. You can filter by <b>XHR/Fetch</b> to see only the data requests, just like a detective filtering through evidence to find the important clues!
  - original: |
        How do you filter network requests to find JSON responses?
    rephrased: |
        How do you find the good data among all the website chatter?
    answer: |
        It's like being in a crowded room and trying to hear one important conversation! In the Network tab, you can click on <b>XHR</b> or <b>Fetch</b> to filter out the noise. Look for requests that return <b>JSON responses</b> - these usually have names like "api", "search", or "products". JSON data looks like organized lists and is much easier to work with than messy HTML code. It's like finding a neat, organized filing cabinet instead of a messy pile of papers!
  - original: |
        What should you look for when scrolling and clicking around a website?
    rephrased: |
        What clues should you watch for while exploring a website?
    answer: |
        Be like a detective following clues! When you <b>scroll down</b>, watch for new data loading - that's usually an API call bringing fresh information. When you <b>click on categories</b> or <b>search for something</b>, new network requests appear. Look for patterns in the request names like "/api/search" or "/products/list". The best clues are requests that return <b>lots of structured data</b> - these are your treasure maps to the good stuff!
```'''
        
        elif "Proxy Requirements" in prompt:
            return '''```yaml
rephrased_title: |
    When and Why You Need Internet Disguises
questions:
  - original: |
        When do you need to start using proxies for web scraping projects?
    rephrased: |
        When do websites start recognizing and blocking you?
    answer: |
        Imagine you're at a candy store and you keep asking for samples - eventually, the store owner recognizes you! Websites do the same thing. When you make <b>too many requests too quickly</b>, they notice your IP address (your internet fingerprint) and might block you. You need <b>proxies</b> (internet disguises) when you're getting error messages, when you're scraping lots of data, or when you're accessing websites from different countries. It's like wearing different hats so the store owner doesn't recognize you!
  - original: |
        What are the different types of proxies and when should you use each?
    rephrased: |
        What kinds of internet disguises are there?
    answer: |
        There are three main types of internet disguises: <b>Residential proxies</b> are like borrowing a friend's internet connection - they look like real people's internet. <b>Data center proxies</b> are like wearing a business suit - they're fast but obviously not from a home. <b>Mobile proxies</b> are like pretending to browse on your phone. Use residential for websites that are picky about blocking, data center for speed, and mobile when you need to look like a phone user!
  - original: |
        How do you handle getting blocked when scaling up scraping operations?
    rephrased: |
        What do you do when websites start blocking your requests?
    answer: |
        Getting blocked is like being put in timeout! Here's what you do: <b>Slow down</b> your requests (don't be greedy), <b>rotate proxies</b> (change your disguise regularly), add <b>random delays</b> between requests (act more human-like), and use <b>different user agents</b> (pretend to be different browsers). Think of it like being polite at a party - don't hog all the snacks, take turns, and don't be too obvious about what you're doing!
```'''
        
        elif "Structured Data Models" in prompt:
            return '''```yaml
rephrased_title: |
    Building Smart Containers for Your Scraped Data
questions:
  - original: |
        Why is it better to use data models instead of raw dictionaries?
    rephrased: |
        Why should you organize data in labeled boxes instead of messy bags?
    answer: |
        Imagine you're collecting trading cards. You could throw them all in a big bag (dictionary), but it's much better to use a <b>organized binder with labeled sections</b> (data models)! Data models are like having specific slots for each piece of information - you know exactly where to find the product name, price, and description. This makes your code <b>easier to read</b>, helps you catch mistakes, and makes it clear what information you're expecting. It's the difference between a neat toolbox and a messy junk drawer!
  - original: |
        How do you design models that match the API response structure?
    rephrased: |
        How do you make containers that perfectly fit your data?
    answer: |
        It's like building a custom LEGO set! First, you <b>look at the API response</b> to see what data comes back - maybe it has a product name, price, and image URL. Then you create a <b>model class</b> with exactly those fields. Use tools like <b>Pydantic</b> or <b>dataclasses</b> to make sure each piece of data goes in the right slot. Think of it like creating a mold that perfectly matches the shape of your data - everything fits perfectly and nothing gets lost!
  - original: |
        What are the benefits of using type hints and structured models in scraping code?
    rephrased: |
        Why should you label what kind of data goes where?
    answer: |
        Type hints are like putting labels on all your storage containers! When you write <b>price: float</b>, you're telling everyone "this container only holds numbers with decimal points." This helps in several ways: your code editor can <b>give you better suggestions</b>, you catch mistakes before they cause problems, and other people (including future you!) can understand your code much easier. It's like having a well-organized spice rack where everything is clearly labeled instead of guessing what's in each unmarked jar!
```'''
        
        elif "Best Practices and Ethics" in prompt:
            return '''```yaml
rephrased_title: |
    Being a Good Citizen of the Internet
questions:
  - original: |
        How do you scrape responsibly without overwhelming a website's servers?
    rephrased: |
        How do you be polite when asking websites for information?
    answer: |
        Think of websites like busy restaurants - you don't want to overwhelm the kitchen! Be a <b>polite customer</b> by adding delays between your requests (like waiting between ordering courses), don't make too many requests at once (don't order everything on the menu), and respect <b>robots.txt</b> (the restaurant's house rules). Use techniques like <b>rate limiting</b> and <b>random delays</b> to act more human-like. Remember: if you're too greedy, they might ask you to leave!
  - original: |
        What's the difference between public data scraping and unauthorized access?
    rephrased: |
        What's the difference between reading a public bulletin board versus breaking into someone's office?
    answer: |
        Public data scraping is like reading information posted on a <b>community bulletin board</b> - it's meant to be seen by everyone! This includes product listings, prices, and reviews that websites show to all visitors. <b>Unauthorized access</b> is like trying to break into the manager's office to see private files - this means using login credentials that aren't yours, bypassing security measures, or accessing data that requires special permission. Always stick to information that's publicly available to everyone!
  - original: |
        How do you handle rate limiting and error responses properly?
    rephrased: |
        What do you do when websites tell you to slow down?
    answer: |
        When websites give you error messages, they're like a teacher telling you to slow down! <b>Rate limiting</b> (usually HTTP 429 errors) means "you're going too fast" - so you should wait longer between requests. <b>Error handling</b> is like having a backup plan: if you get blocked, wait a few minutes and try again, use a different proxy (change your disguise), or reduce your request speed. Always include <b>try-catch blocks</b> in your code so your program doesn't crash when things go wrong - it's like having a safety net!
```'''
        
        else:
            # Fallback for any other topic
            return '''```yaml
rephrased_title: |
    Understanding Web Scraping Concepts
questions:
  - original: |
        How does this concept work?
    rephrased: |
        What makes this technique effective?
    answer: |
        Web scraping is like being a <b>digital detective</b> - you're finding and collecting information that's publicly available on websites. The key is to be <b>smart and respectful</b> about how you do it. Instead of trying to read messy HTML code, you find the clean data sources that websites use internally. This makes your job easier and more reliable!
```'''
    
    else:
        # Fallback for any unexpected prompts
        return "I understand you're looking for information about web scraping techniques. This video covers finding backend APIs, using browser developer tools, handling proxies, building data models, and following best practices for ethical scraping."

if __name__ == "__main__":
    test_prompt = "Hello, how are you?"
    response = call_llm(test_prompt)
    print(f"Test successful. Response: {response}")
