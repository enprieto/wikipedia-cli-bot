import wikipedia

input_prompt = "\n>>> "
current_page = {}

def random():
    random_pages = wikipedia.random(pages=10)
    for page in random_pages:
        print(page)


def get_page(query):
    global current_page
    current_page = {}
    titles = wikipedia.search(query, results=5)
    if not titles:
        print("I couldn't find any matching Wikipedia pages.")
        return None

    print("\nChoose a page:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")

    page_choice = int(input(input_prompt))
    selected_title = titles[page_choice - 1]
    wikipediaPage = wikipedia.page(selected_title, auto_suggest=False)
    current_page['page'] = wikipediaPage
    current_page['title'] = wikipediaPage.title

def page_summary():
    global current_page
    if 'summary' not in current_page:
        current_page['summary'] = current_page['page'].summary
    print(f"\n{current_page['title']} / Summary:\n")
    print(current_page['summary'])

def page_sections():
    global current_page
    if 'sections' not in current_page:
        current_page['sections'] = current_page['page'].sections
    print(f"\n{current_page['title']} / Sections:\n")
    for i, section in enumerate(current_page['sections'], 1):
        print(f"{i}. {section}")
    print("0. Back")

def page_section(section_choice):
    if 1 <= section_choice <= len(current_page['sections']):
        section = current_page['sections'][section_choice - 1]
        print(f"\n{current_page['title']} : {section}\n")
        print(current_page['page'].section(section))


def chatbot():
    while True:
        print("Enter a search term. Type 'random' for 10 random articles. To leave, type 'exit' or 'quit'.\n")
        user_input = input(input_prompt).lower()
        if user_input in ["exit", "quit"]:
            print("Goodbye!")
            break
        elif user_input in ["random"]:
            random()
        else:
            get_page(user_input)
            while True:
                print(f"\nPage menu for '{current_page['title']}':")
                print("1. Page Summary")
                print("2. Page Sections")
                print("3. Page Links")
                print("4. Page content")
                print("0. Back")

                choice = input(input_prompt).strip()

                if choice == "1": # Page Summary
                    page_summary()
                elif choice == "2": # Page sections
                    while True:
                        page_sections()
                        section_choice = int(input(input_prompt))
                        if section_choice >= 1:
                            page_section(section_choice)  
                        break
                elif choice == "3":
                    print("Links for '" + current_page['title'] + "':")
                    print(current_page['page'].links)
                elif choice == "4":
                    print("Content for '" + current_page['title'] + "':")
                    print(current_page['page'].content)
                else:
                    break

chatbot()
